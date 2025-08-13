# This is a setup script for the Customer Support RAG project is we 
# want to set up the environment and install dependencies.
# Developed by : Ashmin Bhaumik

#!/bin/bash
# Setup script for Customer Support RAG project
# Usage: bash setup.sh

# Mainly make a virtual environment and install dependencies.....
echo "Creating Python virtual environment (.venv)..."
python3 -m venv .venv

# Activate DB server (Chroma DB) if not already running...
echo "Start Chroma DB server..."
python3 start_chroma.py

# Than U have to activate the virtual environment....
echo "Activating virtual environment..."
source .venv/bin/activate

# Than we have to install the required packages....
echo "Upgrading pip..."
pip install --upgrade pip

# Install required Python packages from requirements.txt
echo "Installing required Python packages..."
pip install -r requirements.txt

# Install additional packages for document loaders....
echo "Installing langchain-community loaders (required for document ingestion)..."
pip install -U langchain-community

# Install Streamlit for the web app.....
# Install Chroma CLI for running local ChromaDB server......
echo "Installing Chroma CLI for local ChromaDB server..."
pip install "chromadb[cli]"

echo "Setup complete!"
echo "Next steps:"
echo "1. Copy .env.example to .env and set your GOOGLE_API_KEY."
echo "2. Add your knowledge base files (PDF/TXT/CSV/MD) to data/knowledge_base/"
echo "3. Run: python ingest.py"
echo "4. Run: streamlit run app.py"
echo "5. (Optional) To run Chroma DB server locally: chromadb run --path data/chroma"

# Note for Render hosting:
echo "If deploying on Render, ensure your requirements.txt includes all dependencies."
echo "Do NOT use chromadb run --path ... for serverless hosting; use Chroma in 'client' mode (default in code)."
echo "Render will run pip install -r requirements.txt automatically."
echo "We may need to set GOOGLE_API_KEY and other env vars in Render dashboard."
