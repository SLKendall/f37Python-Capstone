from model import User, Movie, Rating, connect_to_db

def create_user(email, password, username):

    new_user = User(email=email, password=password, username=username)
    return new_user

def get_users():
    return User.query.all()

def get_user_by_email(email):
    return User.query.filter_by(email=email).first()

def get_user_by_id(user_id):
    return User.query.get(user_id)

def create_movie(title, synopsis, movie_poster):
    new_movie = Movie(
        title=title,
        synopsis=synopsis,
        movie_poster=movie_poster
    )
    return new_movie

def get_movies():
    return Movie.query.all()

def get_movie_by_id(movie_id):
    return Movie.query.get(movie_id)

def create_rating(user, movie, score, review):
    new_rating=Rating(
        user=user,
        movie=movie,
        score=score,
        review=review
    )

    return new_rating

#def update_rating(user, movie, review, score):

# def delete_rating(user_id):
#     user = User.query.get(user_id)

#     if user:
#         Rating.query.filter_by(user_id=user_id).delete()
#         return True
    
#     return False

if __name__ == '__main__':
    from server import app
    connect_to_db(app)