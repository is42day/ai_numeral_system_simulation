# Use the official Python image as a base
FROM python:3.9-slim

# Set Spark and Hadoop versions
ENV SPARK_VERSION=3.5.5
ENV HADOOP_VERSION=3

# Install dependencies
RUN apt-get update && \
    apt-get install -y openjdk-17-jdk-headless curl python3 python3-pip unzip git && \
    git \
    openssh-client \
    apt-get clean

# Download and extract Spark
RUN curl -fsSL https://downloads.apache.org/spark/spark-${SPARK_VERSION}/spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz | tar -xz -C /opt && \
    mv /opt/spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION} /opt/spark

# Install Python dependencies
COPY requirements.txt /
RUN pip install --no-cache-dir -r /requirements.txt

# Set the working directory
WORKDIR /app

# Copy the application code
COPY . /app
