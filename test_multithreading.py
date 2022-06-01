import requests
from timer import timer
from urls import urls
from threading import Thread


def getJson(url, filename):
    print("Getting html from:", url)
    response = requests.get(url)
    html = response.text

    print("Writing html to file:", filename)
    with open(filename, "w+") as f:
        f.write(html)


def getAll():
    threads = []
    for i, url in enumerate(urls):
        thread = Thread(target=getJson, args=(url, f"{i+1}.html"))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()


@timer
def main():
    getAll()


if __name__ == '__main__':
    main()
