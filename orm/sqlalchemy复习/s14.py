from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship, backref
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine("mysql+pymysql://root:root@127.0.0.1/ormreview?charset=utf8",
                       encoding='utf8')

session = sessionmaker(engine)()

Base = declarative_base(engine)


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(100), nullable=False)

class Address(Base):
    __tablename__ = "address"
    id = Column(Integer, primary_key=True, autoincrement=True)
    place = Column(String(100))
    uid = Column(ForeignKey("user.id"))
    person = relationship("User",backref=backref("home",uselist=False))

def reset():
    Base.metadata.drop_all()
    Base.metadata.create_all()
    print('---重置成功---')

def add():
    user = User(username='donghao')
    place = Address(place='london')
    user.home = place
    session.add(user)
    session.commit()

if __name__ == '__main__':
    reset()
    add()
