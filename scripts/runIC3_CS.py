import os
import csv
import subprocess
import re
from concurrent.futures import ThreadPoolExecutor
def run_kind2(file_name):

    kind2_command = f"./bin/IC3_CS --enable IC3QE -vv --color false --timeout 500 {file_name}.lus"
    try:
        output = subprocess.run(kind2_command, shell=True, capture_output=True, text=True, timeout=500)
        # print(output)
        print(file_name)
        # Define regex pattern
        pattern_ic3_k = re.compile(r'Final statistics:[\s\S]*?\[IC3QE\][\s\S]*?k\s+:\s+([\d.]+)')
        pattern_ic3_frame_sizes = re.compile(r'Final statistics:[\s\S]*?\[IC3QE\][\s\S]*?Frame sizes\s+:\s+(\d+(?:\s+\d+)*)')
        pattern_ic3_solver = re.compile(r'Final statistics:[\s\S]*?\[IC3QE\][\s\S]*?solver\s+:\s+(\S+)')
        pattern_ind_solver = re.compile(r'Final statistics:[\s\S]*?\[IC3QE\][\s\S]*?ind_solver\s+:\s+(\S+)')
        pattern_ic3_total_time = re.compile(r'Final statistics:[\s\S]*?\[IC3QE\][\s\S]*?IC3 Total time\s+:\s+([\d.]+)')
        pattern_ic3_ind_gen_time = re.compile(r'Final statistics:[\s\S]*?\[IC3QE\][\s\S]*?Inductive_generalization_time\s+:\s+([\d.]+)')

        pattern_assert_time = re.compile(r'Final statistics:[\s\S]*?\[SMT\][\s\S]*?assert-term time\s+:\s+([\d.]+)')
        pattern_check_sat_time = re.compile(r'Final statistics:[\s\S]*?\[SMT\][\s\S]*?check-sat time\s+:\s+([\d.]+)')
        pattern_get_unsat_core_time = re.compile(r'Final statistics:[\s\S]*?\[SMT\][\s\S]*?get-unsat-core time:\s+([\d.]+)')

        pattern_get_value_timee = re.compile(r'Final statistics:[\s\S]*?\[SMT\][\s\S]*?get-value time\s+:\s+([\d.]+)')
        pattern_ic3_extra_ucl = re.compile(r'Final statistics:[\s\S]*?\[IC3QE\][\s\S]*?extra_UCL\s+:\s+([\d.]+)')
        pattern_ic3_add_ucl = re.compile(r'Final statistics:[\s\S]*?\[IC3QE\][\s\S]*?add_UCL\s+:\s+([\d.]+)')
        pattern_ic3_check_ucl = re.compile(r'Final statistics:[\s\S]*?\[IC3QE\][\s\S]*?check_UCL\s+:\s+([\d.]+)')

        pattern_ic3_extra_sml = re.compile(r'Final statistics:[\s\S]*?\[IC3QE\][\s\S]*?extra_SML\s+:\s+([\d.]+)')
        pattern_ic3_add_sml = re.compile(r'Final statistics:[\s\S]*?\[IC3QE\][\s\S]*?add_SML\s+:\s+([\d.]+)')
        pattern_extra_time_c  = re.compile(r'Final statistics:[\s\S]*?\[IC3QE\][\s\S]*?extra_time_block\s+:\s+([\d.]+)')
        pattern_extra_time_c_n1 = re.compile(r'Final statistics:[\s\S]*?\[IC3QE\][\s\S]*?extra_time_n1\s+:\s+([\d.]+)')
        pattern_extra_time_F = re.compile(r'Final statistics:[\s\S]*?\[IC3QE\][\s\S]*?extra_time_F\s+:\s+([\d.]+)')


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

        match_ic3_extra_ucl = pattern_ic3_extra_ucl.search(output.stdout)
        match_ic3_add_ucl = pattern_ic3_add_ucl.search(output.stdout)
        match_ic3_check_ucl = pattern_ic3_check_ucl.search(output.stdout)

        match_ic3_extra_sml = pattern_ic3_extra_sml.search(output.stdout)
        match_ic3_add_sml = pattern_ic3_add_sml.search(output.stdout)

        match_extra_time_c = pattern_extra_time_c.search(output.stdout)
        match_extra_time_c_n1 = pattern_extra_time_c_n1.search(output.stdout)
        match_extra_time_F = pattern_extra_time_F.search(output.stdout)


        valid_match = re.search(r'<Success> Property .* is valid .*', output.stdout)
        invalid_match = re.search(r'<Failure> Property .* is invalid .*', output.stdout)
        if valid_match:
            result = "valid"
        elif invalid_match:
            result = "invalid"
        else:
            result = "unknown"

        # Extracting the matching result 

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

        ic3_extra_UCL = match_ic3_extra_ucl.group(1) if match_ic3_extra_ucl else "N/A"
        ic3_add_UCL = match_ic3_add_ucl.group(1) if match_ic3_add_ucl else "N/A"
        ic3_check_UCL = match_ic3_check_ucl.group(1) if match_ic3_check_ucl else "N/A"

        ic3_extra_SML = match_ic3_extra_sml.group(1) if match_ic3_extra_sml else "N/A"
        ic3_add_SML = match_ic3_add_sml.group(1) if match_ic3_add_sml else "N/A"

        
        ic3_extra_time_c = match_extra_time_c.group(1) if match_extra_time_c else "N/A"
        ic3_extra_time_c_n1 = match_extra_time_c_n1.group(1) if match_extra_time_c_n1 else "N/A"
        ic3_extra_time_F = match_extra_time_F.group(1) if match_extra_time_F else "N/A"




        return file_name,result, ic3_k, ic3_total_time,ic3_frame_sizes, ic3_solver,ic3_extra_UCL,ic3_add_UCL,ic3_check_UCL,ic3_add_SML,ic3_extra_SML, ic3_extra_time_c,ic3_extra_time_c_n1,ic3_extra_time_F,ind_solver,   ic3_ind_gen_time,ic3_assert_time,ic3_check_sat_time,ic3_get_unsat_core_time,ic3_get_value_time

    except subprocess.TimeoutExpired:
        # if timeout occurs,output time message
        return file_name,"timeout","N/A",	"N/A",	"N/A",	"N/A",	"N/A",	"N/A",	"N/A",	"N/A",	"N/A",	"N/A",	"N/A",	"N/A",	"N/A",	"N/A",	"N/A","N/A",	"N/A",	"N/A"

def process_model(model_file):
    file_name,result, ic3_k, ic3_total_time,ic3_frame_sizes, ic3_solver,ic3_extra_UCL,ic3_add_UCL,ic3_check_UCL,ic3_add_SML,ic3_extra_SML, ic3_extra_time_c,ic3_extra_time_c_n1,ic3_extra_time_F,ind_solver,   ic3_ind_gen_time,ic3_assert_time,ic3_check_sat_time,ic3_get_unsat_core_time,ic3_get_value_time = run_kind2(model_file)
    return file_name,result, ic3_k, ic3_total_time,ic3_frame_sizes, ic3_solver,ic3_extra_UCL,ic3_add_UCL,ic3_check_UCL,ic3_add_SML,ic3_extra_SML, ic3_extra_time_c,ic3_extra_time_c_n1,ic3_extra_time_F,ind_solver,   ic3_ind_gen_time,ic3_assert_time,ic3_check_sat_time,ic3_get_unsat_core_time,ic3_get_value_time

def batch_run_kind2(input_csv, output_csv):

    with open(output_csv, mode="w", newline="", encoding="utf-8") as output_csv_file:
        # define CSV  writer
        csv_writer = csv.writer(output_csv_file)

        # writer CSV writerow
        csv_writer.writerow(["Model", "result", "ic3_k", "ic3_origin_time" , "ic3_frame_sizes" , "ic3_solver" ,"ic3_extra_ucl", "ic3_add_ucl","ic3_check_ucl","ic3_add_SML","ic3_extra_SML","ic3_extra_time_c" ," ic3_extra_time_c_n1" , "ic3_extra_time_F" , "ind_solver" ,  "ic3_ind_gen_time" , "ic3_assert_time" , "ic3_check_sat_time", "ic3_get_unsat_core_time","get_value_time"])

        with open(input_csv, mode="r", newline="", encoding="utf-8") as csv_file:
            # define CSV reader
            csv_reader = csv.reader(csv_file)
            model_files = [model[0] for model in csv_reader]
   
    # use ThreadPoolExecutor 
        with ThreadPoolExecutor(max_workers=1) as executor: 
            results = executor.map(process_model, model_files)
         # write the result to CSV 
            for result in results:
                csv_writer.writerow(result)
    print("Batch processing completed. Results saved to", output_csv)

# Call the batch run function
batch_run_kind2("/bin/moredata.csv", "IC3_CS.csv")
