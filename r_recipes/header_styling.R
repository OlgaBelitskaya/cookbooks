dhtml<-function(str) {
    IRdisplay::display_html(paste0(c(
'<style>@import "https://fonts.googleapis.com/css?family=Ewert|Roboto&effect=3d"; ',
'</style><h1 class="font-effect-3d" style="font-family:Ewert; color:#ff355e;"> &#x1F310; &nbsp;',str,'</h1>'),collapse='')) }
