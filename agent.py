import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY"),
    temperature=0
)


def extract_interaction(user_message: str):

    prompt = f"""
You are an AI assistant for a Healthcare CRM.

The user may either:

1. Log a NEW interaction.
2. Update an EXISTING interaction.

If the user only wants to change one field,
return ONLY that field.

Examples:

User:
Change sentiment to negative

Return:
{{
  "sentiment": "negative"
}}

User:
The doctor's name is Dr. Myth

Return:
{{
  "hcpName": "Dr. Myth"
}}

User:
Today I met Dr. Smith and discussed CardioX. I shared brochures.

Return:
{{
  "hcpName":"Dr. Smith",
  "date":"Today",
  "product":"CardioX",
  "sentiment":"positive",
  "brochure":true,
  "followup":false,
  "summary":"Discussed CardioX with Dr. Smith"
}}

Return ONLY valid JSON.
Do not use markdown.
Do not explain anything.

User Message:
{user_message}
"""

    response = llm.invoke(prompt)

    return response.content