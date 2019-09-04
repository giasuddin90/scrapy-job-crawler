from scrapy.exceptions import DropItem
from sqlalchemy.orm import sessionmaker
from jobsbot.models import AllJob, db_connect, create_deals_table


class FilterWordsPipeline(object):
    """A pipeline for filtering out items which contain certain words in their
    description"""

    # put all words in lowercase
    words_to_filter = ['politics', 'religion']

    def process_item(self, item, spider):
        for word in self.words_to_filter:
            if word in str(item['title']):
                raise DropItem("Contains forbidden word: %s" % word)
        else:
            return item




class JobsStorePipeline(object):
    """Livingsocial pipeline for storing scraped items in the database"""
    def __init__(self):
        """
        Initializes database connection and sessionmaker.
        Creates deals table.
        """
        engine = db_connect()
        create_deals_table(engine)
        self.Session = sessionmaker(bind=engine)

    def process_item(self, item, spider):

        """Save deals in the database.

        This method is called for every item pipeline component.

        """
        session = self.Session()
        deal = AllJob(**item)

        try:
            session.add(deal)
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()

        return item