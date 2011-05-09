from settings import *

def copy_src(src):
  if (os.path.isfile(src)):
    dst = os.path.join(SCRIPT_DIR, os.path.dirname(src[1::]))
    if(not os.path.exists(dst)):
      os.makedirs(dst)
    copy(src, dst)
    print("SRC : " + src)
    print("DESTINATION: " + dst)
  if (os.path.isdir(src)):
    dst = os.path.join(SCRIPT_DIR, os.path.abspath(src)[1::])    
    if(os.path.exists(dst)):
      rmtree(dst)
    copytree(src, dst, copy_function=copy)
    print("SRC : " + src)
    print("DESTINATION: " + dst)


for f in dotfiles: 
  copy_src(f)
