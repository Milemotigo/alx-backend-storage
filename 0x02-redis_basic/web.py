import requests
import redis
import time

def get_page(url: str) -> str:
    """ Initialize a Redis connection
    """
    redis_client = redis.Redis()

    count_key = f"count:{url}"
    count = redis_client.get(count_key)

    if count is None:
        redis_client.setex(count_key, 10, 1)
    else:
        redis_client.incr(count_key)

    response = requests.get(url)
    if response.status_code == 200:
        html_content = response.text
    else:
        html_content = f"Failed to fetch content from {url}"

    return html_content

if __name__ == "__main__":
    url = "http://slowwly.robertomurray.co.uk/delay/5000/url/http://example.com"
    html_content = get_page(url)
    print(html_content)
