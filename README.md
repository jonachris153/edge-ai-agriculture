# Edge-AI Smart Agriculture System

This repository contains a **research-oriented, re-implemented prototype**
of an AI-driven decision support system for sustainable agriculture.

The project focuses on **edge intelligence, embedded sensing, and system-level
design**, rather than full-scale commercial deployment.

## Project Objective

To assist farmers in early detection of crop diseases and pests by combining
image-based AI inference with environmental sensing, enabling
**low-latency, energy-efficient, and scalable decision support** at the edge.

## System Overview

The system integrates three major layers:

- **Edge AI Layer**
  - Image preprocessing and inference pipeline
  - Disease / pest classification logic

- **Embedded Sensing Layer**
  - Environmental data acquisition using ESP32
  - Temperature and humidity sensing

- **Decision & Advisory Layer**
  - Fusion of AI inference with sensor data
  - Generation of preventive and corrective recommendations

The design follows an **edge-first approach** to minimize latency and
reduce dependency on continuous internet connectivity.

## Architecture Flow

1. Crop image is captured or uploaded
2. Image is preprocessed for inference
3. AI inference determines crop health status
4. Environmental sensor data is acquired
5. Decision logic combines AI + sensor inputs
6. Advisory output is generated

## Hardware Components

- ESP32 Microcontroller
- Environmental Sensors (Temperature / Humidity)
- Camera or image input device (mobile / edge)

## Software Stack

- **Programming Language:** Python, Embedded C/C++
- **Embedded Platform:** ESP32
- **AI Framework:** TensorFlow (conceptual, placeholder inference)
- **Computer Vision:** OpenCV concepts
- **System Design:** Edge-oriented architecture

## Repository Structure
edge-ai-agriculture/
├── docs/ # System architecture diagrams
├── edge_inference/ # AI inference & preprocessing pipeline
├── firmware/ # ESP32 sensor acquisition firmware
└── README.md

## Project Status

✔ Core system architecture designed  
✔ Edge inference pipeline implemented (demonstration)  
✔ Embedded sensing firmware implemented  
🔄 Model optimization and cloud integration planned

## Note on Implementation

The original system was developed as part of a hackathon deployment.
This repository contains a **clean re-implementation** created to
demonstrate system architecture, edge inference logic, and embedded
design principles for research and academic review.

## Research Relevance

This project demonstrates concepts relevant to:

- Edge AI and TinyML
- Embedded sensing systems
- Sustainable agriculture technologies
- Low-latency decision support systems





