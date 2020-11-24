from IPython.core.display import display,HTML

def danfo_table_csv(url):
    html_str="""<html><head><meta charset='UTF-8'>"""+\
    """<meta name='viewport' """+\
    """content='width=device-width,initial-scale=1.0'>"""+\
    """<script src='https://cdn.jsdelivr.net/npm/"""+\
    """danfojs@0.1.1/dist/index.min.js'> </script></head>"""+\
    """<body><h1>CSV =>>> Danfo DataFrames</h1>"""+\
    """<div id='div015_1'></div><script>"""+\
    """var url='"""+url+"""';"""+\
    """dfd.read_csv(url)"""+\
    """   .then(df=>{df.plot('div015_1').table()})"""+\
    """   .catch(err=>{console.log(err);})"""+\
    """</script></body></html>"""
    display(HTML(html_str))
    
def danfo_chart_csv(url,columns):
    html_str="""<html><head><meta charset='UTF-8'>"""+\
    """<meta name='viewport' """+\
    """content='width=device-width,initial-scale=1.0'>"""+\
    """<script src='https://cdn.jsdelivr.net/npm/"""+\
    """danfojs@0.1.1/dist/index.min.js'> </script></head>"""+\
    """<body><h1>CSV =>>> Danfo DataFrames</h1>"""+\
    """<div id='div015_2'></div><script>"""+\
    """var url='"""+url+"""';"""+\
    """dfd.read_csv(url)"""+\
    """   .then(df=>{df.plot('div015_2').line("""+\
    """   {columns:"""+str(columns)+"""})})"""+\
    """   .catch(err=>{console.log(err);})"""+\
    """</script></body></html>"""
    display(HTML(html_str))