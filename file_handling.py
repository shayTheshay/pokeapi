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
    
    
def extract_poke_data_json(pokemon_id):
    file_exist = check_file_exists()
    if file_exist == False:
        create_json_file()
    with open(file_json_name, 'r') as f:
        data = json.load(f)
    
    pokemon_exist = pokemon_by_id_in_json(pokemon_id, data)
    return pokemon_exist


def insert_pokemon_to_json(pokemon_data): #insert the id name moves and abilities
    with open(file_json_name, 'r') as f:
        data = json.load(f) 

    pokemon_id = str(pokemon_data['id'])
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


def check_id_limit_json(pokemon_site_response):
    pokemon_data = json_data(pokemon_site_response)
    print(pokemon_data)



    
