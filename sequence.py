import sys

def process_results(undo_sd, min_width, current_chrom, current_chrom_results):
    chr_file = out + "." + chrom + ".infile"
    script_file = out + "." + chrom + ".R"

(script, regions_file, min_depth, min_points, undo_sd, min_width, plot_y_min, plot_y_max) = sys.argv
out = "varscan.output.copynumber.called.recentered"
t = "\t"
with open(regions_file, 'r') as regions_f:
    ##do we need line counter?
    line_counter, metMinDepth = 0, 0
    chromos = []
    current_chrom = ""
    current_chrom_results = ''
    next(regions_f)
    for line in regions_f:
        line_counter += 1
        fields = line.split("\t")
        chrom, chr_start, chr_stop, num_pos, norm, tum, log2 = fields[0], fields[1], fields[2], fields[3], fields[4], fields[5], fields[6]
        ##print(chrom, chr_start, chr_stop, num_pos, norm, tum, log2)
        chr_start, chr_stop = int(chr_start), int(chr_stop)
        if chrom not in chromos:
            chromos.append(chrom)
        if current_chrom != "" and chrom != current_chrom:
            print("Chromosome: " + current_chrom + "\n")
            process_results(undo_sd, min_width, current_chrom, current_chrom_results)
            current_chrom_results = ""
            current_chrom = chrom

        if norm >= min_depth or tum >= min_depth:
            metMinDepth += 1
            current_chrom = chrom
            if current_chrom_results != "":
                current_chrom_results = current_chrom_results + "\n"

            region_size = chr_stop - chr_start + 1
         
         ##old program has it printing chr_stop
         #if region small, report just midpoint
            if region_size <= 1000:
                midpt = (chr_stop + chr_start) / 2 
            
                if midpt >= chr_start and midpt <= chr_stop:
                    results = (chrom, str(midpt), num_pos, norm, tum, log2)
                    current_chrom_results = current_chrom_results + t.join(results)
                else:
                    print("no Midpoint " + midpt + " " + chr_start + " " + chr_stop + "\n")
            else:
                results = (chrom, chr_start, num_pos, norm, tum, log2)
                current_chrom_results = current_chrom_results + t.join(results) + "\n"
                results = (chrom, chr_stop, num_pos, norm, tum, log2)
                current_chrom_results = current_chrom_results + t.join(results)
regions_f.close()
print("Chromosome: " + current_chrom)
print(chromos)
process_results(undo_sd, min_width, current_chrom, current_chrom_results)

print(str(line_counter) + " lines parsed")
print(str(metMinDepth) + " met min depth")

with open(out + ".segments.tsv", 'w') as segments:
    header = ("ID", "sample", "chrom", "loc.start", "loc.end", "seg.mean", "bstat", "pval", "lcl", "ucl")
    segments.write(t.join(header))

    with open(out + ".index.html", 'w') as index:
        index.write("<HTML><BODY><TABLE CELLSPACING=0 CELLPADDING=5 BORDER=0 WIDTH=\"100%\">\n")
        index.write("<TR>\n")

    index.close()
segments.close()
    
    
