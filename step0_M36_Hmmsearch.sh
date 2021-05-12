#!/bin/bash
#SBATCH -p short -N 1 -n 16 --mem 16gb --out hmmsearch_1job.log
module load hmmer/3

#make sym lnk to folder with pep fasta files for every strain
ln -s /rhome/myaco005/bigdata/Bd/pep_exclude_low_Busco .

#make index
cat pep_exclude_low_Busco/*.fasta > allseqs.aa
esl-sfetch --index allseqs.aa

#obtain pfam hmm for M36
curl -o Peptidase_M36.hmm http://pfam.xfam.org/family/PF02128/hmm # Peptidase M36

#run the hmmsearch and output to domtbl
hmmsearch --domtbl M36.Hmmsearch.hits.domtbl -E 1e-15 Peptidase_M36.hmm allseqs.aa > Peptidase_M36.hmmsearch

#extract unique hits for the strains to a single fasta file
grep -h -v '^#' M36.Hmmsearch.hits.domtbl | awk '{print $1}' | sort | uniq | esl-sfetch -f allseqs.aa -> M36.hits.aa.fa

#count the number of M36 hits for each strain
grep ">" M36.hits.aa.fa M36_pangen_IDs.txt
