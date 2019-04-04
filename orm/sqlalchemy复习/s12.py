from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Text
from sqlalchemy.orm import sessionmaker, relationship, backref
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime, date
from sqlalchemy.dialects.mysql import LONGTEXT

engine = create_engine("mysql+pymysql://root:root@127.0.0.1/ormreview?charset=utf8",
                       encoding='utf8')

session = sessionmaker(engine)()

Base = declarative_base(engine)


class Aticle(Base):
    __tablename__ = "article"
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(100), nullable=False)
    uid = Column(Integer, ForeignKey("user.id"))
    author = relationship("User", backref=backref("articles",cascade="save-update,delete-orphan, delete, merge"),single_parent=True)


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(100), nullable=False)


class Comment(Base):
    __tablename__ = "comment"
    id = Column(Integer, primary_key=True, autoincrement=True)
    uid = Column(Integer, ForeignKey("user.id"))
    post_id = Column(Integer, ForeignKey("article.id"))
    content = Column(Text)
    author = relationship("User", backref=backref("comments",cascade="save-update,delete-orphan, delete"))
    article = relationship("Aticle", backref=backref("articles",cascade="save-update,delete-orphan, delete"))


def reset():
    Base.metadata.drop_all()
    Base.metadata.create_all()
    print('---重置成功---')

def add():
    user1 = User(username='董豪')
    user2 = User(username='谭雅娟')

    aritcle1 = Aticle(title='鲁班来了1')
    aritcle2 = Aticle(title='鲁班来了2')
    aritcle3 = Aticle(title='王昭君1')
    aritcle4 = Aticle(title='王昭君2')

    comment1 = Comment(content='哈哈哈')
    comment2 = Comment(content='哈哈哈')

    user1.articles.extend([aritcle1, aritcle2])
    user2.articles.extend([aritcle3, aritcle4])

    user1.comments.append(comment1)
    user2.comments.append(comment2)
    comment1.article = aritcle1
    comment2.article = aritcle4
    session.add_all([user1,user2])
    session.commit()

def operation():
    # merge操作 #根据id
    # user = User(id=1,username='ha111hah')
    # session.merge(user)
    # session.commit()

    #user = session.query(User).first()
    #user.articles = []
    #session.commit()
    # session.add(Aticle(id=99,title='hahahahahahhahahahah'))
    # session.commit()
    #
    # user = User(id=1,username='user1')
    # ariticle = Aticle(id=99,title='标题9999999')
    # user.articles.append(ariticle)
    # session.merge(user)
    # session.commit()

    #expunge：移除操作的时候，会将相关联的对象也进行移除。这个操作只是从session中移除，并不会真正的从数据库中删除

    # all：是对save - update, merge, refresh - expire, expunge, delete几种的缩写。
    user = User(username='new user')
    article = Aticle(title='new title')
    session.add_all([user,article])
    session.expunge(user)
    session.commit()

if __name__ == '__main__':
    reset()
    add()
    operation()





