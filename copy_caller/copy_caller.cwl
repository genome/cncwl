cwlVersion: v1.0
class: CommandLineTool
label: "Copy caller for exome varscan"
baseCommand: ["java", "-jar", "/opt/varscan/VarScan.jar","copyCaller"]
inputs:
    copy_num:
        type: File
        inputBinding:
            position: 1
    output_file:
        type: string?
        inputBinding:
            position: 2
            prefix: --output-file
        default: "varscan.output.copynumber.called"    
outputs:
    cn_called_file:
        type: File
        outputBinding:
          glob: "varscan.output.copynumber.called"
##also outputs .gc, not sure if we need that