import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('TkAgg')  # Or try other backends such as 'Qt5Agg', 'Agg'
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter

# Define colors (darker versions)
colors = {
    'H_UC_ind': '#9B59B6',    # Dark purple
    'H_UC_init': '#1976D2',   # Dark blue
    'H_UCL_init': '#388E3C',   # Dark green
    'H_SML_ind': '#E64A19',  # Dark orange
}

# Read Excel file
excel_file = pd.ExcelFile('experimental-result-main/scripts/PlottingScripts/Plotting_data/Scatter_Plot_and_Hit_Rate_Data.xlsx')
df = excel_file.parse('origin')

# Convert string data to numerical values
df['IC3 origin'] = pd.to_numeric(df['ic3_origin'], errors='coerce')
df['IC3_Dual'] = pd.to_numeric(df['ic3_dual'], errors='coerce')
df['f_reuse_sml'] = pd.to_numeric(df['f_reuse_sml'], errors='coerce')
df['f_reuse_ucl'] = pd.to_numeric(df['f_reuse_ucl'], errors='coerce')
df['i_reuse_ucl'] = pd.to_numeric(df['i_reuse_ucl'], errors='coerce')
df['i_reuse_sml'] = pd.to_numeric(df['i_reuse_sml'], errors='coerce')

# Compute runtime ratio and take logarithm
df['IC3_Dual_runtime_ratio'] = np.log10(df['IC3 origin'] / df['IC3_Dual'])

# Extract data for plotting
Dual_runtime_ratio = df['IC3_Dual_runtime_ratio'].values

f_reuse_ucl = df['f_reuse_ucl'].values
i_reuse_ucl = df['i_reuse_ucl'].values
f_reuse_sml = df['f_reuse_sml'].values
i_reuse_sml = df['i_reuse_sml'].values

# Create a figure with two subplots
fig, axs = plt.subplots(1, 2, figsize=(12, 5))  # Adjust overall size

# Set global font size
plt.rcParams.update({'font.size': 12})

# Plot first subplot: UCL hit rate vs. runtime ratio
axs[0].scatter(f_reuse_ucl, Dual_runtime_ratio, label='$H_{UL\_ind}$', marker='o', s=15, color=colors['H_UC_ind'], alpha=0.7)
axs[0].scatter(i_reuse_ucl, Dual_runtime_ratio, label='$H_{UL\_init}$', marker='o', s=15, color=colors['H_UC_init'], alpha=0.7)
axs[0].set_xlabel('UCL hit rate (%) - IC3_Dual', fontsize=12)
axs[0].set_ylabel(r'$\lg(t_{IC3} / t_{IC3\_Dual})$', fontsize=12)  # Use \lg notation
axs[0].axhline(0, color='gray', linestyle='--', linewidth=0.8)
axs[0].grid(True, linestyle='--', alpha=0.5)
axs[0].legend(fontsize=10)

# Plot second subplot: SML hit rate vs. runtime ratio
axs[1].scatter(f_reuse_sml, Dual_runtime_ratio, label='$H_{SL\_ind}$', marker='o', s=15, color=colors['H_SML_ind'], alpha=0.7)
axs[1].scatter(i_reuse_sml, Dual_runtime_ratio, label='$H_{SL\_init}$', marker='o', s=15, color=colors['H_UCL_init'], alpha=0.7)  # Use H_UCL_init color
axs[1].set_xlabel('SML hit rate (%) - IC3_Dual', fontsize=12)
axs[1].set_ylabel(r'$\lg(t_{IC3} / t_{IC3\_Dual})$', fontsize=12)  # Use \lg notation
axs[1].axhline(0, color='gray', linestyle='--', linewidth=0.8)
axs[1].grid(True, linestyle='--', alpha=0.5)
axs[1].legend(fontsize=10)

# Adjust spacing between subplots
plt.tight_layout()

# Add main title
plt.suptitle("Runtime Ratios vs. Hit Rates for IC3_Dual", fontsize=16, y=1.05)

# Show plot
plt.show()
