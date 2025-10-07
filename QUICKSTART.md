# Quick Start Guide

This guide will help you get started with Foto2VAM quickly.

## Prerequisites

- Python 3.10 or newer
- (Optional) CUDA-capable GPU for training
- (Optional) Docker for containerized deployment

## Installation Methods

### Method 1: Standard Python Installation (Recommended)

1. **Clone the repository:**
   ```bash
   git clone https://github.com/SeryogaMiller/foto2vam.git
   cd foto2vam
   ```

2. **Create a virtual environment (recommended):**
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On Linux/macOS
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Verify installation:**
   ```bash
   python foto2vam.py --help
   ```

### Method 2: Docker Installation

1. **Build the Docker image:**
   ```bash
   docker build -t foto2vam .
   ```

2. **Run with Docker:**
   ```bash
   docker run -v $(pwd)/Input:/app/Input -v $(pwd)/Output:/app/Output foto2vam
   ```

### Method 3: Docker Compose (Easiest)

1. **Start the service:**
   ```bash
   docker-compose up
   ```

## Basic Usage

### Step 1: Prepare Input Images

Create an `Input` directory and add your photos:

```bash
mkdir -p Input
# Copy your photos to Input/
```

Supported formats: JPG, PNG

**Tips for best results:**
- Use clear, well-lit photos
- Ensure the face is visible and not obscured
- Front-facing photos work best
- Higher resolution images generally produce better results

### Step 2: Run Foto2VAM

```bash
python foto2vam.py --inputPath Input --outputPath Output
```

This will:
1. Process images from the `Input` directory
2. Generate face encodings
3. Create VAM character JSON files in the `Output` directory
4. Create merged JSON files in `Output_Merged` directory

### Step 3: Use the Output

The generated JSON files in `Output_Merged/` can be imported directly into VAM:

1. Open VAM (Virt-A-Mate)
2. Load a person atom
3. Navigate to the appearance preset tab
4. Load the generated JSON file

## Advanced Usage

### Using Custom Models

If you have trained models, specify them:

```bash
python foto2vam.py \
  --inputPath Input \
  --modelPath path/to/your/model.model \
  --outputPath Output
```

### Using Custom Base JSON

To merge with a custom base character:

```bash
python foto2vam.py \
  --inputPath Input \
  --defaultJson path/to/base_character.json \
  --outputPath Output
```

### Processing with Multiple Models

Use wildcards to process with multiple models:

```bash
python foto2vam.py \
  --inputPath Input \
  --modelPath "models/*.model" \
  --outputPath Output
```

## Training Your Own Model

### Quick Training Workflow

1. **Prepare training data:**
   ```bash
   python Tools/CreateTrainingVariations.py \
     --inputJsonPath Sample \
     --baseJsonPath Sample/body.json \
     --outputPath training_data \
     --numFaces 1000
   ```

2. **Generate training images:**
   ```bash
   python Tools/CreateTrainingImages.py \
     --inputPath training_data \
     --outputPath training_images
   ```

3. **Create face encodings:**
   ```bash
   python Tools/CreateTrainingEncodings.py \
     --inputPath training_images \
     --filter "*.png,*.jpg"
   ```

4. **Generate training CSV:**
   ```bash
   python Tools/CreateTrainingCsv.py \
     --inputPath training_images \
     --configFile models/config.json \
     --outputName training.csv
   ```

5. **Train the model:**
   ```bash
   python Tools/Train.py \
     --trainingCsv training_images/training.csv \
     --validationCsv validation_data/validation.csv \
     --outputFile models/my_model.model
   ```

See the main README for detailed training instructions.

## Troubleshooting

### Common Issues

**Issue: "No face detected"**
- Ensure your image has a clear, visible face
- Try a different photo with better lighting
- Make sure the face is not heavily obscured

**Issue: "Module not found" errors**
- Ensure all dependencies are installed: `pip install -r requirements.txt`
- Activate your virtual environment if using one
- Try upgrading pip: `pip install --upgrade pip`

**Issue: Out of memory errors**
- Process fewer images at once
- Use a machine with more RAM
- For training, reduce batch size or use a GPU with more VRAM

**Issue: Poor quality results**
- Use higher quality input images
- Try training with more varied training data
- Experiment with different models
- Ensure input photos are similar to training data

### Getting Help

1. Check the [README](README.md) for detailed documentation
2. Review [existing issues](https://github.com/SeryogaMiller/foto2vam/issues)
3. Open a new issue with details about your problem

## Next Steps

- Read the full [README](README.md) for comprehensive documentation
- Check [CONTRIBUTING.md](CONTRIBUTING.md) to contribute
- Explore the `Tools/` directory for advanced features
- Experiment with training your own models

## Tips for Success

1. **Start simple:** Begin with the default models and settings
2. **Quality input:** Use high-quality, well-lit photos
3. **Experiment:** Try different photos and settings
4. **Train custom models:** For specific use cases, train your own models
5. **Review output:** Always check the generated JSON in VAM before using

Happy generating! 🎭
