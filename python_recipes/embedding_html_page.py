from IPython.display import display,HTML
def embedding_html_page(html_url):
	display(HTML("""
    <div style="border:10px double white; 
         width:550px; height:950px; overflow:auto; 
         padding:5px; background-color:ghostwhite">
    <iframe src='"""\
    +html_url\
    +"""' width="520" height="920"/></div>"""))