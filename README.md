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


# Tech Stack
Backend: Python, Flask
Database: PostgreSQL
Semantic Search: SentenceTransformers (all-MiniLM-L6-v2), FAISS
Frontend: HTML + basic CSS
Deployment: Render for backend + DB

# App preview.
1)Input Query - 
![Screenshot 1](https://github.com/Suraj-1408/Assessment-Search-Engine/blob/master/Demo/Screenshot%20from%202025-04-08%2015-38-45.png?raw=true)

2) Result - 
![Screenshot 2](https://github.com/Suraj-1408/Assessment-Search-Engine/blob/master/Demo/Screenshot%20from%202025-04-08%2015-39-45.png?raw=true)

3) SHL Product Catalog  -
![Screenshot 3](https://github.com/Suraj-1408/Assessment-Search-Engine/blob/master/Demo/Screenshot%20from%202025-04-08%2015-39-54.png?raw=true)

# File Structure
1) app.py: Flask web server  
2) search.py: Handles search logic using FAISS  
3) build_faiss_index.py: Builds and stores FAISS index from DB  
4) db.py:DB connection
5) templates/: HTML templates (index, result)  

# Usage
1) Clone the repository: 
```
[git clone https://github.com/Suraj-1408/Assessment-Search-Engine.git
```  
2) Navigate to Directory
```
cd Assessment-Search-Engine
```
3) Create and activate virtual environment:  

```
python3 -m venv venv
source venv/bin/activate
```
4)  Install dependencies:
```
pip install -r requirements.txt
Set up PostgreSQL and run build_faiss_index.py to index data.
```

# Run the app:
```
python3 app.py
```
Access it
```
http://localhost:10000.
```
