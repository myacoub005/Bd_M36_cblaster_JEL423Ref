#!/bin/bash
#SBATCH -p short -N 1 -n 32 --mem 64gb --out logs/cblaster_search.log

module unload miniconda2
module load miniconda3
module load diamond
module load cblaster
module load parallel

CPU=$SLURM_CPUS_ON_NODE
if [ -z $CPU ]; then
  CPU=1
fi
INDIR=strains
OUT=results
mkdir -p $OUT
for q in $(ls gbk_queries/*.gbk)
do
	qname=$(basename $q .gbk)
	parallel -j $CPU cblaster search -m local -d DMND/{/.}_ref.dmnd -qf $q -me 1e-100 -o $OUT/{/.}_${qname}_output.csv -ode "," ::: $(ls strains/*.gbk)
	parallel -j $CPU cblaster search -m local -d DMND/{/.}_ref.dmnd -qf $q -me 1e-100 -o $OUT/{/.}_${qname}_output_binary.csv -bde "," ::: $(ls strains/*.gbk)
done
