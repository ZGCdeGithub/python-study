import scrapy


class MyTest(scrapy.Spider):
    name = 'mytest'
    start_urls = [
        'http://quotes.toscrape.com'
    ]

    def parse(self, response):
        select_div = response.css('div.quote')
        for div in select_div:
            yield {
                'text': div.css('span.text::text').extract_first(),
                'author': div.css('span small::text').extract_first(),
                'tags': div.css('div.tags a.tag::text').extract(),
            }

