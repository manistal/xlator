
# Xlator App!

## Running

```
BLUEMIX_API_KEY="<KEY>" BLUEMIX_API_URL="<URL>" python3 -m xlate
```

## Deployment 

```
sudo docker run -d -t -i \ 
    -e BLUEMIX_API_KEY="<KEY>"
    -e BLUEMIX_API_URL="<URL>"
    -p 80:80 \
    --link redis:redis \  
    --name container_name dockerhub_id/image_name
```

Env vars above come from:
https://cloud.ibm.com/docs/services/language-translator?topic=language-translator-gettingstarted
