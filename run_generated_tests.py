#!/usr/bin/env python3
import sys
import os
import glob
import importlib.util
from pathlib import Path

# Add current directory to Python path
sys.path.insert(0, os.getcwd())

def run_test_function(test_func):
    """Run a single test function and return results"""
    try:
        test_func()
        return True, None
    except Exception as e:
        return False, str(e)

def run_tests_from_file(file_path):
    """Load and run all test functions from a file"""
    spec = importlib.util.spec_from_file_location("test_module", file_path)
    module = importlib.util.module_from_spec(spec)
    
    try:
        spec.loader.exec_module(module)
    except Exception as e:
        return [(f"Load Error in {file_path}", False, str(e))]
    
    results = []
    for attr_name in dir(module):
        if attr_name.startswith('test_'):
            test_func = getattr(module, attr_name)
            if callable(test_func):
                success, error = run_test_function(test_func)
                results.append((f"{file_path}::{attr_name}", success, error))
    
    return results

def main():
    test_dir = "dryrun_tests"
    test_pattern = os.path.join(test_dir, "test_case_*.py")
    test_files = glob.glob(test_pattern)
    
    if not test_files:
        print(f"No test files found in {test_dir}")
        return
    
    print(f"Found {len(test_files)} test files")
    print("="*50)
    
    total_tests = 0
    passed_tests = 0
    failed_tests = 0
    errors = []
    
    for i, test_file in enumerate(sorted(test_files), 1):
        if i <= 10:  # Run first 10 tests as a sample
            print(f"Running {test_file}...")
            results = run_tests_from_file(test_file)
            
            for test_name, success, error in results:
                total_tests += 1
                if success:
                    passed_tests += 1
                    print(f"  ✅ {test_name}")
                else:
                    failed_tests += 1
                    print(f"  ❌ {test_name}: {error}")
                    errors.append((test_name, error))
        
    print("\n" + "="*50)
    print(f"Test Summary (first 10 files):")
    print(f"Total tests: {total_tests}")
    print(f"Passed: {passed_tests}")
    print(f"Failed: {failed_tests}")
    
    if errors:
        print("\nErrors:")
        for test_name, error in errors[:5]:  # Show first 5 errors
            print(f"  {test_name}: {error}")
        if len(errors) > 5:
            print(f"  ... and {len(errors) - 5} more errors")

if __name__ == "__main__":
    main()

