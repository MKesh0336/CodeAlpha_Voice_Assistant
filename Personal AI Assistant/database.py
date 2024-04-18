import sqlite3

def establish_connection():
    """ Establishes a SQLite database connection. """
    return sqlite3.connect("AI_Assistant.db")

def initialize_db():
    """ Creates the table if it doesn't already exist in the database. """
    with establish_connection() as conn:
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS TeachingQuestionAndAnswers (
                Questions TEXT UNIQUE,
                Answers TEXT
            )
        """)
        conn.commit()

def get_questionAndanswer():
    """ Retrieves all question-answer pairs from the database. """
    with establish_connection() as conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM TeachingQuestionAndAnswers")
        return cur.fetchall()

def insert_questionAndanswer(Questions, Answers):
    """ Inserts a new question-answer pair into the database using parameterized queries for safety. """
    with establish_connection() as conn:
        cur = conn.cursor()
        try:
            cur.execute("INSERT INTO TeachingQuestionAndAnswers (Questions, Answers) VALUES (?, ?)", (Questions, Answers))
            conn.commit()
        except sqlite3.IntegrityError:
            print(f"An entry with the question '{Questions}' already exists.")

def get_answer(question):
    """ Retrieves an answer from the database for a given question using parameterized queries for efficiency. """
    with establish_connection() as conn:
        cur = conn.cursor()
        cur.execute("SELECT Answers FROM TeachingQuestionAndAnswers WHERE Questions = ?", (question,))
        answer = cur.fetchone()
        return answer[0] if answer else ""

# Example usage:
initialize_db()  # Ensure the database and table are set up.
#insert_questionAndanswer('speech', 'off')  # Insert an example entry.

# Fetch an answer for a specific question.
answer = get_answer('speech')
print("The answer is:", answer if answer else "No answer found.")
