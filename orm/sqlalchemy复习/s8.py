from sqlalchemy import create_engine,Column,Integer,String,ForeignKey
from sqlalchemy.orm import sessionmaker,relationship,backref
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime,date
from sqlalchemy.dialects.mysql import LONGTEXT
engine = create_engine("mysql+pymysql://root:root@127.0.0.1/ormreview?charset=utf8",
                       encoding='utf8')

session = sessionmaker(engine)()

Base = declarative_base(engine)

class Aticle(Base):
    __tablename__ = "article"
    id = Column(Integer,primary_key=True,autoincrement=True)
    title = Column(String(100),nullable=False)
    uid = Column(Integer,ForeignKey("user.id"),nullable=False)
    author = relationship("User",backref=backref("articles",cascade="save-update,delete"),cascade="delete")

class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(100), nullable=False)


class Myoparation(object):
    def __init__(self,session):
        self.session = session
        self.Base = Base

    def reset(self):
        self.Base.metadata.drop_all()
        self.Base.metadata.create_all()
        print('---重置成功---')

    def add(self,colum):
        self.session.add(colum)
        self.session.commit()
        print('---数据添加成功---')


if __name__ == '__main__':
    oparaion = Myoparation(session)
    oparaion.reset()
    user1 = User(username='董浩1')
    user2 = User(username='董浩2')
    aritcle1 = Aticle(title='鲁班来了1')
    aritcle2 = Aticle(title='鲁班来了2')
    aritcle3 = Aticle(title='鲁班来了3')
    aritcle4 = Aticle(title='鲁班来了4')
    user1.articles.extend([aritcle1,aritcle2])
    user2.articles.extend([aritcle3,aritcle4])
    session.add_all([user1,user2])
    session.commit()

    # user = session.query(User).first()
    # session.delete(user)
    # session.commit()

    # article = session.query(Aticle).first()
    # session.delete(article)
    # session.commit()



