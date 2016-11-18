#!/usr/bin/env bash

# 生成迁移文件 alembic revision --autogenerate -m "add article"

# 升级数据库 alembic upgrade head

# 手工编写升降级脚本初始化命令 alembic revision -m "init data"