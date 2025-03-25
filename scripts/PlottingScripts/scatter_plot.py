import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('TkAgg')  # or 'Agg'
import matplotlib.pyplot as plt

# Define colors
colors = {
    'H_UCL_ind': '#D32F2F',   # Dark Red
    'H_UCL_init': '#303F9F',  # Dark Blue
    'H_SML_ind': '#388E3C',   # Dark Green
    'H_SML_init': '#E64A19',  # Dark Orange
    'H_UC_ind': '#9B59B6',    # Dark Purple
    'H_UC_init': '#1976D2',   # Deep Blue
}

# Read Excel file
excel_file = pd.ExcelFile('experimental-result-main/scripts/PlottingScripts/Plotting_data/Scatter_Plot_and_Hit_Rate_Data.xlsx')

# Retrieve data from the specified sheet
df = excel_file.parse('origin')

# Convert string data to numeric values, selecting specific columns from the table
df['IC3 origin'] = pd.to_numeric(df['ic3_origin'], errors='coerce')
df['IC3_Dual'] = pd.to_numeric(df['ic3_dual'], errors='coerce')
df['IC3_UC'] = pd.to_numeric(df['ic3_uc'], errors='coerce')
df['IC3_SM'] = pd.to_numeric(df['ic3_sm'], errors='coerce')

# Filter out non-positive data points
df = df[(df['IC3 origin'] > 0) & (df['IC3_Dual'] > 0) & (df['IC3_UC'] > 0) & (df['IC3_SM'] > 0)]

# Create subplots
fig, axs = plt.subplots(2, 3, figsize=(18, 10))  # Create a 2x3 subplot layout

# Define diagonal lines for each subplot
min_val = df[['IC3 origin', 'IC3_Dual', 'IC3_UC', 'IC3_SM']].min().min()
max_val = df[['IC3 origin', 'IC3_Dual', 'IC3_UC', 'IC3_SM']].max().max()

# First row: IC3_SM vs IC3 origin, IC3_UC vs IC3 origin, IC3_Dual vs IC3 origin
# Subplot 1: IC3_SM vs IC3 origin
axs[0, 0].scatter(df['IC3 origin'], df['IC3_Dual'], marker='x', color=colors['H_UCL_ind'], s=10)  # Dark Red
axs[0, 0].plot([min_val, max_val], [min_val, max_val], 'k--')
axs[0, 0].set_xscale('log')
axs[0, 0].set_yscale('log')
axs[0, 0].set_xlabel('IC3', fontsize=14)
axs[0, 0].set_ylabel('IC3_Dual', fontsize=14)
axs[0, 0].set_title('IC3_Dual vs IC3', fontsize=16)

# Subplot 2: IC3_UC vs IC3 origin
axs[0, 1].scatter(df['IC3 origin'], df['IC3_UC'], marker='o', color=colors['H_UC_ind'], s=10)  # Dark Purple
axs[0, 1].plot([min_val, max_val], [min_val, max_val], 'k--')
axs[0, 1].set_xscale('log')
axs[0, 1].set_yscale('log')
axs[0, 1].set_xlabel('IC3', fontsize=14)
axs[0, 1].set_ylabel('IC3_UC', fontsize=14)
axs[0, 1].set_title('IC3_UC vs IC3', fontsize=16)

# Subplot 3: IC3_Dual vs IC3 origin
axs[0, 2].scatter(df['IC3 origin'], df['IC3_SM'], marker='o', color=colors['H_SML_ind'], s=10)  # Dark Green
axs[0, 2].plot([min_val, max_val], [min_val, max_val], 'k--')
axs[0, 2].set_xscale('log')
axs[0, 2].set_yscale('log')
axs[0, 2].set_xlabel('IC3', fontsize=14)
axs[0, 2].set_ylabel('IC3_SM', fontsize=14)
axs[0, 2].set_title('IC3_SM vs IC3', fontsize=16)

# Subplot 4: IC3_Dual vs IC3_SM
axs[1, 0].scatter(df['IC3_SM'], df['IC3_Dual'], marker='s', color=colors['H_SML_init'], s=10)  # Dark Orange
axs[1, 0].plot([min_val, max_val], [min_val, max_val], 'k--')
axs[1, 0].set_xscale('log')
axs[1, 0].set_yscale('log')
axs[1, 0].set_xlabel('IC3_SM', fontsize=14)
axs[1, 0].set_ylabel('IC3_Dual', fontsize=14)
axs[1, 0].set_title('IC3_Dual vs IC3_SM', fontsize=16)

# Second row: IC3_Dual vs IC3_UC, IC3_Dual vs IC3_SM, IC3_UC vs IC3_SM
# Subplot 5: IC3_Dual vs IC3_UC
axs[1, 1].scatter(df['IC3_UC'], df['IC3_Dual'], marker='x', color=colors['H_UC_init'], s=10)  # Deep Blue
axs[1, 1].plot([min_val, max_val], [min_val, max_val], 'k--')
axs[1, 1].set_xscale('log')
axs[1, 1].set_yscale('log')
axs[1, 1].set_xlabel('IC3_UC', fontsize=14)
axs[1, 1].set_ylabel('IC3_Dual', fontsize=14)
axs[1, 1].set_title('IC3_Dual vs IC3_UC', fontsize=16)

# Subplot 6: IC3_UC vs IC3_SM
axs[1, 2].scatter(df['IC3_SM'], df['IC3_UC'], marker='o', color=colors['H_UCL_init'], s=10)  # Dark Blue
axs[1, 2].plot([min_val, max_val], [min_val, max_val], 'k--')
axs[1, 2].set_xscale('log')
axs[1, 2].set_yscale('log')
axs[1, 2].set_xlabel('IC3_SM', fontsize=14)
axs[1, 2].set_ylabel('IC3_UC', fontsize=14)
axs[1, 2].set_title('IC3_UC vs IC3_SM', fontsize=16)

# Adjust subplot layout
plt.tight_layout()

# Display the plot
plt.show()
