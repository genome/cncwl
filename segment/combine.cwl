cwlVersion: v1.0
class: CommandLineTool
baseCommand: ['python', '/gscmnt/gc3018/info/medseq/tmp/mneveau/cncwl/py_scripts/combine.py']
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
        default: "/gscmnt/gc3018/info/medseq/tmp/mneveau/test_workflow/varscan.out.copynumber"
outputs:
    combined_out:
        type: File
        outputBinding:
            glob: "*.segments.tsv"