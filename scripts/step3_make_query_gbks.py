#!/usr/bin/env python3
#SBATCH -p short -N 1 -n 16 --mem 16gb --out logs/queries.log

module unload miniconda2
module load miniconda3
from Bio import SeqIO
record_dict = SeqIO.index("GCA_000149865.1_BD_JEL423_genomic.gbff", "genbank")
chrom1 = record_dict['DS022300.1']
chrom1_subseq = chrom1[1012752:1027530]
SeqIO.write(chrom1_subseq, "chrom1.1.gbk", "gbk")

chrom1_subseq = chrom1[1081890:1097153]
SeqIO.write(chrom1_subseq, "chrom1.2.gbk", "gbk")

chrom2 = record_dict['DS022301.1']
chrom2_subseq = chrom2[15145:24395]
SeqIO.write(chrom2_subseq, "chrom2.1.gbk", "gbk")

chrom2_subseq = chrom2[1650622:1664965]
SeqIO.write(chrom2_subseq, "chrom2.2.gbk", "gbk")

chrom3 = record_dict['DS022302.1']
chrom3_subseq = chrom3[692174:706871]
SeqIO.write(chrom3_subseq, "chrom3.1.gbk", "gbk")

chrom3 = record_dict['DS022302.1']
chrom3_subseq = chrom3[1464563:1479318]
SeqIO.write(chrom3_subseq, "chrom3.2.gbk", "gbk")

chrom4 = record_dict['DS022303.1']
chrom4_subseq = chrom4[59448:75509]
SeqIO.write(chrom4_subseq, "chrom4.1.gbk", "gbk")

chrom4_subseq = chrom4[409191:424098]
SeqIO.write(chrom4_subseq, "chrom4.2.gbk", "gbk")

chrom4_subseq = chrom4[1705766:1728874]
SeqIO.write(chrom4_subseq, "chrom4.3.gbk", "gbk")

chrom5 = record_dict['DS022304.1']
chrom5_subseq = chrom5[123425:133344]
SeqIO.write(chrom5_subseq, "chrom5.1.gbk", "gbk")
