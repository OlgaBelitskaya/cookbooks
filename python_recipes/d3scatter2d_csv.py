from IPython.core.display import display,HTML
import random

def d3scatter2d_csv(csv_url,x='x',y='y',marker_size=3,
                    background_color='silver',grid_color='black',
                    width=500,height=500):
    randi=random.randint(1,999999999)
    css_str="""<style>.grid1 line,.grid1 path,.xaxis1,.yaxis1 
    {stroke:"""+grid_color+"""; stroke-opacity:.5;}</style>"""
    html_str="""<script src='https://d3js.org/d3.v4.min.js'>
    </"""+"""script><svg id='svg"""+str(randi)+"""' 
    style='background-color:"""+background_color+"""'></svg><br/>"""
    scr_str="""<script>
    var url='"""+csv_url+"""'; 
    d3.csv(url,function(data) {
        var xmin=d3.min(data,function(d) {return parseFloat(d."""+x+""");}),
            xmax=d3.max(data,function(d) {return parseFloat(d."""+x+""");});
        var ymin=d3.min(data,function(d) {return parseFloat(d."""+y+""");}),
            ymax=d3.max(data,function(d) {return parseFloat(d."""+y+""");});
        var n=data.length,m=20,margin={top:m,right:m,bottom:m,left:m},
            width="""+str(width)+"""-margin.left-margin.right,
            height="""+str(height)+"""-margin.top-margin.bottom;
        var xScale=d3.scaleLinear()
                     .domain([1.1*xmin,1.1*xmax]).range([0,width]),
            yScale=d3.scaleLinear()
                     .domain([1.1*ymin,1.1*ymax]).range([height,0]); 
        function make_x_gridlines() {
            return d3.axisBottom(xScale).ticks(11)}; 
        function make_y_gridlines() { 
            return d3.axisLeft(yScale).ticks(11)};  
        var pointColor=d3.scaleSequential().domain([0,n]) 
                         .interpolator(d3.interpolateRainbow);  
        var tr1='translate('+margin.left+','+margin.top+')',
            tr2='translate(0,'+height+')';  
        var svg=d3.select('#svg"""+str(randi)+"""') 
                  .attr('width',width+margin.left+margin.right) 
                  .attr('height',height+margin.top+margin.bottom) 
                  .append('g').attr('transform',tr1);  
        svg.append('g').attr('class','xaxis1') 
           .call(d3.axisBottom(xScale).tickSize(.5)).attr('transform',tr2);  
        svg.append('g').attr('class','yaxis1') 
           .call(d3.axisLeft(yScale).tickSize(.5)); 
        svg.append('g').attr('class','grid1').attr('transform',tr2)
           .call(make_x_gridlines().tickSize(-height).tickFormat(''));
        svg.append('g').attr('class','grid1').call(make_y_gridlines()
           .tickSize(-width).tickFormat(''));
        svg.selectAll('.point').data(data).enter()
           .append('circle').attr('class','point')
           .attr('fill',function(d,i){return pointColor(i)})
           .attr('r',"""+str(marker_size)+""")
           .attr('stroke','#fff')
           .attr('stroke-width',"""+str(.1*marker_size)+""")
           .attr('cx',function(d) {return xScale(d."""+x+""")})
           .attr('cy',function(d) {return yScale(d."""+y+""")}); 
    });</script>"""
    display(HTML(css_str+html_str+scr_str))