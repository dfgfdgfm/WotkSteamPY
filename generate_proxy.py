from bs4 import BeautifulSoup
import requests


def generate_proxy_dict(quantity, last_proxy=None):
    url = f'https://free-proxy-list.net/'
    content = requests.get(url)

    proxy_list = []

    if content.status_code == 200:
        soup = BeautifulSoup(content.text, "html.parser")
        t_body = soup.find('tbody')
        all_proxies = t_body.find_all('tr')

        items_count = 0

        for item in all_proxies:

            td_elements = item.find_all('td')

            ip_address = td_elements[0].text
            port = td_elements[1].text

            proxy = f"http://{ip_address}:{port}"
            if proxy != last_proxy:
                proxy_list.append(f"http://{ip_address}:{port}")

            if items_count >= quantity:
                break

            items_count += 1

    return proxy_list


def get_random_proxy(last_proxy):
    return generate_proxy_dict(1, last_proxy)[0]
