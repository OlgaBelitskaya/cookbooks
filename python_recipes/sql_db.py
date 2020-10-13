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

def connect2db(dbf):
    sqlconn=None
    try:
        sqlconn=sqlite3.connect(dbf)
        return sqlconn
    except Error as err:
        print(err)
        if sqlconn is not None:
            sqlconn.close()

def name(**var):
    return [x for x in var]

def get_query(url,query,ftype='csv'):
    if ftype=='csv':
        df=pd.read_csv(url).dropna()
    if ftype=='json':
        df=pd.read_json(url).dropna()
    connection=connect2db('example.db')
    if connection is not None:
        cursor=connection.cursor()
    data_table=name(df=df)[0]
    df.to_sql(data_table,
              con=connection,
              if_exists='replace')
    sp.pprint(
        r'the result of the sql query from df:'+query)
    tr=[]; cursor.execute(query)
    result=cursor.fetchall()
    for r in result: 
        tr+=[r]
    result=pd.DataFrame.from_records(tr)
    display(result.style.set_table_styles(style_dict))
    if connection is not None:
        connection.close()
    if os.path.exists('example.db'):
        os.remove('example.db')
    else:
        sp.pprint('example.db does not exist')