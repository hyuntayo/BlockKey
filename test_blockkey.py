# test_blockkey.py
"""
Tests for BlockKey module.
"""

import unittest
from blockkey import BlockKey

class TestBlockKey(unittest.TestCase):
    """Test cases for BlockKey class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = BlockKey()
        self.assertIsInstance(instance, BlockKey)
        
    def test_run_method(self):
        """Test the run method."""
        instance = BlockKey()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
