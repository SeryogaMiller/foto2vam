"""
Test cases for Utils.Training.config module
"""

import unittest
import json
import os
import tempfile
import sys

# Add parent directory to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Utils.Training.config import Config


class TestConfig(unittest.TestCase):
    """Test cases for Config class"""

    def setUp(self):
        """Set up test fixtures"""
        # Create temporary directory for test files
        self.test_dir = tempfile.mkdtemp()
        
        # Create a minimal base JSON file
        self.base_json = os.path.join(self.test_dir, "base.json")
        with open(self.base_json, 'w') as f:
            json.dump({
                "storables": [
                    {
                        "id": "geometry",
                        "morphs": [
                            {"name": "test_morph", "value": 0.5, "animatable": True}
                        ]
                    }
                ]
            }, f)

    def tearDown(self):
        """Clean up test files"""
        import shutil
        shutil.rmtree(self.test_dir, ignore_errors=True)

    def test_config_version(self):
        """Test that config version is properly defined"""
        self.assertEqual(Config.CONFIG_VERSION, 1)

    def test_parse_params_basic(self):
        """Test basic parameter parsing"""
        config_data = {
            "baseJson": self.base_json,
            "inputs": [
                {
                    "name": "encoding",
                    "params": [
                        {"name": "angle", "value": "0"}
                    ]
                }
            ],
            "outputs": [
                {
                    "name": "json",
                    "params": []
                }
            ]
        }
        
        config = Config(config_data, self.test_dir)
        
        # Verify angles are collected
        self.assertIn(0.0, config.getAngles())

    def test_parse_params_with_error_handling(self):
        """Test that parameter parsing handles errors gracefully"""
        config_data = {
            "baseJson": self.base_json,
            "inputs": [
                {
                    "name": "encoding",
                    "params": [
                        {"name": "angle", "value": "0"}
                    ]
                },
                # This param is missing required fields
                {
                    "params": []
                }
            ]
        }
        
        # Should not raise an exception, just skip the bad param
        config = Config(config_data, self.test_dir)
        
        # Should still have parsed the valid param
        self.assertIn(0.0, config.getAngles())

    def test_multiple_angles(self):
        """Test parsing multiple angles"""
        config_data = {
            "baseJson": self.base_json,
            "inputs": [
                {
                    "name": "encoding",
                    "params": [
                        {"name": "angle", "value": "0"}
                    ]
                },
                {
                    "name": "encoding",
                    "params": [
                        {"name": "angle", "value": "45"}
                    ]
                },
                {
                    "name": "encoding",
                    "params": [
                        {"name": "angle", "value": "-45"}
                    ]
                }
            ]
        }
        
        config = Config(config_data, self.test_dir)
        angles = config.getAngles()
        
        # Verify all angles are present and sorted
        self.assertEqual(len(angles), 3)
        self.assertIn(0.0, angles)
        self.assertIn(45.0, angles)
        self.assertIn(-45.0, angles)
        # Check they're sorted
        self.assertEqual(angles, sorted(angles))


if __name__ == '__main__':
    unittest.main()
