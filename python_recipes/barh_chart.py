from IPython.display import display,HTML

def barh_chart(data,chart_title,width,
               font_size=16,
               font_family='Wallpoet',
               background_color='#ff355e'):
    dmax=max(data)
    html_str="""<style>
    @import 'https://fonts.googleapis.com/css?family="""+\
    font_family+\
    """'; .div_params {padding:5px; width:"""+\
    str(round(width/100*dmax))+\
    """px; text-align:right; text-shadow:4px 4px 4px slategray; 
    color:lightgray; font-size:"""+\
    str(font_size)+\
    """px; font-family:"""+\
    font_family+\
    """; background:linear-gradient(180deg,lightgray 0%,silver 33%,
    slategray 67%, darkslategray 100%);}
    .div_params_in {background:"""+\
    background_color+\
    """; padding:5px; margin:3px;}
    #div_h2 {text-shadow:4px 4px 4px slategray; color:"""+\
    background_color+"""; font-family:"""+font_family+\
    """;}</style>
    <div class='div_params'><h2 id='div_h2'>"""+\
    chart_title+"""</h2>"""
    for i in range(len(data)):
        html_str+="""<div class='div_params_in' style='width:"""+\
                  str(.9*width/100*data[i])+"""px;'>"""+\
                  str(data[i])+"""</div>"""
    html_str+="""</div><br/>"""
    display(HTML(html_str))
