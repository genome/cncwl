cwlVersion: v1.0
class: CommandLineTool
label: "Recenter copy number data"
baseCommand: ['python', '/gscmnt/gc3018/info/medseq/tmp/mneveau/recenter.py']
inputs:
    cn_called:
        type: File
        inputBinding:
            position: 1
outputs:
    recentered:
        type: File
        outputBinding:
            glob: "*.recentered"