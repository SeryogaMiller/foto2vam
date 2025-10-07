# Changelog

All notable changes to the Foto2VAM project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.1.0] - 2024

### Added
- **Docker Support**: Complete Docker integration with multi-stage builds
  - Standard Dockerfile for production use
  - GPU-enabled Dockerfile.train for training workloads
  - Docker Compose configuration for easy deployment
  - .dockerignore for optimized builds
- **Comprehensive Documentation**
  - Detailed README.md with full setup instructions
  - Quick Start Guide (QUICKSTART.md) for beginners
  - Contributing guidelines (CONTRIBUTING.md)
  - dnSpy integration instructions for VAM assembly modification
  - Input/output examples and troubleshooting section
- **Unit Testing Framework**
  - Test suite in `tests/` directory
  - Tests for EncodedFace class
  - Tests for Config class
  - Tests for ParamGenerator class
  - Development requirements (requirements-dev.txt)
- **CI/CD Pipeline**
  - GitHub Actions workflow for automated testing
  - Multi-version Python testing (3.10, 3.11, 3.12)
  - Docker build verification
  - Code quality checks with flake8
- **Package Configuration**
  - setup.py for pip installation
  - Proper package structure
  - Entry points for command-line usage

### Fixed
- **Critical Bug Fix**: Resolved "Can't parse center. Sequence item with index 0 has a wrong type" error
  - Fixed type conversion in `Utils/Face/encoded.py`
  - Added explicit float conversion for `img_size` values in camera matrix calculation
  - Ensures compatibility with numpy's strict type requirements

### Changed
- **Updated Dependencies**: Modernized all Python dependencies for Python 3.10+ compatibility
  - Updated to TensorFlow 2.13+ (removed deprecated tensorflow-gpu)
  - Updated Keras to 2.13+
  - Updated dlib to 19.24+
  - Updated numpy to 1.24+ with <2.0 constraint
  - Updated opencv-python to 4.8+
  - Updated face_recognition to 1.3+
  - Added version constraints for stability
  - Conditional pywin32 installation (Windows only)
- **Enhanced Error Handling**
  - Improved error messages in config.py with specific exception types
  - Better logging with parameter indices for debugging
  - More descriptive error messages throughout
- **Improved .gitignore**
  - Added Python cache directories
  - Added IDE configuration files
  - Added build and test artifacts
  - Added Docker-related files

### Improved
- **Code Quality**
  - Better error handling and logging
  - Clearer exception messages
  - More maintainable code structure
- **Developer Experience**
  - Easier setup with multiple installation methods
  - Better documentation for contributors
  - Automated testing and CI/CD
  - Development environment setup guide

### Technical Details

#### Breaking Changes
None. This release is fully backward compatible with existing workflows.

#### Deprecated
- `tensorflow-gpu` package (use `tensorflow` which auto-detects GPU)
- Custom face_recognition fork (use standard face_recognition package)

#### Security
- Updated all dependencies to address known vulnerabilities
- Removed outdated packages with security issues

## [1.0.0] - 2018

### Initial Release
- Basic facial recognition and encoding
- Machine learning-based VAM character generation
- Training pipeline for custom models
- VAM integration support
- Multiple camera angle support
- JSON-based configuration system

---

## Migration Guide

### From 1.0.0 to 1.1.0

1. **Update Python**: Ensure you're using Python 3.10 or newer
   ```bash
   python --version  # Should show 3.10 or higher
   ```

2. **Update Dependencies**:
   ```bash
   pip install -r requirements.txt --upgrade
   ```

3. **No Code Changes Required**: Your existing scripts and workflows will continue to work

4. **Optional Enhancements**:
   - Try the Docker deployment for easier setup
   - Use the new Quick Start Guide for new team members
   - Run the test suite to verify your setup: `pytest tests/`

### Known Issues
- Docker builds may fail in corporate networks with SSL certificate issues. Use standard Python installation as a workaround.
- Some legacy GPU configurations may require manual TensorFlow GPU setup

---

## Future Roadmap

Planned features for future releases:

### Version 1.2.0 (Planned)
- [ ] Web interface for easier use
- [ ] Batch processing improvements
- [ ] Pre-trained model distribution
- [ ] Enhanced image preprocessing
- [ ] Support for more VAM morph types

### Version 2.0.0 (Planned)
- [ ] Integration with modern ML models (e.g., diffusion models)
- [ ] Real-time face tracking support
- [ ] Multi-face processing
- [ ] Cloud deployment options
- [ ] REST API for integration

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on contributing to this project.

## Support

For issues and questions:
- Check [existing issues](https://github.com/SeryogaMiller/foto2vam/issues)
- Open a new issue with details
- Review the [troubleshooting section](README.md#troubleshooting) in README
