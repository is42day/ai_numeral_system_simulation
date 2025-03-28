#!/bin/bash

echo "🔍 Checking for running Jupyter instances..."
pkill -f jupyter || true

echo "🚀 Starting JupyterLab in background..."
nohup jupyter lab \
    --ip=0.0.0.0 \
    --port=8888 \
    --no-browser \
    --allow-root > /app/jupyter.log 2>&1 &

sleep 2

if ! lsof -i :8888 > /dev/null; then
    echo "❌ JupyterLab failed to start. Check /app/jupyter.log"
    exit 1
fi

echo "📄 Jupyter logs: /app/jupyter.log"

echo "🔥 Warming up Spark UI..."
nohup bash -c 'python3 -c "
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName(\"WarmUp\").getOrCreate()
spark.range(1).count()
print(\"✅ Spark UI is ready:\", spark.sparkContext.uiWebUrl)
"' > /app/spark-warmup.log 2>&1 &

echo "📄 Spark warm-up logs: /app/spark-warmup.log"

echo "✅ All services launched."
