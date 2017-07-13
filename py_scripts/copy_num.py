import sys
from subprocess import Popen, PIPE

(script, chr_file, norm, tum, ref, ratio_file, varscan_params) = sys.argv

#separate chromosome number:
dirs = str(chr_file).split("/")
parts = dirs[-1].split(".")
chromo = parts[0]
print(chromo)

#get ratio from file
with open(ratio_file, 'r') as ratio_f:
    lines = []
    for line in ratio_f:
        lines.append(line)
    ratio = lines[1]
    print(ratio)

#build mpileup command
mpileup = '/opt/samtools/bin/samtools mpileup -f ' +  ref + ' -B -q 10 -r ' + chromo + ':1 ' + norm + ' ' +  tum

#build java command, creates output file (chrnum).copynumber
cmd = 'bash -c "java -jar /opt/varscan/VarScan.jar copynumber <(' + mpileup + ') ' + chromo + ' --mpileup 1 --data-ratio ' + ratio + " " +  varscan_params + '"'

execution = Popen(cmd, shell=True)
execution.communicate()

