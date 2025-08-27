# 🚀 FastAPI + Google Gemini API

This is a simple **FastAPI** app that connects with **Google Gemini (Generative AI API)**.  
It exposes a `/process/` endpoint where you can send text input and get AI-generated output.

---

## 📂 Project Structure

```
my_fastapi_app/
│── main.py
│── .env
│── requirements.txt
│── README.md
│── screenshots/
    │── input.png
    │── output.png
```

---

## ⚡ Features

- Accepts text input via REST API
- Sends the text directly to **Gemini API**
- Returns AI-generated output in JSON
- Easy to run locally with FastAPI & Uvicorn

---

## 🛠️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/HaswanthKurevella/LearnSemanticKernel/tree/SemanticKernel 
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Add your Gemini API Key

Create a `.env` file:

```ini
GEMINI_API_KEY=your_real_gemini_api_key_here
```

### 4. Run the server

```bash
uvicorn main:app --reload
```

The API will be available at 👉 [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## 📡 Usage

Go to the **Swagger UI** and try the `/process/` endpoint.  
Send a JSON body like:

```json
{
  "text": "Explain how AI works in a few words"
}
```

You’ll get a response like:

```json
{
  "original": "Explain how AI works in a few words",
  "gemini_output": "AI works by learning patterns from data and making predictions or decisions."
}
```

---

## 🖼️ Screenshots

### Input Example

![Input Example](screenshots/input.png)

### Output Example

![Output Example](screenshots/output.png)

---

## 📜 License

This project is licensed under the MIT License.
