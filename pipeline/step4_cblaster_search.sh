#!/bin/bash
#SBATCH -p short -N 1 -n 16 --mem 16gb --out cblaster_search.log

module unload miniconda2
module load miniconda3
module load diamond
module load cblaster

for q in *.gbk; do
  for s in *.dmnd; do
      cblaster search -m local -d DMND/${s} -qf gbk_queries/${q} -me 1e-100 -o results/${s}_${q}_output.csv -ode ","
  done
done
