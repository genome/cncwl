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
    merged_f:
        type: File
        outputSource: merge/merged_f
steps:
    clean:
        run: clean.cwl
        in: 
            segments: segments
        out: [cleaned_file]
    merge:
        run: merge_seg.cwl
        in: 
            segments_f: clean/cleaned_file
            output_f: out
        out: [merged_f]
 