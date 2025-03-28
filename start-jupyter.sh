#!/bin/bash

echo "🔍 Checking for running Jupyter instances..."
pkill -f jupyter || true

echo "🚀 Starting JupyterLab in background..."
nohup jupyter lab \
    --ip=0.0.0.0 \
    --port=8888 \
    --no-browser \
    --allow-root \
    > /app/jupyter.log 2>&1 &

echo "📄 Jupyter logs → /app/jupyter.log"

# Run Spark warm-up in background to avoid blocking
echo "🔥 Warming up Spark (this will trigger port 4040)..."
nohup bash -c 'python3 -c "
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName(\"WarmUp\").getOrCreate()
spark.range(1).count()
print(\"✅ Spark UI ready at:\", spark.sparkContext.uiWebUrl)
"' > /app/spark-warmup.log 2>&1 &

echo "📄 Spark warm-up logs → /app/spark-warmup.log"

echo "✅ All startup scripts triggered (non-blocking mode). DevContainer is ready."
