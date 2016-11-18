# coding:utf-8
from sqlalchemy import Column, Integer, String, DateTime, BigInteger
from .modules import Base


class User(Base):
    __tablename__ = 'sys_user'


    #
    id = Column(Integer, primary_key=True)

    # 用户名
    user_name = Column(String(128), nullable=False, unique=True)

    # 邮箱
    email = Column(String(100))

    # 密码HASH
    password_hash = Column(String(128))

    # 手机号码
    phone_number = Column(String(32))

    # 积分(便于等级计算，规定死人民币1分等于1000个系统单位，前端显示统一使用换算函数进行换算显示)
    integral = Column(BigInteger, nullable=False)

    # IP地址
    ip = Column(String(30))

    # 最后登陆IP
    last_ip = Column(String(30))

    # 注册时间
    created = Column(DateTime, nullable=False)

    # 最后登陆时间
    last_login = Column(DateTime)

    # 账户是否禁用
    disabled = Column(Integer, nullable=False)