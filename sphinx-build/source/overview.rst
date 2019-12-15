Overview 
==========

XLate is a Lightweight text translation front-end for IBM's Watson Language Translator. 

Introduction 
^^^^^^^^^^^^^

There are more than 6,500 languages used around the globe, yet it's more important than ever to understand one another. 
XLate was designed to be as Lightweight as possible, leveraging the power of Watson to do all the heavy lifting without taxing your deployments. 
Provide high speed text translation, without all the overhead of the compute resources to power it. 

Components
^^^^^^^^^^^^

XLate is effectively made up of two components, the Flask application that handles the routing and rendering of the application, and the bluemix api context which handles the translation offload to the IBM Cloud. 

You can find details about the component implementations in the :doc:`API Docs </apidoc>`

**Flask Frontend**

The front-end web service is powered by Flask. Flask is a WSGI framework which allows us to serve web traffic to and from the client by simply defining routes and their functions. This makes the code very maintainable and extensible. 

Future development will focus on providing an API blueprint to go along with the base translator views, this would allow users to serve their own APIs, which solves issues in IBMs own API by allowing users to perform transformations on the data it returns. 

You can find more information about ``Flask``:    
https://www.palletsprojects.com/p/flask/

**Bluemix API**

The back-end is a simple class that provides an API Context for the IBM Cloud connection, leveraging the python library 'requests', and IBMs RESTful API. 

The implementation provides the basis of the data-model in the framework and could also extend SQLALchemy database models in order to cache responses from the server. 

You can find out more information about ``requests``:    
https://requests.readthedocs.io/en/master/

You can find more information about IBM's ``Language Translator API``:    
https://cloud.ibm.com/docs/services/language-translator?topic=language-translator-gettingstarted
