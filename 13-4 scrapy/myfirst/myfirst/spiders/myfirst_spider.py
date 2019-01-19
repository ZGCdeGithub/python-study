import scrapy
import json


class MySpider(scrapy.spiders.Spider):
    """
    定义一个蜘蛛类，类名随意，必须继承scrapy.Spider
    var name：蜘蛛的名称，唯一
    fun start_requests：蜘蛛运行的方法，请求对应的页面
    fun parse：页面请求后的回调方法，后续的解析都会在这里
    """
    name = 'myFirst'
    page_index = 1

    def start_requests(self):
        """
        蜘蛛运行的方法，请求页面
        :return:
        """
        urls = [
            'http://lab.scrapyd.cn/'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        """
        蜘蛛运行后的回调方法，页面的解析会在这里
        :param response:
        :return:
        """
        # page = response.url.split('/')[-2]
        page = self.page_index
        self.page_index += 1
        filename = 'parse_html/scrapyd-%s.html' % page
        body = response.body
        with open(filename, 'wb') as fp:
            fp.write(body)
        # 解析标签
        select_quote = response.css('div.quote')
        data = []
        for div in select_quote:
            text = div.css('.text::text').extract_first()
            author = div.css('.author::text').extract_first()
            tags = ''
            for tag in div.css('.tags .tag'):
                tags += tag.css('::text').extract_first()
            data.append({
                'text': text,
                'author': author,
                'tags': tags
            })
        with open('parse_html/scrapyd-%s.json' % page, 'w') as fp:
            fp.write(json.dumps(data, ensure_ascii=False, indent=2))

        self.log('保存文件 %s ' % filename)

        # 判断是否有下一页
        next_page = response.css('.page-navigator .next a::attr(href)').extract_first()
        if next_page is not None:
            # 继续爬取下一页
            next_page_url = response.urljoin(next_page)
            yield scrapy.Request(url=next_page_url, callback=self.parse)
