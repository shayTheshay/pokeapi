import os.path
import json
from constants import file_json_name
from requests_handle import json_data

def check_file_exists():
    return os.path.isfile(file_json_name)

def create_json_file():
    with open(file_json_name, 'w') as f:
        json.dump({}, f)

def pokemon_by_id_in_json(pokemon_id, data):
    try:
        return data[str(pokemon_id)] 
    except KeyError:
        return False
    
    
def extract_poke_data_json(pokemon_id): #check concern of separation
    file_exist = check_file_exists()
    if file_exist == False:
        create_json_file()
    with open(file_json_name, 'r') as f:
        data = json.load(f)
    
    pokemon_exist = pokemon_by_id_in_json(pokemon_id, data)
    print("This is the pokemon exists place")
    print(pokemon_exist)
    
    return pokemon_exist



def insert_pokemon_to_json(pokemon_data): #insert the id name moves and abilities
    with open(file_json_name, 'r') as f:
        data = json.load(f) 

    pokemon_id = str(change_id_according_to_database(pokemon_data['id']))
    name = pokemon_data['name']
    types = pokemon_data['types']
    abilities = pokemon_data['abilities']

    new_pokemon = {
        "id" : pokemon_id,
        "name" : name,
        "types" : types, 
        "abilities" : abilities,
    }

    data[pokemon_id] = new_pokemon

    with open(file_json_name, 'w') as f:
        json.dump(data, f, indent=4)

    return data[pokemon_id]


def change_id_according_to_database(pokemon_id):###############################CHANGE HERE ACCORDINGLY
    if pokemon_id > 1025:
        pokemon_id = pokemon_id + 1025 - 10000
    return pokemon_id
def check_id_limit_json(pokemon_site_response):
    pokemon_data = json_data(pokemon_site_response)
    print(pokemon_data)



    
