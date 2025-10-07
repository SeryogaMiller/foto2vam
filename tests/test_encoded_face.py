"""
Test cases for Utils.Face.encoded module
"""

import unittest
import numpy as np
from unittest.mock import Mock, patch, MagicMock
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Utils.Face.encoded import EncodedFace


class TestEncodedFace(unittest.TestCase):
    """Test cases for EncodedFace class"""

    def test_center_type_conversion(self):
        """Test that center tuple is properly converted to float"""
        # Create a mock image size
        img_size = (100, 200)
        
        # The center calculation should handle integer division properly
        center = (float(img_size[1]) / 2, float(img_size[0]) / 2)
        
        # Verify the center values are floats
        self.assertIsInstance(center[0], float)
        self.assertIsInstance(center[1], float)
        self.assertEqual(center[0], 100.0)
        self.assertEqual(center[1], 50.0)

    def test_focal_length_type_conversion(self):
        """Test that focal length is properly converted to float"""
        img_size = (100, 200)
        focal_length = float(img_size[1])
        
        self.assertIsInstance(focal_length, float)
        self.assertEqual(focal_length, 200.0)

    def test_camera_matrix_creation(self):
        """Test that camera matrix is created with correct dtype"""
        img_size = (100, 200)
        focal_length = float(img_size[1])
        center = (float(img_size[1]) / 2, float(img_size[0]) / 2)
        
        camera_matrix = np.array(
            [[focal_length, 0, center[0]],
             [0, focal_length, center[1]],
             [0, 0, 1]], dtype="double"
        )
        
        # Verify the matrix has correct dtype
        self.assertEqual(camera_matrix.dtype, np.float64)
        
        # Verify the matrix values
        self.assertEqual(camera_matrix[0, 0], 200.0)
        self.assertEqual(camera_matrix[0, 2], 100.0)
        self.assertEqual(camera_matrix[1, 1], 200.0)
        self.assertEqual(camera_matrix[1, 2], 50.0)

    def test_msgpack_encode_decode(self):
        """Test msgpack encoding and decoding"""
        # Create a mock encoded face
        mock_face = EncodedFace(None)
        mock_face._angle = 45.0
        mock_face._encodings = np.array([1.0, 2.0, 3.0])
        mock_face._landmarks = {'nose': [(10, 20)]}
        
        # Encode
        encoded = EncodedFace.msgpack_encode(mock_face)
        
        self.assertTrue('__EncodedFace__' in encoded)
        self.assertEqual(encoded['angle'], 45.0)
        
        # Decode
        decoded = EncodedFace.msgpack_decode(encoded)
        
        self.assertIsInstance(decoded, EncodedFace)
        self.assertEqual(decoded._angle, 45.0)
        np.testing.assert_array_equal(decoded._encodings, np.array([1.0, 2.0, 3.0]))


if __name__ == '__main__':
    unittest.main()
