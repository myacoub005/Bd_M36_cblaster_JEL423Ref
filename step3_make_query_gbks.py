#!/usr/bin/env python3
#SBATCH -p short -N 1 -n 16 --mem 16gb --out logs/queries.log

module unload miniconda2
module load miniconda3
from Bio import SeqIO
record_dict = SeqIO.index("GCA_000149865.1_BD_JEL423_genomic.gbff", "genbank")
chrom1 = record_dict['DS022321.1']
chrom1_subseq = chrom1[START:STOP]
