from requests_handle import handle_response, json_data
from file_handling import insert_pokemon_to_json
from constants import min_id, base_url, pokemon_list_url



def get_pokemon_data(pokemon_id): #separate all the parts of the function, should be smaller portions.
    site_available = call_poke_site_available()
    if site_available == False:
        print("There was a problem reaching the site")
        return False
    
    max_id = get_max_pokemon_id(site_available)
    
    pokemon_id_available = call_pokemon_value_avilable(pokemon_id)
    if pokemon_id_available == False: # suppossed to check weather the value given exceeds the number of pokemon but should not be here
        #minimum_pokemon_id, maximum_pokemon_id = check_id_limit_json(site_available)
        if min_id > pokemon_id or max_id < pokemon_id:
            print(f"The number id for the pokemon should be between {min_id} to {max_id}")
            return False
        else:
            print("Something went wrong in the calling")
            return None
    else:
        return insert_pokemon_to_json(json_data(pokemon_id_available))
         


def call_poke_site_available():
    return call_url_check(base_url + pokemon_list_url)

def get_max_pokemon_id(data):
    data =  json_data(data)
    return int(data['count'])

def call_pokemon_value_avilable(pokemon_id): #################################### CHANGE HERE ACCORDINGLY
    if pokemon_id <= 1025:
        return call_url_check(base_url + pokemon_list_url + "/" + str(pokemon_id))
    else:
        new_num = pokemon_id - 1025 + 10000
        return call_url_check(base_url + pokemon_list_url + "/" + str(new_num))

def call_url_check(call_url): #make sure it is doing only one thing per concern of separation
    response = handle_response(call_url)
    if response is None:
        print("Network request failed.")
        return False

    if 200 <= response.status_code < 300:
        return response
    else:
        print(f"Unexpected status code: {response.status_code}, {response}")
        return False
    


    

