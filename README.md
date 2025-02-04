# 📚 Bookstore Management System

## 📌 Overview
The **Bookstore Management System** is a simple command-line program built with Python and SQLite to manage a bookstore's inventory. The system allows users to **add, update, delete, search, and display books** stored in a SQLite database.

## ⚡ Features
- 📖 **Add new books** to the database.
- 🔄 **Update book details** such as title, author, and quantity.
- ❌ **Delete books** from the database.
- 🔍 **Search books** by title, author, or book ID.
- 📜 **View all books** currently stored in the database.

## 🛠️ Technologies Used
- **Python 3**
- **SQLite3** (built-in Python library)

## 🏗️ Installation
To run the Bookstore Management System on your local machine:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/karmaniomar/small_bookstore.git
   cd small_bookstore
   ```

2. **Run the script**:
   ```bash
   python small_bookstore.py
   ```

## 📝 Usage
Once the script is running, you will see a menu with the following options:

```
Bookstore Management System
1. Enter book
2. Update book
3. Delete book
4. Search books
5. Show all books
0. Exit
Enter your choice:
```

### 🔹 Adding a Book
- Enter the book ID, title, author, and quantity.
- The system ensures that book IDs are unique.

### 🔹 Updating a Book
- Enter the book ID of the book to update.
- Provide new title, author, and quantity.

### 🔹 Deleting a Book
- Enter the book ID to remove a book from the database.

### 🔹 Searching for a Book
- Search by book ID, title, or author.

### 🔹 Displaying All Books
- Lists all books available in the database.

## 📂 Database Structure
The system uses a SQLite database (`small_bookstore_stock.db`) with the following schema:

| Column  | Type    | Description |
|---------|--------|-------------|
| `id`    | INTEGER (Primary Key) | Unique book ID |
| `title` | TEXT   | Book title (Unique) |
| `author` | TEXT  | Author name |
| `qty`   | INTEGER | Quantity available |

## 🚀 Future Enhancements
- ✅ Add a **GUI** version using Tkinter or PyQt.
- 📊 Implement **inventory tracking** with low-stock alerts.
- 🌐 Develop a **web-based version** with Flask or Django.

## 👨‍💻 Author
- **Omar Karmani**  
- 📧 Email: omar.karmani93@gmail.com
- 🌍 GitHub: [karmaniomar](https://github.com/karmaniomar)

## 📜 License
This project is licensed under the **MIT License**.
