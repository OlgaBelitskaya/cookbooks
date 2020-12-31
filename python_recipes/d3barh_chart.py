from IPython.display import display,HTML
import random

def d3barh_chart(data,chart_title,width,height,
                 color='silver',cmap='Sinebow',
                 font_size=24,font_family='Wallpoet'):
    html_str="""
<style>
@import 'https://fonts.googleapis.com/css?family="""+\
font_family+"""';
#d3barchart_title {color:"""+color+"""; font-family:"""+\
font_family+"""; font-size:"""+str(font_size)+"""px;}
#d3barchart {width:98%; height:95%;}
</style>
<script src='https://d3js.org/d3.v6.min.js'></script>
<div id='d3barchart'><text id='d3barchart_title'></text></div>
<script>
var data="""+str(data)+""";
var tc=setInterval(function(){
    var now=new Date().getTime();
    var width=Math.min(window.screen.width,window.innerWidth);
    var div=d3.select('#d3barchart');
    div.select('#d3barchart_title')
       .text('"""+chart_title+"""');
    div.style('text-align','right')
       .style('text-shadow','3px 3px 3px slategray')
       .style('padding','5px')
       .style('color',d3.interpolate"""+cmap+"""(now/1000000))
       .style('background',d3.interpolate"""+cmap+"""(now/1000000));
    var x=d3.scaleLinear().domain([0,d3.max(data)]).range([0,.9*width])
    div.selectAll('div').data(data).join('div')
       .style('background','"""+color+"""')
       .style('padding','5px').style('margin','3px')
       .style('width',d=>x(d)+'px')
       .style('font-family','"""+font_family+"""')
       .style('font-size','"""+str(font_size)+"""px')
       .text(d=>d);},100);
</script>"""
    file='d3barh_chart'+str(random.uniform(0,9999999))+'.html'
    with open(file,'w') as f:
         f.write(html_str); f.close()
    string="""<div id='html_string2'><iframe src='"""+\
           file+"""' height="""+str(height)+\
           """ width="""+str(width)+"""></iframe></div>"""
    display(HTML(string))
