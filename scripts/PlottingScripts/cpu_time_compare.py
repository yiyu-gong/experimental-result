import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('TkAgg')  # Or try other backends such as 'Qt5Agg', 'Agg'
import matplotlib.pyplot as plt

# Read the Excel file
excel_file = pd.ExcelFile('experimental-result-main/scripts/PlottingScripts/Plotting_data/benchmark_all_cputime_compare.xlsx')

# Retrieve data from the specified worksheet
df = excel_file.parse('output')

# Convert string data to numerical values and read specific columns
df['IC3'] = pd.to_numeric(df['IC3_origin'], errors='coerce')
df['IC3_Dual'] = pd.to_numeric(df['IC3_Dual'], errors='coerce')
df['IC3_UC'] = pd.to_numeric(df['IC3_UC'], errors='coerce')
df['IC3_SM'] = pd.to_numeric(df['IC3_SM'], errors='coerce')  # Add a new column

# Count the number of test cases solved within different time intervals for each method
time_intervals = np.arange(0, 510, 10)
method1_counts = np.zeros(len(time_intervals) - 1)
method2_counts = np.zeros(len(time_intervals) - 1)
method3_counts = np.zeros(len(time_intervals) - 1)
method4_counts = np.zeros(len(time_intervals) - 1)  # Add counter for method 4

for i in range(len(time_intervals) - 1):
    method1_counts[i] = df[(df['IC3'] >= time_intervals[i]) & (df['IC3'] < time_intervals[i + 1])].shape[0]
    method2_counts[i] = df[(df['IC3_Dual'] >= time_intervals[i]) & (df['IC3_Dual'] < time_intervals[i + 1])].shape[0]
    method3_counts[i] = df[(df['IC3_UC'] >= time_intervals[i]) & (df['IC3_UC'] < time_intervals[i + 1])].shape[0]
    method4_counts[i] = df[(df['IC3_SM'] >= time_intervals[i]) & (df['IC3_SM'] < time_intervals[i + 1])].shape[0]  # Add statistics

# Compute the cumulative number of solved test cases
method1_cumulative_counts = np.cumsum(method1_counts)
method2_cumulative_counts = np.cumsum(method2_counts)
method3_cumulative_counts = np.cumsum(method3_counts)
method4_cumulative_counts = np.cumsum(method4_counts)  # Add cumulative computation

# Set figure resolution
plt.rcParams['figure.dpi'] = 150

# Set font style
plt.rcParams['font.sans-serif'] = ['Arial']
plt.rcParams['font.size'] = 10  # Increase font size

# Plot line chart
plt.figure(figsize=(6, 4))  # Increase chart size
plt.plot(time_intervals[:-1], method1_cumulative_counts, linestyle='-', color='blue', label='IC3')
plt.plot(time_intervals[:-1], method3_cumulative_counts, linestyle='-.', color='green', label='IC3_UC')
plt.plot(time_intervals[:-1], method4_cumulative_counts, linestyle=':', color='red', label='IC3_SM')  # Add method 4
plt.plot(time_intervals[:-1], method2_cumulative_counts, linestyle='--', color='orange', label='IC3_Dual')

# Set x-axis range
plt.xlim(left=0)
# plt.ylim(bottom=0)

# Set chart title and labels
# plt.title('Number of Test Cases Solved Over Time', fontsize=12)  # Increase title font size
plt.xlabel('Time(s)', fontsize=10)  # Increase axis label font size
plt.yticks(fontsize=8)  # Increase tick font size
plt.xticks(np.arange(0, max(time_intervals) + 50, 50), fontsize=8)
plt.ylabel('Cases Solved', fontsize=10)  # Increase axis label font size

# Set legend
plt.legend(loc='lower right')  # Adjust legend position

# Display the chart
plt.tight_layout()  # Automatically adjust subplot parameters to fit into the figure area
plt.show()
