from IPython.core.display import display,HTML

def d3scatter_csv(csv_url,background_color,width,height):
    html_str="""<script src='https://d3js.org/d3.v4.min.js'></script>"""+\
    """<svg id='svg0001' style='background-color:"""+background_color+\
    """'></svg><script>var url='"""+csv_url+"""';"""+\
    """d3.csv(url,function(data) {"""+\
    """var n=data.length,m=20,margin={top:m,right:m,bottom:m,left:m},"""+\
    """    width="""+str(width)+"""-margin.left-margin.right,"""+\
    """    height="""+str(height)+"""-margin.top-margin.bottom; """+\
    """var xScale=d3.scaleLinear().domain([-4,4]).range([0,width]); """+\
    """var yScale=d3.scaleLinear().domain([-6,6]).range([height,0]); """+\
    """function make_x_gridlines() {return d3.axisBottom(xScale).ticks(11)}; """+\
    """function make_y_gridlines() {return d3.axisLeft(yScale).ticks(11)}; """+\
    """var pointColor=d3.scaleSequential().domain([0,n])"""+\
    """                 .interpolator(d3.interpolateRainbow); """+\
    """var svg=d3.select('#svg0001')"""+\
    """          .attr('width',width+margin.left+margin.right)"""+\
    """          .attr('height',height+margin.top+margin.bottom)"""+\
    """          .append('g')"""+\
    """          .attr('transform','translate('+margin.left+','+margin.top+')');"""+\
    """svg.append('g').attr('class','xaxis1')"""+\
    """   .call(d3.axisBottom(xScale).tickSize(.5))"""+\
    """   .attr('transform','translate(0,'+height+')'); """+\
    """svg.append('g').attr('class','yaxis1')"""+\
    """   .call(d3.axisLeft(yScale).tickSize(.5)); """+\
    """svg.append('g').attr('class','grid1')"""+\
    """   .attr('transform','translate(0,'+height+')')"""+\
    """   .call(make_x_gridlines().tickSize(-height).tickFormat('')); """+\
    """svg.append('g').attr('class','grid1').call(make_y_gridlines()"""+\
    """   .tickSize(-width).tickFormat(''));"""+\
    """svg.selectAll('.point').data(data).enter()"""+\
    """   .append('circle').attr('class','point')"""+\
    """   .attr('fill',function(d,i){return pointColor(i)}).attr('r',2)"""+\
    """   .attr('stroke','#ffffff').attr('stroke-width','.3')"""+\
    """   .attr('cx',function(d) {return xScale(d.x)})"""+\
    """   .attr('cy',function(d) {return yScale(d.y)}); });"""+\
    """</script>"""
    file='d3scatter_csv.html'
    string="""<div id='html_string'><iframe src='"""+\
           file+"""' height="""+str(height+20)+\
           """ width="""+str(width+20)+"""></iframe></div>"""
    display(HTML(string))