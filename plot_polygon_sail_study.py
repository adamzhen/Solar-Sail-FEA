import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import math
import os

max_acceptable_deformation = 0.1  # m; arbitrary threshold for "too much" deformation

# =====================================================================
# Parse results
# =====================================================================

run_no = 1.1

results_filepath = f'results/factorial_results_{run_no}.txt'
output_directory = f'results/run_{run_no}'
os.makedirs(output_directory, exist_ok=True)

def parse_results(filepath=results_filepath):
    with open(filepath, 'r') as fh:
        lines = [l.rstrip('\r\n') for l in fh.readlines()]

    # locate section markers
    inp_i = next(i for i, l in enumerate(lines) if l.strip() == 'Inputs')
    out_i = next(i for i, l in enumerate(lines) if l.strip() == 'Outputs')

    def read_section(header_line, data_start, data_end):
        cols  = [c.strip() for c in lines[header_line].split(',')]
        rows  = []
        for line in lines[data_start:data_end]:
            if line.strip():
                rows.append([v.strip() for v in line.split(',')])
        df = pd.DataFrame(rows, columns=cols)
        return df.apply(pd.to_numeric, errors='coerce')

    df_in  = read_section(inp_i + 1, inp_i + 2, out_i)
    df_out = read_section(out_i + 1, out_i + 2, None)

    # strip units from column names so we can reference them easily
    df_in.columns  = [c.split('(')[0].strip() for c in df_in.columns]
    df_out.columns = [c.split('(')[0].strip() for c in df_out.columns]

    df = pd.merge(df_in, df_out, on='run_no')
    # wire_mass per spoke = rho * pi * r^2 * L_wire
    # (already in Outputs; just make sure column is present)
    return df

df = parse_results(results_filepath)

N_vals   = sorted(df['N'].unique().astype(int).tolist())
d_vals   = sorted(df['d_wire'].unique().tolist())
alt_vals = sorted(df['altitude'].unique().astype(int).tolist())

N_colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd',
            '#8c564b', '#e377c2', '#7f7f7f'][:len(N_vals)]
N_cmap   = {n: c for n, c in zip(N_vals, N_colors)}

print('N values:       ', N_vals)
print('Diameters (mm): ', d_vals)
print('Altitudes (km): ', alt_vals)
print('Total rows:     ', len(df))

# =====================================================================
# FIGURE 1: Scatter – max deformation vs wire mass, colored by N
# =====================================================================

fig1, ax1 = plt.subplots(figsize=(8, 5.5))

for n in N_vals:
    sub = df[df['N'] == n]
    ax1.scatter(sub['wire_mass'], sub['max_deformation'],
                color=N_cmap[n], s=30, alpha=0.85,
                edgecolors='white', linewidths=0.4,
                label=f'N = {n}', zorder=3)

ax1.set_xscale('linear')
ax1.xaxis.set_major_locator(plt.MaxNLocator(nbins=10))
ax1.set_yscale('log')
ax1.axhline(y=max_acceptable_deformation, color='red', linestyle='--', linewidth=2, label='Max acceptable deformation', zorder=2)
ax1.set_xlabel('Wire Mass  (kg)', fontsize=11)
ax1.set_ylabel('Max Deformation  (m)', fontsize=11)
ax1.set_title('Max Deformation vs Wire Mass\n'
                '(all altitudes and diameters, colored by N)', fontsize=12)
ax1.legend(title='Polygon sides', fontsize=9)
ax1.grid(True, which='both', alpha=0.3, linestyle='--')
fig1.tight_layout()
fig1.savefig(f'{output_directory}/{run_no}_fig1_deform_vs_mass.png', dpi=150, bbox_inches='tight')
plt.close(fig1)
print('Saved: ' + f'{output_directory}/{run_no}_fig1_deform_vs_mass.png')

# =====================================================================
# HELPER: build NxD Z-matrix for one altitude and one variable
# =====================================================================

def build_grid(df, alt, zvar):
    """Return NN (meshgrid), DD (meshgrid), ZZ (values) for surface plot."""
    sub = df[df['altitude'] == alt] if 'altitude' in df.columns else df
    N_arr = np.array(N_vals, dtype=float)
    D_arr = np.array(d_vals,  dtype=float)
    NN, DD = np.meshgrid(N_arr, D_arr)           # shape (n_d, n_N)
    ZZ = np.zeros_like(NN)
    for ni, n in enumerate(N_vals):
        for di, d in enumerate(d_vals):
            mask = (df['N'] == n) & (df['d_wire'] == d) & (df['altitude'] == alt)
            vals = df.loc[mask, zvar].values
            ZZ[di, ni] = vals[0] if len(vals) else np.nan
    return NN, DD, ZZ

# =====================================================================
# FIGURE 2: 5 × 3D subplots – max deformation (one per altitude)
# =====================================================================

def make_3d_fig(zvar, zlabel, cmap_name, out_fname, suptitle):
    fig2 = plt.figure(figsize=(22, 9))
    # layout: row1 cols 1-3 (altitudes 0-2), row2 cols 1-2 centered (alt 3-4)
    positions = [(2, 3, 1), (2, 3, 2), (2, 3, 3), (2, 3, 4), (2, 3, 5)]
    cmap = plt.get_cmap(cmap_name)

    # compute global z range for a shared colorscale
    all_ZZ = [build_grid(df, alt, zvar)[2] for alt in alt_vals]
    zmin   = min(Z[~np.isnan(Z)].min() for Z in all_ZZ)
    zmax   = max(Z[~np.isnan(Z)].max() for Z in all_ZZ)

    axes = []
    for ai, (alt, ZZ) in enumerate(zip(alt_vals, all_ZZ)):
        ax = fig2.add_subplot(*positions[ai], projection='3d')
        NN, DD, _ = build_grid(df, alt, zvar)
        surf = ax.plot_surface(NN, DD, ZZ, cmap=cmap_name,
                               vmin=zmin, vmax=zmax,
                               edgecolor='none', alpha=0.9)
        ax.set_xlabel('N sides', fontsize=8, labelpad=4)
        ax.set_ylabel('Diameter (mm)', fontsize=8, labelpad=4)
        ax.set_zlabel(zlabel, fontsize=8, labelpad=4)
        ax.set_xticks(N_vals)
        ax.set_yticks(d_vals)
        ax.set_title(f'{alt} km', fontsize=10, pad=6)
        ax.tick_params(labelsize=7)
        ax.view_init(elev=25, azim=-50)
        axes.append(ax)

    # shared colorbar
    sm = plt.cm.ScalarMappable(cmap=cmap_name,
                                norm=plt.Normalize(vmin=zmin, vmax=zmax))
    sm.set_array([])
    cbar = fig2.colorbar(sm, ax=axes, shrink=0.55, pad=0.04,
                         orientation='vertical', aspect=25)
    cbar.set_label(zlabel, fontsize=10)

    fig2.suptitle(suptitle, fontsize=13, y=1.01)
    fig2.tight_layout()
    fig2.savefig(out_fname, dpi=150, bbox_inches='tight')
    plt.close(fig2)
    print('Saved: ' + out_fname)

make_3d_fig(
    zvar       = 'max_deformation',
    zlabel     = 'Max Deformation (m)',
    cmap_name  = 'viridis_r',
    out_fname  = f'{output_directory}/{run_no}_fig2_3d_deformation.png',
    suptitle   = 'Max Deformation (m)  —  N × Wire Diameter  ×  Altitude',
)

make_3d_fig(
    zvar       = 'wire_mass',
    zlabel     = 'Wire Mass (kg)',
    cmap_name  = 'plasma',
    out_fname  = f'{output_directory}/{run_no}_fig3_3d_wiremass.png',
    suptitle   = 'Wire Mass (kg)  —  N × Wire Diameter  (mass is altitude-independent)',
)

# =====================================================================
# Data table: export key values to csv
# =====================================================================

summary_cols = ['N', 'd_wire', 'altitude', 'wire_mass', 'max_deformation']
summary_df = df[summary_cols].copy()
summary_df.columns = ['N', 'Wire Diameter (mm)', 'Altitude (km)', 'Wire Mass (kg)', 'Max Deformation (m)']
summary_df.to_csv(f'{output_directory}/{run_no}_summary_data.csv', index=False)
print('Saved: ' + f'{output_directory}/{run_no}_summary_data.csv')