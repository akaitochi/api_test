import psycopg2
conn = psycopg2.connect(database='mydb', user='akaitochi',
                        password='secret123', host='localhost', port='5432')

cur = conn.cursor()

# Таблица "Книга"
cur.execute("""
    CREATE TABLE IF NOT EXISTS books.book (
            id SERIAL PRIMARY KEY,
            title VARCHAR(255) NOT NULL,
            author_id INTEGER REFERENCES author(id),
            publisher_id INTEGER REFERENCES publisher(id)
    );
            """)

# Таблица "Автор"
cur.execute("""
    CREATE TABLE IF NOT EXISTS books.author (
            id SERIAL PRIMARY KEY,
            name VARCHAR(255) NOT NULL
    );
            """)

# Таблица "Издательство"
cur.execute("""
    CREATE TABLE IF NOT EXISTS books.publisher (
            id SERIAL PRIMARY KEY,
            name VARCHAR(255) NOT NULL
    );
            """)

# Таблица "Справочник жанров"
cur.execute("""
    CREATE TABLE IF NOT EXISTS books.genre (
            id SERIAL PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            parent_id INTEGER REFERENCES genre(id)
    );
            """)

# Таблица "Критик"
cur.execute("""
    CREATE TABLE IF NOT EXISTS books.critic (
            id SERIAL PRIMARY KEY,
            name VARCHAR(255) NOT NULL
    );
            """)

# Таблица "Комментарий критика"
cur.execute("""
    CREATE TABLE IF NOT EXISTS books.critic_comment (
            id SERIAL PRIMARY KEY,
            critic_id INTEGER REFERENCES critic(id),
            book_id INTEGER REFERENCES book(id),
            page_number INTEGER,
            line_number INTEGER,
            comment TEXT NOT NULL
    );
            """)

# sql = 'SELECT * FROM genre'
# cur.execute(sql)
# tables = cur.fetchall()

cur.close()
conn.close()
