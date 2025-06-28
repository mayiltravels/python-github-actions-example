import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from app import index  # Now this works because Python knows about 'src'

def test_index():
    assert index() == "Hello, world!"