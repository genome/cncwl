import sys, os, re
from subprocess import Popen
seg_files = []
outdir = sys.argv[1]
output = sys.argv[-1]
for f in sys.argv[2:-1]:
    seg_files.append(f)

def sort_human(l):
    convert = lambda text: float(text) if text.isdigit() else text
    alphanum = lambda key: [ convert(c) for c in re.split('([-+]?[0-9]*\.?[0-9]*)', key) ]
    l.sort( key=alphanum )
    return l

with open("tmp_file", 'a+') as tmp_f:
    with open(output, 'w') as out_f:
        for f in seg_files:
            lines = []
            with open(f, 'r') as cn_f:
                for line in cn_f:
                    lines.append(line)
                if os.stat("tmp_file").st_size == 0:
                    print("Printing header for: ")
                    print(f)
                    print(lines[0])
                    header_fields = ["ID", "sample", "chrom", "loc.start", "loc.end", "num.mark", "seg.mean", "bstat", "pval", "lcl", "ucl\n", ] 
                    header = "\t".join(header_fields)
                    out_f.write(header)
                    for line in lines[1:]:
                        tmp_f.write(line)
                    print(os.stat("tmp_file").st_size)
                else:
                    print("Printing no header for: ")
                    print(f)
                    for line in lines[1:]:
                        tmp_f.write(line)
                    print(os.stat("tmp_file").st_size)
            cn_f.close()
        tmp_f.seek(0)
        lines_to_sort = []
        for line in tmp_f:
            split_line = line.split(" ")
            split_line[2], split_line[0] = split_line[0], split_line[2]
            sort_split_line = "\t".join(split_line)
            lines_to_sort.append(sort_split_line)
        print(lines_to_sort[:5])
        #for line in sorted(lines_to_sort, key=lambda x: x[1]):
        sorted_lines = sort_human(lines_to_sort)
        for line in sorted_lines:
            split_line = line.split("\t")
            split_line[0], split_line[2] = split_line[2], split_line[0]
            sort_split_line = "\t".join(split_line)
            out_f.write(sort_split_line)
    out_f.close()
tmp_f.close()

#cmd = "cp " + output + " " +  outdir
#print(cmd)
#execution = Popen(cmd, shell=True)
#execution.communicate()
