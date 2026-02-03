# Edge-AI Smart Agriculture System

This repository contains a **re-implemented research prototype**
of an AI-driven decision support system for sustainable agriculture.

The project focuses on **edge intelligence, system design, and low-latency
decision making**, rather than full-scale product deployment.

## System Overview
- Image-based crop disease and pest analysis
- Environmental sensing (temperature, humidity)
- Edge-oriented inference pipeline
- Decision logic for preventive and corrective actions

## Architecture
The system follows an edge-first design:
1. Farmer captures or uploads crop image
2. Image preprocessing and inference
3. Environmental data fusion
4. Decision and advisory generation

## Repository Structure
edge-ai-smart-agriculture/
├── edge_inference/ # Image preprocessing & inference logic
├── firmware/ # ESP32-based sensor data acquisition
└── README.md

## Tools & Technologies
- Python (AI inference pipeline)
- ESP32 (embedded sensing)
- Embedded C/C++
- Computer Vision concepts

## Note
The original implementation was developed during a hackathon.
This version is **re-implemented for research clarity and reproducibility**.


