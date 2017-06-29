import sys 

(script, regions_file, min_depth)= sys.argv

out = "varscan.output.copynumber.called.recentered.split"
t = "\t"
with open(regions_file, 'r') as regions_f:
    #skip header line
    next(regions_f)
    line_counter, metMinDepth = 0, 0
    chroms = []
    current_chrom, current_chrom_results = "", ""
    for line in regions_f:
        line_counter += 1
        fields = line.split(t)
        chrom, chr_start, chr_stop, num_pos, norm, tum, log2 = fields[0], fields[1], fields[2], fields[3], fields[4], fields[5], fields[6]
        chr_start, chr_stop = int(chr_start), int(chr_stop)
        ##might not need in the end
        if chrom not in chroms:
            chroms.append(chrom)
        #when sees next chromosome, write data from previous one to unique file
        if current_chrom != "" and chrom != current_chrom:
            with open(out + "." + current_chrom, 'w') as out_f:
                out_f.write(current_chrom_results)
            out_f.close()
            current_chrom_results = ""
            current_chrom = chrom
        
        if norm >= min_depth or tum >= min_depth:
            metMinDepth += 1
            current_chrom = chrom
            region_size = chr_stop - chr_start + 1
            
            #if region size small enough, record just midpt, otherwise record start and stop
            if region_size <= 1000:
                midpt = ((chr_stop - chr_start) / 2) + chr_start
                if midpt >= chr_start and midpt <= chr_stop:
                    results = (chrom, str(midpt), num_pos, norm, tum, log2)
                    current_chrom_results = current_chrom_results + t.join(results) + "\n"
                else:
                    print("Warning: No midpoint here " + str(midpt) + " " + str(chr_start) + " " + str(chr_stop) + "\n")
            else:
                results = (chrom, chr_start, num_pos, norm, tum, log2)
                current_chrom_results = current_chrom_results + t.join(results) + "\n"
                results = (chrom, chr_stop, num_pos, norm, tum, log2)
                current_chrom_results = current_chrom_results + t.join(results) + "\n"
regions_f.close()
print(chroms)
with open(out + "." + chrom, 'w') as out_f:
    out_f.write(current_chrom_results)

