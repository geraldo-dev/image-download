from PIL import Image
from urllib.request import urlopen
from random import randint
from time import sleep

urls = []
path_img = '.\image'

def random_name():
    new_name = str(randint(1, 99))
    return 'img'+ new_name


print('\nTo add multiple images you just need to paste the URLs and press "enter"\n When you want to, just type "stop"')

while True:
    imgs = str(input('enter the image url: '))

    if imgs != 'stop':
        #check valid urls
        if 'https://' in imgs:
            urls.append(imgs)
        else:
            print('url invalida')
    else:
        for url in urls:
            pass
            #save_img(url)
        break

    print(f'\nvoce tem {len(urls)} urls adicionadas para baixar')
