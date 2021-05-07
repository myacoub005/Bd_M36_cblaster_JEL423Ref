#!/usr/bin/env python3
#SBATCH -p short -N 1 -n 16 --mem 16gb --out logs/queries.log

module unload miniconda2
module load miniconda3
from Bio import SeqIO
record_dict = SeqIO.index("GCA_000149865.1_BD_JEL423_genomic.gbff", "genbank")
chrom1 = record_dict['DS022300.1']
chrom1_subseq = chrom1[1012752:1027530]
SeqIO.write(chrom1_subseq, "chrom1.1", "gbk")

chrom1_subseq = chrom1[1081890:1097153]
SeqIO.write(chrom1_subseq, "chrom1.2", "gbk")

chrom2 = record_dict['DS022301.1']
chrom2_subseq = chrom2[15145:24395]
SeqIO.write(chrom2_subseq, "chrom2.1", "gbk")

chrom2_subseq = chrom2[1650622:1664965]
SeqIO.write(chrom2_subseq, "chrom2.2", "gbk")

chrom3 = record_dict['DS022302.1']
chrom3_subseq = chrom3[692174:706871]
SeqIO.write(chrom3_subseq, "chrom3.1", "gbk")
