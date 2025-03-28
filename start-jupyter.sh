#!/bin/bash

echo "🔍 Checking for running Jupyter instances..."
pkill -f jupyter || true

echo "🚀 Starting JupyterLab on port 8888..."
nohup jupyter lab \
    --ip=0.0.0.0 \
    --port=8888 \
    --no-browser \
    --allow-root \
    > /app/jupyter.log 2>&1 &

echo "📄 Jupyter logs: /app/jupyter.log"

echo "🔥 Warming up Spark to activate port 4040..."
nohup python3 - <<EOF > /app/spark-warmup.log 2>&1 &
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("WarmUp").getOrCreate()
spark.range(1).count()
print("✅ Spark UI is up at", spark.sparkContext.uiWebUrl)
EOF

echo "✅ All services started successfully"
