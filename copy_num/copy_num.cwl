cwlVersion: v1.0
class: CommandLineTool
baseCommand: ['python', '/opt/copy_num/copy_num.py']
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
        secondaryFiles: [.bai]
    tumor_bam:
        type: File
        inputBinding:
            position: 3
        secondaryFiles: [.bai]
    reference:
        type: File
        inputBinding:
            position: 4
        secondaryFiles: [.fai]
    norm_tum_ratio:
        type: File
        inputBinding:
            position: 5
    varscan_params:
        type: string
        inputBinding:
            position: 6
outputs:
    copy_num_file:
        type: File
        outputBinding:
            glob: "*.copynumber"