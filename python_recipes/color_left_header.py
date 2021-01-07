from IPython.display import display,HTML
from IPython.core.magic import register_line_magic
import random

@register_line_magic
def left_header(params):
    params=params.split('|'); string=params[0]
    if len(params)==1: font_size=24; font_family='Ewert'
    elif  len(params)==2: font_size=int(params[1]); font_family='Ewert' 
    else: font_size=int(params[1]); font_family=params[2]
    width=650; height=font_size*2.5
    randi=str(random.uniform(0,9999999))
    html_str="""
    <head><script src='https://d3js.org/d3.v6.min.js'></script>
    </head><style>@import 'https://fonts.googleapis.com/css?family="""+\
    font_family+"""&effect=3d'; #colorized1 {font-family:"""+font_family+\
    """; color:white; padding-left:10px; font-size:"""+str(font_size)+\
    """px;}</style><h1 id='colorized1' class='font-effect-3d'>"""+string+\
    """</h1><script>
    var tc=setInterval(function(){
        var now=new Date().getTime();
        var iddoc1=document.getElementById('colorized1');
        iddoc1.style.color=d3.interpolateRainbow(now/20000); },1)
    </script>"""
    file='d3header'+randi+'.html'
    with open(file,'w') as f:
         f.write(html_str); f.close()
    string="""<div id='html_string"""+randi+\
    """'><iframe src='"""+file+\
    """' height="""+str(height)+""" width="""+str(width)+\
    """ style='display:block;'></iframe></div>"""
    display(HTML(string))
