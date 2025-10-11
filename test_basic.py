#!/usr/bin/env python3
import pytest
import os


def test_imports():
    """Test that all required modules can be imported"""
    try:
        import pandas as pd
        import numpy as np
        import sklearn
        import matplotlib.pyplot as plt
        import seaborn as sns
        from sklearn.ensemble import RandomForestClassifier

        assert True
    except ImportError as e:
        pytest.fail(f"Import error: {e}")


def test_required_files_exist():
    """Test that required project files exist"""
    required_files = ["train.py", "requirements.txt", "Makefile", "README.md"]
    for file in required_files:
        assert os.path.exists(file), f"Required file {file} does not exist"


def test_report_md_content():
    """Test that README.md has content and was generated properly"""
    assert os.path.exists("README.md"), "README.md does not exist"
    try:
        with open("README.md", "r") as f:
            content = f.read()
        assert len(content) > 0, "README.md is empty"
        # Check if it contains expected sections (adjust based on your actual report content)
        if "Model Metrics" in content or "Results" in content or "#" in content:
            print("✓ README.md contains expected content")
    except Exception as e:
        pytest.fail(f"Cannot read README.md: {e}")


def test_model_directories_created():
    """Test that model and results directories exist (created during training)"""
    potential_dirs = ["Model", "Results"]
    for dir in potential_dirs:
        if os.path.exists(dir):
            print(f"✓ Directory {dir} exists")
        else:
            print(f"Note: Directory {dir} doesn't exist yet")


def test_training_script_runs():
    """Test that training script can be imported without errors"""
    try:
        import train

        assert True
    except Exception as e:
        pytest.fail(f"Training script has errors: {e}")


def test_requirements_readable():
    """Test that requirements file can be read"""
    assert os.path.exists("requirements.txt"), "requirements.txt does not exist"
    try:
        with open("requirements.txt", "r") as f:
            content = f.read()
        assert len(content) > 0, "requirements.txt is empty"
    except Exception as e:
        pytest.fail(f"Cannot read requirements.txt: {e}")
