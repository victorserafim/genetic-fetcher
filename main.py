import json

import KafkaProducer
import GeneticDataFetcher


def identify_genes(genetic_data):
    genes = []
    gene1 = {"start": "atg", "end": "tag"}
    start = genetic_data.find(gene1["start"])
    while start != -1:
        end = genetic_data.find(gene1["end"], start)
        if end != -1:
            genes.append({"gene": "gene1", "sequence": genetic_data[start:end+len(gene1["end"])]})
        start = genetic_data.find(gene1["start"], start + 1)
    return genes


def calculate_base_frequencies(genetic_data):
    base_frequencies = {
        "A": genetic_data.count("A") / len(genetic_data),
        "T": genetic_data.count("T") / len(genetic_data),
        "C": genetic_data.count("C") / len(genetic_data),
        "G": genetic_data.count("G") / len(genetic_data)
    }
    return base_frequencies


genetic_data = GeneticDataFetcher.fetch_genetic_data("EU490707")

genes = identify_genes(genetic_data)

base_frequencies = calculate_base_frequencies(genetic_data)

message = {
    "original_data": genetic_data,
    "genes": genes,
    "base_frequencies": base_frequencies
}

message_json = json.dumps(message)

KafkaProducer.send_message("my-topic", message_json)
