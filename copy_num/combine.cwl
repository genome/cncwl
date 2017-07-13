cwlVersion: v1.0
class: CommandLineTool
baseCommand: ['python', '/opt/copy_num/combine.py']
arguments: [$(runtime.outdir)]
label: "Combine all chromosomes to one copynumber output file"
inputs:
    ind_files:
        type: File[]
        inputBinding:
            position: 1
    output_f:
        type: string?
        inputBinding:
            position: 2
        default: "varscan.out.copynumber"
outputs:
    combined_out:
        type: File
        outputBinding:
            glob: "*.copynumber"