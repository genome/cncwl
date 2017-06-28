cwlVersion: v1.0
class: CommandLineTool
baseCommand: ['python', '/gscmnt/gc3018/info/medseq/tmp/mneveau/combine.py']
label: "Combine all chromosomes to one copynumber output file"
inputs:
    copy_num_files:
        type: File[]
        inputBinding:
            position: 1
outputs:
    combined_out:
        type: File
        outputBinding:
            glob: "*.copynumber"