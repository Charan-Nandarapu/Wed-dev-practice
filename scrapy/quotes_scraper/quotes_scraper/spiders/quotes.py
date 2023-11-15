import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    allowed_domains = ["example.com"]
    start_urls = ["https://example.com"]

    def parse(self, response):
        for quote in response.css('div.quotes'):
            yield{
                'text':quote.css('span.text::text').get(),
                'author':quote.css('span small.author::text').get(),
                'tags':quote.css('div.tags a.tags::text').getall(),
            }

            next_page=response.css('li.next a::attr(href)').get()
            if next_page is not None:
                yield response.follow(next_page,self.parse)
