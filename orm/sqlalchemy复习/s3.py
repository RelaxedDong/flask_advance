#encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/4/2 20:00

from sqlalchemy import create_engine,Column,Integer,String,DateTime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

engine = create_engine("mysql+pymysql://root:root@127.0.0.1/ormreview?charset=utf8",
                       encoding='utf8')


session = sessionmaker(engine)()

# session: <class 'sqlalchemy.orm.session.Session'>

#调用sessionmaker的  __call__ 方法 ， 返回使用元类创建的Session类
# type(class_.__name__, (class_,), {})

Base = declarative_base(engine)

class Aticle(Base):
    __tablename__ = "article"
    id = Column(Integer,primary_key=True,autoincrement=True)
    title = Column(String(100),nullable=False)
    create_time = Column(DateTime,default=datetime.now,onupdate=datetime.now)

    def __str__(self):
        return "<Article id is %s,title is %s>"%(self.id,self.title)


def add():
    article1 = Aticle(title='鲁班来了1')
    article2 = Aticle(title='鲁班来了2')
    session.add_all([article1,article2])
    session.commit()

def delete():
    pass

def check():
    articles = session.query(Aticle).all()
    a = session.query(Aticle.title).filter(Aticle.title=="鲁班来了").first()
    b = session.query(Aticle).filter_by(title="鲁班来了1").first()
    print(a)
    print(b)

def delete():
    one = session.query(Aticle).first()
    session.delete(one)
    session.commit()

def update():
    article =session.query(Aticle).first()
    article.title = "大学英语"
    session.commit()

if __name__ == '__main__':
    #add()
    #check()
    #delete()
    update()