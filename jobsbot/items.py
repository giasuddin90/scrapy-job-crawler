from scrapy.item import Item, Field


class Website(Item):

    job_detail_url = Field()
    job_title = Field()
    job_description = Field()
    job_organization = Field()
    job_location = Field()
    job_category = Field()
    job_source = Field()
    job_deadline = Field()
    job_image_url = Field()
    job_salary = Field()
    deadline_date = Field()

    job_created_by = Field()
    job_is_published = Field()
