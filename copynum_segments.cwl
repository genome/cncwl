cwlVersion: v1.0
class: CommandLineTool
label: "Copy number segmentation for exome varscan"
baseCommand: []
inputs:
    regions_file:
        type: File
        inputBinding:
            position: 1
    min_depth:
        type: string?
        inputBinding:
            position: 2
        default: 8
    min_points:
        type: string?
        inputBinding:
            position: 3
        default: 100
    undo_sd:
        type: string?
        inputBinding:
            position: 4
        default: 4
    min_width:
        type: string?
        inputBinding:
            position: 5
        default: 2
    plot_y_min:
        type: string?
        inputBinding:
            position: 6
        default: -5
    plot_y_max:
        type: string?
        inputBinding:
            position: 7
        default: 5 
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