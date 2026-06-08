from book import Book
from electronics import Electronic

if __name__ == '__main__':
    
    # create a items list
    items : list = []

    item_book:Book = Book(2, 'naughty', 3_00, 5, 'mia malkova')
    item_electronics:Electronic = Electronic(2, 'keyboard', 1_234, 14, 2)

    # check -> should we add unique or duplicate Items
    if item_book not in items:
        items.append(item_book)
    
    if item_electronics not in items:
        items.append(item_electronics)
    else:
        print('duplicate item found')


    items.sort()
    
    for item in items:
        print(f"items name: {item.get_name()} and price: {item.get_price()} and there id: {item.get_id()}")
