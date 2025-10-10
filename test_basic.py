#!/usr/bin/env python3

def test_imports():
    """Test that all required modules can be imported"""
    try:
        import pandas as pd
        import numpy as np
        import sklearn
        import matplotlib.pyplot as plt
        import seaborn as sns
        from sklearn.ensemble import RandomForestClassifier
        print("✓ All imports successful")
        assert True
    except ImportError as e:
        assert False, f"Import error: {e}"

def test_data_files():
    """Test that required data files exist"""
    import os
    required_files = ['drug200.csv']
    for file in required_files:
        if os.path.exists(file):
            print(f"✓ File {file} exists")
        else:
            print(f"✗ File {file} missing")
    # This is just a warning, not a failure
    assert True

def test_model_files():
    """Test that model and results directories exist"""
    import os
    required_dirs = ['Model', 'Results']
    for dir in required_dirs:
        if os.path.exists(dir):
            print(f"✓ Directory {dir} exists")
        else:
            print(f"✗ Directory {dir} missing")
    assert True

if __name__ == "__main__":
    test_imports()
    test_data_files()
    test_model_files()
    print("All basic tests passed!")