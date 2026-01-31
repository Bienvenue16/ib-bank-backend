from google import genai
import os

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise RuntimeError("❌ GEMINI_API_KEY non définie dans les variables d'environnement")

client = genai.Client(api_key=GEMINI_API_KEY)

def ask_gemini(system_prompt, user_message):
    prompt = f"""
{system_prompt}

Utilisateur : {user_message}
Assistant IB Bank :
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text
