import os
from pathlib import Path

def test_config_exists():
    assert Path('configs/default.yaml').exists()

def test_data_script_exists():
    assert Path('src/data_download.py').exists()
