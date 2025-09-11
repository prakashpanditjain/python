import threading
import time
from concurrent.futures import ThreadPoolExecutor

import requests


def download_page(url_string: str):
    response = requests.get(url_string)

    file_path = f"page_{url_string.split('//')[1].replace('/', '_')}.html"
    thread_name = threading.current_thread().name
    print(f"[{time.strftime('%X')}] {thread_name} started downloading {url_string}")

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(response.text)
    print(f"completed content of {url_string} to {file_path} ")
    return url_string, len(response.text)


list_of_url = [
    'https://www.python.org',
    'https://www.github.com',
    # "https://www.openai.com",com
    "https://www.stackoverflow.com",
    "https://www.wikipedia.com",
    "https://www.x.com"
]

start_time = time.time()

with ThreadPoolExecutor(max_workers=5) as executor:
    result = executor.map(download_page, list_of_url)

for url, length in result:
    print(f"{url} -> size {length}")

end_time = time.time()

print(f"Time taken by ThreadPoolExecutor = {end_time - start_time:.2f}")
