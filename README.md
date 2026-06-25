# 📋 SOP Generator for Business Workflows

An AI-powered Standard Operating Procedure (SOP) generator built with **Groq + Llama 3**, **LangChain-style multi-step chaining**, and **Streamlit**. Describe any business process in 2-3 sentences, answer 5 clarifying questions, and get a fully structured, downloadable SOP document instantly.

---

## 🚀 Live Demo

👉 [Launch the app](https://mithalikp25-sop-generator-app.streamlit.app)

---

## 🧠 What It Does

1. User describes a business process in 2-3 sentences
2. The system conducts a **5-question guided interview** — each question uncovers a different aspect: stakeholders, tools/systems, timelines, exceptions, and compliance
3. The LLM uses the full conversation context to generate a **structured 8-section SOP**
4. User downloads the SOP as a **formatted Word document (.docx)**

### Generated SOP Sections
1. Title and Purpose
2. Scope
3. Roles and Responsibilities
4. Prerequisites / Required Tools
5. Step-by-Step Procedure
6. Decision Points
7. Exception Handling
8. Review and Approval

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| LLM | Llama 3.1 8B via Groq API |
| Backend | Python, Multi-step LLM Chain |
| Frontend | Streamlit |
| Export | python-docx |
| Hosting | Streamlit Community Cloud |

---

## 📁 Project Structure

```
sop-generator/
├── app.py              # Streamlit UI and session state management
├── chain.py            # LLM chain logic (interview + SOP generation)
├── prompts.py          # System prompt for the LLM
├── requirements.txt    # Python dependencies
├── .env.example        # Environment variable template
├── .gitignore          # Excludes secrets and venv
└── sample_sops/        # 5 sample SOPs generated during testing
    ├── sop_01_employee_onboarding.md
    ├── sop_02_customer_complaint.md
    ├── sop_03_invoice_processing.md
    ├── sop_04_product_return_refund.md
    └── sop_05_vendor_onboarding.md
```

---

## ⚙️ Run Locally

### 1. Clone the repo
```bash
git clone https://github.com/mithalikp25/sop-generator.git
cd sop-generator
```

### 2. Create virtual environment
```bash
python -m venv venv
venv\Scripts\activate       # Windows
source venv/bin/activate    # Mac/Linux
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Set up environment variables
```bash
cp .env.example .env
```
Edit `.env` and add your Groq API key:
```
GROQ_API_KEY=your_groq_api_key_here
```
Get a free key at [console.groq.com](https://console.groq.com)

### 5. Run the app
```bash
streamlit run app.py
```

---

## 🧪 Sample SOPs Generated

This project was tested on 5 real business processes:

| # | Business Process |
|---|-----------------|
| 1 | Employee Onboarding |
| 2 | Customer Complaint Handling |
| 3 | Invoice Processing |
| 4 | Product Return and Refund |
| 5 | Vendor Onboarding |

All 5 generated SOPs are available in the `sample_sops/` folder.

---

## 💡 Key Concepts

**Multi-step LLM Chain** — Instead of a single prompt, this project uses a chain where each LLM response depends on previous ones. The conversation history is manually maintained and passed to the API on every call, giving the model full context to ask relevant follow-up questions and generate a highly specific SOP.

**Session State** — Streamlit reruns the entire script on every interaction. `st.session_state` persists the conversation history, current question number, and generated SOP across reruns.

---

## 📄 License

MIT License — free to use and modify.

---

## 👤 Author

**Mithalik** — [github.com/mithalikp25](https://github.com/mithalikp25)
