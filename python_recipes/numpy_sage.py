from IPython.core.display import display,HTML
import random,numpy as np

def sage_list_plot(array,width,height):
    str_array=np.array2string(
        array,precision=8,separator=',',
        suppress_small=True)
    html_str="""<html><head><meta charset='utf-8'>"""+\
    """<script src='https://sagecell.sagemath.org/"""+\
    """static/embedded_sagecell.js'>"""+\
    """</script><script>$(function(){"""+\
    """sagecell.makeSagecell({inputLocation:'#cell0001',"""+\
    """evalButtonText:'run'}); });</script></head>"""+\
    """<style>.sagecell .CodeMirror-scroll {width:99%;"""+\
    """min-height:3em; max-height:11em;}</style>"""+\
    """<body><div id='cell0001'><script type='text/x-sage'>"""+\
    """array="""+str_array+"""\n"""+\
    """n=len(array)\n"""+\
    """p=sum([list_plot(array[i],color=hue(i/n))\n"""+\
    """       for i in range(n)])\n"""+\
    """p.show(figsize=(4.7,3),axes=False,frame=True)"""+\
    """</script></div></body></html>"""
    file='sage_coderun'+str(random.uniform(0,9999999))+'.html'
    with open(file,'w') as f:
        f.write(html_str); f.close()
    string="""<div id='html_string'><iframe src='"""+\
           file+"""' height="""+str(height+20)+\
           """ width="""+str(width+20)+"""></iframe></div>"""
    display(HTML(string))