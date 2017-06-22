cwlVersion: v1.0
class: CommandLineTool
label: "Copy number segmentation for exome varscan"
baseCommand: ["genome-perl", "-I", "~cmiller/git/genome/lib/perl", "`which gmt`", "varscan", "copy-number-segments"]
inputs:
    regions_file:
        type: File
        inputBinding:
          prefix: --regions-file
    output:
        type: string
        inputBinding:
          prefix: --output
outputs:
    segments:
        type: File
        outputBinding:
          glob: varscan.output.copynumber.called.segments.tsv
    index:
        type: File
        outputBinding:
          glob: varscan.output.copynumber.called.index.html
    infile:
        type: File[]
        outputBinding:
          glob: "*.infile"
    p_value:
        type: File[]
        outputBinding:
          glob: "*.infile.segments.p-value"
    sd:
        type: File[]
        outputBinding:
          glob: "*.infile.segments.cd"