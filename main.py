import constants
from file_handling import extract_poke_data_json
from api_calling import get_pokemon_data
from user_print import present_pokemon_data, ask_user_draw_pokemon
from user_input import user_answer
def main():
    ask_user_draw_pokemon()
    yes = str(user_answer())
    while yes == "yes":
        random_pokemon_id = constants.num_pokemon_id
        pokemon = extract_poke_data_json(random_pokemon_id)
        if pokemon != False:
            present_pokemon_data(pokemon)
        else:
            pokemon_data = get_pokemon_data()
            if pokemon_data is None:
                print("There was a problem with the calling")
                return False
            elif pokemon_data is False:
                print("You can try again with the next pokemon calling")
        ask_user_draw_pokemon()
        yes = user_answer()

if __name__ == "__main__":
    main()