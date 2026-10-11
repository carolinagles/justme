# María Carolina · Data Science & Data Engineering Portfolio

A single-page portfolio built with Streamlit, custom HTML and CSS.

**Sections**
- **Hero** with headline and key numbers.
- **What I bring**: six capabilities, each linked to the project that proves it.
- **Work**: featured projects (Restaurant NLP live app, Pump It Up, hostname pipeline, glucose study).
- **Live demo**: a working data pipeline that generates, parses and validates a server inventory, with a CSV download.
- **Why me** and a timeline of my path.
- **Contact**.

## Run locally
```bash
pip install -r requirements.txt
streamlit run app.py
```

## Deploy on Streamlit Community Cloud
1. Push `app.py`, `requirements.txt` and the `.streamlit/` folder to a public GitHub repository.
2. Go to share.streamlit.io, sign in with GitHub and choose **Create app**.
3. Pick the repository, set the main file to `app.py` and deploy.

## Edit the content
Links and capability tiles are at the top of `app.py` (`LINKS`, `CAPABILITIES`).
Section text is in the HTML blocks further down; styles are in the `<style>` block.
