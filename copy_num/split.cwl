cwlVersion: v1.0
class: CommandLineTool
baseCommand: ['python', '/gscmnt/gc3018/info/medseq/tmp/mneveau/split.py']
label: "Create files for every significant chromosome in reference index"
inputs:
    reference:
        type: File
        inputBinding:
            position: 1
        secondaryFiles: [.fai]
outputs:
    cn_chromo_files:
        type: File[]
        outputBinding:
            glob: "*.copynumber" 