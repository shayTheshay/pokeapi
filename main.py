import constants
from file_handling import extract_poke_data_json, insert_pokemon_to_json
from api_calling import get_pokemon_data

def main():

    random_pokemon_id = constants.num_pokemon_id


    pokemon = extract_poke_data_json(random_pokemon_id)
        #extract data from json
    if pokemon != False:
        print("pokemon from json")
    # if the pokemon does not exist in data call the api - check the response is valid and then handle response accordingly 
    pokemon_data = get_pokemon_data()
    if pokemon_data is None:
        print("There was a problem with calling")
        return False
    pokemon_stats = insert_pokemon_to_json(pokemon_data)
    print(pokemon_stats)
            


if __name__ == "__main__":
    main()