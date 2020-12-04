from IPython.display import display,HTML
import random 

f1,f2,f3,f4,f5,f6,f7,f8,f9=\
'Smokum','Akronim','Wallpoet','Orbitron','Ewert',\
'Lobster','Roboto','Miss Fajardose','Monoton'
fs1,fs2,fs3,fs4,fs5,fs6,fs7,fs8,fs9,fs10,fs11=\
10,12,14,16,18,20,22,24,26,28,30

def chtml(string,fontcolor='#ff36ff',font=f2,fontsize=fs9):
    style_str="""<style>@import """+\
    """'https://fonts.googleapis.com/css?family="""+font+\
    """'; .colored_font {color:"""+fontcolor+\
    """; font-family:"""+font+\
    """; font-size:"""+str(fontsize)+"""px;}</style>"""
    h_str="""<h1 class='colored_font'>"""+string+"""</h1>"""
    display(HTML(style_str+h_str))
    
def idhtml(string,fontcolor='darkslategray',font=f5,fontsize=fs5):
    randi=random.randint(1,999999999)
    style_str="""<style>@import """+\
    """'https://fonts.googleapis.com/css?family="""+font+\
    """'; #colored_font"""+str(randi)+\
    """ {color:"""+fontcolor+\
    """; font-family:"""+font+\
    """; font-size:"""+str(fontsize)+"""px;}</style>"""
    h_str="""<h1 id='colored_font"""+str(randi)+\
    """'>"""+string+"""</h1>"""
    script_str="""<script>"""+\
    """var idc=setInterval(function() {"""+\
    """var iddoc=document.getElementById("""+\
    """'colored_font"""+str(randi)+"""'); """+\
    """var now=new Date().getTime(); """+\
    """var sec=Math.floor((now%(1000*60))/1000); """+\
    """var col='rgb('+(5+Math.abs(245-8*sec))+',0,'"""+\
    """+(250-Math.abs(245-8*sec))+')'; """+\
    """iddoc.style.color=col;},1000);</"""+"""script>"""
    display(HTML(style_str+h_str+script_str))

def whtml(string,background_color='black',padding=2,
          font_family='Akronim',font_size_px=int(28),
          deg=int(120),percent=[0,33,67,100],
          colors=['magenta','orange','cyan','purple']):
    randi=random.randint(1,999999999)
    html_str="""<style>@import """+\
    """'https://fonts.googleapis.com/css?family="""+\
    font_family+"""';</style>"""+\
    """<div id='colorized_div' """+str(randi)+\
    """ style='background:"""+background_color+\
    """; padding:"""+str(padding)+"""vw;'>"""+\
    """<div style='background:linear-gradient("""+\
    str(deg)+"""deg, """+\
    colors[0]+""" """+str(percent[0])+"""%,"""+\
    colors[1]+""" """+str(percent[1])+"""%,"""+\
    colors[2]+""" """+str(percent[2])+"""%,"""+\
    colors[3]+""" """+str(percent[3])+"""%"""+\
    """); font-family:"""+font_family+"""; """+\
    """font-size:"""+str(font_size_px)+"""px; """+\
    """-webkit-background-clip:text; color:transparent;'> """+\
    string+"""</div></div>"""   
    display(HTML(html_str))
