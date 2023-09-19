import re

import scrapy

from ..items import PepParseItem
from ..constants import ALLOWED_DOMAINS, START_URLS


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ALLOWED_DOMAINS
    start_urls = START_URLS

    def parse(self, response):
        """Сбор ссылок на документы"""
        links_all = response.xpath(
            '//a[re:test(@href, "^pep-[0-9]{1,4}.$")]/@href'
        ).extract()
        for link in links_all:
            yield response.follow(
                link, callback=self.parse_pep
            )

    def parse_pep(self, response):
        """Парсинг страниц и формированиe items"""
        name = response.xpath('//h1[@class="page-title"]/text()').get()
        number = re.search('[0-9]{1,4}', str(name)).group()
        data = {
            'number': number,
            'name': name,
            'status': response.xpath(
                '//dl[@class="rfc2822 field-list simple"]/dd/abbr/text()'
            ).get()
        }

        yield PepParseItem(data)
