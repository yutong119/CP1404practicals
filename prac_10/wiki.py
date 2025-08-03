
import wikipedia

def get_page_information(title):
        page = wikipedia.page(title, auto_suggest=False) #get the Wikipedia page with the specified title
        print(f"{page.title}") #title
        print(f"{page.summary}")  # summary about this title
        print(f"{page.url}") # the link

title = input("Enter page title: ")
while title != "":
    try:
        get_page_information(title)
    except wikipedia.DisambiguationError:
        print("We need a more specific title. Try one of the following, or a new search:")
    title = input("Enter page title: ")
print("Thank you.")