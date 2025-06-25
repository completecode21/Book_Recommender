# 📚 Book Recommendation System (Streamlit Web App)

A user-friendly web app that provides intelligent book recommendations based on either popularity or content similarity. Built with Python and Streamlit, this project helps users find their next great read.

---

## 🔧 Tools & Technologies

- **Languages & Libraries:** Python, Pandas, NumPy  
- **Machine Learning:** Scikit-learn (Cosine Similarity)  
- **Web App Framework:** Streamlit, streamlit-option-menu  
- **Model & Data Storage:** Pickle (`.pkl` files)

---

## 🎯 Objective

To enhance the reading experience by recommending relevant books based on:

- Popularity (based on user ratings)
- Similarity to a selected book (via cosine similarity)

---

## ⚙️ How It Works

### 1. **Data Sources**
- `Books.csv`: Metadata (Title, Author, Year, Publisher, etc.)
- `Users.csv`: User demographics (Location, Age)
- `Ratings.csv`: User ratings for books

### 2. **Back-End Logic**
- Cleaned and preprocessed datasets (removed nulls, duplicates)
- **Popularity-Based Filtering:** Top books sorted by number of ratings and average rating
- **Similarity-Based Filtering:** Used cosine similarity on a user-book matrix
- Stored final models and filtered data using Pickle for fast loading

### 3. **Streamlit Front-End**
- Sidebar navigation with:
  - **Top 50**: View most popular books
  - **Recommend**: Select a book to get 5 similar book recommendations
- Each recommended book displays:
  - Title, Author, Cover Image, Number of Ratings, Average Rating

---

## 💡 Key Features

- 🔄 **Dual Recommendation Models**  
  Choose between popularity-based or similarity-based recommendations

- ⚡ **Real-Time Web Interface**  
  Interactive Streamlit UI for fast and easy browsing

- 🧠 **Modular Architecture**  
  Separated into `top_50.py`, `recommend.py`, and `main.py` for maintainability

- 📦 **Optimized Loading**  
  Pickled models and datasets ensure quick startup

---

## 🖼️ Sample UI

> *(Replace the URL below with your actual screenshot if needed)*

![App Screenshot](./assets/![book recommendation img](https://github.com/user-attachments/assets/68dabdd4-74cd-42b3-a060-20b11efe5c25)
.png)



---

## 🚀 Getting Started

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/book-recommendation-app.git
   cd book-recommendation-app
