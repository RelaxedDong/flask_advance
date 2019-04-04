from sqlalchemy import create_engine,Column,Integer,String,Float,func
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("mysql+pymysql://root:root@127.0.0.1/ormreview?charset=utf8",
                       encoding='utf8')

session = sessionmaker(engine)()

Base = declarative_base(engine)

class Aticle(Base):
    __tablename__ = "article"
    id = Column(Integer,primary_key=True,autoincrement=True)
    title = Column(String(100),nullable=False)
    price = Column(Float)


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

    def query(self,table):
        #统计行数量
        #count = self.session.query(func.count(table.id)).all()
        
        #avg
        #avg = self.session.query(func.count(table.price)).all()
        ##print(avg)

        #sum
        sum = self.session.query(func.sum(table.price)).all()
        #print(sum)

        #max
        #max = self.session.query(func.max(table.price)).all()
        #print(max)

        # max
        min = self.session.query(func.min(table.price)).all()

    def learn(self):
        #func.min(...)
        # 调用__getattr__魔术方法，返回本身对象_FunctionGenerator
        # 调用__call__方法
        pass

if __name__ == '__main__':
    oparaion = Myoparation(session)
    #oparaion.reset()
    #oparaion.add(Aticle(title='呐喊',price=2))
    #oparaion.add(Aticle(title='呐喊1',price=3))
    #oparaion.add(Aticle(title='呐喊2',price=4))
    oparaion.query(Aticle)
