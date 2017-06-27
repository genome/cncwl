cwlVersion: v1.0
class: CommandLineTool
baseCommand: ['usr/bin/python', 'helper.py']
label: "Get tumor/normal ratio"
requirements:
    - class: InitialWorkDirRequirement
      listing:
          - entryname: 'helper.py'
            entry: |
                 
inputs:
    normal_bam:
        type: File
    tumor_bam:
        type: File
    data_ratio:
        type: string
output:
    tum_norm_ratio:
        type: File