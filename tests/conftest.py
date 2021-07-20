"""
Module for creating a fixture
"""
import pytest
from services.web.project.models.films import Film
from services.web.project.models.genres import Genre
from services.web.project.models.users import User
from services.web.project.models.directors import Director
from services.web.project.models.films_genres import FilmGenre
from services.web.project.models.films_directors import FilmDirector


@pytest.fixture()
def new_entity() -> list:
    """
    Fixture that creates a list of objects of all existing entities
    :return: list of objects of all existing entities
    """
    entities = []
    entities.append(Director("Filanova", "Svetlana"))
    entities.append(Genre("Military"))
    entities.append(User("KovalenkoDen", "123321", "Kovalenko", "Denis", "kovalenko@gmail.com"))
    entities.append(Film(1, "Some film", "2004-11-16", "Some description", 3.2, "http://some_link"))
    entities.append(FilmGenre(1, 1))
    entities.append(FilmDirector(2, 2))
    return entities
