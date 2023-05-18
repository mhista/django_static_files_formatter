import os

def removePath(ff):
    
    if os.path.exists(ff):
        os.remove(ff)     
    
def compare(fil, ff):
    if fil == ff:
        splitter = ff.split('.')[0]
        splited = str(splitter)
        ff = ff.replace(ff,f"i-{splited}.html")
        return ff
    else:
        return ff 

def changeName(fk,fil,fp):
    if fp == fil:
        splitter = fp.split('.')[0]
        split = str(splitter)
        fm = fk.replace(fk,f"{split}.html")
        print(f"removing initial part")
        os.remove(fil)
        os.rename(fk,fm)
        print(f"renaming {fk} to {fm}")
    else:
        os.remove(fil)

        
def convertCss(fil, ff):
    fp = ff
    fk = compare(fil, ff)
    removePath(fk)
    with open(fil, 'r+') as f:
        for line in f:
            li=str(line)        
            lv=li.replace('}','\n}\n')
            li = lv.replace(';', ';\t')
            li = li.replace('{', '{\n\t')
            
            with open(fk, 'a+') as s:
                s.write(li)
    changeName(fk,fil,fp)



def convertHtml(fil,ff):
    fp = ff
    fk = compare(fil, ff)
    removePath(fk)

    with open(fil, 'r+') as fi:
        print(f"converting to {fk}")

        for line in fi:
            lim = str(line) 
            style = lim.replace('<link rel="stylesheet" href=', '<link rel="stylesheet" href= {%  static ')
            kyle = style.replace('<link href=" rel="stylesheet"' , '<link href={%  static "  rel="stylesheet" ')
            images = kyle.replace('href="images', 'href= {%  static "images')
            img = images.replace('href="img', 'href= {%  static "img')
            data = img.replace('data-setbg="img', 'data-setbg= {%  static "img')
            png = data.replace('.png">', '.png" %}>')
            gif = png.replace('.gif">', '.gif" %}>')
            apng = gif.replace('.png"', '.png" %}')
            svg = apng.replace('.svg"', '.svg" %}')
            jpg = svg.replace('.jpg"', '.jpg" %}')
            src = jpg.replace('src=', 'src= {%  static ')
            video = src.replace('type="video', ' %} type="video')
            css = video.replace('.css"', '.css" %}')
            html = css.replace('.js">', '.js" %}>')
        
   
            with open(fk, 'a+') as s:
                s.write(html)


    changeName(fk,fil,fp)
def unwrapHtml(fil,ff):
    fp = ff
    fk = compare(fil, ff)
    removePath(fk)

    with open(fil, 'r+') as fi:
        print(f"converting to {fk}")
        for line in fi:
            lim = str(line)
            html = lim.replace('>', '>\n\t')
            htm = html.replace('\t</', '</')


            with open(fk, 'a+') as s:
                s.write(htm)
    changeName(fk,fil,fp)

# convertHtml('index.html', 'index.html')



def single_file_formatting():
    format = input('format for converting file (e.g html,css,js): ')
    li = {}
    collect_file = input("specify file path to be converted: ")
    name_to_convert = input("filename to be used: ")
    collect_file = f"{collect_file}.{format}"
    name_to_convert = f"{name_to_convert}.{format}"
    li[collect_file] = name_to_convert
    
    print(li)
    print("file conversion in progress..... ")
    
    for f,x in li.items():   
        if format == 'html':
            format = input('choose options\n1. unwrap file\n2. add static for django project\n3. both: ')
            if format == '1':
                unwrapHtml(f,x)
            elif format == '2':
                convertHtml(f,x)
            elif format == '3':
                unwrapHtml(f,x)
                convertHtml(f,x)



        else:
            convertCss(f,x)
def bulk_formatting():
    format = input('format for converting file: ')
    folder = input("folder name: ")
    dir = 'C:/Users/innocent/Desktop/'
    fullpath = os.chdir(f'{dir}{folder}/{folder}')
    pathlist = os.listdir(fullpath)
    print(f"{pathlist}", end='\n')
    pathionary= {}
    for path in pathlist:
        p = str(path)
        pathionary[p] = p
        # print(pathionary)
    print("file conversion in progress..... ")

    for path_x,path_y in pathionary.items():
        if format == 'html':
            convertHtml(path_x,path_y)
        else:
            convertCss(path_x,path_y)
    

def convertMultipleFile():
    print("""
    NOTE: for single file formatting, copy the file to the same directory as the file formmater.
    choose the single file format in the options and type in the file to be converted
    For multiple file converting, create a folder[A], place the file formatter in the folder, 
    create a subfolder in folder[A] with the same name as folder[A], 
    place the files in the subfolder. make sure the files end in the same fileformat e.g '.html'
    """)

    info = input("choose options: \n1. Single file formatting\n2. multiple file formatting: ")
    if '1' in info:
        single_file_formatting()
        print("file conversion successful")
    elif '2' in info:
        bulk_formatting()
        print("file conversion successful")
    # print("(N/B) all files must be in the format,'file.fileformat' e.g 'apex.html'")
    
convertMultipleFile()
