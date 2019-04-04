#encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/1/8 18:01

from sqlalchemy import create_engine,Column,ForeignKey,Integer,String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,relationship,backref

#数据库配置变量
HOSTNAME = '127.0.0.1'
PORT = '3306'
DATABASE = 'firstsqlalchemy'
USERNAME = 'root'
PASSWORD = 'root'
DB_URL = "mysql+pymysql://{}:{}@{}/{}".format(USERNAME,PASSWORD,HOSTNAME,DATABASE)
# 创建引擎
engine = create_engine(DB_URL,encoding='utf8')

session = sessionmaker(engine)()

Base = declarative_base(engine)

# 中间表：
class Article_Tag(Base):
    __tablename__ = 'article_tag'
    article_id = Column(Integer,ForeignKey("article.id"),primary_key=True)
    tag_id = Column(Integer,ForeignKey("tag.id"),primary_key=True)

# 或者：
# post_tag = db.Table(
#     'article_tag',
#     db.Column('post_id',db.ForeignKey("article.id"),primary_key=True),
#     db.Column('tag_id',db.ForeignKey("tag.id"),primary_key=True)
# )


class Article(Base):
    __tablename__ = 'article'
    id = Column(Integer,primary_key=True,autoincrement=True)
    title = Column(String(150))


class Tag(Base):
    __tablename__ = 'tag'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100),nullable=False)
    articles = relationship("Article",backref=backref('tags'),secondary="article_tag")

def init():
    Base.metadata.drop_all()
    Base.metadata.create_all()


def add_func():
    session.query(Article_Tag).filter(Article_Tag.article_id==2,Article_Tag.tag_id==2).delete()
    session.commit()


if __name__ == '__main__':
    # init()
    add_func()


