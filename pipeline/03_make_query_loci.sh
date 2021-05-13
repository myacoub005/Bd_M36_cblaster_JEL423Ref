#!/usr/bin/bash
#SBATCH -p short -N 1 -n 2 --mem 4gb

module unload miniconda2
module load miniconda3
DB=db
OUTDIR=hmmsearch_results
STRAINS=strains
for domain in $(ls $DB/*.hmm); do
	pfam=$(basename $domain .hmm)
	for refgenome in $(ls $DB/*.gbff);
	do
		hmmout=$OUTDIR/$(basename $refgenome .gbff).pep.${pfam}.tab
		./scripts/extract_locus_flank_gbk.py -i $refgenome -t $hmmout
	done
done
