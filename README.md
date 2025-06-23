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
```
