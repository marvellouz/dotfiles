au BufNewFile,BufRead *.asp :set ft=javascript.html.aspjavascript
au BufNewFile,BufRead *.inc :set ft=javascript.html.aspjavascript
au BufNewFile,BufRead *.rkt :set ft=scheme
au BufNewFile,BufRead *.aspx :set ft=xml
au BufNewFile,BufRead *.tpl :set ft=smarty

au Filetype smarty exec('set dictionary=/home/valentina/.vim/syntax/smarty.vim')
au Filetype smarty set complete+=k 

autocmd FileType html set ft=htmldjango.html " For SnipMate
autocmd FileType html set ft=html.django_template " For SnipMate
autocmd FileType python set ft=python.django " For SnipMate
autocmd FileType python set omnifunc=pythoncomplete#Complete
autocmd FileType javascript set omnifunc=javascriptcomplete#CompleteJS
autocmd FileType html set omnifunc=htmlcomplete#CompleteTags
autocmd FileType css set omnifunc=csscomplete#CompleteCSS
