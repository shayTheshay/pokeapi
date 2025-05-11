from requests_handle import handle_response
import constants
from file_handling import check_id_limit_json

def get_pokemon_data():
    site_available = call_poke_site_available()
    if site_available == False:
        print("There was a problem reaching the site")
        return False
    
    pokemon_id_available = call_pokemon_value_avilable()
    if pokemon_id_available == False:
        check_id_limit_json(site_available)
        print("I am here")
    
    if pokemon_id_available == True:
        print("No, I am here")

    

def call_poke_site_available():
    return call_url_check(constants.base_url + constants.pokemon_list_url + constants.limit_url)


def call_pokemon_value_avilable():
    return call_url_check(constants.base_url + constants.pokemon_list_url + "/" + str(constants.num_pokemon_id))


def call_url_check(call_url):
    response = handle_response(call_url)
    if response is None:
        print("Network request failed.")
        return False

    if 200 <= response.status_code < 300:
        return True
    
    else:
        print(f"Unexpected status code: {response.status_code}, {response}")
        return False
    

