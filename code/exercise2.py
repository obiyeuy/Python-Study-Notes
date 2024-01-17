books = []

while True:
    if len(books) == 3:
        break

    name = input('输入书名')

    for book in books:
        if name == book.get('name'):
            print('书名重复')
            break
    else:
        author = input('输入作者')
        price = float(input('输入价格'))

        books.append({'name': name, 'author': author, 'price': price})
