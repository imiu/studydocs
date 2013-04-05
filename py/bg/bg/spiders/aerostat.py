import re
from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from bg.items import AeroEpisode


class AerostatSpider(CrawlSpider):
    name = 'aerostat'
    domain_name = ['aquarium.lipetsk.ru']
    start_urls = ['http://aquarium.lipetsk.ru/MESTA/mp3/Aerostat/']

    rules = (
        Rule(SgmlLinkExtractor(allow=('Aerostat_vol_')),
             callback='parse_item'),
    )

    def parse_item(self, response):
        # self.log('page: %s' % response.url)
        hxs = HtmlXPathSelector(response)

        ep = AeroEpisode()
        mp3_links = hxs.select('/html/body/pre/a/@href')
        for mp3 in mp3_links:
            mp3_link = mp3.extract()
            re_pat = re.compile(r'vol[\._]\d*\.mp3$')
            if re_pat.search(mp3_link):
                print response.url + mp3_link
                ep['link'] = response.url + mp3_link
                return ep
