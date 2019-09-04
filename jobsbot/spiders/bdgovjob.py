from scrapy.spiders import Spider
from scrapy.selector import Selector
from datetime import datetime
import scrapy
from jobsbot.items import Website


class BDJobsSpider(Spider):
    name = "bdgovjob"
    allowed_domains = ["jobs.bdjobs.com"]
    start_urls = [
        "http://jobs.bdjobs.com/JobSearch.asp?requestType=government",
            ]

    deadline_date= ''

    def parse(self, response):
        """
        The lines below is a spider contract. For more info see:
        http://doc.scrapy.org/en/latest/topics/contracts.html


        """
        BASE_URL= "http://jobs.bdjobs.com/"
        sel = response
        all_date_list_first = sel.xpath('//div[@class="dead-text-d"]/strong/text()').getall()
        all_date_list_last = sel.xpath('//div[@class="dead-text-d"]/strong/following-sibling::text()').getall()
        links_list = sel.xpath('//div[@class="job-title-text"]/a/@href').getall()
        key_list=0
        for link in links_list:
            # detail_value = link.xpath('//div[@class="job-title-text"]/a/@href').get().strip()
            detail_url = BASE_URL + link
            dedline_prefix = all_date_list_first[key_list].replace(',', '')
            dedline_postfix = all_date_list_last[key_list]
            dedline_date=dedline_prefix + dedline_postfix.strip()
            print(dedline_date)
            self.deadline_date= dedline_date
            key_list +=1

            # print(detail_url + '===================================')
            yield scrapy.Request(detail_url,
                          callback=self.parse_detail)

    def parse_detail(self, response):
        BASE_URL= "http://jobs.bdjobs.com/"
        item = Website()
        job_detail_url = response.url
        item['job_detail_url'] = job_detail_url

        job_title = response.xpath('//h4[@class="job-title"]/text()').get().strip()
        item['job_title'] = job_title if job_title else None

        organization = response.xpath('//h2[@class="company-name"]/text()').get().strip()
        item['job_organization'] = organization if organization else None

        job_location = None
        item['job_location'] = job_location if job_location else None

        item['job_category'] = 'gov_job'

        dedline_j = self.deadline_date
        item['job_deadline'] = self.deadline_date if dedline_j else None
        item['deadline_date'] = datetime.strptime(dedline_j, '%b %d %Y') if dedline_j else None

        job_image = response.xpath('//div[@class="image"]/img/@src').get()
        if job_image:
            item['job_image_url'] = job_image
        else:
            item['job_image_url'] = None

        job_source = response.xpath('//p[@class="category"]/text()').get().strip()
        item['job_source'] = job_source if job_source else None

        item['job_created_by']= 'jobbot'
        item['job_is_published']= True

        yield item

