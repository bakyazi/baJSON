from bajson.libcsv import json_to_csv, csv_to_json


csv_to_json("output.csv", "output.json")


json_to_csv("test/assets/test.json", "output.csv")
