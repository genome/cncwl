cwlVersion: v1.0
class: Workflow
label: "Copy number segmentation for exome varscan"
requirements:
    - class: ScatterFeatureRequirement
    - class: MultipleInputFeatureRequirement
    - class: SubworkflowFeatureRequirement
inputs:
    regions_file:
        type: File
        inputBinding:
            position: 1
    min_depth:
        type: string?
        inputBinding:
            position: 2
        default: "8"
    min_points:
        type: string?
        inputBinding:
            position: 3
        default: "100"
    undo_sd:
        type: string?
        inputBinding:
            position: 4
        default: "4"
    min_width:
        type: string?
        inputBinding:
            position: 5
        default: "2"
    plot_y_min:
        type: string?
        inputBinding:
            position: 6
        default: "-5"
    plot_y_max:
        type: string?
        inputBinding:
            position: 7
        default: "5" 
outputs:
    segments_tsv:
        type: File[]
        outputSource: process_results/segments_file
        ##  glob: varscan.output.copynumber.called.recentered.segments.tsv
    ##sd:
    ##    type: File[]
    ##    outputBinding:
    ##      glob: "*.infile.segments.cd"
steps:
    parse_regions:
        run: parse_regions.cwl
        in:
            regions_file: regions_file
            min_depth: min_depth
        out:
            [split_regions_files]
    process_results:
        scatter: [split_file]
        run: process_results.cwl
        in:
            split_file: parse_regions/split_regions_files
            min_points: min_points
            undo_sd: undo_sd
            min_wdith: min_width
            plot_y_min: plot_y_min
            plot_y_max: plot_y_max
        out:
            [segments_file]
