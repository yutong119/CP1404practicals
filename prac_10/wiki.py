
import wikipedia

def get_page_information(title):
    page = wikipedia.page(title, auto_suggest=False)

title = input("Enter page title: ")
while title != "":
    get_page_information(title)
    title = input("Enter page title: ")
print("Thank you.")