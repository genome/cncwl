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
        secondaryFiles: [.flagstat, .bai]
    tumor_bam: 
        type: File
        secondaryFiles: [.flagstat, .bai]
    reference: 
        type: File
        secondaryFiles: [.fai]
    data_ratio:
        type: string?
        default: None
    varscan_params:
        type: string?
        default: "--min-coverage 20 --min-segment-size 25 --max-segment-size 100"
outputs:
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
            input_file: split/cn_chromo_files
            normal_bam: normal_bam
            tumor_bam: tumor_bam
            reference: reference
            norm_tum_ratio: get_norm_tum_ratio/norm_tum_ratio
            varscan_params: varscan_params
        out:
            [copy_num_file]
    combine:
        run: combine.cwl
        in:
            ind_files: copy_num/copy_num_file
        out:
            [combined_out]  