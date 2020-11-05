import os
import click
import pandas as pd

APPLICATION_BASE_PATH = os.getcwd()
DEFAULT_RATING_FILE_PATH = os.path.join(APPLICATION_BASE_PATH, './data/ml-25m/ratings.csv')
DEFAULT_USER_RATING_FILE_PATH = os.path.join(APPLICATION_BASE_PATH, './data/analysis/user-mean-rating.csv')
DEFAULT_MOVIE_RATING_FILE_PATH = os.path.join(APPLICATION_BASE_PATH, './data/analysis/movie-mean-rating.csv')


@click.group('generate')
def cli_generate():
    pass


@cli_generate.command()
@click.option('--rating-file', default=DEFAULT_RATING_FILE_PATH, type=click.Path(exists=True))
@click.option('--out_file', default=DEFAULT_USER_RATING_FILE_PATH, type=click.Path())
def user_mean_rating(rating_file, out_file):
    """
    Generate User mean rating file
    """
    _generate_mean_rating(rating_file, out_file, lambda ratings: ratings.rating.groupby(ratings.userId).mean())


@cli_generate.command()
@click.option('--rating-file', default=DEFAULT_RATING_FILE_PATH, type=click.Path(exists=True))
@click.option('--out_file', default=DEFAULT_MOVIE_RATING_FILE_PATH, type=click.Path())
def movie_mean_rating(rating_file, out_file):
    """
    Generate Movie mean rating file
    """
    _generate_mean_rating(rating_file, out_file, lambda ratings: ratings.rating.groupby(ratings.movieId).mean())


def _generate_mean_rating(rating_file, out_file, generate_fun):
    ratings = pd.read_csv(rating_file)
    mean_rating = generate_fun(ratings)
    mean_rating.to_csv(out_file)
