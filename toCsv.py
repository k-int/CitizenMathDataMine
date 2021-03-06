from __future__ import print_function
import zipfile
import json
import sys
from pprint import pprint

reload(sys) 
sys.setdefaultencoding('utf-8')

zf = zipfile.ZipFile('archive.zip', 'r')
# print zf.namelist()

student_file_info = zf.getinfo('models/Student.json')
student_properties_file_info = zf.getinfo('models/StudentPropertyEntity.json')

# print "Got student and student properties file info"

student_data = zf.read('models/Student.json')
student_property_data = zf.read('models/StudentPropertyEntity.json')


# print "Got data"

student_data_as_json = json.loads(student_data)
student_properties_data_as_json = json.loads(student_property_data)

# print "Got json"

# pprint(student_data_as_json)
# pprint(student_properties_data_as_json)

student_data = {}
learner_types = []
additional_properties = []
completion_status = []

for student in student_data_as_json['rows']:
  # print "Processing student "+student['key.name']+' '+student['user_id']
  # print "Additional fields "+student['additional_fields']
  additional_data = json.loads(student['additional_fields'])
  student_data[student['user_id']] = { 'name':student['key.name'], 'additional':{} }

  for additional_prop in additional_data:
    if ( additional_prop[0] not in additional_properties ) :
      additional_properties.append(additional_prop[0]);

    if additional_prop[0] in student_data[student['user_id']]['additional'].keys() :
      student_data[student['user_id']]['additional'][additional_prop[0]].append(additional_prop[1])
    else:
      student_data[student['user_id']]['additional'][additional_prop[0]] = [additional_prop[1]]

  if 'learner_type' in student_data[student['user_id']]['additional'] :
    for lt in student_data[student['user_id']]['additional']['learner_type']:
      if lt not in learner_types :
        learner_types.append(lt);

for student_property in student_properties_data_as_json['rows']:
  student_id_value = student_property['key.name']
  student_id_components = student_id_value.split('-');
  student_id = student_id_components[0]
  json_str = student_property['value']
  json_value = None
  if ( json_str is not None ) :
    json_value = json.loads(json_str);
  # print student_id
 
  if student_id in student_data.keys() :
    student_info_map = student_data[student_id]
    # pprint(student_info_map)
    # print('Located that student')

    student_info_map['value'] = json_value
    if ( json_value != None ) :
      for key in json_value :
        if ( key not in completion_status ) :
          completion_status.append(key)
    else :
       student_info_map['value'] = {}

  #else:
    # print('Cant find that student')

# pprint ( learner_types )
# pprint(student_data)
# pprint(additional_properties)
# pprint(completion_status)

learner_types.sort()
additional_properties.sort()

print( 'name', end='' )
for prop in additional_properties :
  print(',' + prop, end ='' )

for lt in learner_types:
  print(',' + lt, end ='' )

# for prop in completion_status :
#   print(',' + prop, end='' )



print('')

for student_key in student_data :
  student = student_data[student_key]
  print("\""+student['name']+"\",", end='')
  for prop in additional_properties :
    print("\"",end='')
    if ( prop in student['additional'] ) :
      ctr = 0
      for v in student['additional'][prop]:
        if ( ctr > 0 ) :
          print(' ',end='')
        print(v,end='')
        ctr = ctr +1
    else :
      print('', end='')
    print("\",",end='')

  # for completion_key in completion_status:
  #   if ( completion_key in student['value'] ) :
  #     print(",\"", end="");
  #     print(student['value'][completion_key], end="")
  #     print("\"", end="");
  #   else :
  #     print(',', end='')

  # LEarner type processing
  for lt in learner_types:
    # If the student has a learner type property
    print("\"",end='')
    if 'learner_type' in student['additional'].keys() and lt in student['additional']['learner_type']:
      print('Y',end='')
    else:
      print('N',end='')
    print("\",",end='')
    
  print('')


