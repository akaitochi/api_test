CREATE SCHEMA books

CREATE TABLE IF NOT EXISTS books.book (
            id SERIAL PRIMARY KEY,
            title VARCHAR(255) NOT NULL,
            author_id INTEGER REFERENCES author(id),
            genre_id INTEGER REFERENCES genre(id),
            publisher_id INTEGER REFERENCES publisher(id)
    );

CREATE TABLE IF NOT EXISTS books.author (
            id SERIAL PRIMARY KEY,
            name VARCHAR(255) NOT NULL
    );

CREATE TABLE IF NOT EXISTS books.publisher (
            id SERIAL PRIMARY KEY,
            name VARCHAR(255) NOT NULL
    );

CREATE TABLE IF NOT EXISTS books.genre (
            id SERIAL PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            parent_id INTEGER REFERENCES genre(id)
    );

CREATE TABLE IF NOT EXISTS books.critic (
            id SERIAL PRIMARY KEY,
            name VARCHAR(255) NOT NULL
    );

CREATE TABLE IF NOT EXISTS books.critic_comment (
            id SERIAL PRIMARY KEY,
            critic_id INTEGER REFERENCES critic(id),
            book_id INTEGER REFERENCES book(id),
            page_number INTEGER,
            line_number INTEGER,
            comment TEXT NOT NULL
    );


