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
        formatted_string=json.dumps(data)
        library.write(formatted_string)
        # print('Book added successfully!')
        
#load the data from json file
def load_data():
    with open('library.json','r') as library:
        parsed_string = json.load(library)
        # print(parsed_string)
    return parsed_string
    
    
# view library status
def view_status():
    books = load_data()
    for book in books:
        print(book)
#check out and update book status
def checkout(id,name,due_date):
    is_available = True
    # books = load_data()
    with open('library.json', 'r') as library:
        books = json.load(library)
        # print(books)
    for book in books:
        if book['id']== id and book['status'] == 'Available':
            book['status'] = f'check out by {name}'
            book['due-date'] = due_date
            is_available = False
    with open('library.json','w') as library:
        json.dump(books,library)        
        # print(books,'after modified')
    return is_available
def book_return(id):
    is_checkout = False
    with open('library.json', 'r') as library:
        books = json.load(library)
        #print(books,'before return')
    for book in books:
        if book['id']== id  and book['status'] != 'Available':
            is_checkout=True
            book['status'] = 'Available'
            del book['due-date']
            #print(book,'would be returned return')
        
    with open('library.json','w') as library:
        json.dump(books,library)        
        #print(books,'after return')
    return is_checkout

def main():
    
    choice=0
    while choice != 5:
        print('Welcome to the Library Management System')
        print('1. Add book')
        print('2. Check Out Book')
        print('3. Return Book')
        print('4. View Library Status')
        print('5. Exit')
        choice=int(input('Enter your choice between 1 to 5: '))
        
        if choice == 1:
            print('-------Add a new books--------')
            book_title=str(input('Enter book title: '))
            book_author=str(input('Enter author: '))
            book_id= random.randint(1,100)
            status = 'Available'
            add_books(book_title,book_author,book_id,status)
            print('Book is added successfully')
        if choice == 2:
            book_ID = int(input('Enter book id to check out: '))
            borrower_name = str(input('Enter borrower name: '))
            due_date = input('Enter due date (yyyy-mm-dd): ')
            formatted_due_date = datetime.datetime.strptime(due_date,'%Y-%m-%d').date()
            is_exists = checkout(book_ID,borrower_name,due_date)
            if not is_exists:
                print('you have checked out the book')
            else:
                print('Your requested book is not available')
                
        if choice == 3:
            book_ID = int(input('Enter book id to return: '))
            isCheckout = book_return(book_ID)
            if not isCheckout:
                print('The book is not checkout yet')
            else:
                print('You have the return the book successfully')
        if choice == 4:
            print('Books in the library')
            view_status()
        



if __name__ == '__main__':
    main()