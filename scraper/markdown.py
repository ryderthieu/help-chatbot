from bs4 import BeautifulSoup
from markdownify import markdownify as md
import re
import os

def html_to_markdown(html):
    soup = BeautifulSoup(html, "html.parser")

    for tag in soup(["nav", "ads"]):
        tag.decompose()

    return md(str(soup), heading_style="ATX")

def slugify(text):
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")

def save_article(article):
    os.makedirs("articles", exist_ok=True)

    slug = slugify(article["title"])
    content = html_to_markdown(article["body"])

    with open(f"articles/{slug}.md", "w", encoding="utf-8") as f:
        f.write(f"# {article['title']}\n\n")
        f.write(f"Article URL: {article['html_url']} \n\n")
        f.write(content)


