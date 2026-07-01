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