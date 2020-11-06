import os
import click
import pandas as pd

APPLICATION_BASE_PATH = os.getcwd()
DEFAULT_USER_MEAN_RATING_FILE_PATH = f'{APPLICATION_BASE_PATH}/data/analysis/user-mean-rating.csv'
DEFAULT_MOVIE_MEAN_RATING_FILE_PATH = f'{APPLICATION_BASE_PATH}/data/analysis/movie-mean-rating.csv'


@click.group('analysis')
def cli_analysis():
    pass


@cli_analysis.command()
@click.option('--mean-file', default=DEFAULT_USER_MEAN_RATING_FILE_PATH, type=click.Path(exists=True))
@click.argument('ids', nargs=-1, type=click.INT)
def user_mean_rating(mean_file, ids):
    """
    Get User mean rating by user id
    """
    means = pd.read_csv(mean_file)
    click.echo(means[means.userId.isin(ids)])


@cli_analysis.command()
@click.option('--mean-file', default=DEFAULT_MOVIE_MEAN_RATING_FILE_PATH, type=click.Path(exists=True))
@click.argument('ids', nargs=-1, type=click.INT)
def movie_mean_rating(mean_file, ids):
    """
        Get Movie mean rating by movie id
    """
    means = pd.read_csv(mean_file)
    click.echo(means[means.movieId.isin(ids)])
