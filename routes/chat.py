from flask import Blueprint, request, jsonify
from services.gemini_service import ask_gemini

chat_bp = Blueprint("chat", __name__)

# Charge le prompt système
with open("prompts/system_prompt.txt", "r", encoding="utf-8") as f:
    SYSTEM_PROMPT = f.read()

@chat_bp.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_message = data.get("message", "")
    
    reply = ask_gemini(SYSTEM_PROMPT, user_message)
    
    return jsonify({"reply": reply})