import os
import scrapy
import json
import urllib.request
from threading import Thread
from urllib.error import URLError


class Downloader(Thread):
    def __init__(self, url):
        super().__init__()
        self.url = url

    def run(self):
        try:
            print("Thread started ...")
            urllib.request.urlretrieve(self.url, "img/" + self.url.split('/')[-1])
            print("Thread finished!")
        except URLError as e:
            print(e)
            f = open("error.txt", "a+")
            f.write(self.url)
            f.write("\n")
            f.close()


class SubCategory(scrapy.Spider):
    name = 'product-details-v2'
    start_urls = set()

    if os.path.isfile("v2/sub-category-v2.json"):
        with open('v2/sub-category-v2.json') as json_file:
            data = json.load(json_file)
            for p in data:
                start_urls.add(p['product-url'])

    def parse(self, response):
        page = response.xpath("//div[contains(@class,'content-area')]")
        details = page.xpath("//div[contains(@class,'entry-summary')]")
        image = page.xpath(
            "//div[contains(@class,'summary-before')]/div[contains(@class,'product-images')]//div/div/div")

        image_arr = image.xpath("./img/@src").getall()
        yield {
            'product-url': response.url,
            'title': details.xpath("./h1/text()").get(),
            'price': details.xpath("//p[contains(@class,'price')]/span/text()").get(),
            'description': page.xpath(
                "//div[contains(@class,'product-summary-wrap')]/div/div[contains(@class,'entry-summary')]//div[contains(@class,'description')]/p/text()").getall(),
            'categories': details.xpath(
                "./div[contains(@class,'product_meta')]/span[contains(@class,'posted_in')]/a/text()").getall(),
            'image_url': image_arr,
        }

        for src in image_arr:
            if not os.path.isfile("img/" + src.split('/')[-1]):
                Downloader(src).start()
