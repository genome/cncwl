cwlVersion: v1.0
class: CommandLineTool
label: "merge cbs segments"
baseCommand: ['/usr/bin/perl', '/usr/bin/mergeCbsSegsFuzzyLog2.pl']
stdout: "varscan.output.copynumber.called.recentered.segments.tsv.clean.merged"
#stdout: $(inputs.output_name)
inputs:
    segments_f:
        type: File
        inputBinding:
            position: 1
    final_output_name:
        type: string?
        inputBinding:
            position: 2
        default: "varscan.output.copynumber.called.recentered.segments.tsv.clean.merged"

outputs:
     merged_f:
         type: stdout