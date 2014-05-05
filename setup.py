#!/usr/bin/env python

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import sys
#import distutils.core
from setuptools import find_packages, setup
from piplapis import __version__


py_version = sys.version_info[:2]
if py_version not in [(2, 6), (2, 7)]:
    raise RuntimeError('Python 2.6 or 2.7 is required')


#distutils.core.setup(name='piplapis', version=__version__, packages=['piplapis', 'piplapis.data'])

setup(name="piplapis-python",
      version="1.1",
      description="""
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

      """,
      author="marchon - and piplcom piplapis-python ",
      author_email='marchon@gmail.com',
      platforms=["any"],  # or more specific, e.g. "win32", "cygwin", "osx"
      license="APACHE 2.0",
      url="http://github.com/marchon/piplapis-python",
      packages=find_packages(),
      install_requires=[i.strip() for i in open("requirements.txt").readlines()],
      )



