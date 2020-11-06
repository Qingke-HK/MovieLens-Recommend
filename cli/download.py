import os
import tqdm
import click
import zipfile
import requests

APPLICATION_BASE_PATH = os.getcwd()
MOVIE_LENS_DATASOURCE_FILE_LIST = [
    "ml-1m",
    "ml-10m",
    "ml-25m",
    "ml-100k",
    "ml-latest",
    "tag-genome",
    "ml-20mx16x32"
]
MOVIE_LENS_DATASOURCE_FILE_TYPE = {
    'ml-1m': 'zip',
    'ml-10m': 'zip',
    'ml-25m': 'zip',
    'ml-100k': 'zip',
    'ml-latest': 'zip',
    'tag-genome': 'zip',
    'ml-20mx16x32': 'tar'
}
DEFAULT_MOVIE_LENS_DATASOURCE = 'ml-100k'

DEFAULT_DOWNLOAD_DIR_PATH = f'{APPLICATION_BASE_PATH}/data'
MOVIE_LENS_DOWNLOAD_URL_PREFIX = 'http://files.grouplens.org/datasets/movielens/'


@click.command('download')
@click.argument('datasource',
                default=DEFAULT_MOVIE_LENS_DATASOURCE,
                type=click.Choice(MOVIE_LENS_DATASOURCE_FILE_LIST, case_sensitive=False))
@click.option('--file-path', type=click.Path(exists=True))
def cli_download(datasource, file_path):
    file_type = MOVIE_LENS_DATASOURCE_FILE_TYPE[datasource]
    file_name = f'{datasource}.{file_type}'

    response = requests.get(f'{MOVIE_LENS_DOWNLOAD_URL_PREFIX}/{file_name}', stream=True)

    chunk_size = 1024
    file_size = int(response.headers['content-length'])
    pbar = tqdm.tqdm(file_name, total=file_size)

    download_file_path = f'{DEFAULT_DOWNLOAD_DIR_PATH}/{file_name}' if not file_path else file_path
    with open(download_file_path, 'wb') as file:
        for file_chunk_data in response.iter_content(chunk_size=chunk_size):
            file.write(file_chunk_data)
            pbar.update(len(file_chunk_data))

    pbar.close()

    if file_type != 'zip':
        raise NotImplementedError()

    download_zip_file = zipfile.ZipFile(download_file_path)
    download_zip_file.extractall(DEFAULT_DOWNLOAD_DIR_PATH)
