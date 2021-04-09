from searchbooks import search_books
from flask import Flask
from flask import render_template
from flask import request
from flask import send_file
import downloadbooks as db
# Klassen har variabler og definisjoner vi kan bruke
app = Flask(__name__)
#__ betyr at jeg ikke skal gjøre noe med eller tenke
#__ viser ofte til noe internt



#Route with form for doing a search
# /search


@app.route('/search')
def search_input_form():
    # if search_string=something do a API request to NB and return the results to the search template
    # example: /search?search_string=hamsun
    search_string = request.args.get('search_string')
    
    if search_string:
        booklist = search_books(search_string)
        print(booklist)
        return render_template('search.html', booklist=booklist, search_string=search_string)
    
    return render_template('search.html')
    # else just return the search form

@app.route('/download/<URN>/<page_count>')
def fetch_all_pages_from_given_book_and_give_me_pdf_now(URN, page_count):
    # takes URN and page count and downloads all the jpgs from NB
    db.fetch_all_pages_from_given_book(URN,page_count)
    # takes all the jpgs and stitch them together as a pdf file stored in this folder
    db.pdf_maker(URN)
    
    # send the pdf file back to the end-user's browser as a file
    return send_file(f'./books/{URN}/book.pdf', attachment_filename='book.pdf')



#/download/{{book.metadata.identifiers.urn}}

# The search form POSTs its data to a route that takes the search query and returns a list of results from the NB API
# /results

# The results are generated as URLs to a endpoint that gives you the PDF
# E.g. /download/<URN>


#routeren gjør at sidene tar imot requests
