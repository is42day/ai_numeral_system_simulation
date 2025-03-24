print("🚀 AI Numeral System Simulation is starting inside the container...")
import logging
import os
import numpy as np
import random
import pandas as pd

# Set up logging
log_file = "/app/simulation.log"  # Path inside the container
logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

# Also log to the console
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
console_handler.setFormatter(formatter)
logging.getLogger().addHandler(console_handler)

logging.info("🚀 AI Numeral System Simulation started.")


# Define an AI Learner class with extended arithmetic operations
class ExtendedAILearner:
    def __init__(self, base, learning_rate=0.1, decay=0.99):
        self.base = base
        self.knowledge = {}
        self.learning_rate = learning_rate
        self.decay = decay

    def learn(self, num1, num2, operation):
        key = (num1, num2, operation)
        if key not in self.knowledge:
            self.knowledge[key] = self._calculate(num1, num2, operation) + random.uniform(-0.2, 0.2)
        else:
            correct_answer = self._calculate(num1, num2, operation)
            self.knowledge[key] += self.learning_rate * (correct_answer - self.knowledge[key])
            self.learning_rate *= self.decay

    def _calculate(self, num1, num2, operation):
        if operation == "+":
            return (num1 + num2) % self.base
        elif operation == "-":
            return (num1 - num2) % self.base
        elif operation == "*":
            return (num1 * num2) % self.base
        elif operation == "/":
            return (num1 / num2) if num2 != 0 else None
        elif operation == "**":
            return (num1 ** num2) % self.base
        elif operation == "%":
            return num1 % num2 if num2 != 0 else None

    def test_knowledge(self, num1, num2, operation):
        key = (num1, num2, operation)
        return self.knowledge.get(key, None)

# Define numeral bases to compare
bases = [10, 12, 16]

# Initialize AI learners
learners = {base: ExtendedAILearner(base) for base in bases}

# Training phase
num_iterations = random.randint(4000, 6000)  # Each base trains for a different number of iterations
for _ in range(num_iterations):
    for base in bases:
        num1 = random.randint(1, base - 1)
        num2 = random.randint(1, base - 1)
        operation = random.choice(["+", "-", "*", "/", "**", "%"])
        learners[base].learn(num1, num2, operation)

# Testing phase
test_problems = [
    (3, 4, "+"), (6, 2, "-"), (5, 3, "*"), (8, 2, "/"),
    (2, 3, "**"), (10, 4, "%"), (7, 5, "**"), (9, 3, "%")
]
results = []

for base in bases:
    for num1, num2, operation in test_problems:
        ai_answer = learners[base].test_knowledge(num1, num2, operation)
        results.append({"Base": base, "Num1": num1, "Num2": num2, "Operation": operation, "AI Answer": ai_answer})

# Convert results into a DataFrame and save to CSV
df_results = pd.DataFrame(results)
df_results.to_csv("/app/ai_numeral_system_results.csv", index=False, mode="w")

import matplotlib.pyplot as plt

# Read the generated CSV file
csv_file = "/app/ai_numeral_system_results.csv"
df_results = pd.read_csv(csv_file)

# Count occurrences of operations per base
operation_counts = df_results.groupby("Base")["Operation"].count()

# Plot the results
plt.figure(figsize=(8, 5))
operation_counts.plot(kind="bar", color=["blue", "green", "red"])
plt.xlabel("Numeral Base")
plt.ylabel("Number of Operations")
plt.title("Operation Counts per Numeral Base")
plt.xticks(rotation=0)
plt.grid(axis="y")

# Save the figure
graph_path = "/app/simulation_results.png"
plt.savefig(graph_path)

logging.info(f"📊 Simulation results graph saved as '{graph_path}'")


# Print logging message
logging.info("✅ AI Learner Simulation Completed. Results saved as 'ai_numeral_system_results.csv'.")
