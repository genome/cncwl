cwlVersion: v1.0
class: CommandLineTool
baseCommand: ['python', '/gscmnt/gc3018/info/medseq/tmp/mneveau/get_norm_tum_ratio.py']
label: "Get normal:tumor ratio"                 
inputs:
    normal_bam:
        type: File
        inputBinding:
            position: 2
        secondaryFiles: [.flagstat]
    tumor_bam:
        type: File
        inputBinding:
            position: 3
        secondaryFiles: [.flagstat]
    data_ratio:
        type: string?
        default: None
outputs:
    norm_tum_ratio:
        type: File
        outputBinding:
            glob: "output.ratio"