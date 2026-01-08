import os
import json
import hashlib

STATE_FILE = "tracker/state.json"

def load_state(): 
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

def save_state(state):
    with open(STATE_FILE, "w", encoding="utf-8") as f:
        json.dump(state, f)

def reset_state():
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE, "w", encoding="utf-8") as f:
            json.dump({}, f)
    print("State has been reset due to OpenAI API Key or vector store change.")

def get_stored_vector_store_id():
    state = load_state()
    return state.get("_meta", {}).get("vector_store_id")

def save_vector_store_id(vector_store_id):
    state = load_state()
    state.setdefault("_meta", {})["vector_store_id"] = vector_store_id
    save_state(state)

def hash_article(article):
    content_str = f"{article['title']}{article['body']}"
    return hashlib.sha256(content_str.encode("utf-8")).hexdigest()

def get_article_status(article_id, current_hash, state):
    if (str(article_id) not in state):
        return 'NEW', None
    
    stored_data = state[str(article_id)]
    last_hash = stored_data.get('hash')
    last_file_id = stored_data.get('file_id')
    
    if (current_hash != last_hash):
        return 'UPDATED', last_file_id
    
    return 'SKIPPED', last_file_id



