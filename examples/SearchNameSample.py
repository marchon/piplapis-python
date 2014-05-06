__author__ = 'marchon'

import sys
import requests

UserApiKey = '7eeu5nmtvx5xwexv5jepk2z2'


from piplapis.search import SearchAPIRequest

file = None

if sys.argv.__sizeof__() > 0:
    file = open(sys.argv[1])

inputsource = file or sys.stdin

for line in inputsource:
    whatToCheck = line.strip()
    print "Checking Information for Email: (%s) "  % whatToCheck
    Piplrequest = SearchAPIRequest(api_key=UserApiKey,
                                   email=whatToCheck)
    response = Piplrequest.send()
    Collection = response.group_records_by_domain()
    print Collection
    for Domain in Collection:
        print
        print



        for item in Collection[Domain]:
            print "%s %s \n%s" % (Domain , item, item.to_dict())
            print ("")


"""
    >>> from piplapis.data import Record, Email, Phone
    >>> fields = [Email(address='eric@cartman.com'), Phone(number=999888777)]
    >>> record = Record(fields=fields)
    >>> record.emails
    [Email(address=u'eric@cartman.com')]
    >>> record.phones
    [Phone(number=999888777)]
"""
