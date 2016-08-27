# Biopython
from Bio import SeqIO
# regex
import re

# file with protein sequences
infile = "uniprot_sprot_human_fasta.fasta"

# file to write motif matches to
outfile = open("motif_hits.txt", "w")

# motif to search for
ProteinAlphabet = ""

# look through each protein sequence in the infile and write entries containing the motif to the outfile
for seq_record in SeqIO.parse(infile, "fasta"):
        matches = re.findall( ProteinAlphabet, str(seq_record.seq))
        if matches:
                SeqIO.write(seq_record, outfile, "fasta")

outfile.close()



