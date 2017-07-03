cwlVersion: v1.0
class: Workflow
label: "clean and merge the segments.tsv file"
inputs:
    segments:
        type: File
        inputBinding:
            position: 1
    out:
        type: string?
        inputBinding:
            position: 2
        default: "varscan.segments.clean.merged" 
outputs:
    segments_merged:
        type: File
        outputBinding: out
steps:
    clean:
        run: clean.cwl
        in: segments
        out: [clean_f]
    merge:
        run: merge_seg.cwl
        in: clean/clean_f
        out: [segments_merged]
 