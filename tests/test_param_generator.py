"""
Test cases for Utils.Training.param_generator module
"""

import unittest
import numpy as np
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Utils.Training.param_generator import ParamGenerator


class TestParamGenerator(unittest.TestCase):
    """Test cases for ParamGenerator class"""

    def test_vm_add(self):
        """Test VM add operation"""
        workarea = {
            "landmarks": {"test": [10.0, 20.0]},
            "variables": {"var1": 5.0, "var2": 3.0}
        }
        
        result = ParamGenerator._vmAdd(workarea, "var1", "var2")
        self.assertEqual(result, 8.0)

    def test_vm_subtract(self):
        """Test VM subtract operation"""
        workarea = {
            "landmarks": {"test": [10.0, 20.0]},
            "variables": {"var1": 5.0, "var2": 3.0}
        }
        
        result = ParamGenerator._vmSub(workarea, "var1", "var2")
        self.assertEqual(result, 2.0)

    def test_vm_divide(self):
        """Test VM divide operation"""
        workarea = {
            "landmarks": {"test": [10.0, 20.0]},
            "variables": {"var1": 10.0, "var2": 2.0}
        }
        
        result = ParamGenerator._vmDiv(workarea, "var1", "var2")
        self.assertEqual(result, 5.0)

    def test_vm_multiply(self):
        """Test VM multiply operation"""
        workarea = {
            "landmarks": {"test": [10.0, 20.0]},
            "variables": {"var1": 5.0, "var2": 3.0}
        }
        
        result = ParamGenerator._vmMult(workarea, "var1", "var2")
        self.assertEqual(result, 15.0)

    def test_vm_resolve_variable(self):
        """Test VM variable resolution"""
        workarea = {
            "landmarks": {"nose": [10.0, 20.0]},
            "variables": {"test_var": 42.0}
        }
        
        # Test resolving a regular variable
        result = ParamGenerator._vmResolveVariable(workarea, "test_var")
        self.assertEqual(result, 42.0)
        
        # Test resolving landmark width
        result = ParamGenerator._vmResolveVariable(workarea, "nose.w")
        self.assertEqual(result, 10.0)
        
        # Test resolving landmark height
        result = ParamGenerator._vmResolveVariable(workarea, "nose.h")
        self.assertEqual(result, 20.0)

    def test_vm_set_variable(self):
        """Test VM set variable operation"""
        workarea = {
            "landmarks": {},
            "variables": {}
        }
        
        ParamGenerator._vmSetVariable(workarea, "new_var", 100.0)
        self.assertEqual(workarea["variables"]["new_var"], 100.0)

    def test_calc_sizes(self):
        """Test size calculation for landmarks"""
        landmarks = {
            "nose": [(0, 0), (10, 0), (10, 10), (0, 10)],
            "eye": [(0, 0), (5, 0)]
        }
        
        sizes = ParamGenerator._calcSizes(landmarks)
        
        # Nose should have width and height of 10
        self.assertEqual(sizes["nose"][0], 10.0)
        self.assertEqual(sizes["nose"][1], 10.0)
        
        # Eye should have width of 5 and height of 0
        self.assertEqual(sizes["eye"][0], 5.0)
        self.assertEqual(sizes["eye"][1], 0.0)

    def test_calc_average_sizes(self):
        """Test average size calculation"""
        landmarks_list = [
            {"nose": [(0, 0), (10, 0), (0, 10)]},
            {"nose": [(0, 0), (20, 0), (0, 20)]}
        ]
        
        averages = ParamGenerator._calcAverageSizes(landmarks_list)
        
        # Average should be calculated correctly
        self.assertIn("nose", averages)
        # Width average: (10 + 20) / 2 = 15
        self.assertEqual(averages["nose"][0], 15.0)
        # Height average: (10 + 20) / 2 = 15
        self.assertEqual(averages["nose"][1], 15.0)


if __name__ == '__main__':
    unittest.main()
