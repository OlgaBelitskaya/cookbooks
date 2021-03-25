from IPython.core.display import display,HTML
import random

def d3barchart_list(num_list1,num_list2,background_color='silver',
                    width=600,height=400):
    num_list1,num_list2=str(num_list1),str(num_list2) 
    randi=random.randint(1,999999999)
    css_str="""<style>#run_update 
    {fill:slategray;stroke:#fff; fill-opacity:.7}</style>"""
    html_str="""<script src='https://d3js.org/d3.v6.min.js'>
    <"""+"""/script><svg id='svg"""+str(randi)+"""' 
    style='background-color:"""+background_color+""";'></svg><br/><br/>"""
    scr_str="""<script>
        var data="""+num_list1+""",m=20; 
        var n=data.length,ymax=1.2*d3.max(data),
            margin={top:m,right:m,bottom:m,left:m},
            width="""+str(width)+"""-margin.left-margin.right,
            height="""+str(height)+"""-margin.top-margin.bottom;
        var trans='translate('+margin.left+','+margin.top+')'; 
        var xScale=d3.scaleBand().domain(d3.range(n))
                     .rangeRound([0,width]).paddingInner(.1),
            yScale=d3.scaleLinear().domain([0,ymax]).range([0,height]);
        var svg=d3.select('#svg"""+str(randi)+"""')
                  .attr('width',width).attr('height',height)
                  .attr('transform',trans); 
        svg.selectAll('rect').data(data).enter().append('rect')
           .attr('x',function(d,i) {return xScale(i);})
           .attr('y',function(d) {return height-yScale(d);})
           .attr('width',xScale.bandwidth())
           .attr('height',function(d) {return yScale(d);})
           .attr('fill',function(d) { 
               return 'rgb('+Math.round(d*50/ymax)+',0,'+
                       Math.round(d*255/ymax)+')';}); 
        function newData() {
            var n=data.length; 
            while (data.length>0) {data.pop();}; 
            for (var i=0; i<n; i++) {data.push("""+num_list2+"""[i]);}; 
            return data}; 
        function updateBar() {
            svg.selectAll('rect').data(data).transition().duration(3000)
               .attr('y',function(d) {return height-yScale(d);})
               .attr('height',function(d) {return yScale(d);})
               .attr('fill',function(d) {
                   return 'rgb('+Math.round(d*50/ymax)+',0,'+
                          Math.round(d*255/ymax)+')';}); }; 
        svg.append('circle').attr('id','run_update')
           .attr('cx',m).attr('cy',1.25*m).attr('r',15)
           .on('click',function() {newData(); updateBar();}); 
        svg.append('text').text(' <<< UPDATE')
           .attr('x',2*m).attr('y',1.25*m).attr('fill','#fff');
    </script>"""
    display(HTML(css_str+html_str+scr_str))