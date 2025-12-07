"""
Analyses bird species to find migratory and exclusive species per site.
"""
# Import literal_eval library to safely evaluate string input as a Python literal
from ast import literal_eval

# Taking the input
site_records = literal_eval(input())

def analyse_bird_data(site_records):
    # Write your code here
  all_species=set()
  for site,birds in site_records.items():
    all_species.update(birds)
  birds_count={}
  for site,birds in site_records.items():
    for bird in birds:
      birds_count[bird]=(birds_count.get(bird,0)+1)
  migratory_birds=[]
  for bird,count in birds_count.items():
    if count>=3:
      migratory_birds.append(bird)
  exclusive_species={}
  for site,birds in site_records.items():
    exclusive=birds-set(migratory_birds)
    exclusive_species[site]=list(exclusive)


  return [migratory_birds,exclusive_species]
# Print the output
print(analyse_bird_data(site_records))
