from app.agent import extract_interaction
from app.database import SessionLocal
from app.models import Interaction

from sqlalchemy import or_

import json


# -------------------------
# LOG INTERACTION
# -------------------------
def log_interaction(message):

    ai_response = extract_interaction(message)

    ai_response = ai_response.replace("```json", "")
    ai_response = ai_response.replace("```", "")
    ai_response = ai_response.strip()

    data = json.loads(ai_response)

    db = SessionLocal()

    interaction = Interaction(
        hcpName=data.get("hcpName"),
        date=data.get("date"),
        product=data.get("product"),
        sentiment=data.get("sentiment"),
        brochure=data.get("brochure"),
        followup=data.get("followup"),
        summary=data.get("summary"),
    )

    db.add(interaction)
    db.commit()
    db.close()

    return json.dumps(data)


# -------------------------
# EDIT INTERACTION
# -------------------------
def edit_interaction(message):

    ai_response = extract_interaction(message)

    ai_response = ai_response.replace("```json", "")
    ai_response = ai_response.replace("```", "")
    ai_response = ai_response.strip()

    data = json.loads(ai_response)

    db = SessionLocal()

    interaction = db.query(Interaction).order_by(Interaction.id.desc()).first()

    if interaction:

        if data.get("hcpName"):
            interaction.hcpName = data["hcpName"]

        if data.get("date"):
            interaction.date = data["date"]

        if data.get("product"):
            interaction.product = data["product"]

        if data.get("sentiment"):
            interaction.sentiment = data["sentiment"]

        if data.get("brochure") is not None:
            interaction.brochure = data["brochure"]

        if data.get("followup") is not None:
            interaction.followup = data["followup"]

        if data.get("summary"):
            interaction.summary = data["summary"]

        db.commit()

    db.close()

    return json.dumps(data)


# -------------------------
# SEARCH HCP
# -------------------------
def search_hcp(message):

    db = SessionLocal()

    interaction = db.query(Interaction).filter(
        or_(
            Interaction.hcpName.ilike(f"%{message}%"),
            Interaction.product.ilike(f"%{message}%")
        )
    ).first()

    db.close()

    if interaction:

        return f"""
HCP Name : {interaction.hcpName}

Date : {interaction.date}

Product : {interaction.product}

Sentiment : {interaction.sentiment}

Brochure : {interaction.brochure}

Follow-up : {interaction.followup}

Summary : {interaction.summary}
"""

    return "No interaction found."


# -------------------------
# FOLLOW-UP
# -------------------------
def generate_followup(message):

    return "✅ Follow-up scheduled for next week."


# -------------------------
# SUMMARY
# -------------------------
def summarize_interaction(message):

    db = SessionLocal()

    interactions = db.query(Interaction).all()

    db.close()

    if not interactions:
        return "No interactions available."

    summary = ""

    for interaction in interactions:
        summary += (
            f"{interaction.hcpName} discussed "
            f"{interaction.product}. "
        )

    return summary