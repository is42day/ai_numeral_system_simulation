# utils/notebook_setup.py

import os
import sys

def enable_project_imports():
    """
    Ensures that the root of the project is added to sys.path.
    This allows importing project modules from anywhere (e.g., notebooks, scripts).
    """
    try:
        # Get the absolute path to the current file (inside utils/)
        current_file_path = os.path.abspath(__file__)
        # Move two levels up to the project root
        project_root = os.path.abspath(os.path.join(current_file_path, "..", ".."))

        if project_root not in sys.path:
            sys.path.insert(0, project_root)
            print(f"🔧 [notebook_setup] Project root added to sys.path: {project_root}")
        else:
            print("✅ [notebook_setup] Project root already in sys.path.")

    except Exception as e:
        print(f"❌ [notebook_setup] Failed to set up import path: {e}")
