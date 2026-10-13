# María Carolina · Data Science & Data Engineering Portfolio

A one-page portfolio built with Streamlit, custom HTML and CSS.
Design: Swiss / International Typographic Style, with International Klein Blue as the only accent.

**Sections**
- **Hero** and a blue band with the headline numbers.
- **Capabilities**: six skills, each linked to the project that proves it.
- **Selected work**: Madrid Restaurant Intelligence (featured), Pump It Up, Guess the Number, the hostname pipeline and the glucose study.
- **Dashboards**: the Easy Loans Tableau dashboards, embedded from Tableau Public.
- **Live demo**: a working data pipeline that generates, parses and validates a server inventory, with a CSV download.
- **About** and **Contact**.

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
Links, Tableau dashboards and capabilities are at the top of `app.py` (`LINKS`, `TABLEAU_DASHBOARDS`, `CAPABILITIES`).
Section text is in the HTML blocks further down; styles are in the `<style>` block.
