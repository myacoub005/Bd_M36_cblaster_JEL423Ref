#!/bin/bash
#SBATCH -p short -N 1 -n 16 --mem 16gb --out getgbks_1job.log

mkdir strains
#make the sym link
ln -s /bigdata/stajichlab/shared/projects/Chytrid/Bd_popgen/annotate_scaffold/funannotate 

#add the strain gbks to one location
cp /funannotate/*/update_results/*.gbk /strains/
