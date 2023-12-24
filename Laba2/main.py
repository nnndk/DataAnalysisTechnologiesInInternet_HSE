from xml_helper import apply_transformation, get_xpath_result_node, get_xpath_result, get_xpath_result_text


xml_filename = 'tasks/1_timetable.xml'
xsl_to_txt_filename = 'tasks/5_transform_to_txt.xslt'
txt_filename = 'tasks/5_timetable.txt'
xsl_to_html_filename = 'tasks/6_transform_to_html.xslt'
html_filename = 'tasks/6_timetable.html'

apply_transformation(xml_filename, xsl_to_txt_filename, txt_filename)
apply_transformation(xml_filename, xsl_to_html_filename, html_filename)


print(f'1.\n' + get_xpath_result_text(xml_filename, '/timetable/day/class/title'))
print(f'2.\n' + get_xpath_result_text(xml_filename, '/timetable/day/class/room[not(roomNumber = following::room/roomNumber and buildingNumber = following::room/buildingNumber)]/roomNumber'))
print(f'3.\n' + get_xpath_result_text(xml_filename, '/timetable/day/class[@type = "Practice"]/title'))
print(f'4.\n' + get_xpath_result_text(xml_filename, '/timetable/day/class[@type = "Lecture"][room/roomNumber = "102"]/title'))
print(f'5.\n' + get_xpath_result_text(xml_filename, '/timetable/day/class[@type = "Practice"][room/roomNumber = "509"]/teacher', True))
print(f'6.\n' + get_xpath_result_text(xml_filename, '/timetable/day/class[last()]/title'))
print(f'7.\n' + str(get_xpath_result_node(xml_filename, "count(/timetable/day/class)")[1]) + '\n')

