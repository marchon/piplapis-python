from piplapis.name import NameAPIRequest

request = NameAPIRequest(first_name='Rhonda', last_name='Seilhan', api_key='xxxxxxxxxxxxxxxxxxx')
response = request.send()
print dir(response)

print "Response Name: %s " % response.name
print "Gender       : %s %s" % ( response.gender, response.gender_confidence )
print "Ages         : %s " % response.top_ages
print "Full Names   : %s " % response.full_names
print "Locations    : %s " % response.top_locations
print "Nicknames    : %s " % response.nicknames
print "Estimaged Pop: %s " % response.estimated_world_persons_count
print "Spellings    : %s " % response.spellings
print "Warnings     : %s " % response.warnings


