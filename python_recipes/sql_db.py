import sqlite3,os,pylab as pl
import numpy as np,sympy as sp,pandas as pd
from IPython.core.display import display, HTML
from IPython.core.magic import register_line_magic


thp=[('font-size','15px'),('text-align','center'),
     ('font-weight','bold'),('padding','5px 5px'),
     ('color','white'),('background-color','slategray')]
tdp=[('font-size','14px'),('padding','5px 5px'),
     ('text-align','center'),('color','darkblue'),
     ('background-color','silver')]
style_dict=[dict(selector='th',props=thp),
            dict(selector='td',props=tdp)]

def connect_to_db(dbf):
    sqlconn=None
    try:
        sqlconn=sqlite3.connect(dbf)
        return sqlconn
    except Error as err:
        print(err)
        if sqlconn is not None:
            sqlconn.close()

            

@register_line_magic
def get_query(q):
    sp.pprint(r'SQL Queries')
    tr=[]; cursor.execute(q)
    result=cursor.fetchall()
    for r in result: 
        tr+=[r]
    display(pd.DataFrame.from_records(tr)\
              .style.set_table_styles(style_dict))