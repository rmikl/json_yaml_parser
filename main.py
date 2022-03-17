import yaml,os, json 

print("hi jakub")

#f = open("test.yaml","r") 
#print(f.read())
#
#print(yaml.safe_load(f))

#3. odczyt pliku json scheme 
#OTWIERANIE PLIKU YAML
with open("./guests/server1.yaml") as stream:
    try:
        yaml_file = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)

new_memory = yaml_file["RAM_IN_MB"]
print("new memory " + new_memory)

#OTWIERANIE PLIKU JSON
with open('./scheme/variable_scheme.json', 'r') as fcc_file:
    fcc_data = json.load(fcc_file)

memory = fcc_data["variable"]["memory"]["default"]

print("memory " + memory)
fcc_data["variable"]["memory"]["default"] = new_memory

#4. stworzenie pliku json
with open("guests_in_terraform/server1.json", "w") as outfile: 
    json.dump(fcc_data, outfile, indent = 4) 


#wyswietlanie i kasowanie for debuging
f = open("guests_in_terraform/server1.json","r") 
print("zawartosc jsona")
print(f.read())
#os.remove("guests_in_terraform/server1.json")



#1. sprawdzic poprawnosc z plikiem scheme!
#2. sprawdzic czy jest nowy plik? 
#3. odczytac ten plik i na podstawie tego pliku  
#   pliku i pliku variable_scheme.json
#4. stworzyc nowy plik json o tej samej nazwie









