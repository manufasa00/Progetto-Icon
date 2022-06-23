import os
import pandas as pd
from scipy.sparse import csr_matrix
from sklearn.neighbors import NearestNeighbors
from fuzzywuzzy import fuzz
from gensim.parsing.preprocessing import remove_stopwords
import RicercaGrafo
import utils


class KnnRecommender:
    def __init__(self):
        self.path_movies = './data/MovieLens/movies.csv'
        self.path_ratings = './data/MovieLens/ratings.csv'
        self.movie_rating_thres = 10
        self.user_rating_thres = 10
        self.model = NearestNeighbors()
        self.model.set_params(**{
            'n_neighbors': 20,
            'algorithm': 'auto',
            'metric': 'cosine',
        })

    def _prep_data(self):
        """
        prepare data for recommender
        join dataframes
        """
        # read data
        df_movies = pd.read_csv(
            os.path.join(self.path_movies),
            usecols=['movieId', 'title'],
            dtype={'movieId': 'int32', 'title': 'str'})

        df_ratings = pd.read_csv(
            os.path.join(self.path_ratings),
            usecols=['userId', 'movieId', 'rating'],
            dtype={'userId': 'int32', 'movieId': 'int32', 'rating': 'float32'})

        # filter users who rated less than 10 movies and movies with less than 10 rates
        df_movies_cnt = pd.DataFrame(df_ratings.groupby('movieId').size(), columns=['count'])
        popular_movies = list(df_movies_cnt.query('count >= @self.movie_rating_thres').index)
        movies_filter = df_ratings.movieId.isin(popular_movies).values

        df_users_cnt = pd.DataFrame(df_ratings.groupby('userId').size(), columns=['count'])
        active_users = list(df_users_cnt.query('count >= @self.user_rating_thres').index)
        users_filter = df_ratings.userId.isin(active_users).values

        df_ratings_filtered = df_ratings[movies_filter & users_filter]

        # create movie user matrix

        movie_user_mat = df_ratings_filtered.pivot(index='movieId', columns='userId', values='rating').fillna(0)

        # hashmap from movie title to index

        hashmap = {
            movie: i for i, movie in
            enumerate(list(df_movies.set_index('movieId').loc[movie_user_mat.index].title))
        }
        movie_user_mat_sparse = csr_matrix(movie_user_mat.values)
        return movie_user_mat_sparse, hashmap

    def _fuzzy_matching(self, hashmap, fav_movie):
        """
        return the closest match via fuzzy ratio.
        If no match found, return None

        params:

        hashmap: dict, map movie title name to index of the movie in data

        fav_movie: str, name of user input movie

        return:

        index of the closest match
        """
        match_tuple = []
        # get match
        for title, idx in hashmap.items():
            ratio = fuzz.ratio(remove_stopwords(title.lower().replace(",", " ")),
                               remove_stopwords(fav_movie.lower().replace(",", " ")))
            if ratio >= 60:
                match_tuple.append((title, idx, ratio))
        # sort
        match_tuple = sorted(match_tuple, key=lambda x: x[2])[::-1]
        if not match_tuple:
            print('No results found')
        else:
            print('Found results: \n' + str([x[0] for x in match_tuple]))
            return match_tuple[0][1]

    def _inference(self, model, data, hashmap,
                   fav_movie, n_recommendations):
        """
        return top n similar movie recommendations based on user's input movie

        params:

        model: sklearn model, knn model

        data: movie-user matrix

        hashmap: dict, map movie title name to index of the movie in data

        fav_movie: str, name of user input movie

        n_recommendations: int, top n recommendations

        return:

        list of top n similar movie recommendations
        """
        # fit
        model.fit(data)
        # get input movie index
        print('Your movie is:', fav_movie)
        try:
            idx = self._fuzzy_matching(hashmap, fav_movie)
            # inference
            distances, indices = model.kneighbors(
                data[idx],
                n_neighbors=n_recommendations + 1)
        except IndexError:
            exit(0)
        # get list of raw idx of recommendations
        raw_recommends = \
            sorted(
                list(
                    zip(
                        indices.squeeze().tolist(),
                        distances.squeeze().tolist()
                    )
                ),
                key=lambda x: x[1]
            )[1:6]

        # return recommendation (movieId, distance)
        return raw_recommends

    def make_recommendations(self, fav_movie, n_recommendations):
        """
        make top n movie recommendations

        params:

        fav_movie: str, name of user input movie

        n_recommendations: int, top n recommendations
        """
        # get data
        movie_user_mat_sparse, hashmap = self._prep_data()
        # get recommendations
        raw_recommends = self._inference(
            self.model, movie_user_mat_sparse, hashmap,
            fav_movie, n_recommendations)
        # print results
        movie_list = []
        reverse_hashmap = {v: k for k, v in hashmap.items()}
        print('Recommendations for : ' + fav_movie)
        for i, (idx, dist) in enumerate(raw_recommends):
            print('{0}: {1}, with distance '
                  'of {2}'.format(i + 1, reverse_hashmap[idx], dist))
            movie_list.append(reverse_hashmap[idx])
        return movie_list


if __name__ == '__main__':
    input("Press [enter] to show planimetry of the shop")
    utils.show_planimetry()
    movie_name = input('Insert favourite movie name:\n')
    top_n = 5
    recommender = KnnRecommender()
    recommendation = recommender.make_recommendations(movie_name, top_n)
    if recommendation is not None:
        RicercaGrafo.research(recommendation)
    else:
        print("Not found")
