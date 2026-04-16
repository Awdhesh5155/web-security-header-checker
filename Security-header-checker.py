import urllib.request
from urllib.request import Request
from urllib.error import URLError, HTTPError

USER_AGENT = (
    'Mozilla/5.0 (Linux; Android 10) '
    'AppleWebKit/537.36 (KHTML, like Gecko) '
    'Chrome/83.0.4103.101 Mobile Safari/537.36'
)

def chrome_user_agent(url):
    try:
        opener = urllib.request.build_opener()
        opener.addheaders = [('User-Agent', USER_AGENT)]
        urllib.request.install_opener(opener)

        response = urllib.request.urlopen(url, timeout=10)

        print("\nResponse Headers")
        print("--------------------")
        for header, value in response.getheaders():
            print(f"{header}: {value}")

        request = Request(url)
        request.add_header('User-Agent', USER_AGENT)

        #for header, value in request.header_items():
           # print(f"{header}: {value}")

    except HTTPError as e:
        print(f"\nHTTP Error: {e.code} - {e.reason}")

    except URLError as e:
        print(f"\nURL Error: {e.reason}")

    except Exception as e:
        print(f"\nUnexpected Error: {e}")

if __name__ == '__main__':
    url = input("Enter the URL (with https:// or http://): ").strip()

    if not url.startswith(("http://", "https://")):
        print("Invalid URL. Please include http:// or https://")
    else:
        chrome_user_agent(url)
