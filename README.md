
# Xlator App!

## Running

```
BLUEMIX_API_KEY="<KEY>" BLUEMIX_API_URL="<URL>" python3 -m xlate
```

## Deployment 

```
sudo BLUEMIX_API_KEY="<KEY>" BLUEMIX_API_URL="<URL>"  docker-compose up --build 
```

Env vars above come from:
https://cloud.ibm.com/docs/services/language-translator?topic=language-translator-gettingstarted

## On AWS 

```
sudo docker run -p 80:9090 -e BLUEMIX_API_KEY="<KEY>" -e BLUEMIX_API_URL="https://gateway.watsonplatform.net/language-translator/api" -d manistal/xlate:latest
```
