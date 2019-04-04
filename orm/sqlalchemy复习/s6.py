from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import sessionmaker
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
        #colums = self.session.query(table).filter(table.title.like("呐喊%")).all()
        colums = self.session.query(table).filter(table.title.in_(["呐喊","呐喊1","呐喊2"])).all()
        for c in colums:
            print(c.title)


if __name__ == '__main__':
    oparaion = Myoparation(session)
    oparaion.query(Aticle)
