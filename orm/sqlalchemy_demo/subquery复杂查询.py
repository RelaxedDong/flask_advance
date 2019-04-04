#encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/1/8 13:40
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
    age = Column(Integer,default=0)
    city = Column(String(100))


def init():
    Base.metadata.drop_all()
    Base.metadata.create_all()


def add_func():
    user1 = User(username='张三',age=18,city='北京')
    user2 = User(username='王五',age=18,city='北京')
    user3 = User(username='赵六',age=12,city='长沙')
    user4 = User(username='李七',age=48,city='北京')
    session.add_all([user4,user3,user2,user1])
    session.commit()

def opration():
    stmp = session.query(User.age.label('age'),User.city.label('city')).filter(User.username=='张三').subquery()

    results = session.query(User.username,User.age,User.city).filter(User.age==stmp.c.age,User.city==stmp.c.city).all()

    # 关联子查询
    # subqry = session.query(func.count(Server.id).label("sid")).filter(Server.id == Group.id).correlate(Group).as_scalar()
    # result = session.query(Group.name, subqry)
    # """
    # SELECT `group`.name AS group_name, (SELECT count(server.id) AS sid
    # FROM server
    # WHERE server.id = `group`.id) AS anon_1
    # FROM `group`
    # """


if __name__ == '__main__':
    init()
    add_func()
    # opration()
