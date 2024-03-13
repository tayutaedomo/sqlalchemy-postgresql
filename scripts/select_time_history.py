import os

from sqlalchemy import create_engine, Column, Integer, String, TIMESTAMP
from sqlalchemy.orm import declarative_base, sessionmaker

POSTGRES_USER=os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD=os.getenv("POSTGRES_PASSWORD")
POSTGRES_DB=os.getenv("POSTGRES_DB")

DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@localhost:5432/{POSTGRES_DB}"
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


class TimeHistory(Base):
    __tablename__ = 'time_history'
    id = Column(Integer, primary_key=True)
    label = Column(String(255))
    time1 = Column(TIMESTAMP)
    time2 = Column(TIMESTAMP)


if __name__ == "__main__":
    time_history_data = session.query(TimeHistory).all()

    for row in time_history_data:
        print(f"{row.id}\t{row.label}\t{row.time1}\t{row.time2}")

