import random
import json
import datetime
#add book 
def add_books(title,author,id,status):
    # loaded_data = load_data()
    #print(loaded_data,'ffrom load')
    booksCollection= load_data()
    book={
        'title':title,
        'author':author,
        'id':id,
        'status':status
    }
    booksCollection.append(book) 
    save_data(booksCollection)

#save information as json file
def save_data(data):
    with open('library.json','w') as library:
        formated_string=json.dumps(data)
        library.write(formated_string)
        print('Book added successfully!')
        
#load the data from json file
def load_data():
    with open('library.json','r') as library:
        # data= library.read()
        parsed_string = json.load(library)
        # print(parsed_string)
    return parsed_string
    
    
# view library status
def view_status():
    books = load_data()
    for book in books:
        print(book)
#update book status
def update_status(id,name):
    # books = load_data()
    with open('library.json', 'r') as library:
        books = json.load(library)
        print(books)
        # updated_book=0
        for book in books:
            if book['id']== id:
                book['status'] = f'check out by {name}'
                # updated_book = book
                # print(json.dump(updated_book,book))
                print(book,'the updated one')
    with open('library.json','w') as library:
        json.dump(books,library)        
        print(books,'after modified')
        
def book_return(id):
    with open('library.json', 'r') as library:
        books = json.load(library)
        print(books,'before return')
        for book in books:
            if book['id']== id:
                book['status'] = 'available'
                print(book,'whould be returned return')
    with open('library.json','w') as library:
        json.dump(books,library)        
        print(books,'after return')
    
def main():
    
    choice=0
    while choice != 5:
        print('Welcome to the Library Management System')
        print('1. Add book')
        print('2. Check Out Book')
        print('3. Return Book')
        print('4. View Library Status')
        print('5. Exit')
        choice=int(input('Enter your choise: '))
        if choice == 1:
            print('-------Add a new books--------')
            book_title=str(input('Enter book title: '))
            book_author=str(input('Enter author: '))
            book_id= random.randint(1,100)
            status = 'Available'
            add_books(book_title,book_author,book_id,status)
        if choice == 2:
            book_ID = int(input('Enter book id to check out: '))
            borrower_name = str(input('Enter borrower name: '))
            due_date = input('Enter due date (yyyy-mm-dd): ')
            formated_due_date = datetime.datetime.strptime(due_date,'%Y-%m-%d').date()
            print(book_ID,borrower_name,formated_due_date,)
            update_status(book_ID,borrower_name)
        if choice == 3:
            book_ID = int(input('Enter book id to check out: '))
            book_return(book_ID)
        if choice == 4:
            print('Books in the library')
            view_status()



if __name__ == '__main__':
    main()