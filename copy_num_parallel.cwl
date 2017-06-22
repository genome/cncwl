cwlVersion: v1.0
class: CommandLineTool
label: "Varscan copy number parallel"
inputs:
    normal_bam: 
        type: File
        inputBinding:
          prefix: --normal_bam
    tumor_bam: 
        type: File
        inputBinding:
          prefix: --tumor_bam
    reference: 
        type: File
        inputBinding:
          prefix: --reference
    output:
        type: string
        inputBinding: 
          prefix: --output
outputs:
    copy_number:
        type: File[]
        outputBinding:
          glob: *.copynumber
    log:
        type: File[]
        outputBinding:
          glob: *.log