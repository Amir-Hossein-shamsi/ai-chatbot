# 🤖✨ Ai ChatBot

> **An ultra‑stylish, lightning‑fast AI chat experience powered by Groq & LangChain**

---

<br/>

## 🚀 Features

| Feature                   | Description                                  |
| :------------------------ | :------------------------------------------- |
| **⚡ Low‑Latency**         | Real‑time token streaming with Groq LLMs     |
| **💾 Persistent History** | SQLite‑backed chat logs per user session     |
| **🎨 Custom Themes**      | Dark‑mode sidebar & CSS‑styled chat bubbles  |
| **🛠️ Configurable**      | Swap models & tweak creativity (temperature) |
| **🔄 Session Control**    | Start fresh or reload past convos by ID      |
| **📊 Metrics**            | Track usage & performance (coming soon)      |

<br/>

---

## 🎬 Live Demo

<p align="center">
  <img src="docs/demo_screenshot.png" alt="Demo Screenshot" width="600" style="border-radius:12px; box-shadow:0 4px 20px rgba(0,0,0,0.4)"/>
</p>

<br/>

---

## 🛠️ Tech Stack

<div style="display:flex; gap:2rem; flex-wrap:wrap;">
  <div>
    <h4>Frontend</h4>
    - Streamlit<br/>
    - Custom CSS
  </div>
  <div>
    <h4>LLM & Orchestration</h4>
    - LangChain<br/>
    - ChatGroq (Groq LLM API)
  </div>
  <div>
    <h4>Persistence</h4>
    - SQLAlchemy<br/>
    - SQLite (or any SQL‑DB)
  </div>
</div>

<br/>

---

## ⚡ Quick Start

```bash
# 1. Clone repo
git clone https://github.com/Amir-Hossein-shamsi/ai-chatbot.git
cd ai-chat-companion

# 2. Setup venv & install
python -m venv .venv
source .venv/bin/activate  # macOS/Linux
.venv\Scripts\activate    # Windows
pip install -r requirements.txt

# 3. Add API ke
```
