__author__ = 'giasuddin'
from jobsbot import settings
from sqlalchemy import create_engine, Column, Integer, String, DateTime,Text, DATE, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine.url import URL
import datetime


DeclarativeBase = declarative_base()


def db_connect():
    """
    Performs database connection using database settings from settings.py.
    Returns sqlalchemy engine instance
    """
    return create_engine(URL(**settings.DATABASE))


def create_deals_table(engine):
    """"""
    DeclarativeBase.metadata.create_all(engine)


class AllJob(DeclarativeBase):
    """Sqlalchemy govt jobs model"""
    __tablename__ = "nodes"

    id                  = Column(Integer, primary_key=True)
    job_detail_url      = Column('detail_url', String, nullable=False, unique=True)
    job_title           = Column('job_title', String, nullable=False, )
    job_description     = Column('job_description', String)
    job_organization    = Column('job_organization', String, nullable=False)
    job_location        = Column('job_location', String)
    job_category        = Column('job_category', String, nullable=False)
    job_source          = Column('source', String, nullable=False)
    job_deadline        = Column('job_deadline', String, nullable=False)
    job_image_url       = Column('job_image_url', String, nullable=False)
    job_image_name       = Column('job_image_name', String)
    job_salary          = Column('job_salary', String)
    deadline_date       = Column('deadline_date', DATE,)
    collected_time      = Column(DateTime, default=datetime.datetime.now())     #job collection time insert here
    count               = Column(Integer, default=0)                            #job view count sotre here

    # need to add this field
    job_secondary_category = Column('job_secondary_category', String)
    job_created_by      = Column('job_created_by', String)                      #job created user name
    job_updated_by      = Column('job_updated_by', String)                      #job updated user name
    updated_time        = Column('updated_time',  DateTime)                    #job updated time
    job_is_published    = Column('job_is_published',  Boolean)                  #job updated time
    job_is_sticky       = Column('job_is_sticky',  Boolean)



