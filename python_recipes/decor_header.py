import random; from IPython.display import display,HTML
from IPython.core.magic import register_line_magic
@register_line_magic
def decor_header(params):
    params=params.split('|'); string=params[0]
    if len(params)==1: 
        font_size='22'; font_family='Wallpoet'; cmap='Sinebow'
    elif  len(params)==2: 
        font_size=params[1]
        font_family='Wallpoet'; cmap='Sinebow'
    elif  len(params)==3: 
        font_size=params[1]; font_family=params[2]
        cmap='Sinebow'
    else: 
        font_size=params[1]; font_family=params[2]; cmap=params[3]
    height=int(font_size)*3; randi=str(random.uniform(0,9999999))
    html_str="""
<script src='https://d3js.org/d3.v6.min.js'></script>
<style>
@import 'https://fonts.googleapis.com/css?family="""+font_family+"""';
#colorized001 {
font-family:"""+font_family+"""; font-size:"""+font_size+""";}
#canvas001,#canvas002 {width:10%; vertical-align:middle;}
</style>
<text id='colorized001'><canvas id='canvas001'></canvas>
"""+string+"""
<canvas id='canvas002'></canvas></text><br/>
<script>
var tc=setInterval(function() {
    var now=new Date().getTime();
    var iddoc=document.getElementById('colorized001');
    iddoc.style.color=d3.interpolate"""+cmap+"""(now/6000);
    var r=10,n=7;
    var c1=document.getElementById('canvas001'); 
    var context1=c1.getContext('2d');
    var c2=document.getElementById('canvas002'); 
    var context2=c2.getContext('2d');
    c1.style.background=d3.interpolate"""+cmap+"""(now/60000); 
    c2.style.background=d3.interpolate"""+cmap+"""(now/60000);
    context1.strokeStyle=d3.interpolate"""+cmap+"""(now/6000);    
    context2.strokeStyle=d3.interpolate"""+cmap+"""(now/6000);
    for (var i=1; i<n; i++) {
        context1.beginPath(); context2.beginPath();
        for (var j=0; j<6; j++) {
            context1.arc(60*j,r*(n+.5),i*r,0,2*Math.PI);
            context2.arc(60*j,r*(n+.5),i*r,0,2*Math.PI); };
        context1.stroke(); context2.stroke(); }; },1)
</script>"""
    file='d3header'+randi+'.html'
    with open(file,'w') as f:
         f.write(html_str); f.close()
    string="""<div id='html_string"""+randi+\
    """' style='width:100%;'><iframe src='"""+file+\
    """' height="""+str(height)+"""
    style='display:block; width:100%;'></iframe></div>"""
    display(HTML(string))
