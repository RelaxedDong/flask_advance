#encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/4/2 20:00

from sqlalchemy import create_engine,Column,Integer,String,DateTime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

engine = create_engine("mysql+pymysql://root:root@127.0.0.1/ormreview?charset=utf8",
                       encoding='utf8')



session = sessionmaker(engine)()
Base = declarative_base(engine)

class Aticle(Base):
    __tablename__ = "article"
    id = Column(Integer,primary_key=True,autoincrement=True)
    title = Column(String(100),nullable=False)
    create_time = Column(DateTime,default=datetime.now,onupdate=datetime.now)


def init():
    Base.metadata.create_all()
    # Base.metadata.drop_all()

# if __name__ == '__main__':
    # init()
    # pass