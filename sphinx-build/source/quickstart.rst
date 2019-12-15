Quickstart
==================

To develop or contribute to Xlate, you can get started once you register for a Bluemix API key: 

https://cloud.ibm.com/docs/services/language-translator?topic=language-translator-gettingstarted

There are two ways to run the application:

Standalone Python App with Flask Debug
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
``BLUEMIX_API_KEY="<KEY>" BLUEMIX_API_URL="<URL>" python3 -m xlate``

UWSGI with Docker-Compose 
^^^^^^^^^^^^^^^^^^^^^^^^^^^
``BLUEMIX_API_KEY="<KEY>" BLUEMIX_API_URL="<URL>" docker-compose up --build``
