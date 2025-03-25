# Running Environment

## I. Experimental Platform
Our experiments are conducted on a high-performance system with the following specifications:
- **Operating System**: Ubuntu 22.04
- **Python Version**: 3.10.6
- **OCaml**: 4.11.0
- **Z3 Solver**: 4.8.12
## II. Project Directory Description

### 1. Benchmark
- **bench-origin**
  - The benchmarks used in this project are sourced from the public repository [https://github.com/kind2-mc/kind2-benchmarks](https://github.com/kind2-mc/kind2-benchmarks).
  - To ensure the fairness and accuracy of the evaluation, we conducted experiments using the standard benchmark suite provided on the official Kind2 website. We excluded cases of the 'real' type, as their SMT solving time is relatively short, with the majority of the time spent on quantifier elimination, making them unsuitable for effectively assessing the impact of our method. After careful selection, we finalized a total of 1,623 test cases to form the experimental test suite, ensuring the accuracy and validity of the evaluation results.
  - In this set of 1,623 test cases, we selected those that could be verified by all four methods for further data analysis. Additionally, since our approach aims to optimize the verification process and improve efficiency by reusing constraint-solving information, cases with k = 0 only require checking whether property P is violated within 0 or 1 steps, without involving key phases, such as the blocking phase. Similarly, cases with k = 1 can find counterexamples where two-step reachability to ¬P is identified in the blocking phase. These cases involve fewer solver calls and do not adequately demonstrate the advantages of our method in reducing solver overhead and accelerating verification. Therefore, we specifically excluded cases with k ≤ 1 from the test set. After filtering, a total of 704 test cases were selected for further experimental analysis.
- **bench-location**
  - These benchmarks are located in the `/kind2-benchmarks-master/` directory. The `/supplement/benchmark.csv` file indexes the paths of 1,623 relevant files, making it easier to access and utilize the benchmark data. Additionally, the `/supplement/benchmark_refine.csv` file indexes the paths of 704 relevant files used for data analysis.

### 2. Bin
The directory containing the executable binaries of our tool, including:
- **`IC3`**: The default configuration of the IC3 algorithm in Kind2.
- **`IC3_UC`**: The IC3 acceleration verification algorithm focusing on the reuse of UNSAT cores.
- **`IC3_SM`**:The IC3 acceleration verification algorithm focusing on the reuse of satisfiable models.
- **`IC3_Dual`**: The IC3 acceleration verification algorithm utilizing constraint-solving information reuse, which includes reusing UNSAT cores and satisfiable models.

### 3. Scripts
The following Python scripts were used in our experiments:

### Execution Scripts

- **runIC3.py**: Executes the IC3 binary on the benchmarks contained in the `kind2-benchmarks-master` directory.
- **runIC3_UC.py**: Executes the IC3_UC binary for verification on the benchmarks in the `kind2-benchmarks-master` directory.
- **runIC3_SM.py**: Executes the IC3_SM binary for verification on the benchmarks in the `kind2-benchmarks-master` directory.
- **runIC3_Dual.py**: Executes the IC3_Dual binary for verification on the benchmarks in the `kind2-benchmarks-master` directory.

### Plotting Scripts

- **cpu_time_compare.py**: Used to plot the data distribution of the number of solved cases with respect to increasing execution time for the four algorithms.
- **hitrate.py**: Used to plot the Hit Rate of UCL and SML in IC3_Dual.
- **scatter_plot.py**: Used to generate scatter plots for the comparison of CPU time among different configurations.

### 4. Results

### Results (All Test Cases)

- **IC3_all.xlsx**: Results of IC3 on 1,623 test cases.
- **IC3_Dual_all.xlsx**: Results of IC3_Dual on 1,623 test cases.
- **IC3_UC_all.xlsx**: Results of IC3_UC on 1,623 test cases.
- **IC3_SM_all.xlsx**: Results of IC3_SM on 1,623 test cases.

### Results (Refined Test Cases)

- **IC3_refine.xlsx**: Results of IC3 on 704 refined test cases.
- **IC3_Dual_refine.xlsx**: Results of IC3_Dual on 704 refined test cases.
- **IC3_UC_refine.xlsx**: Results of IC3_UC on 704 refined test cases.
- **IC3_SM_refine.xlsx**: Results of IC3_SM on 704 refined test cases.

### 5. README.md

This file provides an overview of the project structure and instructions.

# Instructions for Reproducing Experimental Data

To reproduce the experimental data, follow these steps .

- **Run the IC3 algorithm**  
  Navigate to the `scripts` directory and run:
  
  ```bash
  cd scripts
  python3 runIC3.py
  ```
  This script uses `IC3` to verify each instance in `kind2-benchmarks-master`, with the results saved in `IC3.xlsx`.
  
- **Run the IC3_Dual algorithm**  
  Run the following command to execute IC3_Dual:
  
  ```bash
  python3 runIC3_Dual.py
  ```
  This script uses `IC3_Dual` to verify each instance in `kind2-benchmarks-master`, with the results saved in `IC3_Dual.xlsx`.
  
- **Run the IC3_UC algorithm**  
  Run the following command to execute IC3_UC:
  
  ```bash
  python3 runIC3_UC.py
  ```
  This script uses `IC3_UC` to verify each instance in `kind2-benchmarks-master`, with the results saved in `IC3_UC.xlsx`.
  
- **Run the IC3_SM algorithm**  

  Run the following command to execute IC3_SM:

  ```bash
  python3 runIC3_SM.py
  ```

  This script uses `IC3_SM` to verify each instance in `kind2-benchmarks-master`, with the results saved in `IC3_SM.xlsx`.

  


# Explanation of Results

For each instance, the results include these key data points:

- **result**: Provides the verification result, which can be one of the following values:
  - `valid`: Verification succeeded
  - `invalid`: Verification failed
  - `unknown`: Verification status could not be determined
  - `timeout`: Verification exceeded the allowed time
- **ic3_total_time**: Represents the total time consumed by the IC3 algorithm during the verification process.
- **ic3_solver**: Solver invocations .
- **ic3_assert_time**: Represents the time taken by the IC3 algorithm to add assertions to the solver.
- **ic3_check_sat_time**: Indicates the time taken by the IC3 algorithm to check the satisfiability of the formula.
- **ic3_get_unsat_core_time**: Represents the time taken by the IC3 algorithm to obtain the unsatisfiable core (Get-unsat-core).
- **get_value_time**: Represents the time taken by the IC3 algorithm to obtain satisfiable models.
- **ic3_get_unsat_core_time**: Represents the time taken by the IC3 algorithm to obtain the unsatisfiable core (Get-unsat-core).
- **ic3_extra_ucl**: Represents the additional time spent by the IC3 algorithm when using UCL, beyond standard operations.
- **ic3_add_ucl**: Represents the additional time spent on updating the UCL (Unsatisfiable Core Library).
- **ic3_check_ucl**: Represents the additional time spent on checking the UCL.
- **ic3_add_SML**: Represents the additional time spent on updating the SML (Satisfiable Model Library).
- **ic3_extra_SML**: Represents the additional time spent on processing SML operations.
- **ic3_extra_time_c**: Represents the additional time spent on SML when verifying specific C.
- **ic3_extra_time_c_n1**: Represents the additional time spent on SML when verifying  ¬C.
- **ic3_extra_time_F**: Represents the additional time spent on SML when verifying F.
