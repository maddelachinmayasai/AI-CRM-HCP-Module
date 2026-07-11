from app.database import engine
from app.models import Base
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from app.graph import graph
import json

app = FastAPI(
    title="AI CRM HCP API",
    version="1.0.0"
)
Base.metadata.create_all(bind=engine)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://localhost:5174",
        "http://localhost:5175",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class ChatRequest(BaseModel):
    message: str


@app.get("/")
def home():
    return {
        "message": "AI CRM Backend Running Successfully"
    }


@app.post("/chat")
def chat(data: ChatRequest):

    result = graph.invoke(
        {
            "message": data.message
        }
    )

    tool = result["tool"]

    ai_response = result["result"]

    # LOG and EDIT return JSON from the AI
    if tool in ["log", "edit"]:

        ai_response = ai_response.replace("```json", "")
        ai_response = ai_response.replace("```", "")
        ai_response = ai_response.strip()

        response = json.loads(ai_response)

        response["tool"] = tool

        return response

    # SEARCH / FOLLOWUP / SUMMARY return plain text
    return {
        "tool": tool,
        "message": ai_response
    }