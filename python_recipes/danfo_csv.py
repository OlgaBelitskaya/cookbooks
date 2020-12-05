from IPython.core.display import display,HTML

def danfo_table_csv(url,columns,header_font_size):
    html_str="""<html><head><meta charset='UTF-8'>"""+\
    """<meta name='viewport' """+\
    """content='width=device-width,initial-scale=1.0'>"""+\
    """<script src='https://cdn.jsdelivr.net/npm/"""+\
    """danfojs@0.1.1/dist/index.min.js'></script></head>"""+\
    """<div><p>&nbsp; CSV =>>> Danfo DataFrames</p>"""+\
    """<div id='div015_1'></div><script>"""+\
    """var url='"""+url+"""';"""+\
    """dfd.read_csv(url)"""+\
    """   .then(df=>{df.loc({columns:"""+str(columns)+\
    """}).plot('div015_1').table({header_style:"""+\
    """{font:{size:"""+str(header_font_size)+"""}}})})"""+\
    """   .catch(err=>{console.log(err);})"""+\
    """</script></div></html>"""
    display(HTML(html_str))
    
def danfo_chart_csv(url,columns):
    html_str="""<html><head><meta charset='UTF-8'>"""+\
    """<meta name='viewport' """+\
    """content='width=device-width,initial-scale=1.0'>"""+\
    """<script src='https://cdn.jsdelivr.net/npm/"""+\
    """danfojs@0.1.1/dist/index.min.js'> </script></head>"""+\
    """<body><p>&nbsp; CSV =>>> Danfo DataFrames</p>"""+\
    """<div id='div015_2'></div><script>"""+\
    """var url='"""+url+"""';"""+\
    """dfd.read_csv(url)"""+\
    """   .then(df=>{df.plot('div015_2').line("""+\
    """   {columns:"""+str(columns)+"""})})"""+\
    """   .catch(err=>{console.log(err);})"""+\
    """</script></body></html>"""
    display(HTML(html_str))