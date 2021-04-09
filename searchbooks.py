#passes search string to api.nb.no
import requests as r
import json

def search_books(search_string):
    search_endpoint = 'https://api.nb.no/catalog/v1/items'
    params = dict(

        q=search_string,
        digitalAccessibleOnly=True,
        filter='mediatype:bøker',
        size=50
    )

    search_response = r.get(search_endpoint, params)
    search_data = search_response.json()
    if "items" in search_data['_embedded']:
        book_list = search_data['_embedded']['items']
        #title_list = [book['metadata']['title'] for book in book_list]
        return book_list
    return []
