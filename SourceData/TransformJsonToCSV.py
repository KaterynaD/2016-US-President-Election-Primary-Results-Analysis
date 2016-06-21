from __future__ import division
import json
import os, sys


candidate = {"trump-8639": "Donald Trump",
              "kasich-36679": "John Kasich",
							"cruz-61815": "Ted Cruz",
							"carson-64509": "Ben Carson",
							"gilmore-45650": "Jim Gilmore",
							"rubio-53044": "Marco Rubio",
							"bush-1239": "Jeb Bush",
							"other-999999": "Other",
							"clinton-1746": "Hillary Clinton",
							"sanders-1445": "Bernie Sanders",
							"wilson-999999": "Willie Wilson",
							"steinberg-999999": "Michael Steinberg",
							"de-la-fuente-999999": "Rocky De La Fuente",
							"hewes-999999": "Henry Hewes",
							"judd-999999": "Keith Judd"
							}
def extract_data (data,state,state_abbr,party,output):
    for cnt in data[state]:
        fips=cnt["fips"]
        name=cnt["name"]
        total=0
        for cand in cnt["results"]:
            total=total+cnt["results"][cand]
        for cand in cnt["results"]:
            fraction=float(cnt["results"][cand]/total)
            output.write(state+','+state_abbr+','+name+','+fips+','+party+','+candidate[cand]+','+str(cnt["results"][cand])+','+str(fraction)+'\n')

file_name='primary_results_ca_dem.json'
with open(file_name) as data_file:
    data = json.load(data_file)

with open("primary_results_new.csv", "wb") as output:
    extract_data(data=data,state='California',state_abbr='CA', party='Democrat',output=output)

file_name='primary_results_ca_rep.json'
with open(file_name) as data_file:
    data = json.load(data_file)

with open("primary_results_new.csv", "ab") as output:
    extract_data(data=data,state='California',state_abbr='CA', party='Republican',output=output)

file_name='primary_results_montana_dem.json'
with open(file_name) as data_file:
    data = json.load(data_file)

with open("primary_results_new.csv", "ab") as output:
    extract_data(data=data,state='Montana',state_abbr='MT', party='Democrat',output=output)

file_name='primary_results_montana_rep.json'
with open(file_name) as data_file:
    data = json.load(data_file)

with open("primary_results_new.csv", "ab") as output:
    extract_data(data=data,state='Montana',state_abbr='MT', party='Republican',output=output)
