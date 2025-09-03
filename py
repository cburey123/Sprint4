cd ~/Projects   # or wherever you want
git clone https://github.com/<your-username>/<repo>.git
cd <repo>

# Create environment
python3 -m venv .venv
source .venv/bin/activate

# Upgrade pip
pip install --upgrade pip

# Install core packages
pip install pandas streamlit plotly altair

# Save to requirements.txt
pip freeze > requirements.txt
