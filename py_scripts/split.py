import os, sys

#quit if index doesn't exist
ref = sys.argv[1]
ref_index = ref + ".fai"
if os.path.isfile(ref_index) == False:
    print("Reference index file does not exist")
    sys.exit()

with open(ref_index, 'r') as index_f:
    chromos = []
    for line in index_f:
        fields = line.split("\t")
        if fields[0][0:2] != 'GL' and fields[0][0:2] != 'MT':
            chromos.append(fields[0])
    input_files = []
    for chromo in chromos:
        input_files.append(chromo + ".copynumber")
    print(chromos)
    print(input_files)
    for file in input_files:
       os.open(file, os.O_CREAT)
