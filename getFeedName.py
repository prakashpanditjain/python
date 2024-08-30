import os
from urllib.parse import ParseResult
from urllib.parse import ParseResultBytes
from urllib.parse import urlparse

from dotenv import load_dotenv

def extract_feed_name(url: str) -> str:
    """

    :type url: object
    :return: This functions return feed name
    """
    parsed_url: ParseResult | ParseResultBytes = urlparse(url)
    return parsed_url.netloc.replace("www.", "")


if __name__ == '__main__':
    load_dotenv()
    url: str | None = os.getenv('harry_url')
    feed_name: str = extract_feed_name(url)
    print(feed_name)
