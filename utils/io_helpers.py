import os
from pyspark.sql import SparkSession, DataFrame

def list_files_with_aliases(folder: str, ext: str = "json") -> dict:
    """
    Lists files in a folder and assigns aliases like file1, file2, ...
    Returns a dict: {alias: full_path}
    """
    files = sorted([f for f in os.listdir(folder) if f.endswith(f".{ext}")])
    return {f"file{i+1}": os.path.join(folder, f) for i, f in enumerate(files)}

def load_file_with_alias(spark: SparkSession, folder: str, alias: str, ext: str = "json") -> DataFrame:
    """
    Loads a file from folder based on alias and file extension.
    Supports json and parquet.
    """
    aliases = list_files_with_aliases(folder, ext)
    if alias not in aliases:
        raise ValueError(f"Alias '{alias}' not found. Available: {list(aliases.keys())}")
    
    path = aliases[alias]
    print(f"📥 Loading file: {alias} → {path}")
    
    if ext == "json":
        return spark.read.json(path)
    elif ext == "parquet":
        return spark.read.parquet(path)
    else:
        raise ValueError("Unsupported file type. Use 'json' or 'parquet'.")
