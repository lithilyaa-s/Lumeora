# ============================================
#  LUMEORA — Movie Recommendation System
#  app.py — Complete Flask Backend
# ============================================

from flask import Flask, render_template, request, redirect, url_for, flash
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)
app.secret_key = 'lumeora_secret_key'


# ============================================
#  DATABASE CONNECTION
# ============================================
def get_connection():
    try:
        conn = mysql.connector.connect(
            host     = 'localhost',
            port     = 3307,
            user     = 'root',
            password = 'root',
            database = 'lumeora_db'
        )
        return conn
    except Error as e:
        print(f"Database connection failed: {e}")
        return None


# ============================================
#  ROUTE 1 — HOME PAGE
#  Shows the filter form
# ============================================
@app.route('/')
def index():
    return render_template('index.html')


# ============================================
#  ROUTE 2 — RECOMMEND
#  Fetches movies based on language, genre, duration
# ============================================
@app.route('/recommend', methods=['GET', 'POST'])
def recommend():

    # Get filter values from the homepage form
    language = request.form.get('language')
    genre    = request.form.get('genre')
    duration = request.form.get('duration')

    # Connect to database
    conn = get_connection()

    if conn is None:
        flash('⚠️ Database connection failed. Try again.')
        return redirect(url_for('index'))

    try:
        cursor = conn.cursor(dictionary=True)
        # dictionary=True → each row returned as a dict
        # e.g. {"title": "Leo", "language": "Tamil", ...}

        query = """
            SELECT
                movie_id,
                title,
                language,
                genre,
                duration,
                image_url
            FROM movies
            WHERE language = %s
              AND genre    = %s
              AND duration <= %s
            ORDER BY title ASC
        """
        cursor.execute(query, (language, genre, int(duration)))
        movies = cursor.fetchall()
        # fetchall() returns a list of all matching rows

    except Exception as e:
        print(f"Query failed: {e}")
        movies = []

    finally:
        cursor.close()
        conn.close()

    return render_template(
        'movies.html',
        movies            = movies,
        selected_language = language,
        selected_genre    = genre,
        selected_duration = duration
    )


# ============================================
#  ROUTE 3 — SUBMIT REVIEW
#  Inserts rating and review into MySQL
# ============================================
@app.route('/submit_review', methods=['POST'])
def submit_review():

    # Get form data
    movie_id = request.form.get('movie_id')
    rating   = request.form.get('rating')
    review   = request.form.get('review')

    # Hardcoded for now — replace with session['user_id'] after login is built
    user_id  = 1

    # ── Validate inputs ──
    if not rating or int(rating) == 0:
        flash('⚠️ Please select a star rating.')
        return redirect(request.referrer)

    if not review or review.strip() == '':
        flash('⚠️ Please write a review before submitting.')
        return redirect(request.referrer)

    if not movie_id:
        flash('⚠️ Something went wrong. Movie not found.')
        return redirect(request.referrer)

    if int(rating) < 1 or int(rating) > 5:
        flash('⚠️ Rating must be between 1 and 5.')
        return redirect(request.referrer)

    # ── Connect to database ──
    conn = get_connection()

    if conn is None:
        flash('⚠️ Database connection failed. Try again.')
        return redirect(request.referrer)

    try:
        cursor = conn.cursor()

        query = """
            INSERT INTO reviews (user_id, movie_id, rating, review)
            VALUES (%s, %s, %s, %s)
        """
        cursor.execute(query, (
            int(user_id),
            int(movie_id),
            int(rating),
            review.strip()
        ))

        # IMPORTANT — saves data permanently to MySQL
        conn.commit()
        flash('✅ Review submitted successfully! Thank you.')

    except Exception as e:
        # Undo any partial changes if something goes wrong
        conn.rollback()
        flash(f'⚠️ Failed to submit review: {str(e)}')

    finally:
        cursor.close()
        conn.close()

    return redirect(request.referrer)


# ============================================
#  RUN APP
# ============================================
if __name__ == '__main__':
    app.run(debug=True)