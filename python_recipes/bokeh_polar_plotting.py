import numpy as np; from bokeh.layouts import gridplot
from bokeh.plotting import figure,show,output_file
from IPython.display import display,HTML
t=np.linspace(0,2*np.pi,720); 
x=(np.cos(12*t)+np.cos(6*t))*np.cos(t)
y=(np.cos(12*t)+np.cos(6*t))*np.sin(t)
TOOLS='pan,wheel_zoom,box_zoom,reset,save,box_select'
lbl1=u'ϱ = cos 12 θ + cos 6 θ'; lbl2=u'2 ϱ'
p1=figure(title='PLotting Example 1',tools=TOOLS)
p1.circle(x,y,legend_label=lbl1,color='#3636ff')
p1.circle(2*x,2*y,legend_label=lbl2,color='#ff3636')
p1.legend.title='Polar Functions'
p2=figure(title='Plotting Example 2',tools=TOOLS)
p2.circle(x,y,legend_label=lbl1,color='#3636ff')
p2.line(x,y,legend_label=lbl1,color='#3636ff')
p2.square(2*x,2*y,legend_label=lbl2,
          fill_color=None,line_color='#ff3636')
p2.line(2*x,2*y,legend_label=lbl2,line_color='#ff3636')
output_file('bokeh.html',title='plotting examples')
show(gridplot([p1,p2],ncols=2,plot_width=300,plot_height=300))
display(HTML("""<div id='data'><iframe src='bokeh.html' 
height='350' width='650'></iframe></div>"""))
