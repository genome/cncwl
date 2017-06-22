#!/usr/bin/env cwl-runner

cwlVersion: v1.0
class: Workflow
label: "somatic pipeline"
requirements:
    - class: SubworkflowFeatureRequirement
inputs:
    normal_bam:
    tumor_bam:
    reference:
output:
    cn:
        type: File
        outputSource: plot_segments/cn_final
steps:
    copy_num_parallel:
    copy_num_caller:
    recenter:
    segment:
    clean_and_merge:
    plot_segments:
        run:
        in:
        out: [cn_final]