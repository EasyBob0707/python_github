# -*- coding:utf-8 -*-
import glob

data = glob.glob('chapter/*.txt')
athletes = athlelemodel.put_to_store(data)
print(yate.start_response())
print(yate.include_header("Coach Kelly's List of Athletes"))
print(yate.start_form('generate_timing_data.py'))
print(yate.para("Select an athlete from the list to work with:"))
for each_athlete in athletes:
    print(yate.radio_button("Witch_athlete", athletes[each_athlete].name))
print(yate.end_form("Select"))
print(yate.include_footer({"Home":"/index.html"}))