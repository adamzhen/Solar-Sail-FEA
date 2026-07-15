"""
polygon_sail_scaling_study.py
===========================================================================
Scaling study for a boomless, non-spinning octagonal (N=8) solar sail
deployed via SMA (Nitinol) wires along radial flasher origami fold lines.

Four panels:
  (a) Deployment actuation force SF   — SMA force vs. fold-crease resistance
  (b) SRP wire bending stress SF      — wires as beams under SRP lateral load
  (c) Wrinkling disturbance torque    — first-principles CP/CM offset model
  (d) Wire mass vs. CF boom mass      — linear scale, boom uncertainty band

ALL DERIVATIONS are documented inline.  Formula origins are cited.
===========================================================================
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import os

# ======================================================================
# PARAMETERS
# ======================================================================
N     = 8        # polygon sides (octagon)
R_hub = 0.06     # hub circumradius  [m]

D_WIRES_MM = [0.5, 1.0, 1.5, 2.0]              # wire diameters [mm]
R_WIRES    = [d / 2000.0 for d in D_WIRES_MM]  # radii [m]
COLORS     = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728"]

A_arr = np.linspace(10, 200, 500)   # sail area sweep [m²]

# ----------------------------------------------------------------------
# SMA (Nitinol) material
# Source: Dynalloy Inc., "Technical Characteristics of FLEXINOL Actuator
#         Wires" (TCF1140),  https://www.dynalloy.com/pdfs/TCF1140.pdf
# Source: Otsuka & Wayman (eds.), "Shape Memory Materials," Cambridge UP 1998
# ----------------------------------------------------------------------
rho_NiTi       = 6450.0    # density          [kg/m³]   [Dynalloy TCF1140]
sigma_recovery = 172.0e6   # recovery stress  [Pa]  repeated-cycle  [Dynalloy TCF1140]
sigma_yield    = 345.0e6   # austenite yield  [Pa]                   [Otsuka & Wayman 1998]

# ----------------------------------------------------------------------
# Kapton HN 7.5 µm sail film
# Source: DuPont, "Kapton HN Polyimide Film — Summary of Properties"
#         H-38479-4  (https://www.dupont.com)
# Source: Greschik & Mikulas, J. Spacecraft & Rockets 39(5), 2002
# ----------------------------------------------------------------------
E_film  = 2.5e9    # Young's modulus    [Pa]
nu_film = 0.34     # Poisson ratio      [—]
t_film  = 7.5e-6   # thickness          [m]

# Flexural rigidity per unit width:  D = E t³ / [12(1-ν²)]
#   Units: [Pa·m³] = [N/m² · m³] = [N·m]
#   Physical meaning: moment per unit fold-width = D × curvature  [N·m/m × 1/m = N]
D_flex = E_film * t_film**3 / (12.0 * (1.0 - nu_film**2))

# Fold crease radius after stowage storage:
# Source: Lechenault et al., Phys. Rev. Lett. 2010 — tight folds: R_fold ≈ 3–8 × t
# We use 5 × t as a mid-range estimate.
R_fold = 5.0 * t_film   # [m]

# ----------------------------------------------------------------------
# Solar radiation pressure at 1 AU
# Source: Wertz, Everett & Puschell (eds.), "Space Mission Engineering,"
#         Microcosm 2011;  McInnes, "Solar Sailing," Springer 1999
# P_srp = (1 + η) × W_sun / c   for a reflective flat sail at normal incidence
# ----------------------------------------------------------------------
W_sun       = 1361.0    # solar constant  [W/m²]
c_light     = 2.998e8   # speed of light  [m/s]
eta_reflect = 0.88      # reflectivity (aluminised Kapton)  [Greschik & Mikulas 2002]
P_srp = (1.0 + eta_reflect) * W_sun / c_light   # ≈ 8.53×10⁻⁶ N/m²

# ----------------------------------------------------------------------
# Boom mass scaling
# The Murphy & Murphey (2003) J. Spacecraft & Rockets 40(4) paper derives
# m_boom ∝ A^(7/6) under TWO simultaneous constraints: constant sail
# loading (m/A = const) AND constant relative boom deflection.
# This is the structural upper bound.
#
# Empirically, LightSail-2 (A≈32 m², ~0.8 kg total boom mass) and
# NASA ACS3 (A≈80 m², ~2 kg total boom mass) both give ~0.025 kg/m²,
# consistent with m_boom ∝ A^1 (linear) over this range.
# Using a shaded band from A^0.75 (lower) to A^7/6 (upper theoretical)
# with both curves calibrated to pass through the ACS3 data point.
# ----------------------------------------------------------------------
A_ACS3 = 80.0; m_ACS3 = 2.0   # NASA ACS3 reference [m², kg]
exp_boom_lo = 0.75
exp_boom_hi = 7.0 / 6.0        # ≈ 1.167  [Murphy & Murphey 2003]
C_boom_lo   = m_ACS3 / A_ACS3**exp_boom_lo
C_boom_hi   = m_ACS3 / A_ACS3**exp_boom_hi
C_boom_lin  = m_ACS3 / A_ACS3  # = 0.025 kg/m²

# Attitude control torque authority
# Source: Wertz et al. "Space Mission Engineering" — typical small-sat RW: 1–10 mN·m
T_RW_lo = 1.0e-3   # [N·m]
T_RW_hi = 10.0e-3  # [N·m]

# CP-offset fraction for wrinkling torque estimate
eps_cp = 0.02   # 2 %  (see panel-c derivation; 0.2–5 % from FEA literature)

# ======================================================================
# GEOMETRY  (from sail geometry derivation)
# ======================================================================
a_hub  = R_hub * np.sin(np.pi / N)
b_hub  = R_hub * np.cos(np.pi / N)
R_sail = np.sqrt(2.0 * A_arr / (N * np.sin(2.0 * np.pi / N)))
L_wire = np.sqrt(R_sail**2 - b_hub**2) - a_hub

# ======================================================================
# DERIVED QUANTITIES
# ======================================================================

# 1. NiTi wire mass
M_wire = {d: N * rho_NiTi * np.pi * r**2 * L_wire
          for d, r in zip(D_WIRES_MM, R_WIRES)}

# Boom mass curves
M_boom_lo  = C_boom_lo  * A_arr**exp_boom_lo
M_boom_hi  = C_boom_hi  * A_arr**exp_boom_hi
M_boom_lin = C_boom_lin * A_arr

# -----------------------------------------------------------------------
# 2.  PANEL (a) — Deployment actuation force safety factor
# -----------------------------------------------------------------------
# PHYSICAL MODEL:
#   The sail is stowed as a radial flasher origami.  On deployment the
#   SMA wires are heated and contract, pulling outer vertices inward;
#   this triggers the flasher kinematic mechanism which opens the panels.
#   The wires must supply enough force to overcome the Kapton membrane's
#   bending resistance at each fold crease.
#
# AVAILABLE force per wire:
#   F_SMA = sigma_recovery × pi × r²   [N]
#   (total SMA recovery force; sigma_recovery is the two-way recovery
#    stress for repeated cycling from Dynalloy TCF1140 datasheet)
#
# REQUIRED force — derivation:
#   For a crease of total length L_wire with curvature 1/R_fold, the
#   restoring moment per unit crease length is:
#       dM/dl = D_flex / R_fold   [N·m/m = N]
#   (D_flex = flexural rigidity of Kapton, R_fold = crease radius)
#
#   Total restoring moment for one fold line of length L_wire:
#       M_fold = (D_flex / R_fold) × L_wire   [N·m]
#
#   For a wire pulling at its tip with effective lever arm L_wire/2
#   (distributed crease force centroid):
#       F_single = M_fold / (L_wire/2) = 2 × D_flex / R_fold   [N]
#   → This is CONSTANT (independent of L_wire or A) for a single fold.
#
#   For a radial flasher pattern that stows a sail of circumradius R_sail
#   into a hub of radius R_hub, the approximate number of radial fold
#   layers is:
#       N_folds ≈ R_sail / R_hub
#   All fold layers must be opened simultaneously, so:
#       F_req = 2 × (D_flex / R_fold) × (R_sail / R_hub)   [N]
#   This gives F_req ∝ R_sail ∝ √A, reflecting the physical reality
#   that a larger sail packs more fold layers into the same hub.
#
# SAFETY FACTOR:
#   SF_dep = F_SMA / F_req

F_avail = {d: sigma_recovery * np.pi * r**2
           for d, r in zip(D_WIRES_MM, R_WIRES)}
F_req   = 2.0 * (D_flex / R_fold) * (R_sail / R_hub)
SF_dep  = {d: F_avail[d] / F_req for d in D_WIRES_MM}

# -----------------------------------------------------------------------
# 3.  PANEL (b) — SRP wire bending stress safety factor
# -----------------------------------------------------------------------
# PHYSICAL MODEL:
#   The SRP creates an out-of-plane pressure on the sail membrane.  This
#   load is transferred to the fold lines (SMA wires) as a distributed
#   transverse load — so the relevant failure mode is BENDING, not axial
#   tension.  Each wire is modelled as a simply-supported beam.
#
# Distributed load per wire:
#   q = P_srp × A / (N × L_wire)   [N/m]
#   (total SRP force shared equally among N wires, distributed over
#    wire length L_wire)
#
# Maximum mid-span bending moment (simply-supported, uniform load):
#   M_max = q × L_wire² / 8   [N·m]
#
# Maximum bending stress (circular cross-section):
#   I     = π r⁴ / 4
#   σ_b   = M_max × r / I = 4 × M_max / (π r³)   [Pa]
#   Stress scales as: σ_b ∝ A × L_wire / r³ ∝ A^(3/2) / r³
#
# Safety factor:
#   SF_bend = σ_yield / σ_b

q_srp  = (P_srp * A_arr / N) / L_wire          # [N/m]
M_max  = q_srp * L_wire**2 / 8.0              # [N·m]
sig_b  = {}
SF_srp = {}
for d, r in zip(D_WIRES_MM, R_WIRES):
    sb = 4.0 * M_max / (np.pi * r**3)         # [Pa]
    sig_b[d]  = sb
    SF_srp[d] = sigma_yield / sb

# -----------------------------------------------------------------------
# 4.  PANEL (c) — Wrinkling disturbance torque
# -----------------------------------------------------------------------
# DERIVATION FROM FIRST PRINCIPLES:
#
# Step 1 — Total SRP force on sail:
#   F_SRP = P_srp × A   [N]
#   (valid for flat sail at normal solar incidence; P_srp accounts for
#    both absorbed and reflected photon momentum)
#
# Step 2 — Centre-of-pressure offset:
#   For a perfectly flat, symmetric sail the CP coincides with the CM
#   (geometric centre) and there is no SRP torque.  Wrinkling shifts the
#   CP by d_cp.  We model:
#       d_cp = ε_cp × L_char   where   L_char = √A
#   The characteristic length is √A because the sail's half-diagonal
#   (and hence any CP displacement scale) grows as √A.
#   The fraction ε_cp is an engineering estimate; FEA simulations of
#   wrinkled square sails (Sleight & Muheim, 45th AIAA SDM, 2004) give
#   CP shifts of ~1–3 % of characteristic length under moderate wrinkling.
#   We use ε_cp = 2 % as a conservative upper-bound.
#   Wie (JGCD 2004) quotes a 40×40 m sail (A=1600 m², ε_cp ≈ 0.2 %)
#   giving T ≈ 1 mN·m; our 2 % estimate for a freshly-stowed sail is
#   therefore a factor ~10× conservative.
#
# Step 3 — Combine:
#   T = F_SRP × d_cp = P_srp × A × ε_cp × √A
#     = P_srp × ε_cp × A^(3/2)   [N·m]
#
# IMPORTANT CAVEAT:
#   This is an order-of-magnitude estimate.  The actual torque depends
#   on the wrinkling pattern, membrane pretension, and solar incidence
#   angle.  Use the plot to identify the scale at which wrinkling torque
#   approaches your RW authority, then carry out a higher-fidelity
#   membrane FEA.

T_wrinkle = P_srp * eps_cp * A_arr**1.5   # [N·m]

# ======================================================================
# PLOT
# ======================================================================
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.patch.set_facecolor('#f8f8f8')

def style_ax(ax, ylabel, title):
    ax.set_facecolor('#ffffff')
    ax.grid(True, which='major', ls='--', lw=0.65, alpha=0.5, color='#aaa')
    ax.grid(True, which='minor', ls=':',  lw=0.40, alpha=0.2, color='#ccc')
    ax.spines[['top','right']].set_visible(False)
    ax.tick_params(labelsize=9.5)
    ax.set_xlabel('Sail Area  A  (m²)', fontsize=10)
    ax.set_ylabel(ylabel, fontsize=10)
    ax.set_title(title, fontsize=11, fontweight='bold', pad=6)
    ax.set_xlim(10, 200)

lw   = 2.2
LBLS = [f'{d} mm' for d in D_WIRES_MM]
lkw  = dict(color='crimson', lw=1.6, ls='--', zorder=6)
fb   = dict(fc='#eef3fa', ec='#8ab', boxstyle='round,pad=0.4', lw=0.8)
fb2  = dict(fc='#fff8e8', ec='#cca', boxstyle='round,pad=0.4', lw=0.8)

# ── (a) Deployment SF ───────────────────────────────────────────────
ax = axes[0, 0]
style_ax(ax, 'Safety Factor  $F_{SMA}\\,/\\,F_{req}$',
         '(a)  Deployment Actuation Force SF')
for d, col, lbl in zip(D_WIRES_MM, COLORS, LBLS):
    ax.semilogy(A_arr, SF_dep[d], color=col, lw=lw, label=lbl)
ax.axhline(1, **lkw, label='SF = 1')
ax.yaxis.set_minor_locator(ticker.LogLocator(subs='all', numticks=15))
ax.legend(title='Wire diam.', fontsize=8.5, title_fontsize=8.5,
          loc='upper left', framealpha=0.9)
ax.text(0.98, 0.05,
        '$F_{SMA}=\\sigma_{rec}\\pi r^2$\n'
        '$F_{req}=2\\,\\frac{D_{flex}}{R_{fold}}\\,\\frac{R_{sail}}{R_{hub}}$',
        transform=ax.transAxes, fontsize=9, va='bottom', ha='right', bbox=fb)

# ── (b) SRP bending SF ──────────────────────────────────────────────
ax = axes[0, 1]
style_ax(ax, 'Safety Factor  $\\sigma_{yield}\\,/\\,\\sigma_{bend}$',
         '(b)  SRP Wire Bending Stress SF')
for d, col, lbl in zip(D_WIRES_MM, COLORS, LBLS):
    ax.semilogy(A_arr, SF_srp[d], color=col, lw=lw, label=lbl)
ax.axhline(1, **lkw, label='SF = 1')
ax.yaxis.set_minor_locator(ticker.LogLocator(subs='all', numticks=15))
ax.legend(title='Wire diam.', fontsize=8.5, title_fontsize=8.5,
          loc='upper right', framealpha=0.9)
ax.text(0.98, 0.38,
        '$q=P_{srp}A/(N L_w)$\n'
        '$M_{max}=qL_w^{2}/8$\n'
        '$\\sigma_{b}=4M_{max}/(\\pi r^{3})$',
        transform=ax.transAxes, fontsize=9, va='bottom', ha='right', bbox=fb)

# ── (c) Wrinkling torque ─────────────────────────────────────────────
ax = axes[1, 0]
style_ax(ax, 'Disturbance Torque  (mN·m)',
         '(c)  Wrinkling Disturbance Torque')
ax.semilogy(A_arr, T_wrinkle * 1e3, color='#4455cc', lw=2.6,
            label='$T$ ($\\varepsilon_{cp}=2\\%$, upper bound)')
ax.axhline(T_RW_lo * 1e3, color='darkorange', lw=1.8, ls='--',
           label='Small-sat RW  1 mN·m')
ax.axhline(T_RW_hi * 1e3, color='firebrick', lw=1.8, ls='-.',
           label='Capable RW  10 mN·m')
ax.fill_between(A_arr, T_wrinkle * 1e3, T_RW_lo * 1e3,
                where=T_wrinkle * 1e3 > T_RW_lo * 1e3,
                color='red', alpha=0.10, zorder=0)
ax.yaxis.set_minor_locator(ticker.LogLocator(subs='all', numticks=15))
ax.legend(fontsize=8.5, loc='upper left', framealpha=0.9)
ax.text(0.98, 0.05,
        '$T = P_{srp}\\,\\varepsilon_{cp}\\,A^{3/2}$\n'
        '(order-of-magnitude: see code notes)',
        transform=ax.transAxes, fontsize=9, va='bottom', ha='right', bbox=fb2)

# ── (d) Wire mass vs boom mass — LINEAR ──────────────────────────────
ax = axes[1, 1]
style_ax(ax, 'Mass  (kg)', '(d)  Wire Mass vs. Sail Area')
ax.fill_between(A_arr, M_boom_lo, M_boom_hi, color='#999', alpha=0.22,
                label=r'CF boom band  ($A^{0.75}$–$A^{7/6}$)', zorder=1)
ax.plot(A_arr, M_boom_lin, color='#444', lw=2.0, ls='--',
        label=r'CF booms  $A^{1}$  (emp.)', zorder=3)
for d, col, lbl in zip(D_WIRES_MM, COLORS, LBLS):
    ax.plot(A_arr, M_wire[d], color=col, lw=lw, label=f'SMA wires  {lbl}', zorder=4)
ax.set_ylim(0, None)
ax.yaxis.set_minor_locator(ticker.AutoMinorLocator(5))
ax.legend(fontsize=8.2, loc='upper left', framealpha=0.9)
ax.text(0.98, 0.05,
        '$M_{wire}=N\\rho_{Ni}\\pi r^2 L_w\\propto\\sqrt{A}$\n'
        'Boom band calibrated to ACS3 point',
        transform=ax.transAxes, fontsize=8.5, va='bottom', ha='right', bbox=fb)

fig.suptitle(
    'Boomless SMA-Deployed Octagonal Solar Sail — Scaling Study  (N=8)',
    fontsize=12.5, fontweight='bold')
fig.tight_layout(rect=[0, 0, 1, 0.97], h_pad=3.5, w_pad=3.0)
out = 'sail_scaling_study.png'
fig.savefig(out, dpi=160, bbox_inches='tight')
plt.close(fig)
print(f"Saved: {os.path.abspath(out)}")
