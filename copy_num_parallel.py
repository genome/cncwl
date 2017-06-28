
#!/usr/bin/env python

import sys, os
import argparse
from subprocess import Popen, PIPE

##rid of any params not needed for this part
parser = argparse.ArgumentParser()
parser.add_argument("-I_norm")
parser.add_argument("-I_tum")
parser.add_argument("-R")
parser.add_argument("-O")
##do we want this to work for a selection of chromosomes?
#chromo = parser.add_argument("--chromo")
parser.add_argument("--data_ratio")
parser.add_argument("--varscan_params")
args = parser.parse_args()
norm = args.I_norm
tum = args.I_tum
ref = args.R
output = args.O
varscan_params = args.varscan_params
norm_tum_ratio = args.data_ratio

#get duplicate and mapped values
def get_flagstat(bam):
    flagstat = bam + ".flagstat"
    if os.path.isfile(bam + ".flagstat") == False:
        print("Flagstat does not exist for " + bam)
        sys.exit()
    values, lines  = [], []
    with open(flagstat, 'r') as flag_f:
        for line in flag_f:
            lines.append(line)
        dup = lines[1].split(" ")
        values.append(dup[0])
        mapped = lines[2].split(" ")
        values.append(mapped[0])
        print(values)
    return(values)

def calc_avg_read_len(bam):
    reads_file = bam + ".reads"
    execution = Popen("samtools view " + bam + " 2>/dev/null | head -10000 | cut -f 10> " + reads_file, shell=True)
    execution.communicate()
    len_sum, len_num = 0, 0
    with open(reads_file, 'r') as reads_f:
        for line in reads_f:
            len_sum = len_sum +  len(line)
            len_num += 1
        if len_num == 0:
            print("No lines in " + bam)
    avg_readlen = len_sum / len_num 
    return(avg_readlen)

#quit if index doesn't exist
ref_index = ref + ".fai"
if os.path.isfile(ref_index) == False:
    print("Reference index file does not exist")
    sys.exit()


if varscan_params != None:
    print("Do something with varscan params")
    ##write to file to use as script? 

#use provided norm_tum ratio or compute it
if norm_tum_ratio == None:
    print("Find ratio: ")
    norm_values = get_flagstat(norm)
    tum_values = get_flagstat(tum)
    read_len_norm = calc_avg_read_len(norm)
    read_len_tum = calc_avg_read_len(tum)

    uniq_bp_norm = (int(norm_values[1]) - int(norm_values[0])) * read_len_norm
    uniq_bp_tum = (int(tum_values[1]) - int(tum_values[0])) * read_len_tum
    
    norm_tum_ratio = uniq_bp_norm / uniq_bp_tum
    print(norm_tum_ratio)
else:
    print("Using provided ratio:" + norm_tum_ratio)
    
with open(ref_index, 'r') as index_f:
    chromos = []
    for line in index_f:
        fields = line.split("\t")
        if fields[0][0:2] != 'GL' and fields[0][0:2] != 'MT':
            chromos.append(fields[0])
    input_files = []
    for chromo in chromos:
        input_files.append(output + "." + chromo + ".copynumber")
    print(chromos)
    print(input_files)
    for file in input_files:
       os.open(file, os.O_CREAT)
## with open(file, 'w+') as f:
            
            

    #for chrom in chroms:
        






