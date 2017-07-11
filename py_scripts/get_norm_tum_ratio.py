#!/usr/bin/env python
import sys
import os
from subprocess import Popen

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

#calculate avg read length for a bam
def calc_avg_read_len(bam):
    reads_file = bam + ".reads"
    cmd = "samtools view " + bam + " | head -10000 | cut -f 10 >" + reads_file
    print(cmd)
    execution = Popen(cmd, shell=True)
    execution.communicate()
    print("Communication finished")
    len_sum, len_num = 0, 0
    with open(reads_file, 'r') as reads_f:
        for line in reads_f:
            len_sum = len_sum +  len(line)
            len_num += 1
        if len_num == 0:
            print("No lines in " + bam)
            sys.exit()
    avg_readlen = len_sum / (len_num * 1.0) 
    print("Average read length: ")
    print(avg_readlen)
    return(avg_readlen)

(script, norm, tum) = sys.argv
if len(sys.argv) == 3:
    ratio = None
elif len(sys.argv) == 4:
    ratio = sys.argv[3]
output = "output.ratio"
with open(output, 'w+') as ratio_f:
    ratio_f.write("Normal/Tumor Ratio\n")
#if normal/tumor ratio was provided, use this, else compute it
    if ratio != None:
        ratio_f.write(str(ratio))
    else:
        print("Find ratio: ")
        norm_values = get_flagstat(norm)
        tum_values = get_flagstat(tum)
        read_len_norm = calc_avg_read_len(norm)
        read_len_tum = calc_avg_read_len(tum)

        uniq_bp_norm = (int(norm_values[1]) - int(norm_values[0])) * read_len_norm
        uniq_bp_tum = (int(tum_values[1]) - int(tum_values[0])) * read_len_tum
    
        norm_tum_ratio = uniq_bp_norm / uniq_bp_tum
 
        ratio_f.write(str(norm_tum_ratio))
    ratio_f.close()
    print(norm_tum_ratio)
    
#/gscmnt/gc12001/info/build_merged_alignments/merged-alignment-blade12-3-6.gsc.wustl.edu-apipe-builder-29030-123189855/123189855.bam /gscmnt/gc12001/info/build_merged_alignments/merged-alignment-blade10-4-7.gsc.wustl.edu-apipe-builder-8390-123170111/123170111.bam
