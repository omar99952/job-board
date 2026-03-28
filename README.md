# 💼 Django Job Board

A simple and scalable job board web application built with Django.
Users can browse jobs, apply for positions, and companies can post job listings.

---

## 🚀 Features

* 🔐 User authentication (Register / Login / Logout)
* 🧑‍💼 Job seekers can:

  * Browse available jobs
  * View job details
  * Apply for jobs
* 🏢 Employers can:

  * Post new job listings
  * Edit and delete jobs
  * 🔎 Search and filter jobs
  * 🗂 Organized job categories

---

## 🛠️ Tech Stack

* **Backend:** Django (Python)
* **Database:** SQLite (default) 
* **Frontend:** HTML, CSS, JavaScript
* **Authentication:** Django built-in auth syste

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/omar99952/job-board.git
cd job-board
```

### 2️⃣ Create virtual environment

```bash
python -m venv venv
source venv/bin/activate   # Linux / Mac
Scripts\activate      # Windows
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Apply migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5️⃣ Run the server

```bash
python manage.py runserver
```

Open your browser at:

```
http://127.0.0.1:8000/
```

---

## 👤 Admin Panel

Create superuser:

```bash
python manage.py createsuperuser
```

Access admin panel:

```
http://127.0.0.1:8000/admin/
```

---


## 📌 Future Improvements

* ✅ REST API using Django REST Framework
* ✅ Job recommendations system
* ✅ Email notifications
* ✅ Deployment (Render / Vercel / AWS)

---

## 🤝 Contributing

Contributions are welcome!
Feel free to fork this repo and submit a pull request.

---

## 📄 License

This project is open-source and available under the MIT License.

---

## 👨‍💻 Author

Omar Mohamed
Backend Developer | Django & FastAPI
