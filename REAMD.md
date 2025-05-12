# 🧬 Pokémon Card Drawer

## 🎴 Description

A command-line Python project that lets you draw random Pokémon cards using data from the [PokeAPI](https://pokeapi.co/). It caches Pokémon locally in a JSON file, handles edge-case API ID jumps, and ensures smooth and repeated gameplay without spamming the API.

---

## 📦 Features

- ✅ Randomly draw Pokémon by ID.
- ✅ Fetch Pokémon from the PokeAPI and cache locally.
- ✅ Automatically skip broken ID ranges in the PokeAPI (e.g., jump from `1025` to `10001`).
- ✅ Presents Pokémon details: **name**, **type(s)**, and **abilities**.
- ✅ Graceful handling of API/network errors.
- ✅ Interactive loop that lets users keep drawing.

---

## 🗂️ Project Structure

.
├── main.py # Main entry point for the game loop
├── file_handling.py # Manages reading/writing to JSON and local cache
├── api_calling.py # Fetches Pokémon from the API, with error handling
├── requests_handle.py # Wraps API calls and handles HTTP response statuses
├── constants.py # Stores global constants like URLs and ID ranges
├── convert_file.py # Converts between API ID and local ID formats
├── pokemon_random.py # Chooses a random valid Pokémon ID
├── user_input.py # Handles user input (yes/no)
├── user_print.py # Displays messages and Pokémon info
├── pokemon_data.json # Local cache of previously fetched Pokémon

---

## 🚀 How It Works

1. **User Prompt**: Asks the user if they want to draw a Pokémon card.
2. **ID Selection**: Picks a random Pokémon ID between 1 and 1302.
3. **Check Cache**: If the Pokémon exists in `pokemon_data.json`, it’s displayed.
4. **API Call**: If not cached, it’s fetched from PokeAPI (with ID jump handling).
5. **Display**: Shows Pokémon name, types, and abilities.
6. **Repeat**: Prompts the user again until they decline.

---

## 🔧 Requirements

- Python 3.7 or higher
- `requests` library  
  Install with:
  ```bash
  pip install requests
  ```
