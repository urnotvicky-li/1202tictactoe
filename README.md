# Notes on how to setup fresh development environment

# create empty git repo on GitHub
# clone the git repo from GitHub
git clone https://github.com/ianchen06/techin509-au24-tictactoe
cd techin509-au24-tictactoe

# setup a new virtual environment, and activate it for this terminal session
python -m venv venv
source venv/bin/activate

# Install packages and freeze into requirements.txt file
pip install numpy openai django
pip freeze > requirements.txt

# commit requirements.txt to GitHub so others can use to reproduce your environment
git add requirements.txt

