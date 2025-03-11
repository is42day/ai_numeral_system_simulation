# 🧠 AI Numeral System Simulation

## 📌 Project Overview
This project explores **how AI learners understand arithmetic** in different numeral systems: **Base-10, Base-12, and Base-16**. The goal is to analyze whether alternative numeral systems offer advantages in calculations, efficiency, or real-world applications.

## 🚀 Features
- AI learners trained to perform **arithmetic operations** (`+`, `-`, `*`, `/`, `**`, `%`).
- **Comparison of learning efficiency** across different number bases.
- **Automated logging** to track results.
- **Data visualization** to display AI learning performance.
- **Runs inside Docker** for easy setup and execution.
- **Uses Docker Compose** to simplify running multiple simulations.

---

## 🛠 Technologies Used
- **Python** (Numpy, Pandas, Matplotlib, Logging)
- **Docker & Docker Compose** (for containerization)
- **GitHub** (Version Control)

---

## 📥 Installation & Setup

### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/YOUR_USERNAME/ai_numeral_system_simulation.git
cd ai_numeral_system_simulation
```

### **2️⃣ Install Dependencies (Optional for Local Execution)**
If you want to run the script outside Docker:
```bash
pip install -r requirements.txt
```

### **3️⃣ Run the Project with Docker Compose**
To execute the simulation inside a Docker container, simply run:
```bash
docker-compose up --build
```
This will:
✅ Build the Docker image.  
✅ Run the AI simulation.  
✅ Save results in a CSV file & generate a visualization.

---

## 📊 How It Works
1. **AI Learners** are initialized for Base-10, Base-12, and Base-16.
2. They are **trained** with arithmetic operations.
3. The results are **logged** and stored in `simulation.log`.
4. A **graph is generated** (`simulation_results.png`) to compare performance.
5. The final dataset is **saved to `ai_numeral_system_results.csv`**.

---

## 📂 Project Structure
```
📁 ai_numeral_system_simulation
 ├── 📄 ai_numeral_system_simulation.py   # Main AI training script
 ├── 📄 Dockerfile                        # Defines the Docker environment
 ├── 📄 docker-compose.yml                # Simplifies container execution
 ├── 📄 requirements.txt                   # Python dependencies
 ├── 📄 simulation.log                     # Logs AI learning progress
 ├── 📊 simulation_results.png             # Visual representation of results
 ├── 📄 ai_numeral_system_results.csv      # AI simulation results (CSV)
 ├── 📄 README.md                          # Documentation (this file)
```

---

## 📌 Example Output
After running the simulation, you will see:
✅ **Terminal Output:**
```bash
🚀 AI Numeral System Simulation is starting inside the container...
✅ AI Learner Simulation Completed. Results saved as 'ai_numeral_system_results.csv'.
```
✅ **Generated Files:**
- `simulation_results.png` (Graph showing the number of operations per numeral base)
- `ai_numeral_system_results.csv` (Detailed results of AI learning)
- `simulation.log` (Logs tracking the AI’s learning process)

---

## 🏆 Next Steps
🚀 **Possible Improvements:**
- **Smarter AI Learning:** Adjust learning speeds for different bases.
- **Web Dashboard:** Display results in a live web interface.
- **Parallel Simulations:** Run multiple AI training sessions at once.
- **GitHub Actions Automation:** Auto-run tests and build Docker images.

Would you like to contribute? **Pull requests are welcome!**

---

## 🤝 Contributing
1. **Fork this repository**
2. **Create a new branch** (`feature-branch`)
3. **Commit your changes** (`git commit -m 'Added new feature'`)
4. **Push to your branch** (`git push origin feature-branch`)
5. **Create a Pull Request** 🚀

---

## 📜 License
This project is open-source and available under the **MIT License**.

---

## 📬 Contact
🔗 **GitHub:** [IS42DAY](https://github.com/is42day)  
📧 **Email:** antifree@gmail.com

---

**Happy Coding! 🚀**

