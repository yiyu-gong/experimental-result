import os
import csv
import subprocess
import re
from concurrent.futures import ThreadPoolExecutor
def run_kind2(file_name):
 
    kind2_command = f"/usr/bin/time -v ./IC3 --enable IC3QE -vv --color false --timeout 500 {file_name}.lus"
    try:
        output = subprocess.run(kind2_command, shell=True, capture_output=True, text=True, timeout=500)
        # print(output)
        print(file_name)
        
        pattern_ic3_k = re.compile(r'Final statistics:[\s\S]*?\[IC3QE\][\s\S]*?k\s+:\s+([\d.]+)')
        pattern_ic3_frame_sizes = re.compile(r'Final statistics:[\s\S]*?\[IC3QE\][\s\S]*?Frame sizes\s+:\s+(\d+(?:\s+\d+)*)')
        pattern_ic3_solver = re.compile(r'Final statistics:[\s\S]*?\[IC3QE\][\s\S]*?solver\s+:\s+(\S+)')
        pattern_ind_solver = re.compile(r'Final statistics:[\s\S]*?\[IC3QE\][\s\S]*?ind_solver\s+:\s+(\S+)')
        pattern_ic3_total_time = re.compile(r'Final statistics:[\s\S]*?\[IC3QE\][\s\S]*?IC3 Total time\s+:\s+([\d.]+)')
        pattern_ic3_ind_gen_time = re.compile(r'Final statistics:[\s\S]*?\[IC3QE\][\s\S]*?Inductive_generalization_time:\s+([\d.]+)')

        pattern_assert_time = re.compile(r'Final statistics:[\s\S]*?\[SMT\][\s\S]*?assert-term time\s+:\s+([\d.]+)')
        pattern_check_sat_time = re.compile(r'Final statistics:[\s\S]*?\[SMT\][\s\S]*?check-sat time\s+:\s+([\d.]+)')
        pattern_get_unsat_core_time = re.compile(r'Final statistics:[\s\S]*?\[SMT\][\s\S]*?get-unsat-core time:\s+([\d.]+)')
        pattern_get_value_timee = re.compile(r'Final statistics:[\s\S]*?\[SMT\][\s\S]*?get-value time\s+:\s+([\d.]+)')
        max_size = re.compile(r"Maximum resident set size \(kbytes\): (\d+)")

        match_ic3_k = pattern_ic3_k.search(output.stdout)   
        match_ic3_frame_sizes = pattern_ic3_frame_sizes.search(output.stdout)
        match_ic3_solver = pattern_ic3_solver.search(output.stdout)
        match_ind_solver = pattern_ind_solver.search(output.stdout)
        match_ic3_total_time = pattern_ic3_total_time.search(output.stdout)
        match_ic3_ind_gen_time = pattern_ic3_ind_gen_time.search(output.stdout)
        match_assert_time = pattern_assert_time.search(output.stdout)
        match_check_sat_time = pattern_check_sat_time.search(output.stdout)
        match_get_unsat_core_time = pattern_get_unsat_core_time.search(output.stdout)
        match_get_value_time = pattern_get_value_timee.search(output.stdout)
        match_max_size = max_size.search(output.stderr)
        valid_match = re.search(r'<Success> Property .* is valid .*', output.stdout)
        invalid_match = re.search(r'<Failure> Property .* is invalid .*', output.stdout)
        if valid_match:
            result = "valid"
        elif invalid_match:
            result = "invalid"
        else:
            result = "unknown"

       
        ic3_k = match_ic3_k.group(1) if match_ic3_k else "N/A"
        ic3_frame_sizes = match_ic3_frame_sizes.group(1) if match_ic3_frame_sizes else "N/A"
        ic3_solver = match_ic3_solver.group(1) if match_ic3_solver else "N/A"
        ind_solver = match_ind_solver.group(1) if match_ind_solver else "N/A"
        ic3_total_time = match_ic3_total_time.group(1) if match_ic3_total_time else "N/A"
        ic3_ind_gen_time = match_ic3_ind_gen_time.group(1) if match_ic3_ind_gen_time else "N/A"
        ic3_assert_time = match_assert_time.group(1) if match_assert_time else "N/A"
        ic3_check_sat_time = match_check_sat_time.group(1) if match_check_sat_time else "N/A"
        ic3_get_unsat_core_time = match_get_unsat_core_time.group(1) if match_get_unsat_core_time else "N/A"
        ic3_get_value_time = match_get_value_time.group(1) if match_get_value_time  else"N/A"
        ic3_max_size = match_max_size.group(1) if match_max_size else "N/A"
 

        return file_name,result, ic3_k, ic3_total_time,ic3_frame_sizes, ic3_solver,ind_solver,   ic3_ind_gen_time,ic3_assert_time,ic3_check_sat_time,ic3_get_unsat_core_time,ic3_get_value_time,ic3_max_size

    except subprocess.TimeoutExpired:
        # timeout
        return file_name,"timeout","N/A",	"N/A",	"N/A",	"N/A",	"N/A",	"N/A",	"N/A",	"N/A",	"N/A",	"N/A"	,"N/A"

def process_model(model_file):
    file_name,result, ic3_k, ic3_total_time,ic3_frame_sizes, ic3_solver,ind_solver,   ic3_ind_gen_time,ic3_assert_time,ic3_check_sat_time,ic3_get_unsat_core_time,ic3_get_value_time , ic3_max_size = run_kind2(model_file)
    return file_name,result, ic3_k, ic3_total_time,ic3_frame_sizes, ic3_solver,ind_solver,   ic3_ind_gen_time,ic3_assert_time,ic3_check_sat_time,ic3_get_unsat_core_time,ic3_get_value_time,ic3_max_size

def batch_run_kind2(input_csv, output_csv):
   

    # open CSV file, write data
    with open(output_csv, mode="w", newline="", encoding="utf-8") as output_csv_file:
        # define csv writer
        csv_writer = csv.writer(output_csv_file)

        csv_writer.writerow(["Model", "result", "ic3_k", "ic3_total_time" , "ic3_frame_sizes" , "ic3_solver" ,"ind_solver" ,  "ic3_ind_gen_time" , "ic3_assert_time" , "ic3_check_sat_time", "ic3_get_unsat_core_time","get_value_time","max_size"])

        with open(input_csv, mode="r", newline="", encoding="utf-8") as csv_file:
           
            csv_reader = csv.reader(csv_file)
            model_files = [model[0] for model in csv_reader]
   
        with ThreadPoolExecutor(max_workers=1) as executor: 
            results = executor.map(process_model, model_files)

    
            for result in results:
                csv_writer.writerow(result)
    print("Batch processing completed. Results saved to", output_csv)

# 调用批量运行函数
batch_run_kind2("/experimental-result-main/supplement/benchmark.csv", "IC3_all.csv")
