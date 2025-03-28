FROM python:3.9-slim

# Spark/Hadoop config
ENV SPARK_VERSION=3.5.5
ENV HADOOP_VERSION=3
ENV SPARK_HOME=/opt/spark
ENV PATH=$PATH:$SPARK_HOME/bin

# Install system deps + Java + SSL certs + sudo
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        make \
        openjdk-17-jdk-headless \
        curl \
        git \
        openssh-client \
        ca-certificates \
        sudo && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* && \
    update-ca-certificates && \
    echo "appuser ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers && \
    chmod 0440 /etc/sudoers

# Download Spark (corrected URL format)
RUN curl -k -fsSL https://downloads.apache.org/spark/spark-${SPARK_VERSION}/spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz \
    | tar -xz -C /opt && \
    mv /opt/spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION} /opt/spark

# Install Python deps
COPY requirements.txt /tmp/
RUN pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org \
    --no-cache-dir -r /tmp/requirements.txt

# Add health check
HEALTHCHECK --interval=30s --timeout=3s \
    CMD curl -f http://localhost:8888 || exit 1

WORKDIR /app
COPY . /app
RUN useradd -m appuser && chown -R appuser:appuser /app
USER appuser