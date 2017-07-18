cwlVersion: v1.0
class: CommandLineTool
label: "clean up the output of the workflow"
baseCommand: ["/bin/bash", "/opt/copy_num/clean_helper.sh"]
inputs:
    segments:
        type: File
        inputBinding:
            position: 1
outputs:
    cleaned_file:
        type: File
        outputBinding:
            glob: "tmp"
    clean:
        type: File
        outputBinding:
            glob: "*.clean"