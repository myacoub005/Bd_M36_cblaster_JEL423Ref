#!/usr/bin/bash
#SBATCH -p short -N 1 -n 32 --mem 64gb --out logs/make_next_query_loci.log

module unload miniconda2
module load miniconda3

DB=db
OUTDIR=hmmsearch_results
STRAINS=strains
for domain in $(ls $DB/*.hmm); do
	pfam=$(basename $domain .hmm)
	for genome in $(ls $STRAINS/*.gbk);
	do
		hmmout=$OUTDIR/$(basename $genome .gbk).pep.${pfam}.tab
		echo "$hmmout $genome"
		./scripts/extract_locus_flank_gbk.py -i $genome -t $hmmout -g ignore.txt
		bash pipeline/04_cblaster_search.sh 
		./scripts/gather_cblaster_clusters.py
		#./scripts/extract_locus_flank_gbk.py -i $refgenome -t $hmmout -g ignore.txt
		break
	done
done
