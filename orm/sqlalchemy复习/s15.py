from sqlalchemy import create_engine, Column, Integer, String, ForeignKey,Table
from sqlalchemy.orm import sessionmaker, relationship, backref
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine("mysql+pymysql://root:root@127.0.0.1/ormreview?charset=utf8",
                       encoding='utf8')

session = sessionmaker(engine)()

Base = declarative_base(engine)

# article_tag = Table(
#     "article_tag",
#     Base.metadata,
#     Column('tag_id', Integer,  ForeignKey("tag.id"), primary_key=True),
#     Column('article_id', Integer, ForeignKey("article.id"), primary_key=True),
# )
class ArticleTag(Base):
    __tablename__ = 'article_tag'
    tag_id = Column(Integer,ForeignKey("tag.id"),primary_key=True)
    article_id = Column(Integer,ForeignKey("article.id"),primary_key=True)


class Tag(Base):
    __tablename__ = "tag"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)

class Aticle(Base):
    __tablename__ = "article"
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(100), nullable=False)
    tags = relationship("Tag",secondary="article_tag",backref=backref("articles"))

def reset():
    Base.metadata.drop_all()
    Base.metadata.create_all()
    print('---重置成功---')

def add():
    article1 = Aticle(title='第1篇文章')
    tag1 = Tag(name='美食')
    tag2 = Tag(name='美女')
    article1.tags.append(tag1)
    article1.tags.append(tag2)
    session.add(article1)
    session.commit()

    # article = Aticle(title='new')
    # tag = session.query(Tag).first()
    # tag.articles.append(article)
    # session.add(tag)
    # session.commit()

    # article = session.query(Aticle).first()
    # print(article.tags)

def delete():
    article = session.query(Aticle).first()
    article.tags = []
    session.commit()

if __name__ == '__main__':
   reset()
   add()
   delete()
