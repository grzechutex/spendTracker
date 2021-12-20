open('Categories.txt')

def adding():
    Category = input('What category? ')
    if Category == 'new':
        #tworzymy nową kategorie
        CategoryMaker()


#funkcja tworzaca nowa kategorie
def CategoryMaker():
    CatName = input('Name the category: ')
    #CatColour = input('What colour should this category have?') nie wiem jak to zrobić na razie