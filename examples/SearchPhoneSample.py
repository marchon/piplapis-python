__author__ = 'marchon'

import sys
import requests

UserApiKey = 'jq9c88aa2pp7zu56u3d8r538'

#####################################################
#
#  Usage: python SearchPhoneSample [filenameOfPhoneNumbers]
#
#  Will make a pipl lookup for each line in the file
#  or via stdin if no file is specified
#
#
#


from piplapis.search import SearchAPIRequest

file = None

if sys.argv.__len__() > 1:
    file = open(sys.argv[1])

inputsource = file or sys.stdin

for line in inputsource:
    whatToCheck = line.strip()
    whatToCheck = whatToCheck.replace('-','')
    print "Checking Information for phone number : (%s) "  % whatToCheck
    Piplrequest = SearchAPIRequest(api_key=UserApiKey,
                                   phone=whatToCheck)
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
