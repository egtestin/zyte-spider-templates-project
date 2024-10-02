from scrapy import Spider


class MySpider(Spider):
    ...
    metadata = {
        "title": "My template",
        "description": "Description of my template.",
        "template": True,
    }
