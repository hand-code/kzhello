# coding:utf-8

from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, BigInteger, text, Text
from .modules import Base
from database import db_session


class Article(Base):
    __tablename__ = 'sys_article'


    #
    id = Column(Integer, primary_key=True)

    # 用户ID
    user_id = Column(Integer, nullable=False, index=True)

    # 分类编号
    catalog_id = Column(Integer, nullable=False)

    # 标题
    title = Column(String(128))

    # 摘要
    summary = Column(String(2048))

    # 访问次数
    read_num = Column(Integer, nullable=False, server_default=text("'0'"))

    # 发布时间
    publish_time = Column(DateTime)

    # 图片列表
    picture_tickets = Column(Text)

    # 图片的个数(【注意】请设置这个参数,以便在查询图片张数的场景下需要用到)
    picture_number = Column(Integer, nullable=False)

    # 发布者显示名称
    author = Column(String(64))

    # 审核 0未审核 1通过 2 不通过
    check = Column(Integer, nullable=False)

    def add(self):
        self.publish_time = datetime.now()

        sc = db_session()
        sc.add(self)
        sc.commit()
        sc.close()

    @staticmethod
    def delete(_id):
        sc = db_session()
        sc.query(Article).filter(Article.id == _id).delete(synchronize_session=False)
        sc.commit()
        sc.close()