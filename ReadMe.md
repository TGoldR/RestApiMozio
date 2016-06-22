====================================
Polygon project using the Django Rest Framework
====================================

------------
Requirements
------------

1. Django
2. Django REST Framework

------------
Installation
------------


From Source
^^^^^^^^^^^

::

    $ git clone https://TGoldR/RestApiMozio.git
    $ cd RestApiMozio && pip install -e .


Running the example app
^^^^^^^^^^^^^^^^^^^^^^^

::

    $ git clone https://TGoldR/RestApiMozio.git
    $ cd RestApiMozio && pip install -e .
    $ django-admin.py runserver --settings=example.settings

Browse to http://localhost:8000


Running Tests
^^^^^^^^^^^^^

It is recommended to create a virtualenv for testing. Assuming it is already 
installed and activated:

::

    $ pip install -e .
    $ pip install -r requirements-development.txt
    $ py.test


-----
Usage
-----


``rest_framework_json_api`` assumes you are using class-based views in Django
Rest Framework.


Settings
^^^^^^^^

One can either add ``rest_framework_json_api.parsers.JSONParser`` and
``rest_framework_json_api.renderers.JSONRenderer`` to each ``ViewSet`` class, or
override ``settings.REST_FRAMEWORK``

::

    REST_FRAMEWORK = {
        'PAGE_SIZE': 10,
        'EXCEPTION_HANDLER': 'rest_framework_json_api.exceptions.exception_handler',
        'DEFAULT_PAGINATION_CLASS':
            'rest_framework_json_api.pagination.PageNumberPagination',
        'DEFAULT_PARSER_CLASSES': (
            'rest_framework_json_api.parsers.JSONParser',
            'rest_framework.parsers.FormParser',
            'rest_framework.parsers.MultiPartParser'
        ),
        'DEFAULT_RENDERER_CLASSES': (
            'rest_framework_json_api.renderers.JSONRenderer',
            'rest_framework.renderers.BrowsableAPIRenderer',
        ),
        'DEFAULT_METADATA_CLASS': 'rest_framework_json_api.metadata.JSONAPIMetadata',
    }

