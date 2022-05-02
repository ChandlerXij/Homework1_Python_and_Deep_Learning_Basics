import requests
from bs4 import BeautifulSoup


def Spider(url: str = 'https://wdc.kugi.kyoto-u.ac.jp/igrf/coef/igrf13coeffs.html'):
    """
        Get url of targeted website and crawl the content
        and generate the soup of the website.
    """

    headers = \
        {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
                AppleWebKit/537.36 (KHTML, like Gecko) \
                Chrome/100.0.4896.127 Safari/537.36 Edg/100.0.1185.50',
            'Host': 'wdc.kugi.kyoto-u.ac.jp'
        }

    r = requests.get(url,
                     headers=headers)

    soup = BeautifulSoup(r.text, "html.parser")
    return soup


def download_img(url_info):
    """Example in class."""

    if url_info[1]:
        print("-----------downloading image %s" % (url_info[0]))
        try:
            url = url_info[0]
            response = requests.get(url)
            img = response.content

            # Save Path
            path = '%s' % (url_info[1])
            with open(path, 'wb') as f:
                f.write(img)
            return (True, path)
        except Exception as ex:
            print("--------Error----")
            pass
