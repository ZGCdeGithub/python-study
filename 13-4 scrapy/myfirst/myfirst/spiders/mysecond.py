import scrapy
import json


class MySecondSpider(scrapy.Spider):
    """
    定义一个蜘蛛
    var name：蜘蛛的名称。唯一
    var start_urls：蜘蛛要爬取的页面，这里定义这个可以省略start_requests方法
    """
    name = 'mySecond'
    start_urls = [
        'http://lab.scrapyd.cn/page/3/',
        'http://lab.scrapyd.cn/page/4/'
    ]

    def parse(self, response):
        """
        页面的解析方法
        :param response:
        :return:
        """
        page = response.url.split('/')[-2]
        filename = 'parse_html/scrapyd-%s.html' % page
        with open(filename, 'wb') as fp:
            fp.write(response.body)
        select_quote = response.css('div.quote')
        text_list = select_quote.css('.text::text').extract()
        author_list = select_quote.css('.author::text').extract()
        tags_list = select_quote.css('.tags')
        data = []
        k = 0
        for v in select_quote:
            data.append({
                'text': text_list[k],
                'author': author_list[k],
                'tags': ','.join(tags_list[k].css('.tag::text').extract())
            })
            k += 1
        with open('parse_html/scrapyd-%s.json' % page, 'w') as fp:
            fp.write(json.dumps(data, ensure_ascii=False, indent=2))

        self.log(__class__.__name__+' 保存文件 %s ' % filename)
