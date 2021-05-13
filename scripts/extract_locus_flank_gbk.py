#!/usr/bin/env python3
from Bio import SeqIO
import os, argparse, re, time

parser = argparse.ArgumentParser(description="Process GBK files into Protein FastA format sequence")
parser.add_argument('-i','--input',help='Input GenBank file',required=True)

parser.add_argument('-t','--hmmer',help='HMMSEARCH domtblout file',
                    required=True, type=argparse.FileType('r') )

parser.add_argument('-o','--outdir',help='Output folder',
                    default="query_loci",
                    required=False)

parser.add_argument('-c','--cutoff',help='Further filter HMMER results by e-value', default=1e-20,
                    required=False)


parser.add_argument('--ext',help='Outfile extension',
                    required=False, default=".gbk")

parser.add_argument('-v','--debug',help='Extra Debugging output',action='store_true')

args = parser.parse_args()

target_genes = set()
for line in args.hmmer:
    if line.startswith("#"):
        continue
    row = line.split()

    gene = re.sub(r'(\.|-)T\d+$','',row[0]) # remove isoform numbers

    evalue = float(row[6])
    if evalue > args.cutoff:
        if args.debug:
            print("skipping hit for {} {} from {} to {}, evalue {} ({} of {})".                  format(gene,row[1], row[19],row[20],evalue,
                         row[9],row[10]))
        continue # skip this hit/sequence (using the sequence evalue
                 # so will be identical across multi-domain hits
    target_genes.add(gene)

target_genes = sorted(target_genes)
print(target_genes)

if not os.path.exists(args.outdir):
    os.mkdir(args.outdir)

gb = SeqIO.index_db(args.input +".idx",args.input, "genbank")

for seqname in gb:
    description = gb[seqname].description
    print(description)
    found_genes = []
    i = 0
    t0 = time.time()
    fcount = len(gb[seqname].features)
    gene_features = []
    for feature in gb[seqname].features:
        if feature.type == "gene":
            gene_features.append(feature)
            locus  = feature.qualifiers['locus_tag'][0]
            if locus in target_genes:
                found_genes.append([i,locus])
            i += 1
    if args.debug:
        t1 = time.time()
        total = t1-t0
        print("-->time took {} out of {} records = {} 1000 r/s".
              format(total,fcount,1000 * total/fcount))
        print("total gene features {}".format(len(gene_features)))
    i = 0
    if args.debug:
        print("found_genes are {}".format(found_genes))
    # build flanking locus
    for idx,targetlocus in found_genes:
        locus_flank = []
        maxgeneidx = len(gene_features)
        print("max geneidx id ",maxgeneidx)
        for ii in range(idx-2,idx+3):
            if ii >= 0 and ii <= maxgeneidx:
                locus_flank.append(gene_features[ii])

        left = min(locus_flank[0].location.start,
                   locus_flank[0].location.end)
        right = max(locus_flank[-1].location.start,
                    locus_flank[-1].location.end)
        region = gb[seqname][left:right]
        outfile = os.path.join(args.outdir,"{}.gbk".format(targetlocus))
        SeqIO.write(region,outfile,"genbank")
