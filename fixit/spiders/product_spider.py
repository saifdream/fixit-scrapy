import scrapy


class ProductSpider(scrapy.Spider):
    name = "product"
    start_urls = [
        # 'https://www.fixit.com.bd/product-category/tools-hardware/hand-tools/',
        'https://www.fixit.com.bd/product-category/tools-hardware/power-tools/',
        'https://www.fixit.com.bd/product-category/tools-hardware/air-tools/',
        'https://www.fixit.com.bd/product-category/tools-hardware/chain-rope/',
        'https://www.fixit.com.bd/product-category/tools-hardware/door-knobs-hardware/',
        'https://www.fixit.com.bd/product-category/tools-hardware/safety-security/',
        'https://www.fixit.com.bd/product-category/tools-hardware/fasteners/',
        'https://www.fixit.com.bd/product-category/tools-hardware/nails-anchors/',
        'https://www.fixit.com.bd/product-category/tools-hardware/welding-soldering/',
        'https://www.fixit.com.bd/product-category/tools-hardware/power-tool-accessories/',
        'https://www.fixit.com.bd/product-category/tools-hardware/tools-storage/',
        'https://www.fixit.com.bd/product-category/tools-hardware/cabinet-furniture-hardware/',
        # 'https://www.fixit.com.bd/product-category/kitchen/cooking-food-preparation/',
        'https://www.fixit.com.bd/product-category/kitchen/small-appliances-kitchen/kitchen-accessories/',
        'https://www.fixit.com.bd/product-category/kitchen/kitchen-storage-organization/',
        'https://www.fixit.com.bd/product-category/appliance/small-appliances/',
        'https://www.fixit.com.bd/product-category/kitchen/water-dispensers-filters/',
        'https://www.fixit.com.bd/product-category/kitchen/wine-bar-tools/',
        'https://www.fixit.com.bd/product-category/kitchen/tableware-bar/',
        'https://www.fixit.com.bd/product-category/kitchen/cleaning-ironing/',
        'https://www.fixit.com.bd/product-category/kitchen/sewing/',
        # 'https://www.fixit.com.bd/product-category/cleaning/cleaning-tools-supplies/',
        # 'https://www.fixit.com.bd/product-category/cleaning/household-cleaners/',
        # 'https://www.fixit.com.bd/product-category/cleaning/air-care/',
        # 'https://www.fixit.com.bd/product-category/cleaning/personal-care/',
        # 'https://www.fixit.com.bd/product-category/cleaning/trash-recycling/',
        'https://www.fixit.com.bd/product-category/cleaning/furniture-upholstery-cleaners-cleaning/',
        # 'https://www.fixit.com.bd/product-category/electrical/batteries/',
        # 'https://www.fixit.com.bd/product-category/electrical/circuit-breakers-panels/',
        'https://www.fixit.com.bd/product-category/electrical/door-bells-intercoms/',
        'https://www.fixit.com.bd/product-category/electrical/electrical-tools-accessories/',
        'https://www.fixit.com.bd/product-category/electrical/fan-regulators-dimmers/',
        'https://www.fixit.com.bd/product-category/electrical/switches-outlets/',
        'https://www.fixit.com.bd/product-category/lawn-garden/garden-tools/',
        'https://www.fixit.com.bd/product-category/lawn-garden/insect-pest-control/',
        'https://www.fixit.com.bd/product-category/lawn-garden/watering-irrigation/',
        'https://www.fixit.com.bd/product-category/lawn-garden/wheelbarrows/',
        'https://www.fixit.com.bd/product-category/paint/spray-paint/',
        'https://www.fixit.com.bd/product-category/paint/paint-supplies/',
        'https://www.fixit.com.bd/product-category/paint/craft-art-supplies/',
        'https://www.fixit.com.bd/product-category/paint/craft-art-supplies/clay-modeling-materials/',
        'https://www.fixit.com.bd/product-category/paint/craft-art-supplies/paint-colors/',
        'https://www.fixit.com.bd/product-category/paint/glues-epoxy/',
        'https://www.fixit.com.bd/product-category/3d-printer-supplies/',
        'https://www.fixit.com.bd/product-category/automotive/',
        'https://www.fixit.com.bd/product-category/outdoor-living/',
        'https://www.fixit.com.bd/product-category/storage-organization/',
        'https://www.fixit.com.bd/product-category/appliance/',
        'https://www.fixit.com.bd/product-category/building-materials/',
        'https://www.fixit.com.bd/product-category/bath-faucets/',
        'https://www.fixit.com.bd/product-category/plumbing/',
        'https://www.fixit.com.bd/product-category/doors-windows/',
        'https://www.fixit.com.bd/product-category/heating-cooling/',
        'https://www.fixit.com.bd/product-category/flooring-area-rugs/',

        # 'https://www.fixit.com.bd/product-category/tools-hardware/hand-tools/spanners-wrenches/',
        # 'https://www.fixit.com.bd/product-category/tools-hardware/hand-tools/adjustable-wrenches/',
        # 'https://www.fixit.com.bd/product-category/tools-hardware/hand-tools/pipe-wrenches/',
        # 'https://www.fixit.com.bd/product-category/tools-hardware/hand-tools/wrenches/socket-wrenches/',
        # 'https://www.fixit.com.bd/product-category/tools-hardware/hand-tools/wrenches/',
        # 'https://www.fixit.com.bd/product-category/tools-hardware/hand-tools/measure-layout-tools/',
        # 'https://www.fixit.com.bd/product-category/tools-hardware/hand-tools/pliers/',
        # 'https://www.fixit.com.bd/product-category/tools-hardware/hand-tools/planers/',
        # 'https://www.fixit.com.bd/product-category/kitchen/cooking-food-preparation/scissors/',
        # 'https://www.fixit.com.bd/product-category/tools-hardware/hand-tools/screwdrivers/',
        # 'https://www.fixit.com.bd/product-category/tools-hardware/hand-tools/hammers/',
        # 'https://www.fixit.com.bd/product-category/tools-hardware/hand-tools/knives-blades/',
        # 'https://www.fixit.com.bd/product-category/tools-hardware/hand-tools/combination-spanner/',
        # 'https://www.fixit.com.bd/product-category/tools-hardware/power-tools/drill-machine/',
        # 'https://www.fixit.com.bd/product-category/tools-hardware/power-tools/hammer-drill-machine/',
        # 'https://www.fixit.com.bd/product-category/tools-hardware/power-tools/heat-guns/',
        # 'https://www.fixit.com.bd/product-category/tools-hardware/power-tools/cordless-screwdrivers/',
        # 'https://www.fixit.com.bd/product-category/tools-hardware/power-tools/dust-blower/',
        # 'https://www.fixit.com.bd/product-category/tools-hardware/power-tools/jig-saws/',
        # 'https://www.fixit.com.bd/product-category/tools-hardware/power-tools/belt-sanders/',
        # 'https://www.fixit.com.bd/product-category/tools-hardware/power-tools/sander-machine/',
        # 'https://www.fixit.com.bd/product-category/tools-hardware/power-tools/angle-grinders/',
        # 'https://www.fixit.com.bd/product-category/tools-hardware/tools-storage/tool-bags/',
        # 'https://www.fixit.com.bd/product-category/tools-hardware/tools-storage/tool-belts/',
        # 'https://www.fixit.com.bd/product-category/kitchen/cooking-food-preparation/can-openers/',
        # 'https://www.fixit.com.bd/product-category/kitchen/cooking-food-preparation/charcoal-starter-lighters/',
        # 'https://www.fixit.com.bd/product-category/kitchen/cooking-food-preparation/egg-separator/',
        # 'https://www.fixit.com.bd/product-category/kitchen/cooking-food-preparation/graters-peelers/',
        # 'https://www.fixit.com.bd/product-category/kitchen/cooking-food-preparation/kitchen-gadgets-tools/',
        # 'https://www.fixit.com.bd/product-category/kitchen/cooking-food-preparation/ladles-spoons/',
        # 'https://www.fixit.com.bd/product-category/kitchen/cooking-food-preparation/manual-graters-slicers/',
        # 'https://www.fixit.com.bd/product-category/cleaning/cleaning-tools-supplies/floor-brushes/',
        # 'https://www.fixit.com.bd/product-category/cleaning/cleaning-tools-supplies/hand-brushes/',
        # 'https://www.fixit.com.bd/product-category/cleaning/cleaning-tools-supplies/metal-polish/',
        # 'https://www.fixit.com.bd/product-category/cleaning/cleaning-tools-supplies/mops-mop-accessories/',
        # 'https://www.fixit.com.bd/product-category/cleaning/cleaning-tools-supplies/nail-brushes/',
        # 'https://www.fixit.com.bd/product-category/cleaning/cleaning-tools-supplies/shoe-brushes/',
        # 'https://www.fixit.com.bd/product-category/cleaning/cleaning-tools-supplies/shoe-polish/',
        # 'https://www.fixit.com.bd/product-category/cleaning/cleaning-tools-supplies/sponges-scouring-pads/',
        # 'https://www.fixit.com.bd/product-category/cleaning/cleaning-tools-supplies/toilet-brushes-holders/',
        # 'https://www.fixit.com.bd/product-category/cleaning/cleaning-tools-supplies/wire-brushes/',
        # 'https://www.fixit.com.bd/product-category/cleaning/household-cleaners/all-purpose-cleaners/',
        # 'https://www.fixit.com.bd/product-category/cleaning/household-cleaners/cloth-cleaners/',
        # 'https://www.fixit.com.bd/product-category/cleaning/household-cleaners/dishwasher-detergent-soap/',
        # 'https://www.fixit.com.bd/product-category/cleaning/household-cleaners/electronic-cleaners/',
        # 'https://www.fixit.com.bd/product-category/cleaning/household-cleaners/furniture-upholstery-cleaners/',
        # 'https://www.fixit.com.bd/product-category/cleaning/household-cleaners/glass-window-cleaners/',
        # 'https://www.fixit.com.bd/product-category/cleaning/household-cleaners/floor-cleaners/',
        # 'https://www.fixit.com.bd/product-category/cleaning/household-cleaners/toilet-cleaners/',
        # 'https://www.fixit.com.bd/product-category/cleaning/air-care/air-fresheners/',
        # 'https://www.fixit.com.bd/product-category/cleaning/personal-care/nail-care/',
        # 'https://www.fixit.com.bd/product-category/cleaning/personal-care/apron/',
        # 'https://www.fixit.com.bd/product-category/cleaning/personal-care/grooming-kit/',
        # 'https://www.fixit.com.bd/product-category/cleaning/personal-care/fabric-conditioner/',
        # 'https://www.fixit.com.bd/product-category/cleaning/personal-care/hair-combs/',
        # 'https://www.fixit.com.bd/product-category/cleaning/personal-care/hand-soaps-sanitizers/',
        # 'https://www.fixit.com.bd/product-category/cleaning/trash-recycling/recycling-bins/',
        # 'https://www.fixit.com.bd/product-category/electrical/batteries/household-batteries/',
        # 'https://www.fixit.com.bd/product-category/electrical/circuit-breakers-panels/circuit-breakers/',
        # 'https://www.fixit.com.bd/product-category/electrical/circuit-breakers-panels/subpanels/',
        # 'https://www.fixit.com.bd/product-category/electrical/fan-regulators-dimmers/dim-lights/',
        # 'https://www.fixit.com.bd/product-category/electrical/dimmers/plugs-connectors/',
        # 'https://www.fixit.com.bd/product-category/electrical/switches-outlets/sockets/'
    ]

    def parse(self, response):
        for product in response.xpath("//div[contains(@class, 'archive-products')]//ul/li"):
            yield {
                'title': product.xpath("./a[contains(@class, 'product-loop-title')]/h2/text()").get(),
                'price': product.xpath("./span[contains(@class,'price')]/span/text()").get(),
                'image': product.xpath("./div[contains(@class, 'product-image')]/a/div[contains(@class, 'inner')]/img[contains(@class,'wp-post-image')]/@src").get(),
            }

        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)