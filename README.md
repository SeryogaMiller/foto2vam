# Foto2VAM

Generate VAM (Virt-A-Mate) character models from photographs using machine learning.

## Overview

Foto2VAM is a Python-based tool that uses facial recognition and machine learning to generate VAM character models from photos. The project analyzes facial features from input images and translates them into VAM-compatible character morphs.

## Features

- Facial recognition and encoding from photos
- Machine learning-based character generation
- Training data generation and model training
- Support for multiple camera angles
- JSON-based configuration system

## Quick Start

**New to Foto2VAM?** Check out the [Quick Start Guide](QUICKSTART.md) for step-by-step instructions!

## Requirements

- Python 3.10 or newer
- CUDA-capable GPU (recommended for training)
- Windows/Linux/macOS

## Installation

### Standard Installation

1. Clone the repository:
```bash
git clone https://github.com/SeryogaMiller/foto2vam.git
cd foto2vam
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

For training:
```bash
pip install -r requirements-train.txt
```

### Docker Installation

1. Build the Docker image:
```bash
docker build -t foto2vam .
```

2. Run the container:
```bash
docker run -v $(pwd)/Input:/app/Input -v $(pwd)/Output:/app/Output foto2vam
```

**Note:** If you encounter SSL certificate errors during Docker build in corporate/restricted network environments, you may need to configure your Docker daemon to use your organization's certificate authorities or use the standard Python installation method instead.

## Usage

### Basic Usage

Generate VAM characters from images:

```bash
python foto2vam.py --inputPath Input --outputPath Output
```

### Advanced Options

```bash
python foto2vam.py \
  --inputPath Input \
  --modelPath models/*.model \
  --defaultJson mergeBase.json \
  --outputPath Output \
  --mergedOutputPath Output_Merged
```

### Training Your Own Model

1. **Create Training Variations:**
```bash
python Tools/CreateTrainingVariations.py \
  --inputJsonPath <path_to_json_files> \
  --baseJsonPath <base_json_with_animatable_morphs> \
  --outputPath training_output \
  --numFaces 10000
```

2. **Create Training Images:**
```bash
python Tools/CreateTrainingImages.py \
  --inputPath <training_variations_path> \
  --outputPath <images_output_path>
```

3. **Create Training Encodings:**
```bash
python Tools/CreateTrainingEncodings.py \
  --inputPath <images_path> \
  --filter "*.png,*.jpg" \
  --normalizeSize 150
```

4. **Create Training CSV:**
```bash
python Tools/CreateTrainingCsv.py \
  --inputPath <encodings_path> \
  --configFile config.json \
  --outputName training.csv
```

5. **Train the Model:**
```bash
python Tools/Train.py \
  --trainingCsv training.csv \
  --validationCsv validation.csv \
  --outputFile model.model
```

6. **Make Predictions:**
```bash
python Tools/MakePrediction.py \
  --modelFile model.model \
  --inputDir <encodings_path> \
  --outputDir <output_path>
```

## VAM Assembly Modification (dnSpy)

To enable communication between Foto2VAM and VAM, you need to modify the VAM assembly using dnSpy:

### Prerequisites
- Download [dnSpy](https://github.com/dnSpy/dnSpy/releases)
- Locate your VAM installation (typically `VaM.exe` or the Assembly-CSharp.dll)

### Steps

1. **Open VAM Assembly in dnSpy:**
   - Launch dnSpy
   - File → Open → Navigate to VAM installation folder
   - Open `Assembly-CSharp.dll`

2. **Inject Foto2VamServer:**
   - Locate the `Utils/VamMod/VamMod.cs` file in this repository
   - In dnSpy, find an appropriate entry point (e.g., main game initialization class)
   - Right-click → Edit Class
   - Add code to instantiate `Foto2VamServer` on startup:
   ```csharp
   var foto2vamServer = new VamMod.Foto2VamServer();
   ```

3. **Compile and Save:**
   - File → Save Module
   - Test the modified assembly with VAM

4. **Configure Named Pipes:**
   - Ensure the pipe name in `VamMod.cs` matches your Foto2VAM configuration
   - Default pipe name: `foto2vam_pipe`

### VamMod Features

The VamMod enables:
- Screenshot capture from VAM at specified angles
- Automated character pose adjustment
- Direct communication with Foto2VAM via named pipes
- Batch processing support

## Project Structure

```
foto2vam/
├── foto2vam.py          # Main entry point
├── requirements.txt      # Python dependencies
├── requirements-train.txt # Training dependencies
├── Dockerfile           # Docker configuration
├── Utils/
│   ├── Face/           # Face processing utilities
│   ├── Training/       # Training configuration
│   └── VamMod/         # VAM modification code (C#)
├── Tools/              # Training and processing tools
│   ├── CreateTrainingVariations.py
│   ├── CreateTrainingImages.py
│   ├── CreateTrainingEncodings.py
│   ├── CreateTrainingCsv.py
│   ├── Train.py
│   ├── MakePrediction.py
│   └── MergeJson.py
└── Sample/             # Sample configuration files
```

## Configuration Files

### Base JSON Files
- `mergeBase.json`: Base character look to merge with predictions
- `Sample/body.json`: Base body configuration
- `Sample/minimum.json`: Minimum morph values
- `Sample/maximum.json`: Maximum morph values

### Model Configuration
Model configuration files (`.json`) accompany each model file (`.model`) and define:
- Input parameters (facial encodings, landmarks)
- Output parameters (VAM morphs)
- Camera angles for training
- Base face configuration

Example configuration structure:
```json
{
  "config_version": 1,
  "baseJson": "path/to/base.json",
  "minJson": "path/to/minimum.json",
  "maxJson": "path/to/maximum.json",
  "inputs": [
    {
      "name": "encoding",
      "params": [{"name": "angle", "value": "0"}]
    }
  ],
  "outputs": [
    {
      "name": "json",
      "params": []
    }
  ]
}
```

## Input/Output Examples

### Input
Place images in the `Input/` directory:
```
Input/
├── person1.jpg
├── person2.png
└── person3.jpg
```

Supported formats: JPG, PNG

### Output
Generated VAM character files in `Output/` and `Output_Merged/`:
```
Output/
├── person1.json
├── person2.json
└── person3.json

Output_Merged/
├── person1_merged.json
├── person2_merged.json
└── person3_merged.json
```

The merged output files can be directly imported into VAM.

## Troubleshooting

### Common Issues

1. **"Can't parse center" Error:**
   - This has been fixed in the latest version
   - Ensure you're using the updated code with proper type conversions

2. **No Face Detected:**
   - Ensure input images are clear and well-lit
   - Face should be clearly visible and not heavily obscured
   - Try images with faces looking directly at the camera

3. **CUDA/GPU Issues:**
   - For training, ensure CUDA is properly installed
   - Use `tensorflow` instead of `tensorflow-gpu` for CPU-only systems
   - Check GPU memory availability

4. **Import Errors:**
   - Verify all dependencies are installed: `pip install -r requirements.txt`
   - For Windows users, ensure Visual C++ redistributables are installed for dlib

5. **Model Loading Errors:**
   - Ensure model file and corresponding JSON configuration exist
   - Check that paths in configuration files are correct
   - Verify model version compatibility

## Performance Tips

- Use GPU acceleration for training (NVIDIA GPU with CUDA support)
- Batch process images when possible
- Adjust `numJitters` parameter for speed vs. accuracy tradeoff
- Use lower resolution images for faster processing during testing

## Contributing

Contributions are welcome! Please feel free to submit issues and pull requests.

### Development Setup

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run tests (if available)
5. Submit a pull request

## License

See LICENSE file for details.

## Credits

- Face recognition powered by [dlib](http://dlib.net/) and [face_recognition](https://github.com/ageitgey/face_recognition)
- Machine learning with TensorFlow and Keras
- Designed for [Virt-A-Mate](https://www.virtamate.com/)

## Support

For issues and questions:
- Open an issue on GitHub
- Check existing issues for solutions
- Review the troubleshooting section above

## Changelog

### Latest Updates (2024)
- Fixed "Can't parse center" type conversion error
- Updated dependencies for Python 3.10+ compatibility
- Added Docker support
- Improved documentation with setup instructions
- Added comprehensive README

### Original Release (2018)
- Initial implementation
- Basic training pipeline
- VAM integration support
