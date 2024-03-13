import os

from sqlalchemy import create_engine, Column, Integer, Numeric, String, Table, MetaData
from sqlalchemy.orm import declarative_base, sessionmaker

POSTGRES_USER=os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD=os.getenv("POSTGRES_PASSWORD")
POSTGRES_DB=os.getenv("POSTGRES_DB")

DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@localhost:5432/{POSTGRES_DB}"
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


class EmpSalary(Base):
    __tablename__ = 'empsalary'

    id = Column(Integer, primary_key=True)
    depname = Column(String)
    empno = Column(Integer)
    salary = Column(Numeric)


if __name__ == "__main__":
    empsalary_data = session.query(EmpSalary).all()

    for row in empsalary_data:
        print(f"{row.id}\t{row.depname}\t{row.empno}\t{row.salary}")

