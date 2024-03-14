import os

from sqlalchemy import create_engine, Column, Integer, String, TIMESTAMP, func, desc
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
    subq = session.query(
        TimeHistory.label,
        TimeHistory.time1,
        TimeHistory.time2,
        func.rank().over(
            partition_by=TimeHistory.time1,
            order_by=TimeHistory.time2.desc()
        ).label('pos')
    ).subquery()

    query = session.query(
        subq.c.label,
        subq.c.time1,
        subq.c.time2,
        subq.c.pos
    ).filter(subq.c.pos <= 2).order_by(subq.c.pos)

    for label, time1, time2, pos in query:
        print(f"Label: {label}, Time1: {time1}, Time2: {time2}, Position: {pos}")

