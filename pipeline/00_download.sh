#!/usr/bin/bash
#SBATCH -p short --out logs/download.log
#curl -L -O https://ftp.ncbi.nlm.nih.gov/genomes/refseq/fungi/Batrachochytrium_dendrobatidis/latest_assembly_versions/GCF_000203795.1_v1.0/GCF_000203795.1_v1.0_genomic.gbff.gz

curl -L -O https://ftp.ncbi.nlm.nih.gov/genomes/genbank/fungi/Batrachochytrium_dendrobatidis/latest_assembly_versions/GCA_000149865.1_BD_JEL423/GCA_000149865.1_BD_JEL423_genomic.gbff.gz

pigz -d GCA_000149865.1_BD_JEL423_genomic.gbff.gz
