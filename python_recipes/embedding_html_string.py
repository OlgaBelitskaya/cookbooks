from IPython.display import display,HTML
def embedding_html_string(html_str,width,height,num):
    html_file=open("file"+str(num)+".html","w")
    html_file.write(html_str)
    html_file.close()
    string='''<div id="html_string'''+str(num)+'''">'''\
           +'''<iframe src="file'''+str(num)+'''.html"'''\
           +''' height='''+str(height)\
           +''' width='''+str(width)\
           +'''></iframe></div>'''
    display(HTML(string))