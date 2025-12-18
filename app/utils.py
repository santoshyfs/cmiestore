from bs4 import BeautifulSoup


def strip_html(html: str | None) -> str | None:
    if not html:
        return None
    return BeautifulSoup(html, "html.parser").get_text(strip=True)
