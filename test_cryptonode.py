# test_cryptonode.py
"""
Tests for CryptoNode module.
"""

import unittest
from cryptonode import CryptoNode

class TestCryptoNode(unittest.TestCase):
    """Test cases for CryptoNode class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = CryptoNode()
        self.assertIsInstance(instance, CryptoNode)
        
    def test_run_method(self):
        """Test the run method."""
        instance = CryptoNode()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
