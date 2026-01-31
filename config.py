import os
from pathlib import Path
from dotenv import load_dotenv

# Calcule le chemin du dossier où se trouve ce fichier config.py
base_dir = Path(__file__).resolve().parent
env_path = base_dir / ".env"

# Charge le .env en spécifiant le chemin exact
load_dotenv(dotenv_path=env_path)

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    # Ce print t'aidera à déboguer dans ta console
    print(f"DEBUG: Tentative de lecture du fichier : {env_path}")
    raise RuntimeError("❌ GEMINI_API_KEY non définie")