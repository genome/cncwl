cwlVersion: v1.0
class: CommandLineTool
baseCommand: ['python', '/gscmnt/gc3018/info/medseq/tmp/mneveau/copy_num.py']
label: "Determine copy number for a chromosome"
inputs:
    input_file:
        type: File
        inputBinding:
            position: 1
    normal_bam:
        type: File
        inputBinding:
            position: 2
    tumor_bam:
        type: File
        inputBinding:
            position: 3
    reference:
        type: File
        inputBinding:
            position: 4
    norm_tum_ratio:
        type: File
        inputBinding:
            position: 5
    varscan_params:
        type: string
        inputBinding:
            position: 6
    output:
        type: string
        inputBinding:
            position: 7
outputs:
    cn_files:
        type: File[]
        outputBinding:
            glob: "*.copynumber"