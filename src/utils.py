import csv
from fuzzywuzzy import fuzz
from gensim.parsing.preprocessing import remove_stopwords
from PIL import Image


def show_planimetry():
    """
    prints planimetry image
    :return:
    """
    im = Image.open("./data/videoteca.png")
    im.show()


def find_movie(movie):
    csv_file = csv.reader(open('./data/MovieLens/movies.csv', "r", encoding="utf8"), delimiter=",")
    max = 0
    for row in csv_file:
        if fuzz.ratio(remove_stopwords(movie.lower().replace(",", " ")),
                      remove_stopwords(row[1].lower().replace(",", " "))) > 60:
            if fuzz.ratio(remove_stopwords(movie.lower().replace(",", " ")),
                          remove_stopwords(row[1].lower().replace(",", " "))) > max:
                max = fuzz.ratio(remove_stopwords(movie.lower().replace(",", " ")),
                                 remove_stopwords(row[1].lower().replace(",", " ")))
                ris = row
    return ris


def get_movie_id(movie):
    ris = find_movie(movie)[0]
    return ris


def get_movie_name(movie):
    ris = find_movie(movie)[1]
    return ris


def get_rack(movie_id):
    n_rack = int(float(movie_id) / 3520) + 1
    return n_rack


def get_nodes(rack):
    if rack == 1 or rack == 2 or rack == 3:
        return 1
    if rack == 15:
        return 2
    if rack == 4 or rack == 5:
        return 3
    if rack == 6 or rack == 7 or rack == 9:
        return 4
    if rack == 16 or rack == 55:
        return 5
    if rack == 54:
        return 7
    if rack == 53:
        return 9
    if rack == 25 or rack == 52:
        return 10
    if rack == 8:
        return 11
    if rack == 20 or rack == 24:
        return 12
    if rack == 17 or rack == 18 or rack == 19:
        return 14
    if rack == 10 or rack == 11 or rack == 12:
        return 15
    if rack == 13 or rack == 14:
        return 16
    if rack == 21:
        return 17
    if rack == 22:
        return 18
    if rack == 27:
        return 19
    if rack == 23 or rack == 26:
        return 20
    if rack == 29 or rack == 31 or rack == 34:
        return 22
    if rack == 35 or rack == 37 or rack == 38:
        return 23
    if rack == 33 or rack == 36:
        return 24
    if rack == 32:
        return 25
    if rack == 28 or rack == 30:
        return 26
    if rack == 50:
        return 27
    if rack == 49 or rack == 51:
        return 29
    if rack == 48:
        return 30
    if rack == 39 or rack == 42:
        return 31
    if rack == 41:
        return 32
    if rack == 40 or rack == 46:
        return 33
    if rack == 47:
        return 34
    if rack == 43 or rack == 44:
        return 35
