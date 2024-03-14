import os

from sqlalchemy import create_engine, Column, Integer, Numeric, String, func, desc

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
    subq = session.query(
        EmpSalary.depname,
        EmpSalary.empno,
        EmpSalary.salary,
        func.rank().over(
            partition_by=EmpSalary.depname,
            order_by=desc(EmpSalary.salary)
        ).label('pos')
    ).subquery('ranked_salaries')

    # サブクエリを使ってpos < 3 のレコードを取得
    query = session.query(
        subq.c.depname,
        subq.c.empno,
        subq.c.salary,
        subq.c.pos
    ).filter(subq.c.pos < 3)

    for depname, empno, salary, pos in query:
        print(f"Department: {depname}, Employee Number: {empno}, Salary: {salary}, Position: {pos}")

