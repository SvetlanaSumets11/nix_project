
from project.models.films_directors import FilmDirector
from project.models.films_genres import FilmGenre
from project.models.directors import Director
from project.models.genres import Genre
from project.models.users import User
from project.models.films import Film

from project import db


def seed_user():
    db.session.add(User(user_login="KirillGlushko", user_password="123kirill", first_name="Glushko",
                        last_name="Kirill", email="kirillglu@gmail.com"))
    db.session.add(User(user_login="Dmitrovich", user_password="dmitrovich11", first_name="Dmitro",
                        last_name="Kirill", email="dmitrovich@gmail.com"))
    db.session.add(User(user_login="RomanRut", user_password="rutchenko9", first_name="Rutchenko",
                        last_name="Poman", email="rutchenko@gmail.com"))
    db.session.add(User(user_login="TanyaTit", user_password="titorenko12", first_name="Titorenko",
                        last_name="Tanya", email="titorenko@gmail.com"))
    db.session.add(User(user_login="LizaSurova", user_password="surova1256", first_name="Surova",
                        last_name="Liza", email="lizok@gmail.com"))
    db.session.add(User(user_login="AnnRudova", user_password="rudovabest", first_name="Rudova",
                        last_name="Anna", email="annrud@gmail.com"))
    db.session.add(User(user_login="SvetlanaSum", user_password="superman", first_name="Sumets",
                        last_name="Svetlana", email="svetasumets@gmail.com"))
    db.session.add(User(user_login="ValeraSinko", user_password="sinkolove", first_name="Sinko",
                        last_name="Valera", email="sinkoval@gmail.com"))
    db.session.add(User(user_login="ArtemBerko", user_password="berkovich", first_name="Berko",
                        last_name="Artem", email="berkovich@gmail.com"))
    db.session.add(User(user_login="PavAnn", user_password="ann1290", first_name="Pavlenko",
                        last_name="Anna", email="pavlenko@gmail.com"))
    db.session.add(User(user_login="Katusha", user_password="123456", first_name="Drunko",
                        last_name="Katya", email="drunkokatya@gmail.com"))
    db.session.commit()


def seed_genre():
    db.session.add(Genre(genre_name="Psychology"))
    db.session.add(Genre(genre_name="Romantic"))
    db.session.add(Genre(genre_name="Thriller"))
    db.session.add(Genre(genre_name="Tragedy"))
    db.session.add(Genre(genre_name="Comedy"))
    db.session.add(Genre(genre_name="Horror"))

    db.session.commit()


def seed_director():
    db.session.add(Director(dir_first_name="Divnaya", dir_last_name="Svetlana"))
    db.session.add(Director(dir_first_name="Stepchenko", dir_last_name="Denis"))
    db.session.add(Director(dir_first_name="Danskaya", dir_last_name="Katya"))
    db.session.add(Director(dir_first_name="Lonskaya", dir_last_name="Katya"))
    db.session.add(Director(dir_first_name="Stognif", dir_last_name="Kirill"))
    db.session.add(Director(dir_first_name="Kirko", dir_last_name="Kirill"))
    db.session.add(Director(dir_first_name="Tringer", dir_last_name="Ann"))
    db.session.add(Director(dir_first_name="Surko", dir_last_name="Denis"))
    db.session.add(Director(dir_first_name="Kutro", dir_last_name="Katya"))
    db.session.add(Director(dir_first_name="Kurort", dir_last_name="Ann"))
    db.session.add(Director(dir_first_name="Roza", dir_last_name="Artem"))

    db.session.commit()


def seed_film():
    db.session.add(Film(user_id=1, film_name="1944", release_date='2001-12-22',
                        description="Some description", rating=9.1, poster="http://some_link"))
    db.session.add(Film(user_id=1, film_name="Father", release_date='1999-09-9',
                        description="Some description", rating=7.8, poster="http://some_link"))
    db.session.add(Film(user_id=2, film_name="Family", release_date='2003-02-21',
                        description="Some description", rating=7.4, poster="http://some_link"))
    db.session.add(Film(user_id=3, film_name="Friend", release_date='2005-03-11',
                        description="Some description", rating=5.4, poster="http://some_link"))
    db.session.add(Film(user_id=4, film_name="Time", release_date='2004-11-16',
                        description="Some description", rating=1.2, poster="http://some_link"))
    db.session.add(Film(user_id=5, film_name="Boyfriend", release_date='2021-4-4',
                        description="Some description", rating=2.5, poster="http://some_link"))
    db.session.add(Film(user_id=6, film_name="Girl", release_date='2007-07-1',
                        description="Some description", rating=6.2, poster="http://some_link"))
    db.session.add(Film(user_id=7, film_name="Boy", release_date='2020-08-10',
                        description="Some description", rating=9.1, poster="http://some_link"))
    db.session.add(Film(user_id=8, film_name="Mather", release_date='2020-01-12',
                        description="Some description", rating=5.0, poster="http://some_link"))
    db.session.add(Film(user_id=9, film_name="Love", release_date='2020-01-12',
                        description="Some description", rating=5.2, poster="http://some_link"))
    db.session.add(Film(user_id=10, film_name="Girlfriend", release_date='1997-10-11',
                        description="Some description", rating=8.7, poster="http://some_link"))

    db.session.commit()


def seed_film_director():
    db.session.add(FilmDirector(film_id=1, director_id=1))
    db.session.add(FilmDirector(film_id=1, director_id=7))
    db.session.add(FilmDirector(film_id=1, director_id=9))

    db.session.add(FilmDirector(film_id=2, director_id=5))

    db.session.add(FilmDirector(film_id=4, director_id=5))
    db.session.add(FilmDirector(film_id=4, director_id=4))

    db.session.add(FilmDirector(film_id=6, director_id=8))

    db.session.add(FilmDirector(film_id=8, director_id=7))
    db.session.add(FilmDirector(film_id=8, director_id=1))

    db.session.add(FilmDirector(film_id=10, director_id=3))
    db.session.add(FilmDirector(film_id=10, director_id=4))
    db.session.add(FilmDirector(film_id=10, director_id=10))

    db.session.commit()


def seed_film_genre():
    db.session.add(FilmGenre(film_id=1, genre_id=4))
    db.session.add(FilmGenre(film_id=1, genre_id=6))
    db.session.add(FilmGenre(film_id=1, genre_id=5))

    db.session.add(FilmGenre(film_id=2, genre_id=3))

    db.session.add(FilmGenre(film_id=3, genre_id=5))
    db.session.add(FilmGenre(film_id=3, genre_id=4))

    db.session.add(FilmGenre(film_id=5, genre_id=1))

    db.session.add(FilmGenre(film_id=6, genre_id=6))
    db.session.add(FilmGenre(film_id=6, genre_id=1))
    db.session.add(FilmGenre(film_id=6, genre_id=2))

    db.session.add(FilmGenre(film_id=8, genre_id=5))

    db.session.add(FilmGenre(film_id=9, genre_id=2))
    db.session.add(FilmGenre(film_id=9, genre_id=3))

    db.session.add(FilmGenre(film_id=10, genre_id=6))
    db.session.add(FilmGenre(film_id=10, genre_id=4))

    db.session.add(FilmGenre(film_id=11, genre_id=5))

    db.session.commit()


def seeder():
    seed_user()
    seed_film()
    seed_genre()
    seed_director()
    seed_film_genre()
    seed_film_director()

    user = User.query.get_or_404(7)
    user.set_admin()

    db.session.commit()
