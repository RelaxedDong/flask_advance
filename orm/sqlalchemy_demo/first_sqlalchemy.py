#encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/1/4 17:07

from sqlalchemy import create_engine,Column,ForeignKey,Integer,String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,relationship,backref

#数据库配置变量
HOSTNAME = '127.0.0.1'
PORT = '3306'
DATABASE = 'firstsqlalchemy'
USERNAME = 'root'
PASSWORD = 'root'
DB_URL = "mysql+pymysql://root:root@127.0.0.1/firstsqlalchemy".format(USERNAME,PASSWORD,HOSTNAME,DATABASE)
# 创建引擎
engine = create_engine(DB_URL,encoding='utf8')


session = sessionmaker(engine)()

Base = declarative_base(engine)

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer,primary_key=True,autoincrement=True)
    username = Column(String(150))

class Article(Base):
    __tablename__ = 'article'
    id = Column(Integer,primary_key=True,autoincrement=True)
    title = Column(String(150))

    uid = Column(Integer,ForeignKey("user.id"))
    author = relationship("User",backref=backref('articles',cascade='save-update,delete,delete-orphan,expunge'
                                                 ,single_parent=True,lazy='dynamic'),cascade="save-update,delete")
    def __repr__(self):
        return '<Article %s>'%self.title
def init():
    Base.metadata.drop_all()
    Base.metadata.create_all()

def addfunc():
    user = User(username='123')
    article1 = Article(title='12a')
    article2 = Article(title='456')
    user.articles.append(article1)
    user.articles.append(article2)
    session.add(user)
    session.commit()

from sqlalchemy.orm.dynamic import AppenderQuery
from sqlalchemy.orm import Query
from sqlalchemy import and_,or_
from sqlalchemy import literal
from sqlalchemy.orm import aliased


def filter_something(criterion):
    def transform(q):
        return q.filter(criterion)
    return transform

def oparation():
    # user_aliased = aliased(User)
    # q = session.query(user_aliased,user_aliased.username).filter(user_aliased.username == '666')
    # print(q.column_descriptions)

    # users = session.query(User.username.label('name')).all()
    # for user in users:
    #     print(user.name)

    # users = session.query(User).filter(User.username.like('6%')).from_self()
    # for user in users:
    #     print(user.username,user.id)
    # user = session.query(Article).add_columns(Article.author,Article.title).all()
    # print(user)

    # from sqlalchemy import text
    # article = session.query(Article).filter(text('id>:id')).params(id = 1).all()
    # print(article)

    articles = session.query(Article).with_transformation(filter_something(Article.id>1)).all()
    print(articles)

if __name__ == '__main__':
    # init()
    # addfunc()
    oparation()


