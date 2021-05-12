#!/bin/bash
#SBATCH -p short -N 1 -n 32 --mem 32gb --out logs/getgbks_1job.log

mkdir -p strains DMND
CPU=$SLURM_CPUS_ON_NODE
if [ -z $CPU ]; then
  CPU=1
fi

INDIR=/bigdata/stajichlab/shared/projects/Chytrid/Bd_popgen/annotate_scaffold/funannotate

#make the sym link
#add the strain gbks to one location
ln -s $INDIR/*/update_results/*.gbk strains/

module load cblaster
module load diamond
module load parallel
parallel -j $CPU cblaster makedb {} -n DMND/{/.}_ref ::: $(ls strains/*.gbk)
