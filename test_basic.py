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

def test_data_files():
    """Test that required data files exist"""
    required_files = ['drug200.csv']
    for file in required_files:
        assert os.path.exists(file), f"Required file {file} does not exist"

def test_model_directories():
    """Test that model and results directories exist"""
    required_dirs = ['Model', 'Results']
    for dir in required_dirs:
        assert os.path.exists(dir), f"Required directory {dir} does not exist"

def test_training_script_exists():
    """Test that training script exists"""
    assert os.path.exists('train.py'), "Training script train.py does not exist"

def test_requirements_exists():
    """Test that requirements file exists"""
    assert os.path.exists('requirements.txt'), "requirements.txt does not exist"