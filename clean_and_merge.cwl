cwlVersion: v1.0
class: Workflow
label: "clean and merge the segments.tsv file"
inputs:
    segments:
        type: File
    out:
        type: string?
        default: "varscan.segments.clean.merged" 
outputs:
    segments_merged:
        type: File
        outputBinding: out
steps:
    clean:
        run: clean.cwl
        in: 
            segments: segments
        out: 
            [clean_f]
    merge:
        run: merge_seg.cwl
        in: 
	    clean_f: clean/clean_f
            out_f: out
        out: 
            [segments_merged_final]
 