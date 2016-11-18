# coding:utf-8

from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from modules.modules import Base


engine = create_engine('postgresql://root:cxf218dj1q8@10.144.177.116:5432/feed', convert_unicode=True, echo=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))

Base.query = db_session.query_property()


def init_db():
  Base.metadata.create_all(bind=engine)


if __name__ == '__main__':
    init_db()