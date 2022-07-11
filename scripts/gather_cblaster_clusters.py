#!/usr/bin/env python3

# ToDo: we will still need to better retool the filename setup to reflect analyses of multiple domains
import argparse, os, re, csv

parser = argparse.ArgumentParser(description="Gather CBlaster Results To Cluster")
parser.add_argument('-i','--indir',help='Input Directory',required=False, default="results/cblaster")

parser.add_argument('-o','--outfile',help='Output Ignore File',required=False, default="ignore.txt")

parser.add_argument('--ext',help='CBlaster File Extension',required=False, default="count.txt")

parser.add_argument('-v','--debug',help='Extra Debugging output',action='store_true')

args = parser.parse_args()

if args.ext[0] != ".":
    args.ext = "." + args.ext

clusters = {}
strainclusters = {}

for strain in os.listdir(args.indir):
    straindir = os.path.join(args.indir,strain)
    if os.path.isdir(straindir):
        if strain not in strainclusters:
            strainclusters[strain] = {}

        for fname in os.listdir(straindir):
            if fname.endswith(args.ext):
                genename = re.sub(args.ext,'',fname)
                if args.debug:
                    print("strain is {} gene is {} in {}".format(strain,genename,fname))
                if genename not in clusters:
                    clusters[genename] = {}
                if strain in clusters[genename]:
                    print("warning already seen strain {} and gene {}".format(strain,genename))
                with open(os.path.join(straindir,fname),"r") as fh:
                    besthit = []
                    process = 0
                    for line in fh:
                        if line.startswith("Cluster "):
                            process = 0
                        elif line.startswith("Query,"):
                            process = 1
                        elif len(line) > 1 and process:
                            row = line.split(",")
                            gname = row[0]
                            hname = row[1]
                            ident = row[2]
                            coverage = row[3]
                            evalue   = row[4]
                            if gname == genename:
                                if not besthit or besthit[1] < ident:
                                    besthit = [hname,ident,coverage,evalue]
                    if len(besthit):
                        clusters[genename][strain]              = besthit[0]
                        strainclusters[strain][besthit[0]] = genename

with open(args.outfile,"w") as ofh:
    for strain in strainclusters:
        for gene in strainclusters[strain]:
            ofh.write("{}\n".format(gene))
