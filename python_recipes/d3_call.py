import inspect,os,numpy as np
from string import Template

def get_dir():
    get_file=inspect.getfile(inspect.currentframe())
    return os.path.dirname(os.path.abspath(get_file))

def get_styles(css_file_names):
    if type(css_file_names)==str:
        style=open(get_dir()+'/css/'+\
        	       css_file_names+'.css','r').read()
    else:
        style=''
        for css_file_name in css_file_names:
            style+=open(get_dir()+'/css/'+\
            	        css_file_name+'.css','r').read()
    return '<style>'+style+'</style>'

def get_graph(type,data_dict):
    js_code=Template('''<div id='maindiv${div_num}'></div>
    	                <script>$main_code</script>''')
    div_num=np.random.randint(0,9999999999)
    data_dict['divnum']=div_num
    code_template=Template(open(get_dir()+'/js/'+\
    	                        type+'.js','r').read())
    main_code=code_template.safe_substitute(data_dict)
    return js_code.safe_substitute({'divnum':div_num,
    	                            'main_code':main_code})