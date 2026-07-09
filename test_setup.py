"""
Test script to verify the AI Data Visualization application setup
"""

import sys
import importlib

def test_imports():
    """Test if all required packages are installed"""
    
    required_packages = [
        'flask',
        'pandas',
        'openpyxl',
        'docx',
        'plotly',
        'numpy',
        'sklearn'
    ]
    
    print("Testing package imports...")
    print("-" * 50)
    
    all_ok = True
    for package in required_packages:
        try:
            if package == 'docx':
                importlib.import_module('docx')
            elif package == 'sklearn':
                importlib.import_module('sklearn')
            else:
                importlib.import_module(package)
            print(f"✓ {package:20s} - OK")
        except ImportError as e:
            print(f"✗ {package:20s} - MISSING")
            all_ok = False
    
    print("-" * 50)
    
    if all_ok:
        print("\n✓ All packages are installed correctly!")
        return True
    else:
        print("\n✗ Some packages are missing. Please run: pip install -r requirements.txt")
        return False

def test_modules():
    """Test if custom modules can be imported"""
    
    print("\nTesting custom modules...")
    print("-" * 50)
    
    modules = [
        'modules.data_extraction',
        'modules.data_cleaning',
        'modules.eda',
        'modules.visualization'
    ]
    
    all_ok = True
    for module in modules:
        try:
            importlib.import_module(module)
            print(f"✓ {module:30s} - OK")
        except ImportError as e:
            print(f"✗ {module:30s} - MISSING")
            print(f"  Error: {e}")
            all_ok = False
    
    print("-" * 50)
    
    if all_ok:
        print("\n✓ All custom modules are available!")
        return True
    else:
        print("\n✗ Some modules are missing. Check file structure.")
        return False

def test_directories():
    """Test if required directories exist"""
    
    print("\nTesting directory structure...")
    print("-" * 50)
    
    import os
    
    required_dirs = [
        'modules',
        'templates',
        'uploads',
        'output'
    ]
    
    all_ok = True
    for dir_name in required_dirs:
        if os.path.exists(dir_name):
            print(f"✓ {dir_name:20s} - EXISTS")
        else:
            print(f"✗ {dir_name:20s} - MISSING (will be created on first run)")
    
    print("-" * 50)
    
    return True

def run_all_tests():
    """Run all tests"""
    
    print("\n" + "="*50)
    print("AI DATA VISUALIZATION - SETUP TEST")
    print("="*50 + "\n")
    
    results = []
    
    results.append(("Package Imports", test_imports()))
    results.append(("Custom Modules", test_modules()))
    results.append(("Directory Structure", test_directories()))
    
    print("\n" + "="*50)
    print("TEST SUMMARY")
    print("="*50)
    
    for test_name, result in results:
        status = "✓ PASS" if result else "✗ FAIL"
        print(f"{test_name:30s}: {status}")
    
    print("="*50 + "\n")
    
    if all(r[1] for r in results):
        print("✓ All tests passed! You can start the application with: python app.py")
        return 0
    else:
        print("✗ Some tests failed. Please fix the issues above.")
        return 1

if __name__ == "__main__":
    sys.exit(run_all_tests())
