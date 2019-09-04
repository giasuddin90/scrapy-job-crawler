from scrapy.spiders import Spider
from scrapy.selector import Selector
from datetime import datetime
import scrapy
from bs4 import BeautifulSoup
from jobsbot.items import Website


class DmozSpider(Spider):
    name = "govjob"
    allowed_domains = ["chakri.com"]
    start_urls = [
        "http://www.chakri.com/job?circular_type=govtjob&page=1",
        "http://www.chakri.com/job?circular_type=govtjob&page=2",
        "http://www.chakri.com/job?circular_type=govtjob&page=3",
    ]

    def parse(self, response):
        """
        The lines below is a spider contract. For more info see:
        http://doc.scrapy.org/en/latest/topics/contracts.html

        @url http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/
        @scrapes name
        """
        BASE_URL= "http://www.chakri.com"
        sel = Selector(response)
        all_links = sel.xpath('//div[@class="ctgry_dtls_job_each_container"]')
        for link in all_links:
            detail_value = link.xpath('div[@class="row"]/div/h3/a/@href').extract()
            detail_url = BASE_URL + detail_value[0]

            # print(detail_url + '===================================')
            yield scrapy.Request(detail_url,
                          callback=self.parse_detail)

    def parse_detail(self, response):
        BASE_URL= "http://www.chakri.com"

        item = Website()
        soup = BeautifulSoup(response.body_as_unicode(), "lxml")
        job_detail_url = response.url
        item['job_detail_url'] = job_detail_url

        job_title = soup.find('div', {"class" : "col-xs-9 col-sm-10 col-md-9"}).h1.get_text().strip()
        item['job_title'] = job_title if job_title else None

        organization = soup.find('p', {"class" : "dtls_company_name"}).get_text().strip()
        item['job_organization'] = organization if organization else None

        job_location = soup.find('p', {"class" : "dtls_company_location"}).get_text().strip()
        item['job_location'] = job_location if job_location else None

        item['job_category'] = 'gov_job'

        job_deadline = soup.findAll('span', {"class" : "dtls_date_posted_job"})[1].get_text().strip()
        dedline_j = job_deadline.replace(",", "")
        item['job_deadline'] = job_deadline if job_deadline else None
        item['deadline_date'] = datetime.strptime(dedline_j, '%b %d %Y') if job_deadline else None

        job_image = soup.find('h2', {"class" : "apply_instruction"}).a.get('href', None)
        if job_image:
            item['job_image_url'] = BASE_URL + job_image
        else:
            item['job_image_url'] = None
        job_source = soup.find('h2',text='Published').parent.p.get_text().strip()
        item['job_source'] = job_source if job_source else None

        item['job_created_by']= 'jobbot'
        item['job_is_published']= True

        yield item

