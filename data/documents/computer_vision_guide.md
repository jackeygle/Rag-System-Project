# Computer Vision Guide

## What is Computer Vision?

Computer Vision is a field of AI that enables computers to interpret and understand visual information from the world, including images and videos.

## Image Basics

### Digital Images

- **Pixels**: Smallest unit of an image
- **Resolution**: Width × Height in pixels
- **Color Channels**: RGB (3 channels), Grayscale (1 channel)
- **Bit Depth**: 8-bit (0-255), 16-bit, 32-bit

### Color Spaces

- **RGB**: Red, Green, Blue
- **HSV**: Hue, Saturation, Value
- **LAB**: Lightness, A (green-red), B (blue-yellow)
- **YCbCr**: Luminance and chrominance

## Classical Computer Vision

### Image Filtering

- **Blur**: Gaussian, Box, Median
- **Sharpen**: Unsharp masking
- **Edge Detection**: Sobel, Canny

### Feature Detection

1. **SIFT**: Scale-Invariant Feature Transform
2. **SURF**: Speeded-Up Robust Features
3. **ORB**: Oriented FAST and Rotated BRIEF
4. **Harris Corner Detection**

### Image Transformations

- Rotation, Scaling, Translation
- Affine Transformation
- Perspective Transformation

## Deep Learning for Vision

### Image Classification

Assign single label to entire image:
- AlexNet, VGG, ResNet, EfficientNet
- ImageNet benchmark (1000 classes)

### Object Detection

Locate and classify multiple objects:

**Two-Stage Detectors:**
- R-CNN, Fast R-CNN, Faster R-CNN
- Region proposals + classification

**One-Stage Detectors:**
- YOLO (You Only Look Once) - v1 to v8
- SSD (Single Shot Detector)
- RetinaNet (Focal Loss)

**Transformer-based:**
- DETR: Detection Transformer
- DINO, Grounding DINO

### Semantic Segmentation

Classify every pixel:
- FCN (Fully Convolutional Network)
- U-Net (encoder-decoder)
- DeepLab (atrous convolution)
- SegFormer (Transformer-based)

### Instance Segmentation

Separate instances of same class:
- Mask R-CNN
- YOLACT
- SOLOv2

### Panoptic Segmentation

Combines semantic + instance segmentation

### Pose Estimation

Detect human body keypoints:
- OpenPose
- HRNet
- MediaPipe

### Face Recognition

- **Face Detection**: Find faces in image
- **Face Alignment**: Normalize face position
- **Face Embedding**: Convert to vector
- **Face Matching**: Compare embeddings

Models: FaceNet, ArcFace, DeepFace

### Image Generation

**GANs:**
- StyleGAN: High-quality faces
- BigGAN: Class-conditional generation
- CycleGAN: Style transfer

**Diffusion Models:**
- DALL-E: Text-to-image
- Stable Diffusion: Open-source
- Midjourney: Creative generation
- Imagen: Google's model

### Vision Transformers (ViT)

Applying transformers to images:
- Split image into patches
- Treat patches as tokens
- Self-attention across patches

Variants:
- DeiT: Data-efficient ViT
- Swin Transformer: Hierarchical with windows
- BEiT: BERT-style pretraining

### Vision-Language Models

Combine vision and language:
- **CLIP**: Contrastive Language-Image Pre-training
- **BLIP**: Bootstrapping Language-Image Pre-training
- **LLaVA**: Large Language and Vision Assistant
- **GPT-4V**: Multimodal GPT

## Video Understanding

### Video Classification

Classify entire video:
- 3D CNNs (C3D, I3D)
- Two-Stream Networks
- SlowFast Networks
- Video Transformers (TimeSformer, ViViT)

### Action Recognition

Identify human actions:
- Temporal modeling
- Skeleton-based methods

### Object Tracking

Follow objects across frames:
- SORT, DeepSORT
- ByteTrack
- Transformer trackers

### Video Segmentation

Segment objects across time:
- Propagation-based methods
- SAM (Segment Anything) + video

## 3D Vision

### Depth Estimation

- **Monocular**: Single image
- **Stereo**: Two cameras
- **Structured Light**: Project patterns

### 3D Reconstruction

- Multi-View Stereo (MVS)
- NeRF: Neural Radiance Fields
- 3D Gaussian Splatting

### Point Cloud Processing

- PointNet, PointNet++
- 3D object detection
- LiDAR processing

## Applications

- **Autonomous Driving**: Detection, segmentation, depth
- **Medical Imaging**: Diagnosis, analysis
- **Retail**: Checkout-free stores, inventory
- **Security**: Surveillance, face recognition
- **AR/VR**: Scene understanding, tracking
- **Agriculture**: Crop monitoring, disease detection
- **Manufacturing**: Quality inspection

## Tools and Libraries

- **OpenCV**: Classic CV library
- **PIL/Pillow**: Image processing
- **torchvision**: PyTorch vision
- **Albumentations**: Data augmentation
- **Detectron2**: Facebook's detection library
- **MMDetection**: OpenMMLab detection
- **Ultralytics**: YOLO implementation
