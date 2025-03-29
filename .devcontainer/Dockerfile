FROM python:3.9-slim

ENV SPARK_VERSION=3.5.5
ENV HADOOP_VERSION=3
ENV SPARK_HOME=/opt/spark
ENV PATH=$PATH:$SPARK_HOME/bin

RUN apt-get update && apt-get install -y --no-install-recommends \
    openjdk-17-jdk-headless \
    curl \
    python3 \
    python3-pip \
    unzip \
    git \
    openssh-client \
    ca-certificates \
    sudo \
    procps && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Download and setup Spark
RUN curl -k -fsSL https://downloads.apache.org/spark/spark-${SPARK_VERSION}/spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz \
    | tar -xz -C /opt && \
    mv /opt/spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION} /opt/spark

COPY requirements.txt /tmp/
RUN pip install --no-cache-dir -r /tmp/requirements.txt

WORKDIR /app
COPY . /app

RUN useradd -m appuser && chown -R appuser:appuser /app /opt/spark
USER appuser

EXPOSE 8888 4040
