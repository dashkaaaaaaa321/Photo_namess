import sqlite3
conn = sqlite3.connect("Blog.db")
cursore = conn.cursor()

cursore.execute('''
CREATE TABLE IF NOT EXISTS rublics(
   id INTEGER PRIMARY KEY,
   name TEXT);
''')

cursore.execute('''
CREATE TABLE IF NOT EXISTS users(
id INTEGER PRIMARY KEY,
full_name TEXT,
birth_date DATE,
role TEXT,
registration_date DATE);
''')

cursore.execute('''
CREATE TABLE IF NOT EXISTS posts(
id INTEGER PRIMARY KEY,
rublic_id INTEGER,
user_id INTEGER,
text TEXT,
FOREIGN KEY (rublic_id) REFERENCES Rublics(id),
FOREIGN KEY (user_id) REFERENCES Users(id));
''')

conn.commit()

rubrics_data = [
    ('1', 'Technology'),
    ('2', 'Travel'),
    ('3', 'Food'),
    ('4', 'Lifestyle'),
    ('5', 'Fashion')
]
cursore.executemany('INTEGER INTO rublics(id, name) VALUES(?,?);', rubrics_data)

users_data = [
    (1, 'Daria Boroznova', '2006-07-12', 'author', '2023-01-14'),
    (2, 'Ivan Cmolovskiy', '1990-06-24', 'reader', '2022-08-22'),
    (3, 'Anna Brown', '2008-08-10', 'author', '2021-09-30'),
    (4, 'Maria Novskaya', '1993-01-21', 'reader', '2023-12-29'),
    (5, 'Alex Browskiy', '1975-01-20', 'admin', '2020-01-31')
]
cursore.executemany('INSERT INTO users (id, full_name, birth_date, role, registration_date) VALUES (?, ?, ?, ?, ?);', users_data)

posts_data = [
    (1,1,1, ' Exploring the Latest Tech Trends'),
    (2,2,2, ' A Jorney Through the Mountains'),
    (3,3,3, 'Delicious |Recipes for Every Foodie'),
    (4,4,4, 'Balansing Work and Hobbies'),
    (5,5,5, 'Summer Fashion Essentials')
]

cursore.executemany('INSERT INTO posts (id, rublic_id, user_id, text) VALUES (?,?,?,?);', posts_data)
conn.commit()
conn.close()