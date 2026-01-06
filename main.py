from scraper.zendesk import get_articles

domain = "support.optisigns.com"
per_page = 60
articles = get_articles(domain = domain, per_page = per_page)
print(articles[0])
