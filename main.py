from PIL import Image
from urllib.request import urlopen

url = "https://img.freepik.com/vetores-gratis/elefante-fofo-usando-oculos-de-desenho-animado-icone-vetorial-ilustracao-icone-de-natureza-animal-isolado_138676-13787.jpg?semt=ais_hybrid"
urls = []
format_img = '.png'
name_img = 'teste'
path_img = '.\image\\'

print('para adiciona varias imagens voce so precisa ir colando as urls e dando "enter"\nquando quize para apena digite "stop"')

while True:
    imgs = str(input('informe a url da image: '))

    img =  Image.open(urlopen(url))

    if imgs != 'stop':
        #check valid urls
        if 'https://' in imgs:
            urls.append(imgs)
        else:
            print('url invalida')
    else:
        break

    print(urls)

# img.save(f'{path_img}{name_img}{format_img}')