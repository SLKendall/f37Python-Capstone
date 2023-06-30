import os
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):

    __tablename__ = "users"

    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    username = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"<User user_id={self.user_id} email={self.email} username = {self.username}>"

class Movie(db.Model):

    __tablename__ = "movies"

    movie_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    title = db.Column(db.String)
    synopsis = db.Column(db.Text)
    movie_poster = db.Column(db.String)

    def __repr__(self):
        return f"<Movie movie_id={self.movie_id} title={self.title}>"

class Rating(db.Model):

    __tablename__ = "ratings"

    rating_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    score = db.Column(db.Integer)
    review = db.Column(db.Text)
    movie_id = db.Column(db.Integer, db.ForeignKey("movies.movie_id"))
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))

    movie = db.relationship("Movie", backref="ratings", lazy=False)
    user = db.relationship("User", backref="ratings", lazy=False)

    def __repr__(self):
        return f"<Rating rating_id={self.rating_id} score={self.score} review={self.review}"


def connect_to_db(flask_app, db_uri=os.environ["DATABASE_URI"]):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)

    print("Database connected.")

if __name__ == "__main__":
    from server import app

    connect_to_db(app)