#!/bin/bash
#SBATCH -p short -N 1 -n 1 --mem 2gb --out getgbks_1job.log

mkdir -p strains
#make the sym link
INDIR=/bigdata/stajichlab/shared/projects/Chytrid/Bd_popgen/annotate_scaffold/funannotate

#add the strain gbks to one location
rsync -a $INDIR/funannotate/*/update_results/*.gbk strains/
