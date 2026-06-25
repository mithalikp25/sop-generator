import re
import os
from dotenv import load_dotenv
from groq import Groq
from prompts import SYSTEM_PROMPT

load_dotenv()

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
MODEL = "llama-3.1-8b-instant"


def clean_response(text):
    text = re.sub(r'<think>.*?</think>', '', text, flags=re.DOTALL)
    text = re.sub(r'<think>.*', '', text, flags=re.DOTALL)
    return text.strip()


def call_llm(messages, temperature=0.7):
    response = client.chat.completions.create(
        model=MODEL,
        messages=messages,
        temperature=temperature,
        max_tokens=4096
    )
    return clean_response(response.choices[0].message.content)


def get_initial_messages(business_process):
    return [
        {"role": "system", "content": SYSTEM_PROMPT},
        {
            "role": "user",
            "content": f"I want to create an SOP for the following business process:\n\n{business_process}\n\nPlease begin the clarification interview. Ask your first question only."
        }
    ]


def get_next_question(messages):
    return call_llm(messages, temperature=0.7)


def generate_sop(messages):
    messages.append({
        "role": "user",
        "content": "Thank you for the clarifications. Now generate the complete SOP document following all 8 sections and formatting rules exactly as instructed. Do not truncate any section."
    })
    return call_llm(messages, temperature=0.3)