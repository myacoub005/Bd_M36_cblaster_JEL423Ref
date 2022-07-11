#!/usr/bin/env python3

import argparse, re, os
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord

parser = argparse.ArgumentParser(description="Process GBK files into Protein FastA format sequence")
parser.add_argument('-i','--input',help='Input GenBank file',required=True)

parser.add_argument('-o','--output',help='Output Fasta Protein file',
                    required=False)

parser.add_argument('-pe','--pepext',help='Peptide File Extension default',
                    required=False, default=".pep.fa")

parser.add_argument('-v','--debug',help='Extra Debugging output',action='store_true')

args = parser.parse_args()

if not args.output:
    args.output = re.sub(r'\.(gbk|gbff|genbank)$',args.pepext,
                      args.input,
                      flags=re.IGNORECASE)

#fname, fextension = os.path.splitext(args.output)

# indexing this as we will likely need to come back to it again anyways
gb = SeqIO.index_db(args.input + ".idx", args.input, "genbank")

pepseqs = []
locuscounts  = {}
for seqname in gb:
    description = gb[seqname].description
    for feature in gb[seqname].features:
        if feature.type == "CDS":

            if 'translation' in feature.qualifiers:
                cdsseq = feature.qualifiers['translation'][0]
                locus  = feature.qualifiers['locus_tag'][0]
                newlocus = ""
                if 'product' in feature.qualifiers:
                    m = re.search(r'(isoform|variant) (\d+)$',feature.qualifiers['product'][0])
                    if m:
                        newlocus = "{}-T{}".format(locus,m.group(2))

                if not newlocus:
                    if locus in locuscounts:
                        locuscounts[locus] += 1
                        newlocus = "{}-T{}".format(locus,locuscounts[locus])
                    else:
                        newlocus = locus
                        locuscounts[locus] = 1
                        desc = "{}:{}..{}".format(
                        seqname,feature.location.start, feature.location.end)
                if args.debug:
                    print ("desc = {} id={}".format(desc,newlocus))
                pepseq = SeqRecord(
                    seq=Seq(cdsseq),
                    id=newlocus,description=desc)
                pepseqs.append(pepseq)

SeqIO.write(pepseqs,args.output,"fasta")
