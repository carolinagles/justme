# Data Science & Data Engineering Portfolio

Interactive portfolio of Maria Carolina Gonzalez Bernal, built with Streamlit.

**Tabs**
- **Projects**: NLP/MLOps, machine learning, data engineering and statistics projects, with key metrics and links.
- **Live demo: data pipeline**: generates a synthetic server inventory, parses each hostname into fields, runs data quality checks and lets you download the CSV.
- **Skills**: skills mapped to the projects where they were used, plus the full toolkit.
- **Background**: education, experience and languages.

## Run locally
```bash
pip install -r requirements.txt
streamlit run app.py
```

## Deploy on Streamlit Community Cloud
1. Push this folder (`app.py`, `requirements.txt`, `.streamlit/config.toml`) to a public GitHub repository.
2. Go to share.streamlit.io, sign in with GitHub and choose **Create app**.
3. Select the repository and branch, set the main file to `app.py`, and deploy.

## Update the content
All text lives in the `PROFILE`, `PROJECTS`, `SKILLS`, `EVIDENCE`, `EDUCATION` and `EXPERIENCE` blocks at the top of `app.py`.
