# with the libraries rpy_sklearn.R
corpus=c('Have you already set your goals for the New Year?',
         paste0('Do you want to lose ten kilos, ',
                'run a marathon or speak fluent English?'), 
         'Some experts believe that you need systems, not goals.',
         'A system is something you do on a regular basis.',
         paste0('This means focusing on what you can control ',
                '(your actions) rather than what you can’t.'),
         'For example, do not focus on losing ten kilos.',
         paste0('Focus on shopping for healthy food and ',
                'cooking something light every day.'),
         'Do not focus on the marathon.',
         'Focus on the training schedule.',
         paste0('Invent a system to improve your English, ',
                'one step at a time.'),
         'Good luck!')
cv<-slfe$text$CountVectorizer(max_df=100)
corpus_features<-cv$fit_transform(
    np$array(corpus,dtype='object'))
options(repr.plot.width=10,repr.plot.height=7)
for (i in 1:11){
    matplot(corpus_features[i,]+3*(i-1),
            xlab='',ylab='',pch='*',ylim=c(0,33),col=i,
            main='The Words` Occurrence in Sentences'); 
    par(new=TRUE)}
ca<-cv$build_analyzer(); print(ca(corpus[1]))