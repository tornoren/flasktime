# ta delen av cli-programmet som henter bilder og laster og bruke den til å lage pdf klar for nedlasting
import requests as r
import img2pdf
import glob
import os
from PIL import Image


def fetch_page(URN, page_id):
    page_number = str(page_id).zfill(4)
    url = f'https://www.nb.no/services/image/resolver?url_ver=geneza&urn={URN}_{page_number}&maxLevel=6&level=4&col=0&row=0&resX=3168&resY=4096&tileWidth=1024&tileHeight=10024'

    print(url)
    try:
        response = r.get(url)
        response.raise_for_status()
    except Exception as err:
        print(f'Error occured: {err}')
        return False
    return response.content



def save_page(page_data, page_id, URN):
    with open(f'./books/{URN}/{str(page_id)}.jpg', "wb") as file:
        file.write(page_data)

def fetch_all_pages_from_given_book(URN, page_number_total):
    made_folder = make_folder(URN)
    if made_folder:
        for i in range(int(page_number_total)):
            page_id = i + 1
            page = fetch_page(URN, page_id)
            if page != False:
                save_page(page, page_id, URN)



def pdf_maker(URN):
    # replace "book" in "book.pdf" with the title        
    if not os.path.isfile(f'./books/{URN}/book.pdf'): 
        with open(f'./books/{URN}/book.pdf', "wb") as pdf_file:
            image_files = glob.glob(f'./books/{URN}/*.jpg')
            # change the original order of list items in the image_files variable
            image_files.reverse()
            pdf_data = img2pdf.convert(image_files)
            pdf_file.write(pdf_data)

def make_folder(URN):
    try: 
        os.mkdir(f'./books/{URN}')
        return True
    except: 
        print('Du har denne mappa fra før')
        return False 
        


    
    