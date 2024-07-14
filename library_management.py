import random
import json
import datetime

#load the data from json file
def load_data():
    with open('library.json','r') as library:
        parsed_string = json.load(library)
        # print(parsed_string)
    return parsed_string

#save information as json file
def save_data(data):
    with open('library.json','w') as library:
        formatted_string=json.dumps(data)
        library.write(formatted_string)

#add book 
def add_book(book_info):
    books_list = load_data()
    books_list.append(book_info)
    save_data(books_list)

# view library status
def view_status():
    books = load_data()
    for book in books:
        print(book)

#check out and update book status
def checkout(checkout_info):
    is_available = True
    books = load_data()
    (id,name,due_date)=checkout_info
    for book in books:
        if book['id']== id and book['status'] == 'Available':
            book['status'] = f'check out by {name}'
            book['due-date'] = due_date
            is_available = False
    save_data(books)
    return is_available

#return book and update status
def book_return(id):
    is_checkout = False
    books = load_data()
    for book in books:
        if book['id']== id  and book['status'] != 'Available':
            is_checkout=True
            book['status'] = 'Available'
            del book['due-date']
    save_data(books)
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
            book_info = {'title':book_title,'author':book_author,'id':book_id,'status':status}
            add_book(book_info)
            print('Book is added successfully')

        if choice == 2:
            book_ID = int(input('Enter book id to check out: '))
            borrower_name = str(input('Enter borrower name: '))
            due_date = input('Enter due date (yyyy-mm-dd): ')
            formatted_due_date = datetime.datetime.strptime(due_date,'%Y-%m-%d').date()
            checkout_info = (book_ID,borrower_name,due_date)
            is_exists = checkout(checkout_info)
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

# main function to be executed
if __name__ == '__main__':
    main()