import multiprocessing as mp
import requests
from timer import timer
from urls import urls


def getJson(url, filename):
    print("Getting html from:", url)
    response = requests.get(url)
    html = response.text

    print("Writing html to file:", filename)
    with open(filename, "w+") as f:
        f.write(html)


def getAll():
    pool = mp.Pool()
    jobs = []
    for i, url in enumerate(urls):
        jobs.append(pool.apply_async(getJson, (url, f"{i+1}.html")))

    return [job.get() for job in jobs]


@timer
def main():
    return getAll()


if __name__ == '__main__':
    main()
