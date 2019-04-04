from sqlalchemy import create_engine,Column,ForeignKey,Integer,String,Enum,func
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
    username = Column(String(100),nullable=False)
    age = Column(Integer,default=0)
    gender = Column(Enum("male","female","secret"),default="male")

def init():
    Base.metadata.drop_all()
    Base.metadata.create_all()

def add_m():
    user1 = User(username='董浩1',age=14,gender="male")
    user2 = User(username='董浩2',age=15,gender="female")
    user3 = User(username='董浩3',age=18,gender="secret")
    user4 = User(username='董浩4',age=18,gender="male")
    session.add_all([user1,user2,user3,user4])
    session.commit()

def group_by():
    result = session.query(User.age,func.count(User.age)).group_by(User.age).all()
    '''sql:
    SELECT user.age AS user_age, count(user.age) AS count_1 
    FROM user GROUP BY user.age'''
    print(result)

def having():
    result = session.query(User.age,func.count(User.age)).group_by(User.age).filter(User.age>16).all()
    print(result)
    '''having可以对group分组的结果集进行过滤，因其执行在分组之后，并其过滤可以基于分组聚集值。(having子句中可以直接使用聚合函数)
有这样的说法，“having子句中的列只能是group by子句中的列或者聚合函数的列”。实际上这也可以用上面所说的来解释－－having在group by分组后才执行。
总结：
涉及到对分组结果集的过滤操作，都用having。
非分组结果集的操作，行级的操作，用where。
'''

if __name__ == '__main__':
    # init()
    # add_m()
    # group_by()
    having()













