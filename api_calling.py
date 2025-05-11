from requests_handle import handle_response, json_data
from file_handling import check_id_limit_json, insert_pokemon_to_json
import constants

def get_pokemon_data(): #separate all the parts of the function, should be smaller portions.
    site_available = call_poke_site_available()
    if site_available == False:
        print("There was a problem reaching the site")
        return False
    
    pokemon_id_available = call_pokemon_value_avilable()
    if pokemon_id_available == False:
        minimum_pokemon_id, maximum_pokemon_id = check_id_limit_json(site_available)
        if minimum_pokemon_id > constants.num_pokemon_id or maximum_pokemon_id < constants.num_pokemon_id:
            print(f"The number id for the pokemon should be between {minimum_pokemon_id} to {maximum_pokemon_id}")
            return False
        else:
            print("Something went wrong in the calling")
            return None
    else:
        print(pokemon_id_available)
        insert_pokemon_to_json(json_data(pokemon_id_available))
        return pokemon_id_available

def call_poke_site_available():
    return call_url_check(constants.base_url + constants.pokemon_list_url + constants.limit_url)

def call_pokemon_value_avilable():
    return call_url_check(constants.base_url + constants.pokemon_list_url + "/" + str(constants.num_pokemon_id))

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
    


    

