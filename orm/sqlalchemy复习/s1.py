#encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/4/2 20:00

from sqlalchemy import create_engine
engine = create_engine("mysql+pymysql://root:root@127.0.0.1/ormreview?charset=utf8",
                       encoding='utf8')

# 判断是否连接成功
with engine.connect() as f:
    result = f.execute("select 1")
    print(result.fetchone())
    print(type(result))
    # (1,)
    #<class 'sqlalchemy.engine.result.ResultProxy'>



