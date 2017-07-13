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

##newMPileupCmd = '/opt/samtools/bin/samtools mpileup -f /gscmnt/gc3018/info/medseq/tmp/mneveau/all_sequences.fa -B -q 10 -r 1:1 /gscmnt/gc12001/info/build_merged_alignments/merged-alignment-blade12-3-6.gsc.wustl.edu-apipe-builder-29030-123189855/123189855.bam /gscmnt/gc12001/info/build_merged_alignments/merged-alignment-blade10-4-7.gsc.wustl.edu-apipe-builder-8390-123170111/123170111.bam >mpileup2'

##newJavaCmd = 'java -jar /opt/varscan/VarScan.jar copynumber mpileup2 out2 --mpileup 1 --data-ratio 1 --min-coverage 20 --min-segment-size 25 --max-segment-size 100'

print(cmd)

execution = Popen(cmd, shell=True)
execution.communicate()

#execute
#execution = Popen(newMPileupCmd, shell=True)
#execution.communicate()

#execution = Popen(newJavaCmd, shell=True)
#execution.communicate()

