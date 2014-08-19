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

# pprint(student_data_as_json)
# pprint(student_properties_data_as_json)

student_data = {}

for student in student_data_as_json['rows']:
  # print "Processing student "+student['key.name']+' '+student['user_id']
  # print "Additional fields "+student['additional_fields']
  additional_data = json.loads(student['additional_fields'])
  student_data[student['user_id']] = { 'name':student['key.name'], 'additional':additional_data }

for student_property in student_properties_data_as_json['rows']:
  student_id_value = student_property['key.name']
  student_id_components = student_id_value.split('-');
  student_id = student_id_components[0]
  print student_id
  student_info_map = student_data[student_id]
  if student_info_map :
    print('Located that student')
  else:
    print('Cant find that student')



