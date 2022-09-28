import os
import scrapy
import json
import urllib.request
from threading import Thread
from urllib.error import URLError

from lxml import html
import logging


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


class ProductDetails(scrapy.Spider):
    name = 'product-details-v3'
    start_urls = set()

    if os.path.isfile("v2/sub-category-v2.json"):
        with open('v2/sub-category-v2.json') as json_file:
            data = json.load(json_file)
            for p in data:
                start_urls.add(p['product-url'])

    def parse(self, response):
        page = response.xpath("//div[contains(@class,'content-area')]")
        details = page.xpath("//div[contains(@class,'entry-summary')]")
        image = page.xpath( "//div[contains(@class,'summary-before')]/div[contains(@class,'product-images')]//div/div/div")

        image_arr = image.xpath("./img/@src").getall()
        images = set()
        for url in image_arr:
            images.add(url.split('/')[-1])

        regular_price = ''
        if details.xpath("//p[contains(@class,'price')]/span/text()").get():
            regular_price = details.xpath("//p[contains(@class,'price')]/span/text()").get()
        elif details.xpath("//p[contains(@class,'price')]/ins/span/text()").get():
            regular_price = details.xpath("//p[contains(@class,'price')]/ins/span/text()").get()

        yield {
            'SL NO': '',
            'Type': 'simple',
            'SKU': '',
            'Name': details.xpath("./h1/text()").get(),
            'Published': 1,
            'Is featured?': 0,
            'Visibility in catalog': 'visible',
            'Short Description': page.xpath("//div[contains(@class,'product-summary-wrap')]/div/div[contains(@class,'entry-summary')]//div[contains(@class,'description')]/p/text()").getall(),
            'Description': page.xpath('//div[contains(@class,"content-area")]//*[@id="tab-description"]/p/text()').getall(),
            'In stock?': 1,
            'Sold individually?': 0,
            'Allow customer reviews?': 1,
            'Purchase note': 'Thanks for purchasing',
            'Sale price': details.xpath("//p[contains(@class,'price')]/del/span/text()").get(),
            'Regular price': regular_price,
            'Categories': details.xpath("./div[contains(@class,'product_meta')]/span[contains(@class,'posted_in')]/a/text()").getall(),
            'Tags': '',
            'Shipping class': 'Dhaka Only',
            'Images': ','.join(map(str, images)),
            'Position': 0,
            'Attribute 1 name': '',
            'Attribute 1 value(s)': '',
            'Attribute 1 visible': 1,
            'Attribute 1 global': 1,
            'attributes': page.xpath('//*[@id="tab-description"]/table/tbody/tr/td/text()').getall(),
            'Meta: _specifications_display_attributes': 'yes',
            'Meta: _per_product_admin_commission_type': 'percentage',
            'product-url': response.url,
            'image_url': image_arr,
        }

        # attributes_tr = page.xpath('//*[@id="tab-description"]/table/tbody/tr')
        # attributes_td = attributes_tr.xpath('./td/text()').getall()
        # attributes_len = len(attributes_td)
        # for i in range(attributes_len):
        #     if i > 0:
        #         mod = i % 2
        #         if mod > 0:
        #             attribute_name = 'Attribute ' + str(i) + ' name'
        #             attribute_values = 'Attribute ' + str(i) + ' value(s)'
        #             attribute_visible = 'Attribute ' + str(i) + ' visible'
        #             attribute_global = 'Attribute ' + str(i) + ' global'
        #
        #             yield {
        #                 attribute_name: attributes_td[i],
        #                 attribute_values: attributes_td[i+1],
        #                 attribute_visible: 1,
        #                 attribute_global: 1,
        #             }

        # attributes_list = []

        attributes = page.xpath('//*[@id="tab-description"]/table/tbody/tr').getall()
        idx = 0
        if attributes:
            for att in attributes:
                doc = html.fromstring(att)
                attribute_arr = doc.xpath('./td/text()')
                if len(attribute_arr) == 2:
                    idx = idx + 1
                    attribute_name = 'Attribute ' + str(idx) + ' name'
                    attribute_values = 'Attribute ' + str(idx) + ' value(s)'
                    attribute_visible = 'Attribute ' + str(idx) + ' visible'
                    attribute_global = 'Attribute ' + str(idx) + ' global'

                    yield {
                        attribute_name: attribute_arr[0],
                        attribute_values: attribute_arr[1],
                        attribute_visible: 1,
                        attribute_global: 1,
                    }

        # for src in image_arr:
        #     if not os.path.isfile("img/" + src.split('/')[-1]):
        #         Downloader(src).start()
