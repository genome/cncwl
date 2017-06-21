cwlVersion: v1.0
class: CommandLineTool
label: "Copy caller for exome varscan"
baseCommand: ["genome-perl", "-I", "~/cmiller/git/genome/lib/perl", "`which gmt`", "varscan", "copy-number-segments"]
inputs:
    copy_num:
        type: File
    output:
        type: string
        inputBinding:
          prefix: "--output-file"
    homdel_file:
        type: string
        inputBinding:
          prefix: "--homdel-file"
outputs:
    output:
        type: File
        outputBinding:
          glob: "varscan.output.copynumber.called"