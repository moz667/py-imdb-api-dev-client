# py-imdb-api-dev-client

A Client for imdbapi.dev REST services


## Generate

```bash
user_id=`id -u`
group_id=`id -g`

docker run --rm -it --user $user_id:$group_id \
    --volume ./imdbapi.swagger.yaml:/imdbapi.swagger.yaml \
    --volume ./imdbapi.swagger.config.json:/imdbapi.swagger.config.json \
    --volume ./py-imdb-api-dev-client:/py-imdb-api-dev-client \
    swaggerapi/swagger-codegen-cli:latest generate \
    -i /imdbapi.swagger.yaml \
    -o /py-imdb-api-dev-client -c /imdbapi.swagger.config.json \
    --api-package imdbapi \
    -l python

sed -e 's/from imdbapi/from py_imdb_api_dev_client.imdbapi/g' -i py_imdb_api_dev_client/py_imdb_api_dev_client/__init__.py 
sed -e 's/from imdbapi/from py_imdb_api_dev_client.imdbapi/g' -i py_imdb_api_dev_client/py_imdb_api_dev_client/imdbapi/__init__.py
```

## Install

```bash
cd py_imdb_api_dev_client/
python setup.py install
```

## Test

```shell
$ python
# >>> from py_imdb_api_dev_client.imdbapi.title_api import TitleApi
# >>> title_api = TitleApi()
# >>> title_api.i_mdb_api_service_get_title('tt0168122')
# {'end_year': None,
#  'genres': ['Biography', 'Drama', 'History'],
#  'id': 'tt0168122',
#  'is_adult': None,
#  'original_title': None,
#  'plot': 'History of Apple and Microsoft.',
#  'primary_image': {'height': 500,
#                    'url': 'https://m.media-amazon.com/images/M/MV5BNDc2NTE0NzE4N15BMl5BanBnXkFtZTgwMDQ5MzgwMzE@._V1_.jpg',
#                    'width': 350},
#  'primary_title': 'Pirates of Silicon Valley',
#  'rating': {'aggregate_rating': 7.2, 'votes_count': 25743},
#  'runtime_minutes': 95,
#  'start_year': 1999,
#  'type': 'tvMovie'}
```