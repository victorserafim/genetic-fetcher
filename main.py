import KafkaProducer
import GeneticDataFetcher

genetic_data = GeneticDataFetcher.fetch_genetic_data("EU490707")

# Qualquer tratamento que eu queira para esses dados

KafkaProducer.send_message("my-topic", genetic_data)
