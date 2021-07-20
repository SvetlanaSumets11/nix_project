"""
Initializing the variables required for tests
"""
PORT = 5000
NUM = 10

JSON = "application/json"
HEADERS = {"Content-Type": JSON, "Accept": JSON}


USER_LOGIN_DATA = [
    {"user_login": "KirillGlushko", "user_password": "123kirill"},
    {"user_login": "Dmitrovich", "user_password": "dmitrovich11"},
    {"user_login": "LizaSurova", "user_password": "surova1256"},
    {"user_login": "ValeraSinko", "user_password": "sinkolove"},
    {"user_login": "SvetlanaSum", "user_password": "superman"},
    {"user_login": "TanyaTit", "user_password": "titorenko12"},
    {"user_login": "AnnRudova", "user_password": "rudovabest"},
    {"user_login": "ArtemBerko", "user_password": "berkovich"},
    {"user_login": "RomanRut", "user_password": "rutchenko9"},
    {"user_login": "PavAnn", "user_password": "ann1290"}]

ENTITIES = ["users", "genres", "directors", "films"]

FILM_PART = ["gi", "Boy", "im", "IE", "44", "Math", "OVE", "f", "y", "END"]

GENRE_PART_EXIST = ["Psych", "ETECTI", "f", "omant", "aged", "ILL", "ANTA", "Dete", "Logy", "D"]
GENRE_PART_NOT_EXIST = \
    ["Crim", "come", "ORRo", "Omedy", "Cartoo", "ImE", "or", "RIM", "meDY", "hOr"]

DIRECTOR_PART_EXIST = ["sVETLA", "DanS", "kaya", "KA", "ANN", "lons", "ORT", "gnif", "Denis", "tri"]
DIRECTOR_PART_NOT_EXIST = ["ART", "oza", "StEp", "enKo", "irko", "OZ", "em", "AR", "Kirko", "PCH"]

YEAR_START = [2001, 2002, 2003, 2004, 2006, 2007, 2014, 2016, 2018, 2020]
YEAR_FINISH = [2007, 2020, 2014, 2016, 2022, 2018, 2021, 2010, 2021, 2021]

GENRE_1 = {"genre_name": "Psychology"}
DIRECTOR_1 = {"dir_first_name": "Divnaya", "dir_last_name": "Svetlana"}
FILM_1 = {"user_id": 1, "film_name": "1944", "release_date": "2001-12-22",
          "description": "Some description", "rating": 9.1, "poster": "http://some_link"}
USER_1 = {"user_login": "KirillGlushko", "first_name": "Glushko",
          "last_name": "Kirill", "email": "kirillglu@gmail.com"}


def start_finish() -> list:
    """
    The function generates a list of dates
    :return: date list
    """
    return [f"{start}/{finish}" for start, finish in zip(YEAR_START, YEAR_FINISH)]


def user_signup_data() -> list:
    """
    The function generates fake data for registration
    :return: List of fake user data
    """
    data = []
    for i in range(NUM):
        var = str(i) * 5
        data.append({"user_login": var, "user_password": var,
                     "first_name": var, "last_name": var, "email": var + "@gmail.com"})
    return data


def failed_rating() -> list:
    """
    The function generates invalid values to check the rating validation
    :return: List of numbers
    """
    return list(range(15, 30)) + list(range(-25, -1))


DATA_1 = [USER_1, GENRE_1, DIRECTOR_1, FILM_1]
USER_SIGNUP_DATA = user_signup_data()
RATING = failed_rating()
YEAR = start_finish()
