import sys
import os.path
from subprocess import Popen

def parse_line(line):
    split_line = line.split(" ")
    x_line = [field.replace('"X"', 'X') for field in split_line]
    y_line = [field.replace('"Y"', 'Y') for field in x_line]
    return(y_line)
        

(script, chr_file, min_pts, undo_sd, min_width, plot_y_min, plot_y_max) = sys.argv

min_pts = int(min_pts)
with open(chr_file, 'r') as chr_f:
    #get chrom number from file_name
    dirs = chr_file.split("/")
    pieces = dirs[-1].split(".")
    chrom = pieces[5]

    out = "varscan.output.copynumber.called.recentered."
    out_chrom_p = out + chrom + ".segments.pvalue"
    out_chrom_sd = out + chrom + ".segments.sd"

    lines = []
    num_col = 0
    for line in chr_f:
        #get line count
        lines.append(line)
        line_count = len(lines)
    #get col count    
    fields = lines[0].split("\t")
    col_count = len(fields)
    print(col_count)
    print(line_count)
chr_f.close()
#if large enough to plot, do so 
if line_count >= min_pts:
    print("Chromosome: " + chrom)

    with open(out + chrom + ".R", 'w') as R_script:
        R_script.write("library(DNAcopy)\n")
        R_script.write("regions <- read.table(\"" + chr_file + "\")\n")
        R_script.write("head(regions)\n")
        R_script.write('CNA.object <- CNA(regions$V' + str(col_count) + ', regions$V1, regions$V2, data.type="logratio", sampleid=c("Chromosome ' + chrom + '"))\nsmoothed.CNA.object <- smooth.CNA(CNA.object)\n')
        R_script.write('segment.smoothed.CNA.object <- segment(smoothed.CNA.object, undo.splits="sdundo", undo.SD=' + undo_sd + ', min.width=' + min_width + ', verbose=1)\np.segment.smoothed.CNA.object <- segments.p(segment.smoothed.CNA.object)\nx <- c(' + undo_sd + ', length(p.segment.smoothed.CNA.object$pval[p.segment.smoothed.CNA.object$num.mark>20]))\nwrite.table(x, file ="' + out_chrom_sd + '", append=TRUE)\n')
            
        undo_sd = float(undo_sd)
        while undo_sd > 0.5:
            undo_sd -= 0.5
            R_script.write('if(length(p.segment.smoothed.CNA.object$pval[p.segment.smoothed.CNA.object$num.mark>=20]) < 50)\n{\n\tx <- c(' + str(undo_sd) + ', length(p.segment.smoothed.CNA.object$pval[p.segment.smoothed.CNA.object$num.mark>=20]))\n\t\twrite.table(x, file="' + out_chrom_sd + '", append=TRUE)\n\t\tsegment.smoothed.CNA.object <- segment(smoothed.CNA.object, undo.splits="sdundo", undo.SD=' + str(undo_sd) + ', verbose=1) \n\t\t p.segment.smoothed.CNA.object <- segments.p(segment.smoothed.CNA.object)\n}\n')
        R_script.write('detach(package:DNAcopy)\npar(mar=c(4,4,2,2))\n plot(segment.smoothed.CNA.object$data$maploc, segment.smoothed.CNA.object$data$Chromosome.' + chrom + ', pch=19, cex=0.25, cex.axis=1.25, cex.lab=1.5, col="cornflowerblue", ylim=c(' + plot_y_min + ',' + plot_y_max + '), main="Chromosome ' + chrom + '", xlab="Position", ylab="Copy Number Change (log2)")\nsegments(segment.smoothed.CNA.object$output$loc.start, segment.smoothed.CNA.object$output$seg.mean, segment.smoothed.CNA.object$output$loc.end, segment.smoothed.CNA.object$output$seg.mean, col="red", lwd=2)\n write.table(p.segment.smoothed.CNA.object, file="' + out_chrom_p + '")\n')
        R_script.write('dev.off()\n')
    R_script.close()
        
    cmd = ["R --no-save < " + out + chrom + ".R"]
    execution = Popen(cmd, shell=True)
    execution.communicate()
    ##remove eventually
    if execution.returncode == 0:
        print("R processing complete")

    seg_out = out + "segments.tsv"
    #make sure that data was created by R script
    if os.path.isfile(out_chrom_p) == False:
        print("Error: This chromosome's pvalue data was not created by R")
        sys.exit()

        

        
