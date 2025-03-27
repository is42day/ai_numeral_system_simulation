# Use the official Python image as a base
FROM python:3.9-slim

# Set Spark and Hadoop versions
ENV SPARK_VERSION=3.5.5
ENV HADOOP_VERSION=3
ENV SPARK_HOME=/opt/spark
ENV PATH=$PATH:$SPARK_HOME/bin

# Install dependencies with proper cleanup
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        openjdk-17-jdk-headless \
        curl \
        python3 \
        python3-pip \
        unzip \
        git \
        openssh-client && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Download and extract Spark
RUN curl -k -fsSL https://downloads.apache.org/spark/spark-${SPARK_VERSION}/spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz | \
    tar -xz -C /opt && \
    mv /opt/spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION} ${SPARK_HOME}

# Install Python dependencies
COPY requirements.txt /
RUN pip install --no-cache-dir -r /requirements.txt

# Set the working directory
WORKDIR /app

# Copy the application code
COPY . /app

# Recommended: Set proper permissions
RUN chmod -R a+rwx /app && \
    useradd -m appuser && \
    chown -R appuser:appuser /app

USER appuser