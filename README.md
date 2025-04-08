# SHL Assessment Recommender
This project is a web-based assessment recommendation system that allows users to input a job description or skill and receive the relevant SHL assessment links.

# Features
1)Accepts natural language queries (job roles, skills, or descriptions).
2)The System Recommends up to 3 best-matched assessments from SHL’s catalog.

## Results include:
1)Assessment Name (with link)
2)Remote Testing Support (Yes/No)
3)Adaptive/IRT Support (Yes/No)
4)Duration
5)Test Type

API endpoint also available for external queries.

# Tech Stack
Backend: Python, Flask
Database: PostgreSQL
Semantic Search: SentenceTransformers (all-MiniLM-L6-v2), FAISS
Frontend: HTML + basic CSS
Deployment: Render for backend + DB

📂 File Structure
app.py: Flask web server

search.py: Handles search logic using FAISS

build_faiss_index.py: Builds and stores FAISS index from DB

db.py: Centralized DB connection config

templates/: HTML templates (index, result)

# Usage
Clone the repository:
git clone https://github.com/your-username/shl-assessment-recommender.git
cd shl-assessment-recommender
Create and activate virtual environment:

python3 -m venv venv
source venv/bin/activate
Install dependencies:

pip install -r requirements.txt
Set up PostgreSQL and run build_faiss_index.py to index data.

# Run the app:
python3 app.py
Access it at http://localhost:5000.

