import numpy as np,pandas as pd
from IPython.display import display

def display_dataframe(df,cmap,dhead=False,
                      td_font_size=110,th_font_size=150):
    style_dict={'font-size':'%d'%td_font_size+'%',
                'font-family':'times',
                'text-shadow':'slategray 2px 2px 2px'}
    head_styler=(('color','darkslategray'),
                 ('font-family','times'),
                 ('font-size','%d'%th_font_size+'%'),
                 ('text-shadow','slategray 2px 2px 2px'))
    if dhead=='head': data=df.head()
    elif dhead=='tail': data=df.tail()
    else: data=df
    display(data.style.set_properties(**style_dict)\
            .background_gradient(cmap=cmap)\
            .set_table_styles([dict(selector='th',
                                    props=head_styler)]));

def display_dataframe_example():
    index=[chr(i) for i in range(ord('a'),ord('h')+1)]
    columns=['&#x2654;','&#x2655;','&#x2656;',
             '&#x2657;','&#x2658;','&#x2659;']
    df=pd.DataFrame(np.random.randn(8,6),
                    index=index,columns=columns)
    cmap='bone'
    display_dataframe(df,cmap)