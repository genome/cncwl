cwlVersion: v1.0
class: CommandLineTool
label: "clean up the output of the workflow"
baseCommand: ["/bin/bash", "helper.sh"]
requirements: 
    - class: InitialWorkDirRequirement
      listing:
         - entryname: 'helper.sh'
           entry: |
               #clean up tsv output
               cut -f 3-7 $1 | sed 's/"//g' > varscan.output.copynumber.called.recentered.segments.tsv.clean

               #get rid of calls supported by only a few sites
               #change number to adjust sensitivity/specificity 
               #100 is specific, 10 is sensitive
               perl -nae 'print $_ if $F[3] >= 50 || $F[0] eq '"chrom"'' varscan.output.copynumber.called.recentered.segments.tsv.clean > tmp
inputs:
    segments:
        type: File
        inputBinding:
            position: 1
outputs:
    cleaned_file:
        type: File
        outputBinding:
            glob: "tmp"
    clean:
        type: File
        outputBinding:
            glob: "*.clean"