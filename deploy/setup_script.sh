#!/bin/bash

echo "=== Starting EC2 setup script ==="

# 1. Update system packages
sudo dnf update -y

# 2. Install core tools: Python 3, pip, Git, unzip
sudo dnf install -y python3 python3-pip git unzip

# 3. Move to home directory
cd /home/ec2-user
cat game_output.log

# 4. Clone the project (replace this with your real repo if needed)
echo "Cloning repo..."
git clone https://github.com/shayTheshay/pokeapi
cd pokemon_api

# 5. Fix ownership for EC2 user
sudo chown -R ec2-user:ec2-user /home/ec2-user/pokemon_api

# 6. Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate

# 7. Install Python dependencies
pip install --upgrade pip
pip install -r requirements.txt

# 7b. Also explicitly install dotenv if not in requirements.txt
pip install python-dotenv

# 8. Run the Pokémon app in background and log output
nohup python3 core/run_game.py > game_output.log 2>&1 &
