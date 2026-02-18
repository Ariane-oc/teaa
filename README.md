# 🧠 TeAA (Tex Analyzer API)

A simple FastAPI backend that performs emotion classification on text using a locally hosted Transformer model.
The API runs entirely on your machine — no paid APIs required.

## 🚀 Features

- Emotion detection using a pre-trained Transformer model
- Fully local inference (no external API calls)
- Automatic interactive API documentation (/docs)
- Simple REST interface
- Built with FastAPI + Hugging Face Transformers

## 🛠 Tech Stack

- Python 3.10+
- FastAPI
- Uvicorn
- Hugging Face Transformers


## 📦 Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/your-repo.git
    ```
2. Navigate to the project directory:
    ```bash
    cd your-repo
    ```
3. Install dependencies:
    ```bash
    npm install
    ```

## 📡 API Usage

Endpoint
```bash
POST /analyze
```

Request Body
```bash
{
  "text": "I feel amazing today!"
}
```

Response Example
```bash
{
  "emotion": "joy",
  "confidence": 0.9821
}
```

## 🧪 Example Using curl

You can test the API directly from your terminal:

    ```bash
    curl -X POST "http://127.0.0.1:8000/analyze" \
     -H "Content-Type: application/json" \
     -d '{"text": "I am very excited about this project!"}'
    ```
Example response:
    ```bash
    {
         "emotion": "joy",
         "confidence": 0.9913
    }
    ```