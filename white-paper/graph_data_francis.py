# This file converts dictionary of case_ID and Value into 3D surface graph


#=================================================================================
# Generate the 3D surface graph
#=================================================================================
import re
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D


# Abaqus Case_ID : maximum displacement (m)
displacement_data = {
    'A20_D0p0005': 3.503773,
    'A20_D0p001': 2.586100,
    'A20_D0p0015': 1.125883,
    'A20_D0p002': 0.399359,
    'A20_D0p0025': 0.165684,


    'A50_D0p0005': 5.786058,
    'A50_D0p001': 5.286636,
    'A50_D0p0015': 4.308163,
    'A50_D0p002': 2.814896,
    'A50_D0p0025': 1.500227,


    'A100_D0p0005': 8.358884,
    'A100_D0p001': 7.950987,
    'A100_D0p0015': 7.355083,
    'A100_D0p002': 6.389957,
    'A100_D0p0025': 5.008001,


    'A150_D0p0005': 10.264720,
    'A150_D0p001': 9.927347,
    'A150_D0p0015': 9.449410,
    'A150_D0p002': 8.741940,
    'A150_D0p0025': 7.703323,


    'A200_D0p0005': 11.812070,
    'A200_D0p001': 11.572140,
    'A200_D0p0015': 11.159630,
    'A200_D0p002': 10.573360,
    'A200_D0p0025': 9.743808
}




# ------------------------------------------------------------------------------
# Parse Case_ID values:
# Example: A20_D0p0005 --> sail area = 20 m², diameter = 0.0005 m
# ------------------------------------------------------------------------------
parsed_data = []


for case_id, max_displacement in displacement_data.items():
    match = re.match(r'^A(\d+)_D(\d+)p(\d+)$', case_id)


    if match is None:
        raise ValueError(
            f'Case ID "{case_id}" does not match the expected pattern, '
            'for example: A20_D0p0005'
        )


    sail_area = float(match.group(1))
    wire_diameter_m = float(
        match.group(2) + '.' + match.group(3)
    )


    parsed_data.append(
        (sail_area, wire_diameter_m, max_displacement)
    )




# Obtain sorted unique sail areas and diameters directly from the dictionary.
sail_areas = np.array(
    sorted({row[0] for row in parsed_data}),
    dtype=float
)


wire_diameters_m = np.array(
    sorted({row[1] for row in parsed_data}),
    dtype=float
)


wire_diameters_mm = wire_diameters_m * 1000.0




# ------------------------------------------------------------------------------
# Create a surface-data matrix from the dictionary entries
# Rows = sail areas; columns = wire diameters
# ------------------------------------------------------------------------------
max_displacement_m = np.full(
    (len(sail_areas), len(wire_diameters_m)),
    np.nan
)


for sail_area, wire_diameter_m, max_displacement in parsed_data:
    area_index = np.where(sail_areas == sail_area)[0][0]
    diameter_index = np.where(
        wire_diameters_m == wire_diameter_m
    )[0][0]


    max_displacement_m[area_index, diameter_index] = max_displacement




if np.isnan(max_displacement_m).any():
    raise ValueError(
        'At least one sail-area/wire-diameter combination is missing '
        'from displacement_data.'
    )




# ------------------------------------------------------------------------------
# Create 3D surface plot
# ------------------------------------------------------------------------------
area_grid, diameter_grid = np.meshgrid(
    sail_areas,
    wire_diameters_mm,
    indexing='ij'
)


fig = plt.figure(figsize=(11, 8))
ax = fig.add_subplot(111, projection='3d')


surface = ax.plot_surface(
    area_grid,
    diameter_grid,
    max_displacement_m,
    cmap='viridis',
    edgecolor='black',
    linewidth=0.5,
    antialiased=True,
    alpha=0.90
)


ax.scatter(
    area_grid.ravel(),
    diameter_grid.ravel(),
    max_displacement_m.ravel(),
    color='black',
    s=24,
    depthshade=False,
    label='Abaqus simulation results'
)


ax.set_xlabel('Sail area (m²)', labelpad=12)
ax.set_ylabel('Wire diameter (mm)', labelpad=12)
ax.set_zlabel('Maximum displacement (m)', labelpad=12)


ax.set_title(
    'Maximum Wire Displacement vs. Sail Area and Wire Diameter',
    pad=20
)


ax.set_xticks(sail_areas)
ax.set_yticks(wire_diameters_mm)


ax.view_init(elev=28, azim=-135)


colorbar = fig.colorbar(surface, ax=ax, shrink=0.65, pad=0.12)
colorbar.set_label('Maximum displacement (m)')


ax.legend(loc='upper left')


plt.tight_layout()


plt.savefig(
    'sail_area_wire_diameter_max_displacement_3d.png',
    dpi=300,
    bbox_inches='tight'
)


#=================================================================================
# Generate the 2D graph
#=================================================================================


# ------------------------------------------------------------------------------
# X = sail area
# Y = maximum displacement
# Color = wire diameter
# Marker shape = sail area
# ------------------------------------------------------------------------------


# One marker shape assigned to each sail area.
area_markers = {
    20.0: 'o',     # Circle
    50.0: 's',     # Square
    100.0: '^',    # Triangle up
    150.0: 'D',    # Diamond
    200.0: 'P'     # Filled plus
}




# One color assigned to each wire diameter.
diameter_colors = {
    0.5: '#440154',    # Purple
    1.0: '#3b528b',    # Blue
    1.5: '#21918c',    # Teal
    2.0: '#5ec962',    # Green
    2.5: '#fde725'     # Yellow
}




fig_2d, ax_2d = plt.subplots(figsize=(11, 7))




# Plot each area / diameter result.
for area_index, sail_area in enumerate(sail_areas):
    for diameter_index, wire_diameter_mm in enumerate(wire_diameters_mm):


        ax_2d.scatter(
            sail_area,
            max_displacement_m[area_index, diameter_index],
            color=diameter_colors[wire_diameter_mm],
            marker=area_markers[sail_area],
            s=115,
            edgecolors='black',
            linewidths=0.7,
            zorder=3
        )




# Connect equivalent diameter values across different sail areas.
# These lines help show the displacement trend for each wire diameter.
for diameter_index, wire_diameter_mm in enumerate(wire_diameters_mm):


    ax_2d.plot(
        sail_areas,
        max_displacement_m[:, diameter_index],
        color=diameter_colors[wire_diameter_mm],
        linewidth=1.2,
        alpha=0.55,
        zorder=1
    )




ax_2d.set_xlabel('Sail area (m²)', fontsize=12)
ax_2d.set_ylabel('Maximum displacement (m)', fontsize=12)


ax_2d.set_title(
    'Maximum Wire Displacement by Sail Area and Wire Diameter',
    fontsize=14,
    pad=14
)


ax_2d.set_xticks(sail_areas)
ax_2d.grid(True, linestyle='--', linewidth=0.6, alpha=0.6)
ax_2d.set_axisbelow(True)




# ------------------------------------------------------------------------------
# Legend 1: colors represent wire diameter
# ------------------------------------------------------------------------------
diameter_legend_handles = [
    Line2D(
        [0],
        [0],
        marker='o',
        color='white',
        markerfacecolor=diameter_colors[wire_diameter_mm],
        markeredgecolor='black',
        markersize=9,
        label=f'{wire_diameter_mm:.1f} mm'
    )
    for wire_diameter_mm in wire_diameters_mm
]






# ------------------------------------------------------------------------------
# Legend 2: marker shapes represent sail area
# ------------------------------------------------------------------------------
area_legend_handles = [
    Line2D(
        [0],
        [0],
        marker=area_markers[sail_area],
        color='white',
        markerfacecolor='lightgray',
        markeredgecolor='black',
        markersize=9,
        label=f'{int(sail_area)} m²'
    )
    for sail_area in sail_areas
]


plt.tight_layout()


plt.savefig(
    'sail_area_wire_diameter_max_displacement_2d.png',
    dpi=300,
    bbox_inches='tight'
)


diameter_legend = ax_2d.legend(
    handles=diameter_legend_handles,
    title='Wire diameter',
    loc='upper left',
    bbox_to_anchor=(0.00, 1.00),
    frameon=True
)


ax_2d.add_artist(diameter_legend)


ax_2d.legend(
    handles=area_legend_handles,
    title='Sail area / marker',
    loc='upper left',
    bbox_to_anchor=(0.19, 1.00),
    frameon=True
)


plt.show()