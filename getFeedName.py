import os
from urllib.parse import urlparse

from dotenv import load_dotenv

def extract_feed_name(url):
    parsed_url = urlparse(url)
    return parsed_url.netloc.replace("www.", "")


if __name__ == '__main__':
    load_dotenv()
    url = os.getenv('harry_url')
    feedname = extract_feed_name(url)
    print(feedname)
