from scraper.zendesk import get_articles
from scraper.markdown import save_article
domain = "support.optisigns.com"
per_page = 50
articles = get_articles(domain = domain, per_page = per_page)

for a in articles:
    save_article(a)

