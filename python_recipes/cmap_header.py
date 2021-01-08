from IPython.display import display,HTML
from IPython.core.magic import register_line_magic
import random
#Sequential (Single-Hue,Multi-Hue),Diverging, Cyclical cmaps: 
#Reds,Sinebow,Rainbow,Turbo,Warm,Cool,Plasma,Spectral,etc.
@register_line_magic
def cmap_header(params):
    params=params.split('|'); string=params[0]
    if len(params)==1: 
        font_size='30'; font_family='Akronim'; cmap='Sinebow'
    elif  len(params)==2: 
        font_size=params[1]
        font_family='Akronim'; cmap='Sinebow'
    elif  len(params)==3: 
        font_size=params[1]; font_family=params[2]
        cmap='Sinebow'
    else: 
        font_size=params[1]; font_family=params[2]; cmap=params[3]
    height=int(font_size)*2.5; randi=str(random.uniform(0,9999999))
    html_str="""
    <head><script src='https://d3js.org/d3.v6.min.js'></script>
    </head><style>@import 'https://fonts.googleapis.com/css?family="""+\
    font_family+"""&effect=3d'; #colorized {font-family:"""+font_family+\
    """; color:white; padding-left:10px; font-size:"""+font_size+\
    """px;}</style><h1 id='colorized' class='font-effect-3d'>"""+\
    string+"""</h1><script>
    var tc=setInterval(function(){
        var now=new Date().getTime();
        var iddoc=document.getElementById('colorized');
        iddoc.style.color=d3.interpolate"""+cmap+\
    """(now%(30000)/30000);},1)</script>"""
    file='d3header'+randi+'.html'
    with open(file,'w') as f:
         f.write(html_str); f.close()
    string="""<div id='html_string"""+randi+\
    """' style='width:100%;'><iframe src='"""+file+\
    """' height="""+str(height)+"""
    style='display:block; width:100%;'></iframe></div>"""
    display(HTML(string))
