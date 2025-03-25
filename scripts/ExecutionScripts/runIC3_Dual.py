import os
import csv
import subprocess
import re
from concurrent.futures import ThreadPoolExecutor
def run_kind2(file_name):
    
    kind2_command = f"/usr/bin/time -v ./kind2 --enable IC3QE -vv --color false --timeout 500 {file_name}.lus"
    try:
        output = subprocess.run(kind2_command, shell=True, capture_output=True, text=True, timeout=500)
        # print(output)
        print(file_name)
        # 定义正则表达式模式
        pattern_ic3_k = re.compile(r'Final statistics:[\s\S]*?\[IC3QE\][\s\S]*?k\s+:\s+([\d.]+)')
        pattern_ic3_frame_sizes = re.compile(r'Final statistics:[\s\S]*?\[IC3QE\][\s\S]*?Frame sizes\s+:\s+(\d+(?:\s+\d+)*)')
        pattern_ic3_solver = re.compile(r'Final statistics:[\s\S]*?\[IC3QE\][\s\S]*?solver\s+:\s+(\S+)')
    
        pattern_ic3_total_time = re.compile(r'Final statistics:[\s\S]*?\[IC3QE\][\s\S]*?IC3 Total time\s+:\s+([\d.]+)')

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

        pattern_i_ucl = re.compile(r'Final statistics:[\s\S]*?\[IC3QE\][\s\S]*?i_ucl\s+:\s+([\d.]+)')
        pattern_i_reuse_ucl = re.compile(r'Final statistics:[\s\S]*?\[IC3QE\][\s\S]*?i_reuse_ucl\s+:\s+([\d.]+)')
        pattern_f_ucl = re.compile(r'Final statistics:[\s\S]*?\[IC3QE\][\s\S]*?f_ucl\s+:\s+([\d.]+)')
        pattern_f_reuse_ucl = re.compile(r'Final statistics:[\s\S]*?\[IC3QE\][\s\S]*?f_reuse_ucl\s+:\s+([\d.]+)')
        pattern_f_sml = re.compile(r'Final statistics:[\s\S]*?\[IC3QE\][\s\S]*?f_sml\s+:\s+([\d.]+)')
        pattern_f_reuse_sml = re.compile(r'Final statistics:[\s\S]*?\[IC3QE\][\s\S]*?f_reuse_sml\s+:\s+([\d.]+)')
        pattern_sml_ind_length = re.compile(r'Final statistics:[\s\S]*?\[IC3QE\][\s\S]*?sml_ind_length\s+:\s+(\d+)')
        pattern_ul_ind_length = re.compile(r'Final statistics:[\s\S]*?\[IC3QE\][\s\S]*?ul_ind_length\s+:\s+(\d+)')
        pattern_ul_init_length = re.compile(r'Final statistics:[\s\S]*?\[IC3QE\][\s\S]*?ul_init_length\s+:\s+(\d+)')
        pattern_sml_ind_mem = re.compile(r'Final statistics:[\s\S]*?\[IC3QE\][\s\S]*?sml_ind_mem\s+:\s+([\d.]+)')
        pattern_ul_ind_mem = re.compile(r'Final statistics:[\s\S]*?\[IC3QE\][\s\S]*?ul_ind_mem\s+:\s+([\d.]+)')
        pattern_ul_init_mem = re.compile(r'Final statistics:[\s\S]*?\[IC3QE\][\s\S]*?ul_init_mem\s+:\s+([\d.]+)')

        pattern_sml_init_length = re.compile(r'Final statistics:[\s\S]*?\[IC3QE\][\s\S]*?sml_init_length\s+:\s+(\d+)')
        pattern_sml_init_mem = re.compile(r'Final statistics:[\s\S]*?\[IC3QE\][\s\S]*?sml_init_mem\s+:\s+([\d.]+)')
        pattern_i_sml = re.compile(r'Final statistics:[\s\S]*?\[IC3QE\][\s\S]*?i_sml\s+:\s+([\d.]+)')
        pattern_i_reuse_sml = re.compile(r'Final statistics:[\s\S]*?\[IC3QE\][\s\S]*?i_reuse_sml\s+:\s+([\d.]+)')
        pattern_ic3_extra_time_n0 = re.compile(r'Final statistics:[\s\S]*?\[IC3QE\][\s\S]*?extra_time_n0\s+:\s+([\d.]+)')
        max_size = re.compile(r"Maximum resident set size \(kbytes\): (\d+)")

        match_ic3_k = pattern_ic3_k.search(output.stdout)   
        match_ic3_frame_sizes = pattern_ic3_frame_sizes.search(output.stdout)
        match_ic3_solver = pattern_ic3_solver.search(output.stdout)
        match_ic3_total_time = pattern_ic3_total_time.search(output.stdout)
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

        match_i_ucl = pattern_i_ucl.search(output.stdout)
        match_i_reuse_ucl = pattern_i_reuse_ucl.search(output.stdout)
        match_f_ucl = pattern_f_ucl.search(output.stdout)
        match_f_reuse_ucl = pattern_f_reuse_ucl.search(output.stdout)
        match_f_sml = pattern_f_sml.search(output.stdout)
        match_f_reuse_sml = pattern_f_reuse_sml.search(output.stdout)
        match_sml_ind_length = pattern_sml_ind_length.search(output.stdout)
        match_ul_ind_length = pattern_ul_ind_length.search(output.stdout)
        match_ul_init_length = pattern_ul_init_length.search(output.stdout)
        match_sml_ind_mem = pattern_sml_ind_mem.search(output.stdout)
        match_ul_ind_mem = pattern_ul_ind_mem.search(output.stdout)
        match_ul_init_mem = pattern_ul_init_mem.search(output.stdout)

        match_sml_init_length = pattern_sml_init_length.search(output.stdout)
        match_sml_init_mem = pattern_sml_init_mem.search(output.stdout)
        match_i_sml = pattern_i_sml.search(output.stdout)
        match_i_reuse_sml = pattern_i_reuse_sml.search(output.stdout)
        match_ic3_extra_time_n0 = pattern_ic3_extra_time_n0.search(output.stdout)
        match_max_size = max_size.search(output.stderr)

        valid_match = re.search(r'<Success> Property .* is valid .*', output.stdout)
        invalid_match = re.search(r'<Failure> Property .* is invalid .*', output.stdout)
        if valid_match:
            result = "valid"
        elif invalid_match:
            result = "invalid"
        else:
            result = "unknown"

        # 提取匹配结果
        # 提取匹配结果
        ic3_k = match_ic3_k.group(1) if match_ic3_k else "N/A"
        ic3_frame_sizes = match_ic3_frame_sizes.group(1) if match_ic3_frame_sizes else "N/A"
        ic3_solver = match_ic3_solver.group(1) if match_ic3_solver else "N/A"
        ic3_total_time = match_ic3_total_time.group(1) if match_ic3_total_time else "N/A"
        ic3_assert_time = match_assert_time.group(1) if match_assert_time else "N/A"
        ic3_check_sat_time = match_check_sat_time.group(1) if match_check_sat_time else "N/A"
        ic3_get_unsat_core_time = match_get_unsat_core_time.group(1) if match_get_unsat_core_time else "N/A"
        ic3_get_value_time = match_get_value_time.group(1) if match_get_value_time  else"N/A"

        ic3_extra_ucl = match_ic3_extra_ucl.group(1) if match_ic3_extra_ucl else "N/A"
        ic3_add_ucl = match_ic3_add_ucl.group(1) if match_ic3_add_ucl else "N/A"
        ic3_check_ucl = match_ic3_check_ucl.group(1) if match_ic3_check_ucl else "N/A"

        ic3_extra_sml = match_ic3_extra_sml.group(1) if match_ic3_extra_sml else "N/A"
        ic3_add_sml = match_ic3_add_sml.group(1) if match_ic3_add_sml else "N/A"

        
        ic3_extra_time_c = match_extra_time_c.group(1) if match_extra_time_c else "N/A"
        ic3_extra_time_c_n1 = match_extra_time_c_n1.group(1) if match_extra_time_c_n1 else "N/A"
        ic3_extra_time_F = match_extra_time_F.group(1) if match_extra_time_F else "N/A"


        i_ucl = match_i_ucl.group(1) if match_i_ucl else "N/A"
        i_reuse_ucl = match_i_reuse_ucl.group(1) if match_i_reuse_ucl else "N/A"
        f_ucl = match_f_ucl.group(1) if match_f_ucl else "N/A"
        f_reuse_ucl = match_f_reuse_ucl.group(1) if match_f_reuse_ucl else "N/A"
        f_sml = match_f_sml.group(1) if match_f_sml else "N/A"
        f_reuse_sml = match_f_reuse_sml.group(1) if match_f_reuse_sml else "N/A"
        sml_ind_length = match_sml_ind_length.group(1) if match_sml_ind_length else "N/A"
        ul_ind_length = match_ul_ind_length.group(1) if match_ul_ind_length else "N/A"
        ul_init_length = match_ul_init_length.group(1) if match_ul_init_length else "N/A"
        sml_ind_mem = match_sml_ind_mem.group(1) if match_sml_ind_mem else "N/A"
        ul_ind_mem = match_ul_ind_mem.group(1) if match_ul_ind_mem else "N/A"
        ul_init_mem = match_ul_init_mem.group(1) if match_ul_init_mem else "N/A"
        sml_init_length = match_sml_init_length.group(1) if match_sml_init_length else "N/A"
        sml_init_mem = match_sml_init_mem.group(1) if match_sml_init_mem else "N/A"
        i_sml = match_i_sml.group(1) if match_i_sml else "N/A"
        i_reuse_sml = match_i_reuse_sml.group(1) if match_i_reuse_sml else "N/A"
        ic3_extra_time_n0 = match_ic3_extra_time_n0.group(1) if match_ic3_extra_time_n0 else "N/A"
        ic3_max_size = match_max_size.group(1) if match_max_size else "N/A"


        return file_name, result, ic3_k, ic3_total_time, ic3_frame_sizes, ic3_solver, ic3_extra_ucl, ic3_add_ucl, ic3_check_ucl, ic3_add_sml, ic3_extra_sml, ic3_extra_time_c, ic3_extra_time_c_n1, ic3_extra_time_F, ic3_assert_time, ic3_check_sat_time, ic3_get_unsat_core_time, ic3_get_value_time, i_ucl, i_reuse_ucl, f_ucl, f_reuse_ucl, f_sml, f_reuse_sml, sml_ind_length, ul_ind_length, ul_init_length, sml_ind_mem, ul_ind_mem, ul_init_mem,sml_init_length, sml_init_mem, i_sml, i_reuse_sml, ic3_extra_time_n0 ,ic3_max_size

    except subprocess.TimeoutExpired:
        # 如果超时，输出超时信息
        return file_name,"timeout","N/A","N/A",	"N/A",	"N/A",	"N/A",	"N/A",	"N/A",	"N/A",	"N/A",	"N/A",	"N/A",	"N/A",	"N/A","N/A",	"N/A",	"N/A",	"N/A",	"N/A",	"N/A","N/A",	"N/A",	"N/A",	"N/A",	"N/A",	"N/A","N/A",	"N/A",	"N/A","N/A",	"N/A",	"N/A","N/A", "N/A" , "N/A"

def process_model(model_file):
    file_name, result, ic3_k, ic3_total_time, ic3_frame_sizes, ic3_solver, ic3_extra_ucl, ic3_add_ucl, ic3_check_ucl, ic3_add_sml, ic3_extra_sml, ic3_extra_time_c, ic3_extra_time_c_n1, ic3_extra_time_F, ic3_assert_time, ic3_check_sat_time, ic3_get_unsat_core_time, ic3_get_value_time, i_ucl, i_reuse_ucl, f_ucl, f_reuse_ucl, f_sml, f_reuse_sml, sml_ind_length, ul_ind_length, ul_init_length, sml_ind_mem, ul_ind_mem, ul_init_mem ,sml_init_length, sml_init_mem, i_sml, i_reuse_sml, ic3_extra_time_n0 , ic3_max_size = run_kind2(model_file)
    return file_name, result, ic3_k, ic3_total_time, ic3_frame_sizes, ic3_solver, ic3_extra_ucl, ic3_add_ucl, ic3_check_ucl, ic3_add_sml, ic3_extra_sml, ic3_extra_time_c, ic3_extra_time_c_n1, ic3_extra_time_F, ic3_assert_time, ic3_check_sat_time, ic3_get_unsat_core_time, ic3_get_value_time, i_ucl, i_reuse_ucl, f_ucl, f_reuse_ucl, f_sml, f_reuse_sml, sml_ind_length, ul_ind_length, ul_init_length, sml_ind_mem, ul_ind_mem, ul_init_mem , sml_init_length, sml_init_mem, i_sml, i_reuse_sml, ic3_extra_time_n0 ,ic3_max_size

def batch_run_kind2(input_csv, output_csv):


    with open(output_csv, mode="w", newline="", encoding="utf-8") as output_csv_file:
      
        csv_writer = csv.writer(output_csv_file)

        csv_writer.writerow(["Model", "result", "ic3_k", "ic3_total_time", "ic3_frame_sizes", "ic3_solver", "ic3_extra_ucl", "ic3_add_ucl", "ic3_check_ucl", "ic3_add_sml", "ic3_extra_sml", "ic3_extra_time_c", "ic3_extra_time_c_n1", "ic3_extra_time_F",  "ic3_assert_time", "ic3_check_sat_time", "ic3_get_unsat_core_time","get_value_time", "i_ucl", "i_reuse_ucl", "f_ucl", "f_reuse_ucl", "f_sml", "f_reuse_sml",  "sml_ind_length", "ul_ind_length", "ul_init_length", "sml_ind_mem", "ul_ind_mem", "ul_init_mem", "sml_init_length", "sml_init_mem", "i_sml", "i_reuse_sml", "ic3_extra_time_n0","max_size"])

        with open(input_csv, mode="r", newline="", encoding="utf-8") as csv_file:
            csv_reader = csv.reader(csv_file)
            model_files = [model[0] for model in csv_reader]

        with ThreadPoolExecutor(max_workers=1) as executor: 
            results = executor.map(process_model, model_files)

            for result in results:
                csv_writer.writerow(result)
    print("Batch processing completed. Results saved to", output_csv)


batch_run_kind2("/experimental-result-main/supplement/benchmark.csv", "IC3_Dual_all.csv")
