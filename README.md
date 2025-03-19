# 📝 Blog Project

A dynamic and fully responsive blog application built with Django (or your preferred framework). This project allows users to create, read, update, and delete blog posts seamlessly. It supports user authentication, comments, and a clean, modern UI design.  

---

## ✨ Features  

- 🖊️ **Create, edit, and delete posts**  
- 🔒 **User registration and authentication**  
- 💬 **Comment system**  
- 🔍 **Search functionality**  
- 🎯 **Pagination for better content browsing**  
- 📱 **Fully responsive design**  

---

## 🔧 Technologies Used  

- **Backend:** Django / Flask / Node.js (adjust to your stack)  
- **Frontend:** HTML, CSS, JavaScript  
- **Database:** SQLite / PostgreSQL / etc.  

---

💡 **Feel free to fork, improve, and contribute!**  


## Installation

### Prerequisites

- Python 3.8 or higher
- PostgreSQL

### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/almahesabnet/AlmaHesabNet-Platform.git
   ```

2. Navigate into the project directory:
   ```bash
   cd AlmaHesabNet
   ```

3. Set up a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

4. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

5. Set up the environment variables using a `.env` file or through your preferred method (e.g., `decouple`).

6. Apply database migrations:
   ```bash
   python manage.py migrate
   ```

7. Create Cache Table:
   ```bash
   python manage.py createcachetable
   ```

8. Create a superuser to access the admin panel:
   ```bash
   python manage.py createsuperuser
   ```

9. Run the development server:
   ```bash
   python manage.py runserver
   ```

10. Open your browser and navigate to `http://127.0.0.1:8000` to see the application in action.


---