# rodando o Kafka

- Estou utilizando o kafka_2.13-3.7.0, dentro dele se tem todos os scripts

primeiro inicia-se o ZooKeeper

```bash
bin/zookeeper-server-start.sh config/zookeeper.properties
```

Após isso inicia-se a sessão do kafka

```bash
bin/kafka-server-start.sh config/server.properties
```

## Scripts em Python

Com o servidor Kafka rodando e o tópico criado, Rode o main.py para receber os dados
e rode o KafkaConsumer.py para consultar os dados dentro do tópico do Kafka.