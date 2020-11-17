from IPython.core.display import display,HTML
import random

def d3barchart_list(num_list,
                    background_color='silver',
                    width=600,height=400):
    num_list=str(num_list)
    html_str="""<style>#circle_bar {fill:#3636ff; """+\
    """stroke:#fff; fill-opacity:.7}</style>"""+\
    """<script src='https://d3js.org/d3.v6.min.js'></script>"""+\
    """<svg id='svg0001' style='background-color:"""+\
    background_color+""";'></svg><script>"""+\
    """var data="""+num_list+""",m=20; """\
    """var n=data.length,ymax=1.2*d3.max(data),"""+\
    """    margin={top:m,right:m,bottom:m,left:m},"""+\
    """    width="""+str(width)+\
    """-margin.left-margin.right,"""+\
    """    height="""+str(height)+\
    """-margin.top-margin.bottom; """+\
    """var trans='translate('+margin.left+','+margin.top+')'; """+\
    """var xScale=d3.scaleBand().domain(d3.range(n))"""+\
    """             .rangeRound([0,width]).paddingInner(.1),"""+\
    """    yScale=d3.scaleLinear().domain([0,ymax])"""+\
    """             .range([0,height]); """+\
    """var svg=d3.select('#svg0001')"""+\
    """          .attr('width',width).attr('height',height)"""+\
    """          .attr('transform',trans); """+\
    """svg.selectAll('rect').data(data).enter().append('rect')"""+\
    """   .attr('x',function(d,i) {return xScale(i);})"""+\
    """   .attr('y',function(d) {return height-yScale(d);})"""+\
    """   .attr('width',xScale.bandwidth())"""+\
    """   .attr('height',function(d) {return yScale(d);})"""+\
    """   .attr('fill',function(d) { """+\
    """       return 'rgb('+Math.round(d)+',0,'+"""+\
    """              Math.round(d*255/ymax)+')';}); """+\
    """function newData() {"""+\
    """    while (data.length>0) {data.pop();}; """+\
    """    for (var i=0; i<30; i++) {"""+\
    """        data.push(Math.floor(Math.random()*30)+1);}; """+\
    """    return data}; """+\
    """function updateBar() {"""+\
    """    svg.selectAll('rect').data(data)"""+\
    """       .transition().duration(3000)"""+\
    """       .attr('y',function(d) {return height-yScale(d);})"""+\
    """       .attr('height', function(d) {return yScale(d);})"""+\
    """       .attr('fill',function(d) {"""+\
    """           return 'rgb('+Math.round(d)+',0,'+"""+\
    """                Math.round(d*255/ymax)+')';}); }; """+\
    """svg.append('circle').attr('id','circle_bar')"""+\
    """   .attr('cx',m).attr('cy',m).attr('r',15)"""+\
    """   .on('click',function() {newData(); updateBar();}); """+\
    """svg.append('text').text('<<< UPDATE')"""+\
    """   .attr('x',2*m).attr('y',1.25*m).attr('fill','#fff');"""+\
    """</script>"""
    file='d3barchart_list'+str(random.uniform(0,9999999))+'.html'
    with open(file,'w') as f:
        f.write(html_str); f.close()
    string="""<div id='html_string'><iframe src='"""+\
           file+"""' height="""+str(height+20)+\
           """ width="""+str(width+20)+"""></iframe></div>"""
    display(HTML(string))