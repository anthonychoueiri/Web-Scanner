from bs4 import BeautifulSoup
import requests
import re


def extract(URL):
    try:
        page = requests.get(URL)
        soup = BeautifulSoup(page.content, "html.parser")
    except:
        print("Something went wrong")
        return

    internal = []
    referral = []

    for link in soup.findAll('a'):
        if link.get('href') is None:
            continue
        else:
            x = re.search("^/", link.get('href'))
            if x is None:
                referral.append(link.get('href'))
            else:
                internal.append(link.get('href'))

    return internal, referral


def main():
    URL = input("Please enter a URL: ")

    print("\n[*] Starting\n")

    internal, referral = extract(URL)

    print("\nINTERNAL:")
    print(internal)

    print("\nREFERRAL: ")
    print(referral)


if __name__ == "__main__":
    main()
