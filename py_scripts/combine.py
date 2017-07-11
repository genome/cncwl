import sys, os
from subprocess import Popen
copy_num_files = []
outdir = sys.argv[1]
output = sys.argv[-1]
for f in sys.argv[2:-1]:
    copy_num_files.append(f)
##maybe change tmp_f to "tmp" within os.stat

with open ("tmp_file", 'a+') as tmp_f:
    with open(output, 'w') as out_f:
        for f in copy_num_files:
            lines = []
            with open(f, 'r') as cn_f:
                for line in cn_f:
                    lines.append(line)
                if os.stat(tmp_f).st_size == 0:
                    print("Printing header for: ")
                    print(f)
                    for line in lines:
                        tmp_f.write(line)
                    print(os.stat(tmp_f).st_size)
                else:
                    print("Printing no header for: ")
                    print(f)
                    for line in lines[1:]:
                        tmp_f.write(line)
            cn_f.close()
        tmp_f.seek(0)
        lines_to_sort = []
        for line in tmp_f:
            lines_to_sort.append(line)
        for line in sorted(lines_to_sort, key=lambda x: (x[0].isdigit(), x)):
            out_f.write(line)
    out_f.close()
tmp_f.close()

cmd = "cp " + output + " " +  outdir
print(cmd)
execution = Popen(cmd, shell=True)
execution.communicate()
