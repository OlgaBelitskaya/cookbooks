from IPython.display import display,HTML
# Crayola Colors
c1,c2,c3,c4,c5,c6,c7,c8,c9,c10=\
'#FF355E','#FF6037','#FF9966','#FFCC33','#FFFF66',\
'#CCFF00','#66FF66','#50BFE6','#FF6EFF','#FF00CC'
fs1,fs2,fs3,fs4,fs5,fs6,fs7,fs8=10,12,14,16,18,20,25,30
f1,f2,f3,f4,f5,f6,f7=\
'Smokum','Akronim','Wallpoet','Orbitron',\
'Ewert','Lobster','Roboto'
def dhtml(string,fontcolor=c1,font=f1,fontsize=fs7):
    display(HTML("""<style>
    @import 'https://fonts.googleapis.com/css?family="""\
    +font+"""&effect=3d-float';</style>
    <h1 class='font-effect-3d-float' 
    style='font-family:"""+font+\
    """; color:"""+fontcolor+\
    """; font-size:"""+str(fontsize)+"""px;'>
    %s</h1>"""%string))