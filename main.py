from uploader.uploader import (get_or_create_vector_store, upload_file, attach_file_to_vector_store, delete_file)
from scraper.zendesk import get_articles
from tracker.tracker import (load_state, hash_article, get_article_status, save_state)
from scraper.markdown import save_article

def main():
    vector_store_id = get_or_create_vector_store()

    DOMAIN = "support.optisigns.com"
    PER_PAGE = 50
    articles = get_articles(domain = DOMAIN, per_page = PER_PAGE)

    state = load_state()
    stats = {"ADDED": 0, "UPDATED": 0, "SKIPPED": 0}

    for article in articles:
        article_id = article["id"]

        current_hash = hash_article(article)

        status, old_file_id = get_article_status(article_id, current_hash, state)

        if (status == "SKIPPED"):
            stats["SKIPPED"] += 1
            continue

        if (status == "UPDATED" and old_file_id):
            delete_file(old_file_id, vector_store_id)
        
        file_path = save_article(article)
        updated_file_id = upload_file(file_path)
        attach_file_to_vector_store(updated_file_id, vector_store_id)
        state[str(article_id)] = {
                "hash": current_hash,
                "file_id": updated_file_id
            }
        
        if (status == "UPDATED"):
            stats["UPDATED"] += 1
        elif (status == "NEW"):
            stats["ADDED"] += 1

    save_state(state)
    print(f"ADDED: {stats['ADDED']}, UPDATED: {stats['UPDATED']}, SKIPPED: {stats['SKIPPED']}")

if __name__ == "__main__":
    main()
    
    

