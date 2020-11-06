from IPython.core.display import display,HTML
from IPython.core.magic import register_line_magic

@register_line_magic
def sage_autorun(code_string):
    start_string=\
    """<html><head><meta charset='utf-8'>"""+\
    """<meta name='viewport' content='width=device-width'>"""+\
    """<script src='https://sagecell.sagemath.org/static/"""+\
    """embedded_sagecell.js'></script><script>"""+\
    """$(function () {sagecell.makeSagecell({"""+\
    """inputLocation:'div.autosage',evalButtonText:'run',"""+\
    """template:sagecell.templates.minimal,autoeval:true});});"""+\
    """</script></head><style>.sagecell_output pre{"""+\
    """min-height:3em; max-height:30em;} """+\
    """.sagecell .CodeMirror-scroll {"""+\
    """min-height:3em; max-height:30em;}</style><body>"""+\
    """<div class='autosage'><script type='text/x-sage'>"""
    split_code_string=code_string.split('  ')
    code_string=""""""; c=0
    for el in split_code_string:
        if el!='':
            code_string+=c*'  '+el+'\n'; c=0
        else: c+=1
    end_string="""</script></div></body></html>"""
    display(HTML(start_string+code_string+end_string))
    
@register_line_magic
def sage_run(code_string):
    start_string=\
    """<html><head><meta charset='utf-8'>"""+\
    """<meta name='viewport' content='width=device-width'>"""+\
    """<script src='https://sagecell.sagemath.org/static/"""+\
    """embedded_sagecell.js'></script><script>"""+\
    """$(function () {sagecell.makeSagecell({"""+\
    """inputLocation:'div.sage',evalButtonText:'run',"""+\
    """template:sagecell.templates.minimal});});"""+\
    """</script></head><style>.sagecell_output pre{"""+\
    """min-height:3em; max-height:30em;} """+\
    """.sagecell .CodeMirror-scroll {"""+\
    """min-height:3em; max-height:30em;}</style><body>"""+\
    """<div class='sage'><script type='text/x-sage'>"""
    split_code_string=code_string.split('  ')
    code_string=""""""; c=0
    for el in split_code_string:
        if el!='':
            code_string+=c*'  '+el+'\n'; c=0
        else: c+=1
    end_string="""</script></div></body></html>"""
    display(HTML(start_string+code_string+end_string))

@register_line_magic
def sage_coderun(params):
    [width,height]=[int(el) for el in params.split()]
    html_str="""<html><head><meta charset='utf-8'>"""+\
    """<script src='https://sagecell.sagemath.org/static/embedded_sagecell.js'>"""+\
    """</script><script>$(function(){"""+\
    """sagecell.makeSagecell({inputLocation:'#cell0001',"""+\
    """evalButtonText:'run'}); });"""+\
    """</script></head><style>.sagecell_output pre{"""+\
    """min-height:3em; max-height:25em;} """+\
    """.sagecell .CodeMirror-scroll {"""+\
    """min-height:3em; max-height:25em;}</style>"""+\
    """<body><div id='cell0001'><script type='text/x-sage'>"""+\
    """print('These code lines are editable.')"""+\
    """print('You can change them right here and run.')"""+\
    """</script></div></body></html>"""
    file='sage_coderun'+str(random.uniform(0,9999999))+'.html'
    with open(file,'w') as f:
        f.write(html_str); f.close()
    string="""<div id='html_string'><iframe src='"""+\
           file+"""' height="""+str(height+20)+\
           """ width="""+str(width+20)+"""></iframe></div>"""
    display(HTML(string))
    
print('Evaluation of SageMath cells is possible ')
print('now with two additional syntax marks: ')
print('the white space and the slash between code lines.')