import sys, os, re
from subprocess import Popen
copy_num_files = []
outdir = sys.argv[1]
output = sys.argv[-1]
for f in sys.argv[2:-1]:
    copy_num_files.append(f)
##maybe change tmp_f to "tmp" within os.stat

def sort_human(l):
  convert = lambda text: float(text) if text.isdigit() else text
  alphanum = lambda key: [ convert(c) for c in re.split('([-+]?[0-9]*\.?[0-9]*)', key) ]
  l.sort( key=alphanum )
  return l

with open("tmp_file", 'a+') as tmp_f:
    with open(output, 'w') as out_f:
        for f in copy_num_files:
            lines = []
            with open(f, 'r') as cn_f:
                for line in cn_f:
                    lines.append(line)
                if os.stat("tmp_file").st_size == 0:
                    print("Printing header for: ")
                    print(f)
                    out_f.write(lines[0])
                    for line in lines[1:]:
                        tmp_f.write(line)
                    print(os.stat("tmp_file").st_size)
                else:
                    print("Printing no header for: ")
                    print(f)
                    for line in lines[1:]:
                        tmp_f.write(line)
            cn_f.close()
        tmp_f.seek(0)
        lines_to_sort = []
        #for line in tmp_f:
        #    fields = line.split("\t")
        #    lines_to_sort.append(fields)
        #for line in sorted(lines_to_sort):
        #    out_f.write(('\t').join(line))
        for line in tmp_f:
            lines_to_sort.append(line)
        
        sorted_line = sort_human(lines_to_sort)

        for line in sorted_line:
            out_f.write(line)
    out_f.close()
tmp_f.close()

cmd = "cp " + output + " " +  outdir
print(cmd)
execution = Popen(cmd, shell=True)
execution.communicate()
