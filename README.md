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
```

## Install

```bash
# From release (must resolve manually the requirements)
wget https://github.com/moz667/py-imdb-api-dev-client/releases/download/2.7.12/py-imdb-api-dev-client_2.7.12.zip
unzip py-imdb-api-dev-client_2.7.12.zip
cd py_imdb_api_dev_client/
python setup.py install

# Or with pip:
pip install git+https://github.com/moz667/py-imdb-api-dev-client@tags/2.7.12#subdirectory=py-imdb-api-dev-client
```

## Configure as requirement

Im too lazy to read and mantain a pip package so...

```
py-imdb-api-dev-client @ git+https://github.com/moz667/py-imdb-api-dev-client@tags/2.7.12#subdirectory=py-imdb-api-dev-client
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

## Generate a release

```bash
# 1. Set TAG version
TAG="<version-tagged>"

# 2. Create a temporary directory
cd /tmp
mkdir /tmp/release-$TAG
cd /tmp/release-$TAG

# 3. Pull sources
git clone --depth 1 --branch $TAG https://github.com/moz667/py-imdb-api-dev-client .

# 4. Zip relase file
zip -r py-imdb-api-dev-client_$TAG.zip py-imdb-api-dev-client

# 5. Goto github and add manually the new relases

# 6. Delete `/tmp/release-$TAG`
```

## TODO

* [ ] Register a pip package
* [ ] Create a facade to simplify (swagger codegen its a bit "intense".)
