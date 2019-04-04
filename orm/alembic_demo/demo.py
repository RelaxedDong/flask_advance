#encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/1/9 16:53

from sqlalchemy import create_engine,Column,ForeignKey,Integer,String,Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,relationship,backref
#数据库配置变量
HOSTNAME = '127.0.0.1'
PORT = '3306'
DATABASE = 'firstsqlalchemy'
USERNAME = 'root'
PASSWORD = 'root'

DB_URL = "mysql+pymysql://root:root}@127.0.0.1/firstsqlalchemy"
# 创建引擎
engine = create_engine(DB_URL,encoding='utf8')

import alembic
session = sessionmaker(engine)()

Base = declarative_base(engine)

class User(Base):
     __tablename__ = 'user'
     id = Column(Integer,primary_key=True)
     username = Column(String(20),nullable=False)
     password = Column(String(100),nullable=False)


class Article(Base):
     __tablename__ = 'article'
     id = Column(Integer,primary_key=True)
     title = Column(String(100),nullable=False)
     content = Column(Text, nullable=False)


import sys
print(sys.path)