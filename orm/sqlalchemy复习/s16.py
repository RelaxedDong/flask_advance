from sqlalchemy import create_engine, Column, Integer, String, ForeignKey,Table
from sqlalchemy.orm import sessionmaker, relationship, backref
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine("mysql+pymysql://root:root@127.0.0.1/ormreview?charset=utf8",
                       encoding='utf8')

session = sessionmaker(engine)()

Base = declarative_base(engine)

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
    tags = relationship("Tag",secondary="article_tag",backref=backref("articles"),lazy="dynamic")

def reset():
    Base.metadata.drop_all()
    Base.metadata.create_all()
    print('---重置成功---')

#lazy dynamic
def lazy():
    article = session.query(Aticle).first()
    from sqlalchemy.orm.dynamic import AppenderQuery  # AppenderQuery(AppenderMixin, Query)
    """
        AppenderMixin: remove extend count append
        
    """
    #article.tags.append(Tag(name='风景'))
    #article.tags.remove(session.query(Tag).first())
    print(article.tags.count())
    #session.commit()


if __name__ == '__main__':
   lazy()
