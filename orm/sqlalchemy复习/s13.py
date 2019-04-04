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
    author = relationship("User", backref=backref("articles",order_by=-id,cascade="save-update,delete-orphan, delete, merge"),single_parent=True)

    # __mapper_args__ = {
    #      "order_by": -id
    # }

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
    #Base.metadata.create_all()
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
    #articles = session.query(Aticle).order_by(Aticle.id.desc()).all()
    user = session.query(User).first()
    for a in user.articles:
        print(a.id)


if __name__ == '__main__':
    # reset()
    # add()
    operation()





