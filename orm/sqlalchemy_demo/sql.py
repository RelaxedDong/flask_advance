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


class UserInfo(Base):
    __tablename__ = 'user_info'
    id = Column(Integer, primary_key=True, autoincrement=True)
    phone = Column(String(11),nullable=False)
    address = Column(String(100))
    user_id = Column(Integer,ForeignKey("user.id"))
    author = relationship("User",backref=backref('userinfo',uselist=False),uselist=False,cascade='save-update,delete')

def init():
    Base.metadata.drop_all()
    Base.metadata.create_all()


def oparation():
    user= session.query(User).get(1)
    info = UserInfo(phone='ccc',address='ccc')
    info.author = user
    session.add(info)
    session.commit()


if __name__ == '__main__':
    # init()
    oparation()