.. XLate documentation master file, created by
   sphinx-quickstart on Sat Dec 14 13:20:43 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to the XLate documentation!
=================================

.. toctree::
   :maxdepth: 1

   :ref:`overview`
   :ref:`getting-started`
   bluemix_translate_api
   translator

.. _overview:
Overview 
==========

Some information is in here

.. _getting-started:
Getting Started 
==================

To develop or contribute to Xlate, you can get started once you register for a Bluemix API key and URL (follow the instructions [here](https://cloud.ibm.com/docs/services/language-translator?topic=language-translator-gettingstarted))

There are two ways to run the application:

Standalone Python App with Flask Debug
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
``BLUEMIX_API_KEY="<KEY>" BLUEMIX_API_URL="<URL>" python3 -m xlate``

UWSGI with Docker-Compose 
^^^^^^^^^^^^^^^^^^^^^^^^^^^
``BLUEMIX_API_KEY="<KEY>" BLUEMIX_API_URL="<URL>" docker-compose up --build``

Development and Deployment Model
=================================

.. image:: ../MSCS621_Xlate_ArchDiagram.png


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
