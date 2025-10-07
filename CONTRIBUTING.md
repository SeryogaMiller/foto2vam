# Contributing to Foto2VAM

Thank you for your interest in contributing to Foto2VAM! This document provides guidelines and instructions for contributing.

## Getting Started

1. **Fork the repository** on GitHub
2. **Clone your fork** locally:
   ```bash
   git clone https://github.com/YOUR_USERNAME/foto2vam.git
   cd foto2vam
   ```
3. **Set up your development environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   pip install -r requirements-dev.txt
   ```

## Development Workflow

### 1. Create a Branch

Create a new branch for your feature or bug fix:

```bash
git checkout -b feature/your-feature-name
# or
git checkout -b fix/issue-number-description
```

### 2. Make Your Changes

- Write clear, readable code
- Follow the existing code style
- Add comments for complex logic
- Update documentation as needed

### 3. Test Your Changes

Run the test suite before committing:

```bash
# Run all tests
python -m pytest tests/ -v

# Or using unittest
python -m unittest discover tests

# Run specific test file
python -m pytest tests/test_encoded_face.py -v
```

### 4. Commit Your Changes

Write clear, descriptive commit messages:

```bash
git add .
git commit -m "Add feature: brief description of changes"
```

Good commit message examples:
- `Fix: resolve center parsing type error in encoded.py`
- `Feature: add Docker support with multi-stage build`
- `Docs: update README with installation instructions`
- `Test: add unit tests for param_generator module`

### 5. Push and Create Pull Request

```bash
git push origin feature/your-feature-name
```

Then create a Pull Request on GitHub with:
- Clear title describing the change
- Description of what was changed and why
- Reference to any related issues

## Code Style Guidelines

### Python Code Style

- Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) style guide
- Use 4 spaces for indentation (no tabs)
- Maximum line length: 127 characters
- Use meaningful variable and function names

### Code Quality

Run linting tools before submitting:

```bash
# Check for syntax errors
flake8 . --select=E9,F63,F7,F82 --show-source --statistics

# Check code style
flake8 . --max-line-length=127 --statistics
```

### Documentation

- Update README.md if you add new features
- Add docstrings to new functions and classes
- Include inline comments for complex logic
- Update or add examples as needed

## Testing Guidelines

### Writing Tests

- Place tests in the `tests/` directory
- Name test files as `test_*.py`
- Name test functions as `test_*`
- Use descriptive test names that explain what is being tested

Example test structure:

```python
import unittest

class TestMyFeature(unittest.TestCase):
    def setUp(self):
        """Set up test fixtures"""
        pass
    
    def test_specific_functionality(self):
        """Test that specific functionality works correctly"""
        # Arrange
        input_data = ...
        
        # Act
        result = my_function(input_data)
        
        # Assert
        self.assertEqual(result, expected_value)
    
    def tearDown(self):
        """Clean up after tests"""
        pass
```

### Running Tests

```bash
# Run all tests with coverage
pytest tests/ --cov=. --cov-report=html

# Run specific test class
python -m pytest tests/test_encoded_face.py::TestEncodedFace -v

# Run with verbose output
python -m pytest tests/ -vv
```

## Docker Development

### Building Docker Images

```bash
# Build standard image
docker build -t foto2vam:dev .

# Build training image with GPU support
docker build -f Dockerfile.train -t foto2vam-train:dev .
```

### Testing Docker Builds

```bash
# Test the image
docker run --rm foto2vam:dev python --version

# Run with volume mounts for testing
docker run --rm \
  -v $(pwd)/Input:/app/Input \
  -v $(pwd)/Output:/app/Output \
  foto2vam:dev
```

## Adding New Features

### New Tools

If adding a new tool to the `Tools/` directory:

1. Create the tool file: `Tools/YourNewTool.py`
2. Include argument parsing with `argparse`
3. Add `--pydev` flag for debugging support
4. Include proper error handling
5. Add usage examples to README.md

Example structure:

```python
import argparse

def main(args):
    if args.pydev:
        print("Enabling debugging with pydev")
        import pydevd
        pydevd.settrace(suspend=False)
    
    # Your tool logic here

def parseArgs():
    parser = argparse.ArgumentParser(description="Tool description")
    parser.add_argument('--input', help="Input path", required=True)
    parser.add_argument("--pydev", action='store_true', default=False, 
                       help="Enable pydevd debugging")
    return parser.parse_args()

if __name__ == "__main__":
    args = parseArgs()
    main(args)
```

### New Dependencies

If you need to add new dependencies:

1. Add to appropriate requirements file:
   - `requirements.txt` - runtime dependencies
   - `requirements-train.txt` - training dependencies
   - `requirements-dev.txt` - development/testing dependencies

2. Pin versions for stability:
   ```
   package-name>=1.0.0,<2.0.0
   ```

3. Update Dockerfile if needed for system dependencies

## Reporting Issues

When reporting issues, please include:

- **Description**: Clear description of the problem
- **Steps to Reproduce**: Minimal steps to reproduce the issue
- **Expected Behavior**: What you expected to happen
- **Actual Behavior**: What actually happened
- **Environment**: 
  - Python version
  - Operating system
  - Relevant dependency versions
- **Logs**: Any error messages or logs

## Pull Request Checklist

Before submitting a pull request:

- [ ] Code follows the project style guidelines
- [ ] All tests pass locally
- [ ] New tests added for new functionality
- [ ] Documentation updated (README, docstrings, etc.)
- [ ] Commit messages are clear and descriptive
- [ ] Branch is up to date with master/main
- [ ] No merge conflicts

## Getting Help

- Check existing issues and pull requests
- Read the README.md and documentation
- Ask questions in issue discussions
- Review the code and existing implementations

## License

By contributing to Foto2VAM, you agree that your contributions will be licensed under the same license as the project.

## Recognition

Contributors will be recognized in the project. Thank you for helping improve Foto2VAM!
