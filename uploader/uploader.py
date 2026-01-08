import os
import requests
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
VECTOR_STORE_ID = "vs_695fa458cb908191912883659abbb343"


HEADERS = {
    "Authorization": f"Bearer {OPENAI_API_KEY}",
}
FILES_UPLOAD_API = "https://api.openai.com/v1/files"
VECTOR_ATTACH_API = f"https://api.openai.com/v1/vector_stores/{VECTOR_STORE_ID}/files"

def upload_file(file_path: Path):
    with open(file_path, "rb") as f:
        response = requests.post(
            FILES_UPLOAD_API,
            headers=HEADERS,
            files={"file": f},
            data={"purpose": "assistants"}
        )
    response.raise_for_status()
    return response.json()["id"]

def attach_file_to_vector_store(file_id: str):
    response = requests.post(
        VECTOR_ATTACH_API,
        headers={**HEADERS, "Content-Type": "application/json"},
        json={"file_id": file_id}
    )
    response.raise_for_status()
    return response.json()

def upload_all_articles():
    articles_dir = Path("articles")
    uploaded = 0

    for md_file in articles_dir.glob("*.md"):
        file_id = upload_file(md_file)
        attach_file_to_vector_store(file_id)
        uploaded += 1
        print(f"Uploaded: {md_file.name}")

    print(f"Total uploaded: {uploaded}")
