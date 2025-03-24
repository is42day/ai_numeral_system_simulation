# 🔥 PySpark Learning Lab

Welcome to your fully Dockerized, Spark-enabled Python environment designed for hands-on data processing, analytics, and machine learning with PySpark.

---

## 🚀 Project Features

- 🐳 **Docker-based** development environment using VSCode Dev Containers
- 🔥 **Apache Spark 3.5.5** installed with Java 17
- 📊 **Jupyter Lab** auto-launching inside container (on port `8888`)
- 🧪 **PySpark** pre-installed and ready to run
- ⚡ Uses `uv` for ultrafast pip installations
- 🧠 Dev-friendly: linting, autocomplete, notebooks, and Python terminal

---

## 📁 Project Structure

pyspark-learning/ ├── notebooks/ # Jupyter Notebooks for lessons & experiments ├── scripts/ # PySpark Python scripts ├── data/ # Sample datasets (CSV, JSON, Parquet) ├── .devcontainer/ # Docker + VSCode config │ ├── Dockerfile │ └── devcontainer.json ├── requirements.txt # Python dependencies └── README.md # You're reading it


---

## 🛠️ Getting Started

### 🧳 Prerequisites
- Docker
- Visual Studio Code
- Dev Containers extension installed

### 🧪 Launch Environment

```bash
git clone https://github.com/YOUR_USERNAME/pyspark-learning.git
cd pyspark-learning
# Open in VSCode and select "Reopen in Container" when prompted

📚 Lessons Available
✅ Lesson 1: SparkSession + DataFrames

🔜 Lesson 2: Reading CSVs & transforming external data

🔜 Lesson 3: Writing Parquet + Performance tips

🔜 Lesson 4: Data Aggregation and Joins

🔜 Lesson 5: ML with PySpark

🤝 Contributing
Feel free to fork and submit PRs with additional lessons, improvements, or data sets. This repo is intended as a learning lab for aspiring Spark + Python engineers.

📜 License
MIT License — do whatever you want, just don’t blame me 😄