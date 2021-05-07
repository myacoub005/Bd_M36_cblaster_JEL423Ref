#!/bin/bash
#SBATCH -p intel --time 12-0:00:00 --ntasks 8 --nodes 1 --mem 24G --out cblaster_binry_search.log

module unload miniconda2
module load miniconda3
module load diamond
module load cblaster

for q in *.gbk; do
  for s in *.dmnd; do
      cblaster search -m local -d DMND/${s} -qf gbk_queries/${q} -me 1e-100 -mi 90 -b binary_results/${s}_${q}_output.csv -bde ","
  done
done
