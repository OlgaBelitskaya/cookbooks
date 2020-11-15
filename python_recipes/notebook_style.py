from IPython.core.display import display,HTML

def notebook_style(span_h_font='Ewert',
                   span_h_color='#ff3636',
                   prompt_font='Ewert',
                   prompt_in_color='#ff3636',
                   prompt_out_color='#3636ff',
                   warn_font='Roboto',
                   warn_color='#ff36ff',
                   out_font='Roboto',
                   out_color='#3636ff',
                   background_out_color='whitesmoke',
                   span_text_shadow=True):
    style_str="""<style>"""+\
    """@import 'https://fonts.googleapis.com/css?family="""+\
    prompt_font+"""|"""+out_font+"""|"""+warn_font+"""'; """
    if span_text_shadow==True:
        style_str+="""span {color:black; """+\
                   """text-shadow:4px 4px 4px #aaa;}"""
    style_str+="""div.alert {text-shadow:4px 4px 4px #aaa;}"""
    style_str+="""span.h1,span.h2,span.h3,"""+\
               """span.h4,span.h5,span.h6 """+\
               """{color:"""+span_h_color+"""; """+\
               """font-family:"""+span_h_font+""";} """
    style_str+="""div.warn {background-color:"""+\
               background_out_color+"""; color:"""+\
               warn_color+"""; font-size:110%; """+\
               """font-family:"""+warn_font+""";} """
    for el in ["""div.output_area pre""",
               """div.output_stderr pre"""
               """div.output_subarea""",
               """div.output_html""",
               """div.output_stderr"""]:
        style_str+=el+"""{background-color:"""+\
                   background_out_color+"""; color:"""+\
                   out_color+"""; font-size:110%; """+\
                   """font-family:"""+out_font+""";} """
    style_str+="""div.input_prompt {color:"""+\
               prompt_in_color+"""; """+\
               """font-family:"""+prompt_font+""";} """
    style_str+="""div.output_prompt {color:"""+\
               prompt_out_color+"""; """+\
               """font-family:"""+prompt_font+""";} """
    style_str+=""".cm-s-ipython span.cm-comment {color:darkslategray;} """
    style_str+=""".cm-s-ipython span.cm-def {color:#3636ff;} """
    style_str+=""".cm-s-ipython span.cm-operator {color:#ff36ff;} """
    style_str+=""".cm-s-ipython span.cm-keyword {color:darkgreen;} """
    style_str+=""".cm-s-ipython span.cm-string {color:#ff3636;} """
    style_str+="""</style>"""
    display(HTML(style_str))