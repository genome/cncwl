cwlVersion: v1.0
class: CommandLineTool
baseCommand: ['python', '/opt/copy_num/seg_combine.py']
#['python', '/opt/copynum/seg_combine.py']
label: "Combine segments into one file"
arguments: [$(runtime.outdir)]
inputs:
    segment_file:
        type: File[]
        inputBinding:
            position: 1
outputs:
    combined_seg:
        type: File
        outputBinding:
            glob: "*segments.tsv"