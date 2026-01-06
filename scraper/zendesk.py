import requests

def get_articles(domain, page = 1, per_page = 30, sort_by = 'updated_at', sort_order = 'desc'):
    url = f"https://{domain}/api/v2/help_center/articles.json?page={page}&per_page={per_page}&sort_by={sort_by}&sort_order={sort_order}"
    articles = []

    response = requests.get(url).json()
    articles.extend(response['articles'])
    
    return articles