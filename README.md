<p align="center">
  <img src="https://img.shields.io/badge/AI-Chat%20Companion-blue?style=for-the-badge&logo=streamlit" alt="AI Chat Companion" />
  &nbsp;
  <img src="https://img.shields.io/badge/License-MIT-green.svg" alt="License: MIT" />
  &nbsp;
  <img src="https://img.shields.io/badge/Python-3.10%2B-yellow" alt="Python 3.10+" />
</p>

# 🤖 AI Chat Companion

> A sleek, Streamlit-based AI assistant with ultra-low latency Groq models, persistent SQL conversation history, and fully customizable UI.

---

## ✨ Highlights

* **⚡ Lightning Fast:** Powered by Groq’s LLMs for sub-second response times.
* **💾 Persistent History:** Conversations stored in SQLite; reload sessions by User ID.
* **🎨 Customizable:** Modify CSS, swap LLMs, adjust temperature for precise control.
* **🔄 Streamed Output:** Token-by-token display for real-time AI thinking.
* **🔒 Secure:** API key managed via environment variables.

---

## 📸 Live Demo

<p align="center">
  <img src="docs/demo_screenshot.png" alt="Demo Screenshot" width="600" />
</p>

---

## 🛠️ Tech Stack

| Component         | Technology                                                  |
| ----------------- | ----------------------------------------------------------- |
| Frontend & Layout | Streamlit                                                   |
| Orchestration     | LangChain                                                   |
| LLM Provider      | Groq (via `langchain_groq`)                                 |
| History Storage   | SQLite (SQLAlchemy + `SQLChatMessageHistory`)               |
| Styling           | Custom CSS                                                  |
| Prompt Templates  | `SystemMessagePromptTemplate`, `HumanMessagePromptTemplate` |
| Output Parsing    | `StrOutputParser`                                           |

---

## 🚀 Quickstart

### 1. Clone & Setup

```bash
git clone https://github.com/Amir-Hossein-shamsi/ai-chatbot.git
cd ai-chatbot
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows
pip install -r requirements.txt
```

### 2. Configure

Create a `.env` in project root:

```dotenv
API_KEY=your_groq_api_key_here
```

### 3. Run

```bash
streamlit run app.py
```

Open your browser at `http://localhost:8501`.

---

## 🎛️ Usage Guide

1. **Sidebar Controls**

   * **User ID:** Enter any identifier; persists session history.
   * **New Conversation:** 🧹 Clear and restart.
   * **Model Config:** Select LLM & adjust temperature slider.

2. **Chat Interface**

   * Type in the input box.
   * Watch the AI reply in styled bubbles (green for you, dark for AI).

3. **History**

   * All messages saved in `chat_history-custom.db`.
   * Reopen with the same User ID to resume.

---

## 🗂️ Project Layout

```
├── app.py                    # Streamlit application entrypoint
├── requirements.txt          # Dependencies
├── chat_history-custom.db    # SQLite database (auto-created)
├── README.md                 # Project documentation
└── docs/
    └── demo_screenshot.png   # Demo image
```

---

## 🎨 Customization Tips

* **CSS**: Edit the `<style>` block in `app.py` to tweak chat bubble colors, fonts, and layout.
* **Models**: Add options in `st.selectbox` for more Groq or other LLMs.
* **Storage**: Replace SQLite with PostgreSQL/MySQL by changing the SQLAlchemy URL.

---

## 🤝 Contributing

1. Fork the repo
2. Create a branch: `git checkout -b feature/YourFeature`
3. Commit: `git commit -m "Add feature"`
4. Push: `git push origin feature/YourFeature`
5. Open a PR

Please run `flake8` before submitting.

---

## 📜 License

This project is licensed under the **MIT** License. See [LICENSE](LICENSE) for details.

---

## 🙏 Acknowledgements

* **Groq** for blazing-fast LLM inference.
* **LangChain** for composable AI pipelines.
* **Streamlit** community for inspiration and examples.

---

<p align="center">Made with ❤️ by AmirHossein</p>
