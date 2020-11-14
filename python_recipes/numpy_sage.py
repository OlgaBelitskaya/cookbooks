from IPython.core.display import display,HTML
import random,numpy as np

def sage_list_plot(array,width,height):
    str_array=np.array2string(
        array,precision=8,separator=',',
        suppress_small=True)
    html_str="""<html><head><meta charset='utf-8'>"""+\
    """<script src='https://sagecell.sagemath.org/"""+\
    """static/embedded_sagecell.js'>"""+\
    """</script><script>$(function() {"""+\
    """sagecell.makeSagecell({inputLocation:'div.plot',"""+\
    """evalButtonText:'run',linked:true}); """+\
    """});</script></head>"""+\
    """<style>#array1.sagecell .CodeMirror-scroll {"""+\
    """min-height:3em; max-height:3em;} """+\
    """.sagecell .CodeMirror-scroll {"""+\
    """min-height:3em; max-height:10em;}</style><body>"""+\
    """<div class='plot' id='array1'><script type='text/x-sage'>"""+\
    """import numpy as np\n"""+\
    """array=np.array("""+str_array+""")\n"""+\
    """</script></div><br/>"""+\
    """<div class='plot'><script type='text/x-sage'>"""+\
    """print('array dimensions:%s'%str(array.shape))\n"""+\
    """n=array.shape[0]\n"""+\
    """p=sum([list_plot(\n"""+\
    """    array[i],color=hue(i/n),plotjoined=True,\n"""+\
    """    marker='o',markersize=2,legend_label=i+1)\n"""+\
    """       for i in range(n)])\n"""+\
    """p.show(figsize=(4.7,3),axes=False,\n"""+\
    """       frame=True,gridlines=True)"""+\
    """</script></div></body></html>"""
    file='sage_coderun'+str(random.uniform(0,9999999))+'.html'
    with open(file,'w') as f:
        f.write(html_str); f.close()
    string="""<div id='html_string'><iframe src='"""+\
           file+"""' height="""+str(height+20)+\
           """ width="""+str(width+20)+"""></iframe></div>"""
    display(HTML(string))