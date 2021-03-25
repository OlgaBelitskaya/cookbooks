from IPython.display import display,HTML
import random

f1,f2,f3,f4,f5,f6,f7,f8,f9=\
'Smokum','Akronim','Wallpoet','Orbitron','Ewert',\
'Lobster','Roboto','Miss Fajardose','Monoton'
fs1,fs2,fs3,fs4,fs5,fs6,fs7,fs8,fs9,fs10,fs11=\
10,12,14,16,18,20,22,24,26,28,30

def chtml(string,font_family=f2,font_size=fs9,font_color='#ff36ff'):
    css_str="""<style>@import """+\
    """'https://fonts.googleapis.com/css?family="""+font_family+"""'; 
    .ch1 {color:"""+font_color+"""; font-family:"""+font_family+"""; 
    font-size:"""+str(font_size)+"""px;}</style>"""
    h1_str="""<h1 class='ch1'>"""+string+"""</h1>"""
    display(HTML(css_str+h1_str))

def idhtml(string,font_family=f5,
           font_size=fs5,font_color='darkslategray'):
    randi=random.randint(1,999999999)
    css_str="""<style>@import """+\
    """'https://fonts.googleapis.com/css?family="""+font_family+"""'; 
    #ch1_"""+str(randi)+""" {font-family:"""+font_family+"""; 
    color:"""+font_color+"""; font-size:"""+str(font_size)+"""px;}</style>"""
    h1_str="""<h1 id='ch1_"""+str(randi)+"""'>"""+string+"""</h1>"""
    scr_str="""<script>
    var idc=setInterval(function() {
        var iddoc=document.getElementById('ch1_"""+str(randi)+"""'), 
            sec=Math.floor(new Date().getTime()%60000/1000); 
        var col='rgb('+(5+Math.abs(245-8*sec))+',0,'+
                (250-Math.abs(245-8*sec))+')';  
        iddoc.style.color=col;}, 1000);</script>"""
    display(HTML(css_str+h1_str+scr_str))
    
def whtml(string,background_color='black',padding=2,
          font_family='Akronim',font_size_px=int(28),
          deg=int(120),percent=[0,33,67,100],
          colors=['magenta','orange','cyan','purple']):
    randi=str(random.randint(1,999999999))
    css_str="""<style>@import 'https://fonts.googleapis.com/"""+\
    """css?family="""+font_family+"""';</style>"""
    html_str="""<div id='col_div"""+str(randi)+"""' 
    style='background:"""+background_color+"""; width:99%; 
    padding:"""+str(padding)+"""vw;'>
    <div style='background:linear-gradient("""+str(deg)+"""deg, 
    """+colors[0]+""" """+str(percent[0])+"""%,
    """+colors[1]+""" """+str(percent[1])+"""%,
    """+colors[2]+""" """+str(percent[2])+"""%,
    """+colors[3]+""" """+str(percent[3])+"""%); 
    font-family:"""+font_family+"""; font-size:"""+str(font_size_px)+"""px; 
    -webkit-background-clip:text; color:transparent;'>"""+string+"""
    </div></div>"""
    display(HTML(css_str+html_str))