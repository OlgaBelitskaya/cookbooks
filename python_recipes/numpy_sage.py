from IPython.core.display import display,HTML
import random,numpy as np

def sage_list_plot(array,labels=None,precision=8,
                   width=650,height=700,
                   kw=.0095,kh=0.0035):
    str_array=np.array2string(
        array,precision=precision,separator=',',
        suppress_small=True)
    if labels==None: 
        labels=[i+1 for i in range(len(array))]
    html_str="""<html><head><meta charset='utf-8'>"""+\
    """<script src='https://sagecell.sagemath.org/"""+\
    """static/embedded_sagecell.js'>"""+\
    """</script><script>$(function() {"""+\
    """sagecell.makeSagecell({inputLocation:'div.plot',"""+\
    """evalButtonText:'run',linked:true}); """+\
    """});</script></head>"""+\
    """<style>#array1.sagecell .CodeMirror-scroll {"""+\
    """min-height:3em; max-height:5em;} """+\
    """.sagecell .CodeMirror-scroll {"""+\
    """min-height:3em; max-height:11em;}</style><body>"""+\
    """<div class='plot' id='array1'><script type='text/x-sage'>"""+\
    """import numpy as np\n"""+\
    """array=np.array("""+str_array+""")\n"""+\
    """labels="""+str(labels)+"""\n"""+\
    """</script></div><br/>"""+\
    """<div class='plot'><script type='text/x-sage'>"""+\
    """print('array dimensions:%s'%str(array.shape))\n"""+\
    """n=array.shape[0]\n"""+\
    """p=sum([list_plot(\n"""+\
    """    array[i],plotjoined=True,\n"""+\
    """    color=hue(i/n),marker='o',markersize=2,\n"""+\
    """    legend_label=labels[i])\n"""+\
    """       for i in range(n)])\n"""+\
    """p.show(figsize=("""+str(
        (np.round(kw*width,2),np.round(kh*height,2)))+\
    """),axes=False,\n"""+\
    """       frame=True,gridlines=True)"""+\
    """</script></div></body></html>"""
    file='sage_coderun'+str(random.uniform(0,9999999))+'.html'
    with open(file,'w') as f:
        f.write(html_str); f.close()
    string="""<div id='html_string1'><iframe src='"""+\
           file+"""' height="""+str(height+20)+\
           """ width="""+str(width+20)+"""></iframe></div>"""
    display(HTML(string))
    
def sage_list_plot_min(array,labels=None,precision=8,
                       width=650,height=450,
                       kw=.0095,kh=.0075):
    str_array=np.array2string(
        array,precision=precision,separator=',',
        suppress_small=True)
    if labels==None: 
        labels=[i+1 for i in range(len(array))]
    html_str="""<html><head><meta charset='utf-8'>"""+\
    """<script src='https://sagecell.sagemath.org/"""+\
    """static/embedded_sagecell.js'>"""+\
    """</script><script>$(function() {"""+\
    """sagecell.makeSagecell({inputLocation:'div.plot_min',"""+\
    """evalButtonText:'run',autoeval:true,"""+\
    """template:sagecell.templates.minimal}); """+\
    """});</script></head><body>"""+\
    """<div class='plot_min'><script type='text/x-sage'>"""+\
    """import numpy as np\n"""+\
    """array=np.array("""+str_array+""")\n"""+\
    """labels="""+str(labels)+"""\n"""+\
    """print('array dimensions:%s'%str(array.shape))\n"""+\
    """n=array.shape[0]\n"""+\
    """p=sum([list_plot(\n"""+\
    """    array[i],plotjoined=True,\n"""+\
    """    color=hue(i/n),marker='o',markersize=2,\n"""+\
    """    legend_label=labels[i])\n"""+\
    """       for i in range(n)])\n"""+\
    """p.show(figsize=("""+str(
        (np.round(kw*width,2),np.round(kh*height,2)))+\
    """),axes=False,\n"""+\
    """       frame=True,gridlines=True)"""+\
    """</script></div></body></html>"""
    file='sage_coderun'+str(random.uniform(0,9999999))+'.html'
    with open(file,'w') as f:
        f.write(html_str); f.close()
    string="""<div id='html_string2'><iframe src='"""+\
           file+"""' height="""+str(height+20)+\
           """ width="""+str(width+20)+"""></iframe></div>"""
    display(HTML(string))