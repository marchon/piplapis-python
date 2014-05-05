piplapis Python Library
===========================

This is a Python client library for easily integrating Pipl's APIs into your application.

      An api to use PIPL.com  hosted on github at https://github.com/marchon/piplapis-python

      Python wrapper for easily making calls to Pipl's API Services.

      There are 3 API's included

      1) Search API
      2) Name API
      3) Thumbnail API

      Detailed Information is available at: http://dev.pipl.com/docs/read/Home

      PIPL SEARCH API
      ---------------------------------------------------------------------------
      Pipl's Search API allows you to query with the information you have about
      a person (his name, address, email, phone, username and more) and in response
      get all the data available on him on the web.


      PIPL NAME API
      ---------------------------------------------------------------------------
      Pipl's Name API provides useful utilities for applications that need to work
      with people names, the utilities include:
      - Parsing a raw name into prefix/first-name/middle-name/last-name/suffix.
      - Getting the gender that's most common for people with the name.
      - Getting possible nicknames of the name.
      - Getting possible full-names of the name (in case the name is a nick).
      - Getting different spelling options of the name.
      - Translating the name to different languages.
      - Getting the list of most common locations for people with this name.
      - Getting the list of most common ages for people with this name.
      - Getting an estimated number of people in the world with this name.

      The classes contained in this module are:
      - NameAPIRequest -- Build your request and send it.
      - NameAPIResponse -- Holds the response from the API in case it contains data.
      - NameAPIError -- An exception raised when the API response is an error.

      - AltNames -- Used in NameAPIResponse for holding alternative names.
      - LocationStats -- Used in NameAPIResponse for holding location data.
      - AgeStats -- Used in NameAPIResponse for holding age data.


      PIPL THUMBNAIL API
      ---------------------------------------------------------------------------
      Pipl's thumbnail API provides a thumbnailing service for presenting images in
      your application.



* Full details about Pipl's APIs - [http://dev.pipl.com](http://dev.pipl.com)  
* This library is available in other languages - [http://dev.pipl.com/docs/libraries](http://dev.pipl.com/docs/libraries)


Library Requirements
--------------------

* Python 2.6 / 2.7

- Version 1.1 updates the HTTPRequest Library to use requests 
  http://docs.python-requests.org/en/latest/ 
  

Installation
------------

    setup.py install

Getting Started & Code Snippets
-------------------------------

**Pipl's Search API**
* Getting started tutorial - [http://dev.pipl.com/docs/search_api/getstarted](http://dev.pipl.com/docs/search_api/getstarted)  
* Code snippets - [http://dev.pipl.com/docs/search_api/code](http://dev.pipl.com/docs/search_api/code)  

**Pipl's Name API**
* Getting started tutorial - [http://dev.pipl.com/docs/name_api/getstarted](http://dev.pipl.com/docs/name_api/getstarted)  
* Code snippets - [http://dev.pipl.com/docs/name_api/code](http://dev.pipl.com/docs/name_api/code)  

**Pipl's Thumbnail API**
* Getting started tutorial - [http://dev.pipl.com/docs/thumbnail_api/getstarted](http://dev.pipl.com/docs/thumbnail_api/getstarted)  
* Code snippets - [http://dev.pipl.com/docs/thumbnail_api/code](http://dev.pipl.com/docs/thumbnail_api/code)  


