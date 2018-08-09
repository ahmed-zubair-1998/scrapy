import scrapy

class BooksSpider(scrapy.Spider):
    name = "books"

    def start_requests(self):
        url = 'https://www.goodreads.com/'
        genres = getattr(self, 'genres', None)
        if genres is not None:
            url = url + 'genres/' + genres

        yield scrapy.Request(url, self.parse_helper)



    def parse_helper(self, response):
        for i in range (5):
            url = 'https://www.goodreads.com'
            url += response.css("div.coverRow div div a::attr(href)")[i].extract()
            yield scrapy.Request(url, self.parse)


    def parse(self, response):
        title = response.css("h1#bookTitle::text").extract_first().strip()
        author = response.css("a.authorName span::text").extract_first()
        yield {
            'title': title,
            'author': author,
        }
