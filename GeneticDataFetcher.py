from Bio import Entrez


def fetch_genetic_data(id):
    Entrez.email = "vituh.almeida1997@gmail.com"
    handle = Entrez.efetch(db="nucleotide", id=id, rettype="gb", retmode="text")
    return handle.read()
