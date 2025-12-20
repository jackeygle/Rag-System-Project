# Deep Learning Complete Guide

## What is Deep Learning?

Deep Learning is a subset of machine learning that uses artificial neural networks with multiple layers (hence "deep") to learn hierarchical representations of data. It has revolutionized AI by achieving state-of-the-art results in computer vision, natural language processing, and speech recognition.

## Neural Network Fundamentals

### Neurons and Activation Functions

A neuron computes: `output = activation(sum(weights * inputs) + bias)`

**Common Activation Functions:**

1. **ReLU (Rectified Linear Unit)**: f(x) = max(0, x)
   - Most popular, computationally efficient
   - Helps avoid vanishing gradient problem

2. **Sigmoid**: f(x) = 1/(1 + e^(-x))
   - Output range: (0, 1)
   - Used for binary classification

3. **Tanh**: f(x) = (e^x - e^(-x))/(e^x + e^(-x))
   - Output range: (-1, 1)
   - Zero-centered

4. **Softmax**: Used for multi-class classification
   - Converts outputs to probability distribution

### Layers Types

1. **Dense/Fully Connected**: Every neuron connects to all neurons in previous layer
2. **Convolutional**: Applies filters to detect local patterns
3. **Pooling**: Reduces spatial dimensions
4. **Dropout**: Randomly deactivates neurons for regularization
5. **Batch Normalization**: Normalizes layer inputs for stable training

## Convolutional Neural Networks (CNN)

CNNs are specialized for processing grid-like data such as images.

### Architecture Components

1. **Convolutional Layer**: Applies learnable filters
   - Extracts features like edges, textures, shapes
   - Parameters: kernel size, stride, padding

2. **Pooling Layer**: Reduces spatial dimensions
   - Max Pooling: Takes maximum value in window
   - Average Pooling: Takes average value

3. **Flatten Layer**: Converts 2D to 1D for dense layers

### Famous CNN Architectures

- **LeNet-5** (1998): First successful CNN for digit recognition
- **AlexNet** (2012): Won ImageNet, started deep learning revolution
- **VGGNet** (2014): Used small 3x3 filters, very deep
- **ResNet** (2015): Introduced skip connections, enabled very deep networks (152+ layers)
- **Inception/GoogLeNet**: Multiple filter sizes in parallel
- **EfficientNet** (2019): Optimal scaling of width, depth, and resolution

### Applications

- Image Classification
- Object Detection (YOLO, Faster R-CNN)
- Semantic Segmentation
- Face Recognition
- Medical Image Analysis

## Recurrent Neural Networks (RNN)

RNNs are designed for sequential data with memory of previous inputs.

### Basic RNN

- Maintains hidden state that captures sequence history
- Problem: Vanishing/exploding gradients for long sequences

### LSTM (Long Short-Term Memory)

Solves vanishing gradient problem with gates:
- **Forget Gate**: What to discard from memory
- **Input Gate**: What new info to store
- **Output Gate**: What to output

### GRU (Gated Recurrent Unit)

Simplified LSTM with fewer parameters:
- **Reset Gate**: How much past to forget
- **Update Gate**: How much past to keep

### Applications

- Language Modeling
- Machine Translation
- Speech Recognition
- Time Series Prediction
- Sentiment Analysis

## Transformer Architecture

Transformers replaced RNNs as the dominant architecture for NLP.

### Key Components

1. **Self-Attention Mechanism**
   - Computes attention weights between all positions
   - Allows parallel processing (unlike RNNs)
   - Query, Key, Value matrices

2. **Multi-Head Attention**
   - Multiple attention heads capture different relationships

3. **Positional Encoding**
   - Adds position information since no recurrence

4. **Feed-Forward Networks**
   - Applied independently to each position

### Famous Transformer Models

- **BERT** (2018): Bidirectional encoder, great for classification
- **GPT Series**: Generative pre-trained transformers
  - GPT-2: 1.5B parameters
  - GPT-3: 175B parameters
  - GPT-4: Multimodal, undisclosed size
- **T5**: Text-to-text framework
- **LLaMA**: Meta's efficient language models
- **Claude, Gemini**: Modern competitors to GPT

## Training Deep Networks

### Loss Functions

- **Cross-Entropy**: Classification tasks
- **MSE (Mean Squared Error)**: Regression
- **Binary Cross-Entropy**: Binary classification
- **Focal Loss**: Imbalanced classification

### Optimizers

1. **SGD (Stochastic Gradient Descent)**
   - Basic but effective with momentum

2. **Adam**: Adaptive learning rates
   - Combines momentum and RMSprop
   - Most popular optimizer

3. **AdamW**: Adam with weight decay
4. **LAMB**: For large batch training

### Learning Rate Scheduling

- Step Decay
- Cosine Annealing
- Warmup + Decay
- One Cycle Policy

### Regularization Techniques

- **Dropout**: Randomly zero out neurons
- **L1/L2 Regularization**: Penalize large weights
- **Early Stopping**: Stop when validation loss increases
- **Data Augmentation**: Artificially expand training data
- **Batch Normalization**: Stabilizes training

## Generative Models

### Variational Autoencoders (VAE)

- Encoder compresses input to latent space
- Decoder reconstructs from latent space
- Can generate new samples by sampling latent space

### Generative Adversarial Networks (GAN)

- **Generator**: Creates fake samples
- **Discriminator**: Distinguishes real from fake
- Trained adversarially

**GAN Variants:**
- DCGAN: Deep Convolutional GAN
- StyleGAN: High-quality image generation
- CycleGAN: Unpaired image-to-image translation
- Pix2Pix: Paired image translation

### Diffusion Models

- Gradually add noise, then learn to denoise
- State-of-the-art image generation
- Examples: DALL-E, Stable Diffusion, Midjourney

## Hardware and Frameworks

### Hardware

- **GPUs**: NVIDIA (CUDA), AMD (ROCm)
- **TPUs**: Google's Tensor Processing Units
- **NPUs**: Neural Processing Units in phones

### Frameworks

- **PyTorch**: Most popular for research
- **TensorFlow**: Production-ready, TensorFlow Lite for mobile
- **JAX**: Google's functional approach
- **Keras**: High-level API
