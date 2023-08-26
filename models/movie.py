from sqlalchemy import create_engine, Column, Integer, String, Float, Boolean, JSON, Date, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
import uuid
# import logging
import json
from tqdm import tqdm
from ..config import *

db_path = f"sqlite:///{SQL_DB_PATH}" # type: ignore
# Define the SQLAlchemy Base class
Base = declarative_base()

class Movie(Base):
    """
    """
    __tablename__ = 'Movie'
    id = Column(String(36), primary_key=True)
    name = Column(String, nullable=False)
    url = Column(String)
    poster = Column(String)
    description = Column(String)
    review = Column(String)
    rating_count = Column(Integer)
    rating_value = Column(Float)
    content_rating = Column(String)
    genre = Column(JSON)
    date = Column(Text)
    keywords = Column(JSON)
    duration = Column(Integer)
    actors = Column(JSON)
    creators = Column(JSON)
    director = Column(JSON)

    def add(self, session: Session):
        unique_id = str(uuid.uuid4())
        self.id = unique_id
        session.add(self)
        try:
            session.commit()
        except Exception as e:
            session.rollback()
            # logging.error("Error adding product to database: ", e)
            raise e   

    def __repr__(self):
        return f"""
            Name: {self.name}
            URL: {self.url}
            Rating: {self.rating_value}
            genre: {self.genre}
            description: {self.description}
        """

engine = create_engine(db_path)
Base.metadata.create_all(engine) # type: ignore
Session = sessionmaker(bind=engine)
session = Session()

def test():
    with open("/Users/suhasjain/Desktop/movie-recommender/scraper/movies.json", "r") as f:
        data = f.read()
        movies = json.loads(data)
        for movie in tqdm(movies["items"]):
            product = Movie(
                name= movie["name"],
                url= movie["url"],
                poster = movie["poster"],
                description = movie["description"],
                review = movie["review"]["reviewBody"],
                rating_count = movie["rating"]["ratingCount"],
                rating_value = movie["rating"]["ratingValue"],
                content_rating = movie["contentRating"],
                genre = movie["genre"],
                date = movie["datePublished"],
                keywords = movie["keywords"],
                duration = movie["duration"],
                actors = movie["actor"],
                creators = movie["creator"],
                director = movie["director"]
            )
            print(product)
            product.add(session=session)

if __name__ == "__main__":
    test()


