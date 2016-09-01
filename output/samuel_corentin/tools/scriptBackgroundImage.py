#! /usr/bin/python3.4

import os

balises=[]
listeImg = os.listdir('./img/')
f = open('backgroundImage.css', 'w')

for index, images in enumerate(listeImg):
    if(images.find("png")!=-1):
        string = "#line{0}{1}\n\tbackground-image:url({4}img/{2}{4});\n{3}\n".format(images.split('.')[0],'{',images,'}','"')
        f.write(string)
f.closed
