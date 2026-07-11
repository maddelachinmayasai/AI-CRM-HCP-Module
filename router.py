import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY"),
    temperature=0
)


def choose_tool(message: str):

    prompt = f"""
You are an AI Router.

Choose ONLY ONE tool from:

log
edit
search
followup
summary

User Message:
{message}

Return ONLY the tool name.
"""

    response = llm.invoke(prompt)

    return response.content.strip().lower()