import os
import scrapy
import json
import urllib.request
from threading import Thread
from scrapy.spidermiddlewares.httperror import HttpError
from twisted.internet.error import DNSLookupError
from twisted.internet.error import TimeoutError, TCPTimedOutError

from lxml import html


class Downloader(Thread):
    def __init__(self, url):
        super().__init__()
        self.url = url

    def run(self):
        try:
            print("Thread started ...")
            urllib.request.urlretrieve(self.url, "img/" + self.url.split('/')[-1])
            print("Thread finished!")
        except:
            f = open("error.txt", "a+")
            f.write(self.url)
            f.write("\n")
            f.close()


def image_name_beautifier(image_name):
    return image_name.translate({ord(c): " " for c in "'\","})


class ProductDetails(scrapy.Spider):
    name = 'product-details'
    start_urls = set()

    if os.path.isfile("v2/sub-category-filtered-v2.json"):
        with open('v2/sub-category-filtered-v2.json') as json_file:
            data = json.load(json_file)
            for p in data:
                start_urls.add(p['product-url'])

    def start_requests(self):
        for u in self.start_urls:
            yield scrapy.Request(u, callback=self.parse, errback=self.err_back, dont_filter=True)

    def parse(self, response):
        page = response.xpath("//div[contains(@class,'content-area')]")
        details = page.xpath("//div[contains(@class,'entry-summary')]")
        image = page.xpath(
            "//div[contains(@class,'summary-before')]/div[contains(@class,'product-images')]//div/div/div")

        image_arr = image.xpath("./img/@src").getall()
        images = set()
        for url in image_arr:
            img_file = image_name_beautifier(url.strip().split('/')[-1])
            images.add(img_file)

        # regular_price = ''
        # if details.xpath("//p[contains(@class,'price')]/span/text()").get():
        #     regular_price = details.xpath("//p[contains(@class,'price')]/span/text()").get()
        # elif details.xpath("//p[contains(@class,'price')]/ins/span/text()").get():
        #     regular_price = details.xpath("//p[contains(@class,'price')]/ins/span/text()").get()

        sale_price = ''
        regular_price = ''
        if page.xpath("//p[contains(@class,'price')]/ins/span/text()").get():
            sale_price = page.xpath("//p[contains(@class,'price')]/ins/span/text()").get()
            regular_price = page.xpath("//p[contains(@class,'price')]/del/span/text()").get()
        else:
            regular_price = page.xpath("//p[contains(@class,'price')]/span/text()").get()

        product = {
            'SL NO': '',
            'Type': 'simple',
            'SKU': '',
            'Name': details.xpath("./h1/text()").get(),
            'Published': 1,
            'Is featured?': 0,
            'Visibility in catalog': 'visible',
            'Short Description': page.xpath(
                "//div[contains(@class,'product-summary-wrap')]/div/div[contains(@class,'entry-summary')]//div[contains(@class,'description')]/p/text()").getall(),
            'Description': page.xpath(
                '//div[contains(@class,"content-area")]//*[@id="tab-description"]/p/text()').getall(),
            'In stock?': 1,
            'Sold individually?': 0,
            'Allow customer reviews?': 1,
            'Purchase note': 'Thanks for purchasing',
            'Sale price': sale_price,  # details.xpath("//p[contains(@class,'price')]/del/span/text()").get()
            'Regular price': regular_price,
            'Categories': details.xpath(
                "./div[contains(@class,'product_meta')]/span[contains(@class,'posted_in')]/a/text()").getall(),
            'Tags': '',
            'Shipping class': 'Dhaka Only',
            'Images': ','.join(map(str, images)),
            'Position': 0,
            'Meta: _specifications_display_attributes': 'yes',
            'Meta: _per_product_admin_commission_type': 'percentage',
            'product-url': response.url,
            'image_url': image_arr,
        }

        for i in range(1, 25):
            attribute_name = 'Attribute ' + str(i) + ' name'
            attribute_values = 'Attribute ' + str(i) + ' value(s)'
            attribute_visible = 'Attribute ' + str(i) + ' visible'
            attribute_global = 'Attribute ' + str(i) + ' global'
            product[attribute_name] = ''
            product[attribute_values] = ''
            product[attribute_visible] = 1
            product[attribute_global] = 1

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

                    product[attribute_name] = attribute_arr[0]
                    product[attribute_values] = attribute_arr[1]
                    product[attribute_visible] = 1
                    product[attribute_global] = 1

        yield product

        # for src in image_arr:
        #     if not os.path.isfile("img/" + src.split('/')[-1]):
        #         Downloader(src).start()

    def err_back(self, failure):
        # log all failures
        self.logger.error(repr(failure))

        f = open("failed_url.txt", "a")

        if failure.check(HttpError):
            # these exceptions come from HttpError spider middleware
            # you can get the non-200 response
            response = failure.value.response
            self.logger.error('HttpError on %s', response.url)
            f.write('HttpError on ' + response.url)
            f.write("\n")

        elif failure.check(DNSLookupError):
            # this is the original request
            request = failure.request
            self.logger.error('DNSLookupError on %s', request.url)
            f.write('DNSLookupError on ' + request.url)
            f.write("\n")

        elif failure.check(TimeoutError, TCPTimedOutError):
            request = failure.request
            self.logger.error('TimeoutError on %s', request.url)
            f.write('TimeoutError on ' + request.url)
            f.write("\n")

        else:
            f.write('failure.value.response on ' + failure.value.response.url)
            f.write("\n")
            f.write('failure.request on ' + failure.request.response.url)
            f.write("\n")

        f.close()
