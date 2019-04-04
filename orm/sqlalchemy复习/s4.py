from sqlalchemy import create_engine,Column,Integer,String,DateTime,Float,DECIMAL,Boolean,Text,Enum,DATE
from sqlalchemy.orm import sessionmaker
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

    #create_time = Column(DateTime,default=datetime.now,onupdate=datetime.now)

    #price = Column(Float)

    #DECIMAL 定点类型
    #小数点前6位，4为小数点位数
    #max_price = Column(DECIMAL(10,4))

    #is_delete = Column(Boolean)
    #content = Column(Text)

    #tag = Column(Enum('美食','美女','美景'),default='美女')

    #Date
    join_time = Column(DATE)


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
    oparaion.add(Aticle(title='呐喊',join_time=date(2019,4,2)))
