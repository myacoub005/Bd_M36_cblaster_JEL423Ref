#!/usr/bin/env python3
from Bio import SeqIO
locations="Seq_locations.tab"
genome="GCA_000149865.1_BD_JEL423_genomic.gbff"

# it would be better if the input file was the BDEG names
# and we were simply getting those locations from the genome file

record_dict = SeqIO.index_db(genome +".idx",genome, "genbank")
with open(locations,"r") as fh:
    for line in fh:
        if line.startswith('Seq'):
            continue
        row = line.split()
        if row[0] in record_dict:
            name  = row[0]
            start = int(row[1])
            stop  = int(row[2])

            region = record_dict[name][start:stop]
            outfile =
            SeqIO.write_record(region,outfile,"genbank")



#chrom1 = record_dict['DS022300.1']
#chrom1_subseq = chrom1[1012752:1027530]
#SeqIO.write(chrom1_subseq, "chrom1.1.gbk", "gbk")
