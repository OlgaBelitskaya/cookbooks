from IPython.core.display import display,HTML
from IPython.core.magic import register_line_magic

@register_line_magic
def sage_run(code_string):
    start_string=\
    """<html><head><meta charset='utf-8'>"""+\
    """<meta name='viewport' content='width=device-width'>"""+\
    """<script src='https://sagecell.sagemath.org/static/"""+\
    """embedded_sagecell.js'></script><script>"""+\
    """$(function () {sagecell.makeSagecell({"""+\
    """inputLocation:'div.sage',evalButtonText:'run',"""+\
    """template:sagecell.templates.minimal,autoeval:true});});"""+\
    """</script></head><style>.sagecell_output pre{"""+\
    """min-height:3em; max-height:30em;} """+\
    """.sagecell .CodeMirror-scroll {"""+\
    """min-height:3em; max-height:30em;}</style><body>"""+\
    """<div class='sage'><script type='text/x-sage'>"""
    split_code_string=code_string.split('  ')
    code_string=""""""
    for el in split_code_string:
        if el!='':
            if el[-1]!=',':
                code_string+=el+"""; """ 
            else:
                code_string+=el
    end_string="""</script></div></body></html>"""
    display(HTML(start_string+code_string+end_string))
    
print("Evaluation of SageMath cells is possible "+\
      "with two additional syntax marks: ")
print("the white space and the slash between code lines.")