from typing import TypedDict
from langgraph.graph import StateGraph

from app.router import choose_tool
from app.tools import (
    log_interaction,
    edit_interaction,
    search_hcp,
    generate_followup,
    summarize_interaction,
)


class GraphState(TypedDict):
    message: str
    tool: str
    result: str


def router(state):

    tool = choose_tool(state["message"])

    print("===================================")
    print("AI Selected Tool:", tool)
    print("===================================")

    if tool == "log":
        return {
            "tool": "log",
            "result": log_interaction(state["message"])
        }

    elif tool == "edit":
        return {
            "tool": "edit",
            "result": edit_interaction(state["message"])
        }

    elif tool == "search":
        return {
            "tool": "search",
            "result": search_hcp(state["message"])
        }

    elif tool == "followup":
        return {
            "tool": "followup",
            "result": generate_followup(state["message"])
        }

    elif tool == "summary":
        return {
            "tool": "summary",
            "result": summarize_interaction(state["message"])
        }

    return {
        "tool": "unknown",
        "result": "Unknown Tool"
    }


builder = StateGraph(GraphState)

builder.add_node("router", router)

builder.set_entry_point("router")

builder.set_finish_point("router")

graph = builder.compile()