# Use a imagem base do Java
FROM openjdk:8-jdk-alpine

# Instale o software necessário
RUN apk add --no-cache bash curl jq

# Baixe e instale o Kafka
ARG KAFKA_VERSION=3.7.0
ARG KAFKA_SCALA_VERSION=2.13
RUN mkdir /opt \
  && curl -SL https://downloads.apache.org/kafka/${KAFKA_VERSION}/kafka_${KAFKA_SCALA_VERSION}-${KAFKA_VERSION}.tgz \
  | tar -xzC /opt \
  && mv /opt/kafka_${KAFKA_SCALA_VERSION}-${KAFKA_VERSION} /opt/kafka

# Defina as variáveis de ambiente
ENV PATH /opt/kafka/bin:$PATH
