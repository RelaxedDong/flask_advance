from sqlalchemy import create_engine, Column, Integer, String, func
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


def reset():
    Base.metadata.drop_all()
    Base.metadata.create_all()
    print('---重置成功---')

def query():
    #查询不一样的标题
    #article = session.query(Aticle.title).distinct().all()

    #update
    #session.query(Aticle).filter(Aticle.id==1).update({"title":'updated title'})

    #delete
   # session.query(Aticle).filter(Aticle.id==1).delete()
    import time
    start = time.time()
    articles = session.query(func.count(Aticle.id)).all()
    end = time.time()
    print('%f'%(end-start))  #有索引  0.028020
                            #没有索引 0.388275
    print(articles)


if __name__ == '__main__':
    # reset()
    query()

