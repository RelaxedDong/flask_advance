from sqlalchemy import create_engine, Column, Integer, String, Float,func
from sqlalchemy.orm import sessionmaker
from sqlalchemy import text
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("mysql+pymysql://root:root@127.0.0.1/ormreview?charset=utf8",
                       encoding='utf8')

session = sessionmaker(engine)()

Base = declarative_base(engine)


class Aticle(Base):
    __tablename__ = "article"
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(100), nullable=False)
    price = Column(Float)


class Myoparation(object):
    def __init__(self, session):
        self.session = session
        self.Base = Base

    def query(self,table):
        #colums = self.session.query(table).filter(text("id<:value and title=:inpuname")).params(value=10,inpuname='呐喊').all()
        #print(colums.id,colums.title)
        a = self.session.query(func.count("*")).select_from(table).scalar()
        print(a)
        b= session.query(func.count(table.id)).scalar()
        print(b)


if __name__ == '__main__':
    oparaion = Myoparation(session)
    oparaion.query(Aticle)
