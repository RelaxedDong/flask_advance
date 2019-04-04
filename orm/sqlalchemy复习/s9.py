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
    uid = Column(Integer,ForeignKey("user.id"))
    author = relationship("User",backref=backref("articles",cascade="save-update,delete-orphan,delete",single_parent=True))

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
    u = User(username='donghao')
    session.add(u)
    session.commit()



