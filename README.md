# María Carolina · Data Science & Data Engineering Portfolio

A one-page portfolio built with Streamlit, custom HTML and CSS.
Design: Swiss typography and grid, liquid-glass panels and a warm palette
(luminous blue, energy orange, pop pink, meadowland green and clay on paper).

**Sections**
- **Hero** with a short introduction and key figures.
- **Projects**: Madrid Restaurant Intelligence (main project), then Pump It Up, Guess the Number, the hostname pipeline and the glucose study, with a filter by area.
- **Capabilities**: six areas, each linked to the project where it shows up.
- **Dashboards**: the Easy Loans Tableau dashboards, embedded from Tableau Public.
- **Live demo**: a data pipeline that generates, parses and validates a server inventory, with a CSV download.
- **About** and **Contact** (email only).

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
Colours, figures, capabilities, projects and Tableau links are at the top of `app.py`
(`PALETTE`, `FIGURES`, `CAPABILITIES`, `PROJECTS`, `TABLEAU_DASHBOARDS`).
Section text is in the HTML blocks further down; styles are in the `<style>` block.
