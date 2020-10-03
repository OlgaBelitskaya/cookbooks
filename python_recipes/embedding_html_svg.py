from IPython.display import display,HTML
def embedding_html_svg(file_name,width,height): 
    string='<figure><embed type="image/svg+xml" '+\
           'src="'+file_name+\
           '" width='+str(width)+\
           ' height='+str(height)+\
           '/></figure>'
    display(HTML(string))