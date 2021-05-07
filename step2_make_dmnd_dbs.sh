#!/bin/bash
#SBATCH -p short -N 1 -n 16 --mem 16gb --out makedb_1job.log

module unload miniconda2
module load miniconda3
module load cblaster
module load diamond

mkdir DMND

for s in *.gbk; do
cblaster makedb /strains/${s} -n /DMND/${s}_ref
done

