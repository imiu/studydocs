import re
from scrapy.selector import HtmlXPathSelector
# from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider
from bg.items import AeroName


class AeronameSpider(CrawlSpider):
    name = 'aeroname'
    domain_name = ['www.aquarium.ru']
    start_urls = []
    for i in xrange(1, 17):
        start_urls.append(
            'http://www.aquarium.ru/misc/aerostat/index%02d.html' % i
        )
    start_urls.append('http://www.aquarium.ru/misc/aerostat/index.html')

    def parse(self, response):
        self.log('page: %s' % response.url)
        hxs = HtmlXPathSelector(response)

        links = hxs.select('//a')
        re_name = re.compile(r'aerostat(\d*)\.html')
        ep_names = []
        for link in links:
            ex_link = link.extract()
            re_match = re_name.search(ex_link)
            if re_match:
                ep_number = re_match.group(1)
                print ex_link
                ep_name_raw = link.select('text()').extract()
                if not ep_name_raw:
                    ep_name_raw = link.select('.//b/text()').extract()
                if ep_name_raw:
                    ep_name = ep_name_raw[0]
                    if (len(ep_name) > len(str(ep_number))):
                        item = AeroName()
                        item['name'] = u"{} - {}".format(ep_number, ep_name)
                        ep_names.append(item)
        return ep_names
