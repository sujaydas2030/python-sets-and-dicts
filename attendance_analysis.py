"""
Analyses attendance data across multiple days.
"""
# Import literal_eval library to safely evaluate string input as a Python literal
from ast import literal_eval

# Taking the input
daily_data = literal_eval(input())

def analyse_attendance(daily_data):
    # Write your code here
    countries_present_each_day=set(daily_data[0].keys())
    for day in daily_data[1:]:
      countries_present_today=set(day.keys())
      countries_present_each_day=countries_present_each_day & countries_present_today
    list_of_countries_present_each_day=list(countries_present_each_day)
    list_of_countries_present_each_day.sort()

    registry_mapping={}
    for day in daily_data:
      for key,value in day.items():
        if key not in registry_mapping:
          registry_mapping[key]=set()
        for val in value:
          registry_mapping[key].add(val)

    # Convert sets in registry_mapping to lists and sort them
    registry_mapping_as_lists = {key: sorted(list(values)) for key, values in registry_mapping.items()}

    present_on_first_day_absent_on_last_day=list(set(daily_data[0].keys())-set(daily_data[-1].keys()))

    return [list_of_countries_present_each_day,registry_mapping_as_lists,present_on_first_day_absent_on_last_day]



# Print the output
print(analyse_attendance(daily_data))
