cwlVersion: v1.0
class: Workflow
label: "Varscan copy number parallel"
requirements:
    - class: ScatterFeatureRequirement
    - class: MultipleInputFeatureRequirement
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
    chromosome:
        type: string?
        inputBinding: 
          prefix: --chromo
    data_ratio:
        type: string?
        inputBinding: 
          prefix: --data_ratio
    varscan_params:
        type: string?
        default: "--min-coverage 20 --min-segment-size 25 --max-segment-size 100"
        inputBinding: 
          prefix: --varscan_params
outputs:
    cn_files:
        type: File[]
        outputSource: copy_num/copy_num_file
    copy_number:
        type: File
        outputSource: combine/combined_out
steps:
    get_norm_tum_ratio:
        run: get_norm_tum_ratio.cwl
        in:
            normal_bam: normal_bam
            tumor_bam: tumor_bam
            data_ratio: data_ratio
        out:
            [norm_tum_ratio]
    split:
        run: split.cwl
        in: 
            reference: reference
        out: 
            [cn_chromo_files]
    copy_num:
        scatter: input_file
        run: copy_num.cwl
        in:
            normal_bam: normal_bam
            tumor_bam: tumor_bam
            reference: reference
            norm_tum_ratio: get_norm_tum_ratio/norm_tum_ratio
            varscan_params: varscan_params
            input_file: split/cn_chromo_files
        out:
            [copy_num_file]
    combine:
        run: combine.cwl
        in:
            copy_num_files: [copy_num/copy_num_file]
        out:
            [combined_out]  