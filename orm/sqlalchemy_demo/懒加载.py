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


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer,primary_key=True,autoincrement=True)
    username = Column(String(150))

class Article(Base):
    __tablename__ = 'article'
    id = Column(Integer,primary_key=True,autoincrement=True)
    title = Column(String(150))

    uid = Column(Integer,ForeignKey("user.id"))
    author = relationship("User",backref=backref('articles',lazy='dynamic'))

    def __repr__(self):
        return '<Article %s>'%self.title

def init():
    Base.metadata.drop_all()
    Base.metadata.create_all()

def oparation():
    user = User(username='donghao')
    for x in range(1,100):
        article = Article(title='%s'%x)
        user.articles.append(article)
    session.add(user)
    session.commit()

def check():
    # user = session.query(User).get(1)
    # article = session.query(Article).get(4)
    #
    #
    # user.articles.remove(article)
    # session.commit()

    from sqlalchemy.orm.dynamic import AppenderQuery
    from sqlalchemy.orm import Query
# class AppenderQuery(AppenderMixin, Query)
# 新方法 append ，count , remove ,extend
    user = session.query(User).get(1)
    article = Article(title='666')
    user.articles.extend([article])
    session.commit()

if __name__ == '__main__':
    # init()
    # oparation()
    check()