import scrapy
from scrapy.spidermiddlewares.httperror import HttpError
from twisted.internet.error import DNSLookupError
from twisted.internet.error import TimeoutError, TCPTimedOutError


class Category(scrapy.Spider):
    name = 'category'
    start_urls = [
        "https://www.fixit.com.bd/product-category/tools-hardware/",
        "https://www.fixit.com.bd/product-category/kitchen/",
        "https://www.fixit.com.bd/product-category/cleaning/",
        "https://www.fixit.com.bd/product-category/electrical/",
        "https://www.fixit.com.bd/product-category/lawn-garden/",
        "https://www.fixit.com.bd/product-category/paint/",
        "https://www.fixit.com.bd/shop/"
    ]

    def start_requests(self):
        for u in self.start_urls:
            yield scrapy.Request(u, callback=self.parse, errback=self.err_back, dont_filter=True)

    def parse(self, response):
        # f = open("paint.html", "w")
        # f.write(response.body.decode("utf-8"))
        # f.close()
        for product in response.xpath("//div[contains(@class,'container')]//aside[@id='woocommerce_product_categories-2']/ul[contains(@class,'product-categories')]/li"):
            # //div[@id='main']//ul[contains(@class,'product-categories')]/li
            url = response.url
            yield {
                'title': url.replace("https://www.fixit.com.bd/product-category/", ""),
                'url': product.xpath("./a/@href").get(),
            }

        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)

    def err_back(self, failure):
        # log all failures
        self.logger.error(repr(failure))

        # in case you want to do something special for some errors,
        # you may need the failure's type:

        if failure.check(HttpError):
            # these exceptions come from HttpError spider middleware
            # you can get the non-200 response
            response = failure.value.response
            self.logger.error('HttpError on %s', response.url)

        elif failure.check(DNSLookupError):
            # this is the original request
            request = failure.request
            self.logger.error('DNSLookupError on %s', request.url)

        elif failure.check(TimeoutError, TCPTimedOutError):
            request = failure.request
            self.logger.error('TimeoutError on %s', request.url)
