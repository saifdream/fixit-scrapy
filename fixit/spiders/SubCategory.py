import scrapy


class SubCategory(scrapy.Spider):
    name = 'sub-category'
    start_urls = [
        'https://www.fixit.com.bd/product-category/tools-hardware/air-tools/',
        'https://www.fixit.com.bd/product-category/tools-hardware/automotive-tools-hardware/',
        'https://www.fixit.com.bd/product-category/tools-hardware/automotive-shop-equipment/',
        'https://www.fixit.com.bd/product-category/tools-hardware/cabinet-furniture-hardware/',
        'https://www.fixit.com.bd/product-category/tools-hardware/chain-rope/',
        'https://www.fixit.com.bd/product-category/tools-hardware/door-knobs-hardware/',
        'https://www.fixit.com.bd/product-category/tools-hardware/fasteners/',
        'https://www.fixit.com.bd/product-category/tools-hardware/gate-hardware/',
        'https://www.fixit.com.bd/product-category/tools-hardware/hand-tools/',
        'https://www.fixit.com.bd/product-category/tools-hardware/keys-accessories/',
        'https://www.fixit.com.bd/product-category/tools-hardware/ladders-scaffolding-ladders/',
        'https://www.fixit.com.bd/product-category/tools-hardware/power-tool-accessories/',
        'https://www.fixit.com.bd/product-category/tools-hardware/power-tools/',
        'https://www.fixit.com.bd/product-category/tools-hardware/safety-security/',
        'https://www.fixit.com.bd/product-category/tools-hardware/safety-gear-equipment/',
        'https://www.fixit.com.bd/product-category/tools-hardware/screws/',
        'https://www.fixit.com.bd/product-category/tools-hardware/nails-anchors/',
        'https://www.fixit.com.bd/product-category/tools-hardware/tools-storage/',
        'https://www.fixit.com.bd/product-category/tools-hardware/welding-soldering/',
        'https://www.fixit.com.bd/product-category/tools-hardware/wire-rope-fittings/',
        'https://www.fixit.com.bd/product-category/kitchen/cleaning-ironing/',
        'https://www.fixit.com.bd/product-category/kitchen/cooking-food-preparation/',
        'https://www.fixit.com.bd/product-category/kitchen/kitchen-accessories-kitchen/',
        'https://www.fixit.com.bd/product-category/kitchen/kitchen-storage-organization/',
        'https://www.fixit.com.bd/product-category/kitchen/sewing/',
        'https://www.fixit.com.bd/product-category/kitchen/small-appliances-kitchen/',
        'https://www.fixit.com.bd/product-category/kitchen/tableware-bar/',
        'https://www.fixit.com.bd/product-category/kitchen/water-dispensers-filters/',
        'https://www.fixit.com.bd/product-category/kitchen/wine-bar-tools/',
        'https://www.fixit.com.bd/product-category/cleaning/air-care/',
        'https://www.fixit.com.bd/product-category/cleaning/cleaning-tools-supplies/',
        'https://www.fixit.com.bd/product-category/cleaning/furniture-upholstery-cleaners-cleaning/',
        'https://www.fixit.com.bd/product-category/cleaning/household-cleaners/',
        'https://www.fixit.com.bd/product-category/cleaning/personal-care/',
        'https://www.fixit.com.bd/product-category/cleaning/trash-recycling/',
        'https://www.fixit.com.bd/product-category/electrical/batteries/',
        'https://www.fixit.com.bd/product-category/electrical/circuit-breakers-panels/',
        'https://www.fixit.com.bd/product-category/electrical/dimmers/',
        'https://www.fixit.com.bd/product-category/electrical/door-bells-intercoms/',
        'https://www.fixit.com.bd/product-category/electrical/electrical-tools-accessories/',
        'https://www.fixit.com.bd/product-category/electrical/extension-cords-surge-protectors/',
        'https://www.fixit.com.bd/product-category/electrical/fan-regulators-dimmers/',
        'https://www.fixit.com.bd/product-category/electrical/fire-safety/',
        'https://www.fixit.com.bd/product-category/electrical/handheld-flashlights/',
        'https://www.fixit.com.bd/product-category/electrical/head-lights/',
        'https://www.fixit.com.bd/product-category/electrical/home-electronics/',
        'https://www.fixit.com.bd/product-category/electrical/indoor-lighting-accessories/',
        'https://www.fixit.com.bd/product-category/electrical/light-bulbs/',
        'https://www.fixit.com.bd/product-category/electrical/network-cable-testers/',
        'https://www.fixit.com.bd/product-category/electrical/outdoor-lighting/',
        'https://www.fixit.com.bd/product-category/electrical/switches-outlets/',
        'https://www.fixit.com.bd/product-category/lawn-garden/garden-tools/',
        'https://www.fixit.com.bd/product-category/lawn-garden/generators-portable-power/',
        'https://www.fixit.com.bd/product-category/lawn-garden/insect-pest-control/',
        'https://www.fixit.com.bd/product-category/lawn-garden/watering-irrigation/',
        'https://www.fixit.com.bd/product-category/lawn-garden/wheelbarrows/',
        'https://www.fixit.com.bd/product-category/paint/caulking-sealants/',
        'https://www.fixit.com.bd/product-category/paint/craft-art-supplies/',
        'https://www.fixit.com.bd/product-category/paint/duct-tape/',
        'https://www.fixit.com.bd/product-category/paint/glues-epoxy/',
        'https://www.fixit.com.bd/product-category/paint/paint-supplies/',
        'https://www.fixit.com.bd/product-category/paint/spray-paint/',
        'https://www.fixit.com.bd/product-category/3d-printer-supplies/',
        'https://www.fixit.com.bd/product-category/appliance/',
        'https://www.fixit.com.bd/product-category/automotive/',
        'https://www.fixit.com.bd/product-category/bath-faucets/',
        'https://www.fixit.com.bd/product-category/building-materials/',
        'https://www.fixit.com.bd/product-category/cleaning/',
        'https://www.fixit.com.bd/product-category/doors-windows/',
        'https://www.fixit.com.bd/product-category/electrical/',
        'https://www.fixit.com.bd/product-category/flooring-area-rugs/',
        'https://www.fixit.com.bd/product-category/heating-cooling/',
        'https://www.fixit.com.bd/product-category/kitchen/',
        'https://www.fixit.com.bd/product-category/lawn-garden/',
        'https://www.fixit.com.bd/product-category/outdoor-living/',
        'https://www.fixit.com.bd/product-category/paint/',
        'https://www.fixit.com.bd/product-category/plumbing/',
        'https://www.fixit.com.bd/product-category/qurbani-special/',
        'https://www.fixit.com.bd/product-category/storage-organization/',
        'https://www.fixit.com.bd/product-category/tools-hardware/',
        'https://www.fixit.com.bd/product-category/uncategorised/',
        'https://www.fixit.com.bd/product-category/uncategorized/'
    ]

    def parse(self, response):
        for product in response.xpath("//div[contains(@class, 'archive-products')]//ul/li"):
            print("For")
            yield {
                'category-url': response.url,
                'product-url': product.xpath("./a[contains(@class, 'product-loop-title')]/@href").get(),
            }

        next_page = response.xpath("//div[contains(@class,'shop-loop-before')]/nav[@class='woocommerce-pagination']/ul//a/@href").extract()
        if next_page is not None:
            print("Next Page")
            print(next_page)
            for url in next_page:
                yield scrapy.Request(url=response.urljoin(url), callback=self.parse)
