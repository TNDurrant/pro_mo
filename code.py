# Biopython
from Bio import SeqIO
# regex
import re

# file with protein sequences e.g. uniprot_sprot_human_fasta.fasta
infile = ""

# file to write motif matches to e.g. motif_hits.txt
outfile = open("", "w")

# motif to search for e.g. Jungmichel motif G.{3}K.{7,13}(F|W).{2}R.F.{30,80}(K|R).{12,14}W
ProteinAlphabet = ""

# look through each protein sequence in the infile and write entries containing the motif to the outfile
for seq_record in SeqIO.parse(infile, "fasta"):
        matches = re.findall( ProteinAlphabet, str(seq_record.seq))
        if matches:
                SeqIO.write(seq_record, outfile, "fasta")

outfile.close()



