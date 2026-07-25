# Axio

> **A Local-First AI Automation Platform powered by Neural Networks and Ollama LLMs**

![Python](https://img.shields.io/badge/Python-3.11+-blue?logo=python)
![License](https://img.shields.io/badge/License-MIT-green)
![Windows](https://img.shields.io/badge/Windows-Supported-0078D6?logo=windows)
![Linux](https://img.shields.io/badge/Linux-Supported-FCC624?logo=linux&logoColor=black)
![macOS](https://img.shields.io/badge/macOS-Supported-000000?logo=apple)
![AI](https://img.shields.io/badge/AI-Ollama-orange)
![Status](https://img.shields.io/badge/Status-Offline-red)
---

## 📖 Overview

**Axio** is an advanced **local-first AI automation platform** that combines custom neural network architectures with locally hosted **Ollama Large Language Models (LLMs)** to create an intelligent assistant capable of understanding natural language and executing real-world automation tasks.

Unlike conventional AI chatbots that are limited to conversation, Axio connects conversational intelligence with practical automation. It can understand user intent, maintain contextual memory, interact with desktop applications, automate browsers, process visual information through computer vision, and communicate with IoT devices.

Designed with a **modular architecture**, Axio enables developers to extend functionality by adding independent modules without modifying the core framework, making it suitable for both productivity and AI research.

---

# ✨ Key Features

## 🧠 Local AI Intelligence

- Fully local-first architecture
- Powered by Ollama LLMs
- Privacy-focused processing
- Offline-capable workflows
- Context-aware conversations
- No dependency on cloud AI APIs

---

## 🤖 Intelligent Automation

Automate repetitive workflows across multiple environments.

Supported capabilities include:

- Desktop application control
- Browser automation
- File management
- Email automation
- Task scheduling
- Process management
- Web scraping
- Data collection
- Script execution
- Custom automation pipelines

---

## 💬 Conversational AI

Interact naturally using human language.

Features include:

- Intent recognition
- Context-aware conversations
- Dynamic response generation
- Multi-step reasoning
- Personalized interactions
- Conversation memory

---

## 👁️ Computer Vision

Computer vision modules enable Axio to understand visual information.

Capabilities include:

- Object detection
- Image processing
- Camera integration
- Visual recognition
- OCR-ready architecture
- Real-time tracking (planned)

---

## 🧠 Contextual Memory

Axio stores structured contextual information to improve future interactions.

Examples include:

- User preferences
- Conversation history
- Frequently executed tasks
- Automation workflows
- System states

---

## 🌐 IoT Integration

Extend automation beyond the desktop.

Potential applications include:

- Smart lighting
- Home automation
- Device monitoring
- Sensor integration
- Custom hardware interfaces

---

## 🔌 Modular & Extensible

Every subsystem is separated into independent modules.

Developers can easily add:

- New automation modules
- AI models
- APIs
- Plugins
- Hardware integrations
- Experimental algorithms

---

# 🏗️ System Architecture

```text
                    User
                      │
            Natural Language Input
                      │
               Ollama Language Model
                      │
         Intent & Response Processing
                      │
          Decision Making / Neural Core
                      │
           Context & Memory Management
                      │
            Automation Dispatch Engine
                      │
 ┌────────────┬────────────┬────────────┬─────────────┐
 │ Desktop    │ Browser    │ Vision     │ IoT Devices │
 │ Automation │ Automation │ Processing │             │
 └────────────┴────────────┴────────────┴─────────────┘
```

The Ollama LLM handles language understanding and response generation, while Axio's internal neural architecture manages reasoning, memory, intent recognition, and automation execution.

---

# 📂 Project Structure

```text
Axio/
│
├── main.py
│   Main application entry point.
│
├── sparc.py
│   Core orchestration engine.
│
├── Nervous_sys/
│   AI reasoning framework.
│   │
│   ├── Brain/
│   │   Core decision-making logic.
│   │
│   ├── Neural_Network/
│   │   Neural network models.
│   │
│   ├── Language_Processing/
│   │   NLP processing modules.
│   │
│   ├── Memory/
│   │   Context storage and retrieval.
│   │
│   ├── Training/
│   │   Model training utilities.
│   │
│   └── Decision Logic/
│
├── Computer_Vision/
│   Object detection, image processing and camera modules.
│
├── Function/
│   Automation modules.
│   │
│   ├── Desktop Automation
│   ├── Browser Automation
│   ├── Email Automation
│   ├── Scheduling
│   ├── Media Generation
│   ├── Utilities
│   └── AI Tools
│
├── DataBase/
│   Local resources.
│   │
│   ├── intents.json
│   ├── Configuration
│   ├── AI Models
│   └── Training Data
│
├── Assets/
│   Images, icons and static resources.
│
├── Models/
│   Machine learning model files.
│
├── requirements.txt
│   Project dependencies.
│
└── README.md
```

---

<p align="center">
  <img src="assets/projectandarchitecture.png" alt="Axio Architecture" width="900">
</p>

# ⚙️ Technology Stack

### Programming

- Python

### Artificial Intelligence

- Ollama
- PyTorch
- TensorFlow
- Custom Neural Networks

### Computer Vision

- OpenCV
- MediaPipe
- YOLO (Ultralytics)
- DeepSORT

### Automation

- Selenium
- PyAutoGUI
- AutoPy

### Speech Processing

- SpeechRecognition
- pyttsx3

### Machine Learning

- NumPy
- Matplotlib

### Data

- SQLite
- JSON

---

# 📦 Requirements

Install the required Python packages:

```bash
pip install -r requirements.txt
```

### requirements.txt

```txt
# Core AI & Machine Learning
torch
torchvision
tensorflow
numpy

# Large Language Model Integration
langchain-core
langchain-ollama

# Computer Vision
opencv-python
mediapipe
ultralytics
deep-sort-realtime
Pillow

# Image Generation
diffusers

# Automation
pyautogui
autopy
selenium

# Speech
SpeechRecognition
pyttsx3

# NLP
nltk

# Networking
requests

# YouTube
pytube

# Visualization
matplotlib

# TensorFlow Logging
absl-py
```

---

# 🚀 Installation

Clone the repository.

```bash
git clone https://github.com/JeeshanHavi/Axio-Model.git
```

Navigate into the project.

```bash
cd Axio
```

Install dependencies.

For Windows 
```bash
pip install -r requirements-windows.txt
```
For MacOS
```bash
pip install -r requirements-macos.txt
```
For Linux
```bash
pip install -r requirements-linux.txt
```

Install an Ollama model.

```bash
ollama pull llama3
```

Run Axio.

```bash
python main.py
```

---

# 🎯 Applications

### Personal Productivity

- Automate repetitive workflows
- Manage schedules
- Organize files
- Generate reports

### Intelligent Desktop Assistant

- Launch applications
- Execute workflows
- Monitor processes
- Control the operating system

### Smart Home

- IoT automation
- Device monitoring
- Sensor integration

### Computer Vision

- Object detection
- Visual automation
- Image analysis

### AI Research

- Local LLM experimentation
- Autonomous agents
- AI-assisted automation
- Neural architecture research

---

# 🛣️ Roadmap

Future development includes:

- Multi-Agent AI
- Plugin Marketplace
- Voice Assistant Improvements
- Long-Term Memory
- Retrieval-Augmented Generation (RAG)
- Linux & macOS Support
- REST API
- Docker Deployment
- Mobile Companion Application
- Distributed Automation Nodes

---

# 🤝 Contributing

Contributions are welcome!

You can contribute by:

- Reporting bugs
- Suggesting new features
- Improving documentation
- Optimizing performance
- Creating automation modules
- Submitting pull requests

---

# 📄 License

MIT License

Copyright (c) 2026 Jeeshan Havi

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.

---

## ⭐ Support the Project

If you find **Axio** useful, consider giving the repository a **⭐ Star**.

Your support helps improve the project and motivates future development.
