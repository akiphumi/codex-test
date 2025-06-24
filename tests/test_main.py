import os
import subprocess
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pytest

from main import add


def test_add_basic():
    assert add(1, 2) == 3


def test_add_left_none():
    assert add(None, 5) == 5


def test_add_right_none():
    assert add(7, None) == 7


def test_add_both_none():
    assert add(None, None) == 0


def test_cli(tmp_path):
    result = subprocess.run([sys.executable, "-m", "main", "3", "4"], capture_output=True, text=True)
    assert result.stdout.strip() == "7"
