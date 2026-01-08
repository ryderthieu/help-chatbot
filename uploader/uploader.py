import os
import requests
from pathlib import Path
from dotenv import load_dotenv
from tracker.tracker import (get_stored_vector_store_id, save_vector_store_id, reset_state)

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

HEADERS = {
    "Authorization": f"Bearer {OPENAI_API_KEY}",
}
FILES_UPLOAD_API = "https://api.openai.com/v1/files"
VECTOR_STORE_API = "https://api.openai.com/v1/vector_stores"

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

def attach_file_to_vector_store(file_id: str, vector_store_id: str):
    url = f"{VECTOR_STORE_API}/{vector_store_id}/files"
    response = requests.post(
        url,
        headers={**HEADERS, "Content-Type": "application/json"},
        json={"file_id": file_id}
    )
    response.raise_for_status()
    return response.json()

def delete_file(file_id: str, vector_store_id: str):
    url = f"{VECTOR_STORE_API}/{vector_store_id}/files/{file_id}"
    response = requests.delete(url, headers=HEADERS)
    response.raise_for_status()
    return response.json()


def check_vector_store_exists(vector_store_id):
    if not vector_store_id:
        return False
    url = f"{VECTOR_STORE_API}/{vector_store_id}"
    try:
        response = requests.get(url, headers=HEADERS)
        return response.status_code == 200
    except:
        return False
    
def get_or_create_vector_store():
    stored_id = get_stored_vector_store_id()
    if stored_id:
        if check_vector_store_exists(stored_id):
            return stored_id
        else:
            reset_state()
    
    url = VECTOR_STORE_API
    data = {"name": "support-articles"}
    response = requests.post(url, headers=HEADERS, json=data)
    response.raise_for_status()

    new_id = response.json()["id"]
    save_vector_store_id(new_id)

    return new_id


