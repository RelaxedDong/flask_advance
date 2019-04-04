#encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/1/7 17:12
from sqlalchemy import create_engine,Column,ForeignKey,Integer,String,func
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

def add_func():
    user1 = User(username='张三')
    user2 = User(username='赵四')
    for x in range(1):
        article = Article(title='%s'%x)
        article.author = user1
        session.add(article)
    session.commit()

    for x in range(2,5):
        article = Article(title='%s'%x)
        article.author = user2
        session.add(article)
    session.commit()


def check():
    users = session.query(User.username,func.count(Article.id)).join(Article).group_by(User.id).order_by(func.count(Article.id).desc()).all()
    '''SELECT user.username AS user_username, count(article.id) AS count_1 
       FROM user INNER JOIN article ON user.id = article.uid GROUP BY user.id ORDER BY count(article.id) DESC'''
    print(users)
if __name__ == '__main__':
    # init()
    # add_func()
    check()
from sqlalchemy.orm import Query