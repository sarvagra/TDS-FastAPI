# 📘 FastAPI Student & Sentiment Management API

This is a simple RESTful API built using **FastAPI** that lets you:

- Manage a list of students with full CRUD operations
- Analyze the sentiment of a given text using OpenAI's GPT model

---

## ✨ Features

### 🎓 Student Management

- Get student details  
- Add a new student  
- Update existing student  
- Partially update student  
- Delete a student  

### 💬 Sentiment Analysis

- **Endpoint**: `/sentiment?text=your_input_here`  
- **Function**: Classifies input text as one of:  
  - `GOOD`  
  - `BAD`  
  - `NEUTRAL`  
- **Powered by**: OpenAI GPT (gpt-4o-mini)

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- FastAPI
- Uvicorn
- httpx
- python-dotenv

### Install Dependencies

```bash
pip install fastapi uvicorn httpx python-dotenv
```