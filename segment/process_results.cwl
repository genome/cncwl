cwlVersion: v1.0
class: CommandLineTool
label: "Create and run python script"
baseCommand: ['python', '/gscmnt/gc3018/cancer-genomics/medseq/tmp/mneveau/cncwl/py_scripts/process_results.py']
inputs:
    split_file:
        type: File
        inputBinding:
            position: 1
    min_points:
        type: string?
        inputBinding:
            position: 2
        default: "100"
    undo_sd:
        type: string?
        inputBinding:
            position: 3
        default: "4"
    min_width:
        type: string?
        inputBinding:
            position: 4
        default: "2"
    plot_y_min:
        type: string?
        inputBinding:
            position: 5
        default: "-5"
    plot_y_max:
        type: string?
        inputBinding:
            position: 6
        default: "5"
outputs:
    segments_file:
        type: File
        outputBinding:
             glob: "*.segments.tsv"
             