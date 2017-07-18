cwlVersion: v1.0
class: Workflow
label: "somatic pipeline"
requirements:
    - class: SubworkflowFeatureRequirement
inputs:
    normal_bam:
        type: File
        inputBinding:
          prefix: -I_norm
        secondaryFiles: [.flagstat, .bai]
    tumor_bam:
        type: File
        inputBinding:
          prefix: -I_tum
        secondaryFiles: [.flagstat, .bai]
    reference:
        type: File
        inputBinding:
          prefix: --R
        secondaryFiles: [.fai]
    output_name:
        type: string?
outputs:
    cn:
        type: File
        outputSource: clean_and_merge/segments_merged
    segments:
        type: File
        outputSource: segment/segments_tsv 
steps:
    copy_num_parallel:
        run: copy_num/copy_num_parallel.cwl
        in:
            normal_bam: normal_bam
            tumor_bam: tumor_bam
            reference: reference
        out:
            [copy_number]
    copy_num_caller: 
         run: copy_caller/copy_caller.cwl
         in:
             copy_num: copy_num_parallel/copy_number
         out:
             [cn_called_file]
    recenter:
         run: recenter/recenter.cwl
         in:
             cn_called: copy_num_caller/cn_called_file
         out:
             [cn_called_recentered]
    segment:
        run: segment/copynum_segments.cwl
        in:
            regions_file: recenter/cn_called_recentered
        out:
            [segments_tsv]
    clean_and_merge:
        run: clean/clean_and_merge.cwl
        in:
            segments: segment/segments_tsv
            output_name: output_name
        out:
            [segments_merged]