# AI Story Generator using LangChain + Groq

An AI-powered storytelling application built using LangChain, Groq LLMs, and Streamlit. The application dynamically generates creative stories based on user-provided characters, settings, and genres.

---

## Live Application

👉 https://storyy-generator.streamlit.app/

# Project Overview

This project demonstrates how Large Language Models (LLMs) can be integrated into Python applications using LangChain orchestration.

Users can:

* Enter a main character
* Enter a supporting character
* Choose a setting
* Select a genre
* Generate a complete AI-written story instantly

The application uses:

* LangChain for prompt orchestration
* Groq for ultra-fast LLM inference
* Streamlit for the interactive UI

---

# Features

* AI-generated creative stories
* Dynamic prompt generation
* Interactive Streamlit interface
* LangChain prompt chaining
* Groq LLM integration
* Environment variable security using `.env`
* Beginner-friendly architecture
* Lightweight and fast deployment

---

# Tech Stack

| Technology | Purpose                         |
| ---------- | ------------------------------- |
| Python     | Core programming language       |
| LangChain  | LLM orchestration framework     |
| Groq       | Free and fast LLM inference     |
| Streamlit  | Interactive web application     |
| dotenv     | Environment variable management |

---

# Project Structure


Story_Generator_Langchain/
│
├── app.py
├── story_generator.py
├── requirements.txt
├── .gitignore
├── README.md
└── .env

---

# How LangChain is Used

This project uses LangChain to create a pipeline for AI story generation.

## LangChain Workflow


User Input
   ↓
PromptTemplate
   ↓
Groq LLM
   ↓
Output Parser
   ↓
Generated Story


## Components Used

### 1. PromptTemplate

LangChain dynamically injects user inputs into a structured prompt.

Example:

```python
prompt = PromptTemplate(
    input_variables=[
        "main_character",
        "supporting_character",
        "setting",
        "genre"
    ],
    template="""
    Create an engaging {genre} story.

    Main Character:
    {main_character}

    Supporting Character:
    {supporting_character}

    Setting:
    {setting}

    Story:
    """
)
```

---

### 2. ChatGroq

LangChain connects to Groq-hosted LLMs using:

```python
llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0.8
)
```

---

### 3. Runnable Chain

LangChain combines the prompt, LLM, and parser into a single pipeline:

```python
chain = prompt | llm | parser
```

This is the core LangChain orchestration mechanism.

---

# Installation

## 1. Clone the Repository

```bash
git clone https://github.com/yourusername/story-generator-langchain.git
```

---

## 2. Navigate to Project Folder

```bash
cd story-generator-langchain
```

---

## 3. Create Virtual Environment

### Mac/Linux

```bash
python3 -m venv .venv
```

### Windows

```bash
python -m venv .venv
```

---

## 4. Activate Virtual Environment

### Mac/Linux

```bash
source .venv/bin/activate
```

### Windows

```bash
.venv\Scripts\activate
```

---

## 5. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Setup Groq API Key

## 1. Create Free Groq Account

Visit:

[https://console.groq.com](https://console.groq.com)

---

## 2. Generate API Key

Navigate to:

* API Keys
* Create API Key

---

## 3. Create `.env` File

Inside the project root folder:

```env
GROQ_API_KEY=your_api_key_here
```

---

# Running the Application

Run the Streamlit app:

```bash
streamlit run app.py
```

The application will open automatically in your browser.

---

# Example Input

| Field                | Example        |
| -------------------- | -------------- |
| Main Character       | Shreya         |
| Supporting Character | Soumya         |
| Setting              | Ancient Forest |
| Genre                | Adventure      |

---

# Example Output

```text
Deep within the ancient forest, Shreya and Soumya discovered a hidden pathway...
```

---

# Deployment on Streamlit Cloud

## 1. Push Project to GitHub

Ensure the following files are included:

* `app.py`
* `story_generator.py`
* `requirements.txt`
* `README.md`

Do NOT upload:

* `.env`
* `.venv`

---

## 2. Open Streamlit Cloud

Visit:

[https://share.streamlit.io](https://share.streamlit.io)

---

## 3. Connect GitHub Repository

* Login with GitHub
* Select repository
* Choose branch
* Select `app.py`

---

## 4. Add Secrets

Inside Streamlit Cloud:

* Open App Settings
* Go to Secrets

Add:

```toml
GROQ_API_KEY="your_api_key_here"
```

---

## 5. Deploy

Click:

```text
Deploy
```

Your app will be live in a few minutes.

---

# Requirements

```txt
streamlit
langchain
langchain-core
langchain-groq
python-dotenv
```

---

# Future Enhancements

Possible upgrades for the project:

* Multi-chapter stories
* AI image generation
* Story continuation
* Story memory
* Character generation
* Story summarization
* Multi-agent architecture
* Voice narration
* Story export to PDF
* RAG-based storytelling

---

# Learning Outcomes

This project demonstrates:

* LangChain fundamentals
* Prompt engineering
* LLM orchestration
* Streamlit deployment
* Environment variable handling
* AI application architecture
* API integration

---

# Author

Shreya Ranjan

---

