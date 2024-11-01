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
  - Given that our method primarily aims to optimize the verification process by reusing constraint-solving information to enhance efficiency, we selectively excluded instances with \(K = 1\) from the Kind2 benchmark suite. Such instances have a low frequency of solver calls and thus do not fully demonstrate the advantages of our approach. Additionally, we removed instances of the `real` type, as their solving time is relatively minor, with the majority of time spent on quantifier elimination, which is not representative for evaluating our method. After careful selection, we finalized a total of 701 test cases to constitute the experimental test suite, thereby ensuring the accuracy and validity of the evaluation results.

- **bench-location**
  - These benchmarks are located in the `/kind2-benchmarks-master/` directory. The `/supplement/benchmark.csv` file indexes the paths of the 701 relevant files, facilitating access and utilization of the benchmark data.

### 2. Bin
The directory containing the executable binaries of our tool, including:
- **`IC3_origin`**: The default configuration of the IC3 algorithm in Kind2.
- **`IC3_CS`**: The IC3 acceleration verification algorithm utilizing constraint-solving information reuse, which includes reusing UNSAT cores and satisfiable models.
- **`IC3_UC`**: The IC3 acceleration verification algorithm focusing on the reuse of UNSAT cores.

### 3. Scripts
Python scripts used in our experiments:
- **runIC3_origin.py**: Executes the IC3_origin binary on the benchmarks contained in `kind2-benchmarks-master`.
- **runIC3_CS.py**: Executes the IC3_CS binary for verification on the benchmarks in `kind2-benchmarks-master`.
- **runIC3_UC.py**: Executes the IC3_UC binary for verification on the benchmarks in `kind2-benchmarks-master`.

### 4. Results
- **IC3_origin.xlsx**: Contains the experimental data obtained from running `runIC3_origin.py`.
- **IC3_CS.xlsx**: Contains the experimental data obtained from running `runIC3_CS.py`.
- **IC3_UC.xlsx**: Contains the experimental data obtained from running `runIC3_UC.py`.

### 5. README.md
This file provides an overview of the project structure and instructions.

# Instructions for Reproducing Experimental Data

To reproduce the experimental data, follow these steps .

- **Run the IC3_origin algorithm**  
  Navigate to the `scripts` directory and run:
  ```bash
  cd scripts
  python3 runIC3_origin.py
  ```
  This script uses `IC3_origin` to verify each instance in `kind2-benchmarks-master`, with the results saved in `IC3_origin.xlsx`.
 
- **Run the IC3_CS algorithm**  
  Run the following command to execute IC3_CS:
  ```bash
  python runIC3_CS.py
  ```
  This script uses `IC3_CS` to verify each instance in `kind2-benchmarks-master`, with the results saved in `IC3_CS.xlsx`.

- **Run the IC3_UC algorithm**  
  Run the following command to execute IC3_UC:
  ```bash
  python runIC3_UC.py
  ```
  This script uses `IC3_UC` to verify each instance in `kind2-benchmarks-master`, with the results saved in `IC3_UC.xlsx`.


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
