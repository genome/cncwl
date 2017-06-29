import sys
from subprocess import Popen, PIPE

(script, chr_file, norm, tum, ref, ratio_file, varscan_params, output) = sys.argv

#separate chromosome number:
parts = str(chr_file).split(".")
chromo = parts[0]
print(chromo)

#get ratio from file
with open(ratio_file, 'r') as ratio_f:
    lines = []
    for line in ratio_f:
        lines.append(line)
    ratio = lines[1]
    print(ratio)
## not using output variable
this = "~/opt/samtools" 

mpileup = "mpileup -f " +  ref + " -B -q 10 -r " + "chromo" + ":1 " + norm + " " +  tum

cmd = "bash -c \"java -jar /gsc/scripts/lib/java/VarScan/VarScan.v2.3.1.jar copynumber < (/opt/samtools " + mpileup + " " + chr_file + " --mpileup 1 --data-ratio " + ratio + " " +  varscan_params + '\"'
total = "bsub -q research-hpc -R\"select[mem>2000 && tmp>2000] rusage[mem=2000]\" -J vsCn -oo  " + chr_file + ".log -Is -a 'docker(mneveau/docker-cle:concordance_addition)' " + cmd

#creating syntax error
everything = "bsub -q research-hpc -R\"select[mem>2000 && tmp>2000] rusage[mem=2000]\" -J vsCn -oo  " + chr_file + ".log -Is -a 'docker(mneveau/docker-cle:concordance_addition)' bash -c \"java -jar /gsc/scripts/lib/java/VarScan/VarScan.v2.3.1.jar copynumber < '(/opt/samtools mpileup -f " +  ref + " -B -q 10 -r " + chromo + ":1 " + norm + " " +  tum ")'" + chr_file + " --mpileup 1 --data-ratio " + ratio + " " +  varscan_params + '\"'

print(total)

execution = Popen(everything, shell=True)
execution.communicate()

