#!/bin/bash
#SBATCH -p short -N 1 -n 32 --mem 64gb --out logs/cblaster_search.log

module unload miniconda2
module load miniconda3
module load diamond
module load cblaster
module load parallel


# define a function we will use
run_cblaster() {
	db=$1
	qfile=$2
	outfile=$3

	if [ ! -f $outfile.count.txt ]; then
		cblaster search -m local -d $db -qf $qfile -me 1e-100 \
			-o $outfile.count.txt -ode "," -bde "," -b $outfile.binary.txt
	fi
}

export -f run_cblaster

CPU=$SLURM_CPUS_ON_NODE
if [ -z $CPU ]; then
  CPU=1
fi
INDIR=strains
OUT=results/cblaster
mkdir -p $OUT
for q in $(ls query_loci/*.gbk)
do
	qname=$(basename $q .gbk)
	parallel -j $CPU run_cblaster DMND/{/.}_ref.dmnd $q $OUT/{/.}__${qname} ::: $(ls strains/*.gbk)

done
