import scrapy


class CategoriesSpider(scrapy.Spider):
    name = "categories"
    start_urls = [
        'https://www.fixit.com.bd',
    ]

    def parse(self, response):
        for main_menu in response.xpath("//div[contains(@class, 'main-menu')]//ul[contains(@class, 'main-menu')]/li"):
            # yield {
            #     'category': main_menu.xpath("./a/text()").get(),
            #     'url': main_menu.xpath("./a/@href").get(),
            # }
            for sub_menu in main_menu.xpath("./div[@class='popup']/div[@class='inner']/ul[@class='sub-menu']/li"):
                # yield {
                #     'category': main_menu.xpath("./a/text()").get(),
                #     'category-url': main_menu.xpath("./a/@href").get(),
                #     'sub-category': sub_menu.xpath("./a/text()").get(),
                #     'sub-url': sub_menu.xpath("./a/@href").get(),
                #     'sub-sub-category': '',
                #     'sub-sub-url': '',
                # }
                for sub_sub_menu in sub_menu.xpath("./ul[@class='sub-menu']/li"):
                    # //div[contains(@class, 'main-menu')]//ul[contains(@class, 'main-menu')]/li/div[@class='popup']/div[@class='inner']/ul[@class='sub-menu']/li/ul[@class='sub-menu']/li
                    yield {
                        'category': main_menu.xpath("./a/text()").get(),
                        'category-url': main_menu.xpath("./a/@href").get(),
                        'sub-category': sub_menu.xpath("./a/text()").get(),
                        'sub-url': sub_menu.xpath("./a/@href").get(),
                        'sub-sub-category': sub_sub_menu.xpath("./a/text()").get(),
                        'sub-sub-url': sub_sub_menu.xpath("./a/@href").get(),
                    }

        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
