# py-imdb-api-dev-client

A python client for [imdbapi.dev](https://imdbapi.dev/) REST services

## Links

* https://imdbapi.dev/
  * https://v2.imdbapi.dev/imdbapi.swagger.yaml
* https://swagger.io/tools/swagger-codegen/

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

# Various fixes for `ModuleNotFoundError: No module named 'imdbapi'` errors
sed -e 's/from imdbapi/from py_imdb_api_dev_client.imdbapi/g' -i py_imdb_api_dev_client/py_imdb_api_dev_client/__init__.py 
sed -e 's/from imdbapi/from py_imdb_api_dev_client.imdbapi/g' -i py_imdb_api_dev_client/py_imdb_api_dev_client/imdbapi/__init__.py

```

## Install

```bash
# From release (must resolve manually the requirements)
wget https://github.com/moz667/py-imdb-api-dev-client/releases/download/1.0.0/py-imdb-api-dev-client_1.0.0.zip
unzip py-imdb-api-dev-client_1.0.0.zip
cd py_imdb_api_dev_client/
python setup.py install

# Or with pip:
pip install git+https://github.com/moz667/py-imdb-api-dev-client@tags/1.0.0#subdirectory=py-imdb-api-dev-client
```

## Configure as requirement

Im too lazy to read and mantain a pip package so...

```
py-imdb-api-dev-client @ git+https://github.com/moz667/py-imdb-api-dev-client@tags/1.0.0#subdirectory=py-imdb-api-dev-client
```

## Test & samples

```shell
$ python
# >>> from py_imdb_api_dev_client.imdbapi.title_api import TitleApi
# >>> TitleApi().i_mdb_api_service_get_title('tt0168122')
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

## TODO

* [ ] Register a pip package
* [ ] Create a facade to simplify (swagger codegen its a bit "intense".)
