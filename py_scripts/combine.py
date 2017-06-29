import sys

(script, copy_num_files) = sys.argv
output = varscan.output.copynumber
with open(output, 'w') as out_f:
    lines = []
    for line in copy_num_file[0]:
        lines.append(line)
    out_f.write(lines[0])
    for cn_file in copy_num_files:
        with open(cn_file, 'r') as cn_f:
            lines = []
            for line in cn_file:
                lines.append(line)
                for line in lines[1:-1]:
                    cn_f.write(line)
            out_f.close()
