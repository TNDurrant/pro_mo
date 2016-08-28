# Biopython
from Bio import SeqIO
# regex
import re

# file containing the protein sequences to search against e.g. uniprot_sprot_human_fasta.fasta contains the uniprot human reference proteome
infile = "uniprot_sprot_human_fasta.fasta"

# file to write motif matches to
outfile = open("motif_hits.txt", "w")

# asks the user to enter the amino acid motif to search the reference proteome for
ProteinAlphabet = input("Enter your amino acid motif and hit the enter key: ")

# looks through each protein sequence in the infile and writes entries containing the motif to the outfile
for seq_record in SeqIO.parse(infile, "fasta"):
        matches = re.findall( ProteinAlphabet, str(seq_record.seq))
        if matches:
                SeqIO.write(seq_record, outfile, "fasta")

outfile.close()


