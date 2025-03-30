# 🔥 PySpark Learning Lab

Welcome to the **PySpark Learning Lab**! This repository offers a fully Dockerized, Spark-enabled Python environment tailored for hands-on data processing, analytics, and machine learning with PySpark.


## 🚀 Project Features

- 🐳 **Docker-Based Development**: Seamlessly set up and manage your development environment using Docker and VS Code Dev Containers.
- 🔥 **Apache Spark 3.5.5**: Pre-installed with Java 17 for robust big data processing capabilities.
- 📊 **JupyterLab Integration**: Automatically launches within the container on port `8888`, providing an interactive interface for your data analysis and visualization needs.
- 🧪 **Ready-to-Use PySpark**: PySpark is pre-configured, allowing immediate execution of Spark jobs.
- ⚡ **Efficient Package Management**: Utilizes `uv` for ultrafast Python package installations.
- 🧠 **Developer-Friendly Tools**: Comes equipped with linting, autocomplete, notebooks, and a Python terminal to enhance your coding experience.


## 📁 Project Structure
pyspark-learning/ ├── notebooks/ # Jupyter Notebooks for lessons & experiments ├── scripts/ # PySpark Python scripts ├── data/ # Sample datasets (CSV, JSON, Parquet) ├── .devcontainer/ # Docker + VS Code configuration │ ├── Dockerfile │ └── devcontainer.json ├── requirements.txt # Python dependencies └── README.md # Project documentation (you're reading it)


## 🛠️ Getting Started

### 🧳 Prerequisites

Before you begin, ensure you have the following installed on your system:

- **Docker**: [Download and Install Docker](https://www.docker.com/get-started)
- **Visual Studio Code (VS Code)**: [Download VS Code](https://code.visualstudio.com/)
- **Dev Containers Extension for VS Code**: [Install Dev Containers Extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)

### 🛠️ Setup Instructions

Follow these steps to set up your development environment:

1️⃣ Clone the Repository

Terminal:
git clone https://github.com/is42day/pyspark-learning
cd pyspark-learning

Open the Project in VS Code:

Launch VS Code and open the pyspark-learning directory.
2️⃣ Open the Project in VS Code
Launch Visual Studio Code

Open the cloned folder (pyspark-learning)

3️⃣ Reopen in Dev Container
On first open, VS Code should prompt:

💡 "Would you like to reopen in a Dev Container?"

✅ Click "Reopen in Container"

If the prompt doesn't show up:

Press F1 or Ctrl+Shift+P to open the Command Palette

Search and select ➡️ "Dev Containers: Reopen in Container"

⏱️ Note: The first time, it may take a few minutes to download and build the image.

4️⃣ Access JupyterLab
Once the container is running:
Run this in terminal to start JupiterLab : jupyter lab --ip=0.0.0.0 --port=8888 --no-browser --allow-root

Open your browser

Go to 👉 http://localhost:8888

You’ll land directly in JupyterLab, ready to code!

5️⃣ Explore the Sample Notebooks
Inside JupyterLab, navigate to the 📁 notebooks/ folder

Try the interactive exercises on Spark DataFrames, transformations, and real-world datasets


📚 Lessons Available
✅ Lesson 1: SparkSession + DataFrames

🔜 Lesson 2: Reading CSVs & transforming external data

🔜 Lesson 3: Writing Parquet + Performance tips

🔜 Lesson 4: Data Aggregation and Joins

🔜 Lesson 5: E.ON projects

🤝 Contributing
Not open for pushing - but feel free to use it as a template and develop your own repo. 

🔍 Additional Setup Details
📦 .devcontainer/devcontainer.json
This file defines the development environment for VS Code using Docker.

🏷️ name: Sets the container name to "pyspark-dev" for easier reference.

🐳 dockerFile: Points to the Dockerfile used to build the image.

📁 context: Sets the build context to the parent directory. Useful if the Dockerfile relies on files outside .devcontainer.

🧩 features: Installs extra tools (like Git) using Dev Containers Features Registry. In this case: ghcr.io/devcontainers/features/git:1.

🔗 mounts: Binds your local workspace folder to /app inside the container with cached consistency for performance.

⚙️ build.args:

🔁 BUILDKIT_INLINE_CACHE: Enables Docker layer caching for faster rebuilds.

🌐 HTTP_PROXY & HTTPS_PROXY: Optional proxy settings if you're behind a firewall.

🧠 customizations.vscode.extensions:

ms-python.python: Python support.

ms-toolsai.jupyter: Jupyter notebook support.

ms-python.vscode-pylance: Autocomplete, linting, and IntelliSense.

🚪 forwardPorts:

8888: Jupyter Lab access.

4040: Spark UI access.

👤 remoteUser: Uses "appuser" inside the container for safety (instead of root).

🐳 Dockerfile Breakdown
The Dockerfile defines how the container is built.

🐍 Base Image:

python:3.9-slim: A lightweight Python image to keep things fast and simple.

🌍 Environment Variables:

SPARK_VERSION, HADOOP_VERSION: Define the versions of Spark and Hadoop to install.

SPARK_HOME: Target installation path for Spark (/opt/spark).

PATH: Adds Spark to the environment for easy CLI access.

🛠️ System Packages Installed:

☕ openjdk-17-jdk-headless: Java runtime required for Spark.

🌐 curl: For downloading Spark binaries.

🧪 git: Version control.

🔐 openssh-client: For SSH-related tasks.

📜 ca-certificates: Ensure SSL works when accessing external APIs.

🧹 Cleanup (apt-get clean, rm -rf) to keep image small.

🔥 Spark Installation:

Uses curl to download Spark from Apache mirrors and extracts it into /opt/spark.

🐍 Python Dependencies:

Installs all Python dependencies listed in requirements.txt using pip.

👷‍♂️ User Setup:

Adds a non-root user called appuser for better security and development safety.

Sets the working directory to /app and gives appropriate permissions.

✅ Development Tools & Commands
This project includes a Makefile to simplify formatting, linting, and testing tasks using Ruff and pytest.

🧼 Code Formatting & Linting (via Ruff)

Commands

make fmt	    Auto-format all Python files
make fmt-check	Check formatting without changing files
make lint	    Run Ruff to find style/linting issues
make fix	    Fix all autofixable lint issues with Ruff

🧪 Run Tests (via pytest)
make test	Run all test files via pytest

💬 Bonus Tips
Use ruff check . --select I to organize imports (like isort).

Use pytest -v for verbose test output.

Combine commands for max productivity:
make fmt lint test


🧼 PySpark Regex Cheat Sheet for Data Cleaning
🔹 Whitespace & Spacing
Regex	Purpose	Example
\\s+	Match one or more whitespace	" a \t b " → "a b"
^\\s+	Match leading whitespace	" abc" → "abc"
\\s+$	Match trailing whitespace	"abc " → "abc"
`^\s+	\s+$`	Match leading or trailing whitespace
[^\\S\\r\\n]+	Match inline whitespace (but preserve \n)	"a b" → "a b"

🔹 Digits and Numbers
Regex	Purpose	Example
\\d+	Match digits	"abc123" → "123"
[^\\d]	Match non-digits	"abc123" → "abc"
\\d{4}	Match exactly 4 digits	"2023-10" → "2023"
\\d{2,4}	Match 2 to 4 digits	"ab1234" → "1234"

🔹 Letters and Words
Regex	Purpose	Example
[A-Za-z]+	Match letters only	"abc123" → "abc"
[^A-Za-z]	Remove non-letters	"a1b2c3" → "abc"
[a-z]{3}	Match 3 lowercase letters	"abcDEF" → "abc"

🔹 Alphanumeric / Word Cleanup
Regex	Purpose	Example
\\w+	Match word characters ([A-Za-z0-9_])	"abc_123" → "abc_123"
\\W+	Match non-word characters	"abc@123" → "@"
[^A-Za-z0-9_]	Match non-alphanum + underscore	"a$ b#" → "$", "#"

🔹 Symbols & Special Characters
Regex	Purpose	Example
[!@#\$%\^&\*]+	Match common symbols	"abc@123!" → "@!"
[^\\w\\s]	Match non-word, non-space characters	"a_b!c" → "!"
[\\p{Punct}]	Match all punctuation (Unicode aware)	"hello!" → "!"

🔹 Line Breaks & Tabs
Regex	Purpose	Example
\\n	Match newline	"a\\nb" → "\\n"
\\r	Match carriage return	"a\\rb"
\\t	Match tab	"a\\tb"
[\\r\\n\\t]+	Match line breaks/tabs	"a\\tb\\nc"

🔹 General Cleaning Patterns
Regex	Purpose
[^A-Za-z0-9\\s]	Remove all punctuation except spaces
\\s{2,}	Collapse multiple spaces to one
[^A-Za-z0-9]	Keep only alphanumeric characters
[^\\x00-\\x7F]	Remove non-ASCII characters (e.g., emojis)
\\bword\\b	Match whole word "word"
(?i)word	Case-insensitive match for "word"

📜 License
MIT License — do whatever you want, just don’t blame me 😄
