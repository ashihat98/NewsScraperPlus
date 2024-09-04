from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Article(Base):
    __tablename__ = 'articles'
    id = Column(Integer, primary_key=True)
    title = Column(String(250), nullable=False)
    link = Column(String(500), nullable=False)

def save_to_database(news_df, db_path='news.db'):
    engine = create_engine(f'sqlite:///{db_path}', echo=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    for _, row in news_df.iterrows():
        article = Article(title=row['title'], link=row['link'])
        session.add(article)

    session.commit()
    session.close()
