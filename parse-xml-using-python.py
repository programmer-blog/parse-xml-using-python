from lxml import etree

def parseBookXML(xmlFile):
    with open(xmlFile) as fobj:
        xml = fobj.read()
    root = etree.fromstring(xml)
    book_dict = {}
    books = []

    for book in root.getchildren():
        for elem in book.getchildren():
            if elem.text:
                text = elem.text
            else:
                text = ''
            if elem.tag == 'author':
                book_dict[elem.tag] = text
        if book.tag == "book":
            books.append(book_dict)
            book_dict = {}
    return books

books_list = parseBookXML("books.xml")

print(books_list)

