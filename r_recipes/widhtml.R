vfont_family<-c('Smokum','Akronim','Wallpoet',
                'Orbitron','Ewert','Lobster',
                'Roboto','Miss Fajardose','Monoton')
vfont_size<-c(8,10,12,14,16,18,20,22,24,26,28,30,32)
vfont_color<-c('#ff36ff','#ff3636','#3636ff',
               '#36ffff','#ff9636','#ff3696')

idhtml<-function(string,font_color=vfont_color[6],
                 font_family=vfont_family[2],
                 font_size=vfont_size[11]) {
    randi<-sample(1:9999999,1)
    s<-sapply(34,intToUtf8)
    html_str<-c(
      '<style>@import ',s,'https://fonts.',
      'googleapis.com/css?family=',font_family,
      s,'; #rh1 {font-family:',font_family,
      '; color:',font_color,'; font-size:',font_size,
      'px; text-shadow:3px 3px 3px #aaa;}</style>',
      '<h1 id=',s,'rh1',s,';>',string,'</h1>')
    str<-paste0(html_str,collapse='')
    IRdisplay::display_html(str)}

ipyhtml<-function(font_color=vfont_color[6],
                 font_family=vfont_family[7],
                 font_size=vfont_size[2]) {
    html_str<-c(
        '<style>span {font-family:',font_family,
        '; color:black; text-shadow:3px 3px 3px #aaa;} ',
        'div.output_area pre{font-family:',
        '; font-size',font_size,'px; color:',
        font_color,';}</style>')
    str<-paste0(html_str,collapse='')
    IRdisplay::display_html(str)}