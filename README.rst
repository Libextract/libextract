Libextract: extract data from websites
======================================

.. image:: https://travis-ci.org/datalib/libextract.svg?branch=master
    :target: https://travis-ci.org/datalib/libextract

::

 ⠀⠀ ⢀⣾⣿⣿⣿⠿⠿⠟⠻⠿⢿⣿⣿⣿⡆
 ⠀⠀⠀⢰⣿⣿⡿⠂⠀⠀⠀⠀⠀⠀⠈⠉⢻⡇ 
⠀⠀⠀⠈⠿⣿⣇⣠⠤⠤⠤⢤⣀⣤⠤⠤⣺⡏
 ⠀⠀⠀⠀⠐⢉⣯⠹⣀⣀⣢⡸⠉⢏⡄⣀⣯⠁
 ⠀⠀ ⠀⠡⠀⢹⣆⠀⠀⠀⣀⡀⡰⠀⢠⠖⠂
 ⠀⠀⠀⠀⠀⠈⠙⣿⣿⠀⠠⠚⢋⡁⠀⡜
 ⠀⠀⠀⠀⠀⠀⢸⠈⠙⠦⣤⣀⣤⣤⡼⠁
          ⣿⣿⣿⣿⣿⣄


Libextract is a `statistics-enabled <https://github.com/datalib/StatsCounter>`_
data extraction library that works on HTML and XML documents and written in 
Python. Originating from `eatiht <http://rodricios.github.io/eatiht/>`_, the
extraction algorithm works by making one simple assumption: *data appear as 
collections of repetitive elements*. You can read about the reasoning 
`here <http://rodricios.github.io/posts/solving_the_data_extraction_problem.html>`_. 


Overview
--------

`libextract.api.extract(document, encoding='utf-8', count=5)` 
    Given an html *document*, and optionally the *encoding*, return
    a list of nodes likely containing data (5 by default).


Installation
------------

::

    pip install libextract

Usage
-----

Due to our simple definition of "data", we open up a single
interfaceable method. Post-processing is up to you. 

.. code-block:: python

    from requests import get
    from libextract.api import extract

    r = get('http://en.wikipedia.org/wiki/Information_extraction')
    textnodes = list(extract(r.content))


Using lxml's built-in methods for post-processing:

.. code-block:: python

    >> print(textnodes[0].text_content())
    Information extraction (IE) is the task of automatically extracting structured information...


The extraction algo is agnostic to article text as it is with
tabular data:

.. code-block:: python

    height_data = get("http://en.wikipedia.org/wiki/Human_height")
    tabs = list(extract(height_data.content))
    

.. code-block:: python

    >> [elem.text_content() for elem in tabs[0].iter('th')]
    ['Country/Region',
     'Average male height',
     'Average female height',
     ...]

Dependencies
~~~~~~~~~~~~

::

    lxml
    statscounter

Disclaimer
~~~~~~~~~~

This project is still in its infancy; and advice and suggestions as
to what this library could and should be would be greatly appreciated

:) 
