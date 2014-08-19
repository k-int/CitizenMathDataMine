import zipfile
import json
from pprint import pprint


zf = zipfile.ZipFile('archive.zip', 'r')
print zf.namelist()

student_file_info = zf.getinfo('models/Student.json')
student_properties_file_info = zf.getinfo('models/StudentPropertyEntity.json')

print "Got student and student properties file info"

student_data = zf.read('models/Student.json')
student_property_data = zf.read('models/StudentPropertyEntity.json')


print "Got data"

student_data_as_json = json.loads(student_data)
student_properties_data_as_json = json.loads(student_property_data)

print "Got json"

pprint(student_data_as_json)
pprint(student_properties_data_as_json)
