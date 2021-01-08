import random; from IPython.display import display,HTML
from IPython.core.magic import register_line_magic
@register_line_magic
def radial_gradient_header(params):
    randi=str(random.randint(1,9999999))
    params=params.split('|'); string=params[0]
    if len(params)==1: 
        font_size=str(30); font_family='Ewert'
    elif len(params)==2: 
        font_size=params[1]; font_family='Ewert'
    else:
        font_size=params[1]; font_family=params[2]
    html_str="""<style>@import 'https://fonts.googleapis.com/css?"""+\
    """family="""+font_family+"""'; #div"""+randi+\
    """ {background:white; padding:2px;}
    .textrg {display:inline-block; font-size:"""+font_size+\
    """px; line-height:1.1; padding:5px; font-family:"""+font_family+\
    """,sans-serif; text-transform:uppercase;
       background:radial-gradient(
           circle farthest-corner at center center,
           orange,magenta,cyan) no-repeat;
       -webkit-background-clip:text;
       -webkit-text-fill-color:transparent;}</style>
    <div id='div"""+randi+"""'><text class='textrg'>"""+string+\
    """</text></div>"""
    display(HTML(html_str))
