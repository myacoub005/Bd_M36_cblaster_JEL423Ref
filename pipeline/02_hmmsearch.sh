#!/usr/bin/bash
#SBATCH -p short -N 1 -n 32 --mem 32gb --out logs/hmmsearch.log

CPU=$SLURM_CPUS_ON_NODE
if [ -z $CPU ]; then
  CPU=1
fi

module load hmmer
module load parallel

# query ref db JEL423
DB=db
STRAINS=strains
OUTDIR=hmmsearch_results
mkdir -p $OUTDIR
for pfam in $(ls $DB/*.hmm); do
	pfamname=$(basename $pfam .hmm)

	parallel -j $CPU hmmsearch --cpu 2 --cut_ga --domtblout $OUTDIR/{/.}.$pfamname.tab $pfam {} \> $OUTDIR/{/.}.$pfamname.out ::: $(ls $DB/*.pep.fa)

	parallel -j $CPU hmmsearch --cpu 2 --cut_ga --domtblout $OUTDIR/{/.}.$pfamname.tab $pfam {} \> $OUTDIR/{/.}.$pfamname.out ::: $(ls $STRAINS/*.pep.fa)

done
