cwlVersion: v1.0
class: CommandLineTool
baseCommand: ["python", "/gscmnt/gc3018/info/medseq/tmp/mneveau/parse_regions.py"]
label: "Parse regions and create individual chromosome files to get results"
inputs:
    regions_file:
        type: File
        inputBinding:
            position: 1
    min_depth:
        type: string?
        inputBinding:
            position: 2
        default: "8"
outputs:
    split_regions_files:
        type: File[]
        outputBinding:
            glob: "varscan.output.copynumer.called.recentered.split.*"