#!/usr/bin/env python3
# -*-  coding: utf-8 -*-

from typing import Optional
from unittest import result
from sqlalchemy import true
from sqlmodel import Field,create_engine,SQLModel,select,Session
from pywebio import *
from pywebio.input import *
from pywebio.output import *


sqlite_filename = "wpmp.db"
sql_url = f"sqlite:///{sqlite_filename}"
engine = create_engine(sql_url,echo=True)

class project_info(SQLModel,table = true):
    proid: Optional[int] = Field(index=True,primary_key=True)
    proname: str
    protype: Optional[int] = Field(default=0) # 0 客户 1 集成
    prodesc: str
    proinfoupdate: str

def create_database_and_tables():
    SQLModel.metadata.create_all(engine)

def create_proinfo(pro_data):
    new_pro = project_info(proname=pro_data['name'],
        prodesc=pro_data['desc']
    )
    with Session(engine) as session:
        session.add(new_pro)
        session.commit() 

def select_proinfo():
    with Session(engine) as session:
        statement = select(project_info)
        results = session.exec(statement)
        return results
      
def main():  # PyWebIO application function
    pro_data = input_group("新建项目",[
        input('项目名称： (required)', name='name', required=True),
        input('项目描述： (required)', name='desc', required=True)
    ])
    create_database_and_tables()
    proinfos = select_proinfo()
    for pro in proinfos:
        put_text(pro.proid,pro.proname,pro.protype,pro.prodesc,pro.proinfoupdate)

if __name__ == "__main__":
    start_server(main, port=8090, debug=True)