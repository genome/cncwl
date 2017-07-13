cwlVersion: v1.0
class: CommandLineTool
baseCommand: ['python', '/opt/copy_num/get_norm_tum_ratio.py']
label: "Get normal:tumor ratio"                 
inputs:
    normal_bam:
        type: File
        inputBinding:
            position: 1
        secondaryFiles: [.flagstat, .bai]
    tumor_bam:
        type: File
        inputBinding:
            position: 2
        secondaryFiles: [.flagstat, .bai]
    data_ratio:
        type: string?
        default: None
outputs:
    norm_tum_ratio:
        type: File
        outputBinding:
            glob: "output.ratio"