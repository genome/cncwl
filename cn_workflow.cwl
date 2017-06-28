#!/usr/bin/env cwl-runner

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
        secondaryFiles: [.flagstat]
    tumor_bam:
        type: File
        inputBinding:
          prefix: -I_tum
        secondaryFiles: [.flagstat]
    reference:
        type: File
        inputBinding:
          prefix: --R
        secondaryFiles: [.fai]
    output:
        type: string
        inputBinding: 
          prefix: -O
output:
    cn:
        type: File
        outputSource: 
steps:
    copy_num_parallel:
        run: copy_num/copy_num_parallel.cwl
        in:
            normal_bam: normal_bam
            tumor_bam: tumor_bam
            reference: reference
        out:
            [copy_number_file]
    copy_num_caller: 
         run: copy_caller.cwl
         in:
             copy_num: copy_num_parallel/copynumber_file
         out:
             [cn_called_file]
    recenter:
         run: recenter.cwl
         in:
             cn_called: copy_num_caller/cn_called_file
         out:
             [cn_called_recentered]
    segment:
    clean_and_merge: