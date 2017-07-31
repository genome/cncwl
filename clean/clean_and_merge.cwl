cwlVersion: v1.0
class: Workflow
label: "clean and merge the segments.tsv file"
inputs:
    segments:
        type: File
    final_output_name:
        type: string?
        default: "varscan.output.copynumber.called.recentered.segments.tsv.clean.merged"  
outputs:
    segments_merged:
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
            final_output_name: final_output_name
        out: [merged_f]
 