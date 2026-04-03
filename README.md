# 🚀 Task 4: Real-Time Object Detection System
### **Apexcify Technologys - AI & Data Science Internship**

## 📌 Project Overview
This project is a high-performance **Object Detection System** developed using the **YOLOv8 (You Only Look Once)** architecture. It can identify and locate multiple objects in real-time from images or video feeds with high accuracy.

## 🛠️ Tech Stack
* **Language:** Python
* **Model:** YOLOv8 (Ultralytics)
* **Libraries:** OpenCV, PyTorch, NumPy
* **Framework:** Computer Vision

## 🎯 Key Features
* **Real-time Detection:** High-speed processing for live video streams.
* **Multiple Object Tracking:** Can detect 80+ different classes (People, Cars, Chairs, etc.) simultaneously.
* **Accuracy:** Uses the pre-trained `yolov8n.pt` (Nano) model for an optimal balance between speed and precision.

## 📂 Project Structure
* `app.py`: The main script to run the detection system.
* `yolov8n.pt`: The pre-trained YOLOv8 weights.
* `README.md`: Project documentation.

## 🚀 How to Run
1. **Install Dependencies:**
   ```bash
   pip install ultralytics opencv-python
