import scrapy


class ArgSpider(scrapy.Spider):
    name = 'arguments_spider'
    page_index = 1

    def start_requests(self):
        url = 'http://lab.scrapyd.cn/'
        # 获取tag参数
        tag = getattr(self, 'tag', None)
        if tag is not None:
            url += 'tag/'+tag
        yield scrapy.Request(url, self.parse)  # 发送请求爬取参数内容

    def parse(self, response):
        """
        蜘蛛运行后的回调方法，页面的解析会在这里
        :param response:
        :return:
        """
        # page = response.url.split('/')[-2]
        page = self.page_index
        self.page_index += 1
        filename = 'parse_html/%s_scrapyd' % __class__.__name__
        body = response.body
        html_file = filename+'-%s.html' % page
        with open(html_file, 'wb') as fp:
            fp.write(body)

        self.log('保存文件 %s ' % html_file)

        # 判断是否有下一页
        next_page = response.css('.page-navigator .next a::attr(href)').extract_first()
        if next_page is not None:
            # 继续爬取下一页
            next_page_url = response.urljoin(next_page)
            yield scrapy.Request(url=next_page_url, callback=self.parse)
