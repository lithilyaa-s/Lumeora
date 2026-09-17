# 🎬 Lumeora

> A Personalized Movie Recommendation System built using PHP and MySQL.

![PHP](https://img.shields.io/badge/PHP-8.x-blue)
![MySQL](https://img.shields.io/badge/MySQL-Database-orange)
![HTML5](https://img.shields.io/badge/HTML-5-red)
![CSS3](https://img.shields.io/badge/CSS-3-blue)
![License](https://img.shields.io/badge/License-MIT-green)

---

## 📖 Overview

Lumeora is a web-based movie recommendation platform that suggests movies based on user preferences such as mood, genre, language, and age group.

Users can:

- Register and Login securely
- Browse movies
- Get personalized recommendations
- Rate movies
- Write reviews
- Save movies to a watchlist

The project demonstrates the practical implementation of Database Management Systems using a normalized relational database (5NF), PHP, MySQL, HTML, CSS, and JavaScript.

---

## ✨ Features

- 🔐 User Authentication
- 🎭 Mood Based Recommendations
- 🎬 Genre Filtering
- 🌍 Language Filtering
- 👶 Age Group Filtering
- ⭐ Top Rated Movies
- ❤️ "Because You Like" Recommendations
- 📋 Personal Watchlist
- ⭐ Ratings
- 💬 Reviews
- 📱 Responsive UI

---

## 🛠 Tech Stack

Frontend
- HTML5
- CSS3
- JavaScript

Backend
- PHP

Database
- MySQL

Server
- XAMPP / Apache

---

## 🗄 Database

The database contains five normalized tables:

- Users
- Movies
- Ratings
- Reviews
- Watchlist

The schema satisfies:

- 1NF
- 2NF
- 3NF
- BCNF
- 4NF
- 5NF

---

## 🚀 Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/Lumeora.git
```

### Move into Project

```bash
cd Lumeora
```

### Start XAMPP

Enable:

- Apache
- MySQL

### Import Database

Open phpMyAdmin

Create a database

```
movierec
```

Import

```
database/movierec.sql
```

### Configure Database

Edit

```
db.php
```

```php
$host="localhost";
$user="root";
$password="";
$db="movierec";
```

### Run

```
http://localhost/Lumeora
```

---

## 📸 Screenshots

| Login | Dashboard |
|--------|-----------|
| Add Screenshot | Add Screenshot |

| Recommendations | Watchlist |
|----------------|-----------|
| Add Screenshot | Add Screenshot |

---

## 📈 Recommendation Filters

- Mood
- Genre
- Language
- Age Group
- Top Rated
- Because You Like

---

## Future Improvements

- AI-based Recommendation Engine
- Collaborative Filtering
- Content-Based Recommendation
- JWT Authentication
- Email Verification
- Dark/Light Theme
- Admin Dashboard
- Movie Trailer Integration
- REST API

---

## License

MIT License

---

## Author

**Lithilyaa S**

BE Computer Science Engineering

SRM Valliammai Engineering College

GitHub: https://github.com/yourusername
