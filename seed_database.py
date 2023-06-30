import os
import json
import crud
import model
import server

from random import choice, randint

os.system("dropdb -U postgres movies_app")
os.system("createdb -U postgres movies_app")

model.connect_to_db(server.app)

with server.app.app_context():
    model.db.create_all()

    with open("data/movies.json") as f:
        movies_raw_data = json.loads(f.read())

        movies_in_db =[]

        for movie in movies_raw_data:
            title = movie["title"]
            synopsis= movie["synopsis"]
            movie_poster = movie["movie_poster"]

            new_movie = crud.create_movie(title, synopsis, movie_poster)

            movies_in_db.append(new_movie)

    model.db.session.add_all(movies_in_db)
    model.db.session.commit()
    print("Movies db successfully seeded")

    for n in range(5):
        email = f"user{n}@test.com"
        password = "test"
        username = f"user_{n}"

        new_user = crud.create_user(email, password, username)
        model.db.session.add(new_user)

        for _ in range(5):
            random_movie = choice(movies_in_db)
            score = randint(1,5)
            review = "One of the movies of all time."

            new_rating=crud.create_rating(new_user,random_movie, score, review)
            model.db.session.add(new_rating)


    model.db.session.commit()