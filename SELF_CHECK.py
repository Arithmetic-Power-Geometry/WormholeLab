"""Offline package self-check. Run with: python SELF_CHECK.py"""
from __future__ import annotations
import compileall
from pathlib import Path
import subprocess, sys

root=Path(__file__).resolve().parent
print("WormholeLab self-check")
print("1/3 Compiling Python sources...")
if not compileall.compile_dir(root, quiet=1):
    raise SystemExit("Python source compilation failed")
print("2/3 Running numerical tests...")
subprocess.run([sys.executable,"-m","pytest","-q"],cwd=root,check=True)
print("3/3 Checking required repository files...")
required=["app.py","requirements.txt","README.md","LICENSE","NOTICE","CITATION.cff",".streamlit/config.toml",".github/workflows/tests.yml"]
missing=[p for p in required if not (root/p).exists()]
if missing:
    raise SystemExit(f"Missing required files: {missing}")
print("PASS: source compilation, numerical tests, and repository structure are valid.")
print("Note: Streamlit runtime launch requires dependencies from requirements.txt.")
