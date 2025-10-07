"""
Setup configuration for Foto2VAM
"""

from setuptools import setup, find_packages
import os

# Read the README file for long description
def read_file(filename):
    filepath = os.path.join(os.path.dirname(__file__), filename)
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()
    return ""

setup(
    name='foto2vam',
    version='1.1.0',
    author='SeryogaMiller',
    description='Generate VAM character models from photographs using machine learning',
    long_description=read_file('README.md'),
    long_description_content_type='text/markdown',
    url='https://github.com/SeryogaMiller/foto2vam',
    packages=find_packages(),
    python_requires='>=3.10',
    install_requires=[
        'pyautogui>=0.9.54',
        'cmake>=3.25.0',
        'dlib>=19.24.0',
        'face_recognition>=1.3.0',
        'deap>=1.4.1',
        'opencv-python>=4.8.0',
        'imutils>=0.5.4',
        'tensorflow>=2.13.0',
        'keras>=2.13.0',
        'numpy>=1.24.0,<2.0.0',
        'Pillow>=10.0.0',
    ],
    extras_require={
        'train': [
            'msgpack>=1.0.5',
            'tqdm>=4.66.0',
        ],
        'dev': [
            'pytest>=7.4.0',
            'pytest-cov>=4.1.0',
            'pytest-mock>=3.11.1',
            'flake8>=6.0.0',
            'pylint>=2.17.0',
        ],
    },
    entry_points={
        'console_scripts': [
            'foto2vam=foto2vam:main',
        ],
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: Multimedia :: Graphics',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
    ],
    keywords='vam character-generation machine-learning face-recognition',
)
