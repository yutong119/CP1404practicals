
import wikipedia

def get_page_information(title):
    try:
        page = wikipedia.page(title, auto_suggest=False)
    except wikipedia.DisambiguationError:
        print("We need a more specific title. Try one of the following, or a new search:")




title = input("Enter page title: ")
while title != "":
    get_page_information(title)
    title = input("Enter page title: ")
print("Thank you.")