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
    output_f:
        type: string?
        inputBinding:
            position: 2
        default: "varscan.output.copynumber.called.recentered.segments.tsv"
outputs:
    combined_seg:
        type: File
        outputBinding:
            glob: "*segments.tsv"