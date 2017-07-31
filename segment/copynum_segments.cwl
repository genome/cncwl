cwlVersion: v1.0
class: Workflow
label: "Copy number segmentation for exome varscan"
requirements:
    - class: ScatterFeatureRequirement
    - class: MultipleInputFeatureRequirement
    - class: SubworkflowFeatureRequirement
inputs:

##remove input binding
    regions_file:
        type: File
    min_depth:
        type: string?
        default: "8"
    min_points:
        type: string?
        default: "100"
    undo_sd:
        type: string?
        default: "4"
    min_width:
        type: string?
        default: "2"
    plot_y_min:
        type: string?
        default: "-5"
    plot_y_max:
        type: string?
        default: "5"
outputs:
    segments_tsv:
        type: File
        outputSource: combine/combined_seg
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
            min_width: min_width
            plot_y_min: plot_y_min
            plot_y_max: plot_y_max
        out:
            [segments_file]
    combine:
        run: seg_combine.cwl
        in:
            segment_file: process_results/segments_file
        out:
            [combined_seg]
