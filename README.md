# Watson Emotion Detection System

A lightweight Python application and API service that leverages IBM Watson's Natural Language Processing (NLP) capabilities to analyze text and predict human emotions. The system evaluates text across five core emotions (**anger, disgust, fear, joy, and sadness**) and dynamically computes the dominant emotion.

## 🚀 Features
*   **Watson NLP Integration:** Leverages the robust Watson Runtime API to perform accurate emotion analysis.
*   **Robust Input Validation:** Automatically detects blank inputs, whitespaces, or invalid non-string data before hitting the network.
*   **Fail-Safe Error Handling:** Captures `500` server errors, network drops (`RequestException`), or altered JSON responses, falling back gracefully to `None` values instead of crashing.
*   **Clean API Status Codes:** Employs explicit HTTP status codes (`200 OK` for success, `400 Bad Request` for invalid/blank text entries).

---

## 🛠️ Project Structure

```text
final_project/
│
├── EmotionDetection/
│   ├── __init__.py           # Package initializer
│   └── emotion_detection.py  # Core detection logic & Watson API connector
│
├── server.py                 # Flask server deployment script
└── README.md                 # Project documentation
```

---

## ⚙️ Core Functions & Logic

### 1. The Emotion Detector Function
Located in `EmotionDetection/emotion_detection.py`, the `emotion_detector(text_to_analyze)` function formats data payload, handles system exceptions, and structures the response interface.

**Sample Output Structure (Success - 200):**
```json
{
    "anger": 0.01,
    "disgust": 0.02,
    "fear": 0.005,
    "joy": 0.85,
    "sadness": 0.115,
    "dominant_emotion": "joy"
}
```

**Sample Output Structure (Blank Input / Error - 400 or 500):**
```json
{
    "anger": null,
    "disgust": null,
    "fear": null,
    "joy": null,
    "sadness": null,
    "dominant_emotion": null
}
```

---

## 💻 Installation & Setup

### Prerequisites
*   Python 3.8 or higher
*   `requests` library

### Dependencies Installation
Install the necessary network request tools locally or inside your virtual environment:
```bash
pip install requests flask
```

### Quick Python Usage Example
You can test the module independently in a Python terminal:
```python
from EmotionDetection.emotion_detection import emotion_detector

# Test with a valid statement
result = emotion_detector("I love this new technology.")
print(result)
# Output: {'anger': ..., 'joy': ..., 'dominant_emotion': 'joy'}

# Test with a blank entry
blank_result = emotion_detector("   ")
print(blank_result)
# Output: {'anger': None, 'disgust': None, ..., 'dominant_emotion': None}
```

---

## 🌐 Web Server Integration (Flask API)

The system is designed to seamlessly integrate with web application platforms. A standard `server.py` implementation intercepts web requests via URL parameters and routes appropriate browser responses:

*   **Endpoint:** `/emotionDetector`
*   **Method:** `GET` or `POST`
*   **Parameter:** `textToAnalyze`

### Client Validation Workflow
When the server application maps the result, it parses the dictionary structure to verify the data health before serving the front-end interface:
```python
if response_dict['anger'] is None:
    return jsonify({"message": "Invalid text! Please try again!"}), 400
```

---

## 🛡️ Exception & Edge Case Handling
1.  **Blank Entries Check:** Evaluates `isinstance(text, str) and not text.strip()` to ensure system sanity.
2.  **Server Fault (500 Error):** Intercepts internal platform downs or malformed server behaviors and overrides script exits.
3.  **JSON Structural Variance:** Wraps collection accessors inside dynamic `.get()` blocks, insulating the code against potential API modifications.
