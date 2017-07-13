import sys
import os
from subprocess import Popen

(script, cn_called) = sys.argv

def load_cn(cn_file):
    cn_dict = {}
    with open(cn_called, 'r') as cn_f:
        next(cn_f)
        for line in cn_f:
            fields = line.split("\t")
            key = fields[0] + fields[1] + fields[2]
            #add to dict markers and mean
            cn_dict[key] = (fields[3], fields[6])
    return(cn_dict)

#aren't considering LOH regions, using mean genome-wide CN value
def get_genome_mean_cn():
    cn_sum, num = 0, 0
    for key in chr_cn_dict:
        num += int(chr_cn_dict[key][0])
        cn_sum += int(chr_cn_dict[key][0]) * float(chr_cn_dict[key][1])
    return(cn_sum/num)

chr_cn_dict = load_cn(cn_called)
avg_neutral_cn = get_genome_mean_cn()
print(avg_neutral_cn)

##unnecessary? creates file with recenter baseline
output = "varscan.output.copynumber.called" +  ".centerinfo"
print(output)
with open(output, 'w') as out_f:
    out_f.write("Recenter baseline:\n")
    out_f.write(str(avg_neutral_cn))
    out_f.close()

#if average neutral copynum is less than zero, recenter down, otherwise, recenter up
output = "varscan.output.copynumber.called" + ".recentered"
cmd = ""
if avg_neutral_cn < 0:
    recenter_baseline = 0 - avg_neutral_cn
    cmd = "java -cp /opt/varscan/VarScan.jar net.sf.varscan.VarScan copyCaller " + cn_called + " --output-file " + output + " --recenter-down " + str(recenter_baseline)
else:
    recenter_baseline = avg_neutral_cn
    cmd = "java -cp /opt/varscan/VarScan.jar net.sf.varscan.VarScan copyCaller " + cn_called + " --output-file " + output + " --recenter-up " + str(recenter_baseline)

print(cmd)
execution = Popen(cmd, shell=True)
execution.communicate()    
if execution.returncode == 0:
    print("Successful")
