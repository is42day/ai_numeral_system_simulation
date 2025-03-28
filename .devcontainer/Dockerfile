FROM python:3.9-slim

# Spark/Hadoop config
ENV SPARK_VERSION=3.5.5
ENV HADOOP_VERSION=3
ENV SPARK_HOME=/opt/spark
ENV PATH=$PATH:$SPARK_HOME/bin

# Install system dependencies, Java, and tools
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        make \
        openjdk-17-jdk-headless \
        curl \
        git \
        openssh-client \
        ca-certificates \
        sudo && \
        procps && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* && \
    update-ca-certificates && \
    echo "appuser ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers && \
    chmod 0440 /etc/sudoers

# Download and install Spark
RUN curl -k -fsSL https://downloads.apache.org/spark/spark-${SPARK_VERSION}/spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz \
    | tar -xz -C /opt && \
    mv /opt/spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION} /opt/spark

# Install Python dependencies
COPY requirements.txt /tmp/
RUN pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org \
    --no-cache-dir -r /tmp/requirements.txt

# Set working directory and copy source
WORKDIR /app
COPY . /app

# Create a non-root user
RUN useradd -m appuser && chown -R appuser:appuser /app
RUN chmod +x /app/start-jupyter.sh
USER appuser

# Expose Jupyter and Spark UI ports
EXPOSE 8888 4040

# Add health check for Jupyter
HEALTHCHECK --interval=30s --timeout=3s CMD curl -f http://localhost:8888 || exit 1

# Default command: launch JupyterLab
CMD ["jupyter", "lab", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]