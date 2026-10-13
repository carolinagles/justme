"""
María Carolina · Data Science & Data Engineering portfolio (Streamlit).
Run locally:  streamlit run app.py

Mood: an editorial newspaper page with liquid-glass panels.
Palette: warm paper background with five accent colours
(luminous blue, energy orange, pop pink, meadowland green, clay) and warm neutrals.

Content lives in the CONTENT section. Styling lives in STYLE.
"""

from datetime import date

import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="María Carolina · Data Scientist", page_icon="📰", layout="wide")


def html(block: str) -> None:
    """Render raw HTML. Lines are left-stripped so Markdown never turns them into code blocks."""
    clean = "\n".join(line.strip() for line in block.strip().splitlines() if line.strip())
    st.markdown(clean, unsafe_allow_html=True)


# =============================================================================
# CONTENT
# =============================================================================
LINKS = {
    "email": "mailto:Carolinagles@gmail.com",
    "restaurants": "https://madrid-restaurant-intelligence.streamlit.app/",
    "restaurants_repo": "https://github.com/carolinagles/madrid-restaurant-intelligence",
    "pumps": "https://github.com/carolinagles/PumpItUp/blob/main/PumpItUp.ipynb",
    "hostnames": "https://app.notion.com/p/Hostnames-Generator-2b9fea9d8900807e9deadffe3bdb83ae",
    "glucose": "https://www.notion.so/Glucose-Levels-307fea9d89008006b054fb9422e09232",
    "guess": "https://guessthenumberrrr.streamlit.app/",
    "guess_repo": "https://github.com/carolinagles/guessthenumberrrr",
}

TABLEAU_DASHBOARDS = {
    "Loan operations": "https://public.tableau.com/views/EasyLoans_17918449786600/LOANOPERATIONS",
    "Merchant analysis": "https://public.tableau.com/views/EasyLoans-TopMerchants/MERCHANTANALYSIS",
}
TABLEAU_PROFILE = "https://public.tableau.com/app/profile/maria.carolina.gonzalez.bernal"

# Palette (sampled from the reference)
PAPER = "#F1ECE8"
PAPER_DEEP = "#EEE5DE"
INK = "#262626"
MUTED = "#6B625A"
BLUE = "#566F97"
ORANGE = "#EA611D"
PINK = "#D684A8"
GREEN = "#88886C"
CLAY = "#B97E54"
SAND = "#CFB79F"
TAUPE = "#AF9A87"
STONE = "#BEB9B6"
LINEN = "#EBDFD1"

# Key figures: colour, number, name, explanation
FIGURES = [
    (BLUE, "1.16M", "Reviews modelled", "Spanish and English restaurant reviews from Madrid, read by one classifier."),
    (ORANGE, "0.808", "Macro F1", "Measured once on 996 restaurants the model never saw during development."),
    (PINK, "0.8132", "Leaderboard score", "DrivenData “Pump It Up”, predicting which water pumps fail."),
    (GREEN, "55", "Peer groups", "Cuisine and price groups covering 96.7% of comparable restaurants."),
    (CLAY, "4.0×", "Alert lift", "How much more often a decline persisted after a Critical alert, in a backtest."),
]

# Area, colour, what it involves, tools, where it shows up
CAPABILITIES = [
    ("Machine learning", BLUE,
     "Models evaluated on data they have not seen, split by group to avoid leakage.",
     "Scikit-learn · LightGBM · CatBoost · XGBoost · Optuna", "Restaurant intelligence, Pump It Up"),
    ("Natural language", ORANGE,
     "Spanish and English text classification, with each prediction explained word by word.",
     "TF-IDF · LinearSVC · Transformers · spaCy · NLTK", "Restaurant intelligence"),
    ("Data engineering", PINK,
     "Data that is generated, parsed, validated and exported with explicit checks.",
     "Pandas · NumPy · Pandera · Parquet · SQL", "Hostname pipeline, Restaurant intelligence"),
    ("Deployment", GREEN,
     "Models served behind a tested API and wrapped in small apps.",
     "FastAPI · MLflow · pytest · Streamlit", "Restaurant intelligence, Guess the Number"),
    ("Statistics and BI", CLAY,
     "Choosing the right test, then presenting results in dashboards that are quick to read.",
     "Hypothesis testing · ANOVA · Regression · Tableau · Plotly", "Glucose study, Easy Loans"),
    ("Big data and cloud", TAUPE,
     "Distributed and cloud tools studied in my M.Sc. at Complutense University of Madrid.",
     "PySpark · Spark SQL · MLlib · Google Cloud · MongoDB · Snowflake", "M.Sc. coursework"),
]

TODAY = date.today().strftime("%A, %d %B %Y")

# =============================================================================
# STYLE
# =============================================================================
html(f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Bodoni+Moda:ital,opsz,wght@0,6..96,400;0,6..96,500;0,6..96,600;1,6..96,400;1,6..96,500&family=Source+Serif+4:ital,opsz,wght@0,8..60,400;0,8..60,500;1,8..60,400&family=Inter:wght@400;500;600&display=swap');
:root {{
  --paper:{PAPER}; --paper-deep:{PAPER_DEEP}; --ink:{INK}; --muted:{MUTED};
  --blue:{BLUE}; --orange:{ORANGE}; --pink:{PINK}; --green:{GREEN}; --clay:{CLAY};
  --sand:{SAND}; --taupe:{TAUPE}; --stone:{STONE}; --linen:{LINEN};
  --display: "Bodoni Moda", "Didot", "Bodoni 72", "Times New Roman", serif;
  --serif: "Source Serif 4", Georgia, "Times New Roman", serif;
  --sans: "Inter", "Helvetica Neue", Arial, sans-serif;
  --glass: rgba(255,255,255,.42);
  --glass-edge: rgba(255,255,255,.78);
  --glass-shadow: 0 1px 0 rgba(255,255,255,.9) inset, 0 0 0 1px rgba(185,126,84,.06), 0 18px 40px rgba(90,62,40,.10);
}}
html, body, .stApp, .stApp :is(h1,h2,h3,h4,p,span,div,a,b,li,label,button,input,small,td,th):not([data-testid="stIconMaterial"]):not(.material-symbols-rounded) {{
  font-family: var(--sans) !important; -webkit-font-smoothing: antialiased; }}
.stApp.stApp.stApp :is(h1,h2,h3,h4,b,em) :is(span,em) {{ font-family: inherit !important; }}
[data-testid="stHeaderActionElements"] {{ display: none !important; }}
header[data-testid="stHeader"], #MainMenu, footer, [data-testid="stToolbar"], [data-testid="stDecoration"] {{ display: none !important; }}

/* Paper background with very soft light so the glass has something to refract */
.stApp {{
  color: var(--ink);
  background:
    radial-gradient(38vw 30vw at 88% 12%, rgba(86,111,151,.10), transparent 70%),
    radial-gradient(34vw 28vw at 6% 46%, rgba(185,126,84,.10), transparent 70%),
    radial-gradient(36vw 30vw at 92% 78%, rgba(214,132,168,.08), transparent 70%),
    radial-gradient(30vw 26vw at 18% 92%, rgba(136,136,108,.09), transparent 70%),
    linear-gradient(180deg, {PAPER_DEEP} 0%, {PAPER} 30%, {PAPER} 100%);
  background-attachment: fixed;
}}
.block-container {{ max-width: 1160px; padding: 0 2rem 2rem 2rem; }}
a {{ color: inherit; }}
::selection {{ background: var(--blue); color: #fff; }}
a:focus-visible, button:focus-visible {{ outline: 2px solid var(--blue); outline-offset: 3px; }}

/* Typography helpers */
.kicker {{ font-size: .72rem; letter-spacing: .22em; text-transform: uppercase; color: var(--ink); font-weight: 500; }}
.kicker.muted {{ color: var(--muted); }}
.stApp.stApp.stApp .byline, .stApp.stApp.stApp .byline * {{ font-family: var(--serif) !important; font-style: italic; color: var(--ink); }}
.stApp.stApp.stApp .serif, .stApp.stApp.stApp .serif * {{ font-family: var(--serif) !important; }}

/* Liquid glass */
.glass, .st-key-demo, .st-key-bi {{
  background: var(--glass);
  backdrop-filter: blur(22px) saturate(150%); -webkit-backdrop-filter: blur(22px) saturate(150%);
  border: 1px solid var(--glass-edge); box-shadow: var(--glass-shadow); border-radius: 18px; position: relative;
}}
.glass::before {{
  content: ""; position: absolute; inset: 0; border-radius: inherit; pointer-events: none;
  background: linear-gradient(140deg, rgba(255,255,255,.55) 0%, rgba(255,255,255,0) 35%, rgba(255,255,255,0) 72%, rgba(255,255,255,.22) 100%);
}}
.glass > * {{ position: relative; }}

/* Masthead */
.masthead {{ padding: 2.2rem 0 0 0; }}
.mast-top {{ display: flex; justify-content: space-between; align-items: center; padding-bottom: .7rem; border-bottom: 1px solid var(--ink); }}
.mast-top .brand {{ font-size: .8rem; letter-spacing: .38em; text-transform: uppercase; font-weight: 500; }}
.stApp.stApp.stApp .masthead h1 {{ font-family: var(--display) !important; font-weight: 400; font-size: clamp(3.4rem, 10.5vw, 8.6rem);
  line-height: .92; letter-spacing: -0.01em; text-transform: uppercase; margin: 1.6rem 0 .4rem -0.02em; padding: 0 !important; color: var(--ink); }}
.masthead .tagline {{ font-size: .86rem; letter-spacing: .26em; text-transform: uppercase; margin: .8rem 0 0 0; padding-bottom: 1.2rem; border-bottom: 1px solid rgba(38,38,38,.35); max-width: 640px; }}
.swatches {{ display: flex; gap: 6px; margin-top: 1.1rem; }}
.swatches i {{ width: 26px; height: 8px; display: block; border-radius: 2px; }}

.mast-grid {{ display: grid; grid-template-columns: 1fr 250px; gap: 2rem; align-items: end; }}
.inside {{ padding: 1.3rem 1.4rem 1rem 1.4rem; margin-bottom: .2rem; }}
.inside .kicker {{ display: block; padding-bottom: .7rem; border-bottom: 1px solid rgba(38,38,38,.25); margin-bottom: .3rem; }}
.stApp .inside a {{ display: flex; gap: .9rem; align-items: baseline; text-decoration: none; color: var(--ink) !important; padding: .55rem 0; border-bottom: 1px solid rgba(38,38,38,.1); font-size: .95rem; }}
.stApp .inside a:last-child {{ border-bottom: none; }}
.stApp .inside a:hover {{ color: var(--clay) !important; }}
.stApp.stApp.stApp .inside em {{ font-family: var(--display) !important; font-style: italic; color: var(--clay); width: 1rem; }}
/* Section bar like a newspaper menu */
.sections {{ position: sticky; top: 0; z-index: 50; margin: 1.8rem 0 0 0; padding: .65rem 1.1rem; display: flex; gap: 1.6rem; flex-wrap: wrap; align-items: center; border-radius: 14px; }}
.stApp .sections a {{ text-decoration: none; font-size: .74rem; letter-spacing: .2em; text-transform: uppercase; color: var(--ink) !important; padding: .2rem 0; border-bottom: 1px solid transparent; }}
.stApp .sections a:hover {{ border-bottom-color: var(--clay); }}
.sections .date {{ margin-left: auto; font-size: .82rem; color: var(--muted); }}

/* Front page */
.front {{ display: grid; grid-template-columns: 1.15fr 1fr; gap: 2.2rem; margin-top: 2.2rem; align-items: start; }}
.article {{ padding: 2.2rem 2.4rem 2rem 2.4rem; }}
.article .byline {{ font-size: 1.05rem; line-height: 1.5; padding-bottom: 1.1rem; border-bottom: 1px solid rgba(38,38,38,.25); margin-bottom: 1.4rem; }}
.stApp.stApp.stApp .article p.body {{ font-family: var(--serif) !important; font-size: 1.12rem; line-height: 1.62; color: var(--ink); margin: 0 0 1.1rem 0; }}
.stApp.stApp.stApp .article p.body.first::first-letter {{ font-family: var(--display) !important; float: left; font-size: 4.3rem; line-height: .82; padding: .35rem .55rem 0 0; color: var(--clay); }}
.pull {{ display: flex; gap: .9rem; align-items: flex-start; margin: 1.6rem 0 1.4rem 0; }}
.stApp.stApp.stApp .pull .mark {{ font-family: var(--display) !important; font-size: 3.4rem; line-height: .7; color: var(--sand); }}
.stApp.stApp.stApp .pull p {{ font-family: var(--serif) !important; font-style: italic; font-size: 1.45rem; line-height: 1.3; margin: 0; }}
.btn {{ display: inline-block; padding: .75rem 1.2rem; font-size: .8rem; letter-spacing: .14em; text-transform: uppercase; text-decoration: none !important;
  border: 1px solid var(--ink); border-radius: 999px; margin: .3rem .5rem .3rem 0; transition: background .2s, color .2s; }}
.btn-ink {{ background: var(--ink); color: var(--paper) !important; }}
.btn-ink:hover {{ background: var(--blue); border-color: var(--blue); }}
.btn-line {{ color: var(--ink) !important; background: rgba(255,255,255,.35); }}
.btn-line:hover {{ background: var(--ink); color: var(--paper) !important; }}

.figures .head {{ text-align: center; margin: .2rem 0 1.4rem 0; }}
.figure {{ display: grid; grid-template-columns: 112px 1fr; gap: 1.4rem; align-items: center; margin-bottom: 1.1rem; }}
.figure .sw {{ height: 104px; border-radius: 4px; display: flex; align-items: flex-end; padding: .55rem .7rem; }}
.stApp.stApp.stApp .figure .sw b {{ font-family: var(--display) !important; color: #fff; font-size: 1.7rem; font-weight: 500; line-height: 1; }}
.figure .txt {{ border-left: 1px solid rgba(38,38,38,.2); padding-left: 1.2rem; }}
.figure .txt .kicker {{ display: block; margin-bottom: .45rem; }}
.figure .txt p {{ margin: 0; font-size: .9rem; line-height: 1.5; color: var(--muted); }}

/* Section headings */
.sec {{ margin-top: 6rem; scroll-margin-top: 80px; }}
.sec-head {{ display: grid; grid-template-columns: 1fr auto; align-items: end; gap: 1rem; border-bottom: 1px solid var(--ink); padding-bottom: .9rem; margin-bottom: 2rem; }}
.stApp.stApp.stApp .sec-head h2 {{ font-family: var(--display) !important; font-weight: 400; font-size: clamp(2.4rem, 5.2vw, 3.9rem);
  line-height: .98; margin: .5rem 0 0 0; padding: 0 !important; text-transform: uppercase; }}
.stApp.stApp.stApp .sec-head .dek {{ font-family: var(--serif) !important; font-style: italic; font-size: 1.05rem; color: var(--muted); max-width: 34ch; text-align: right; margin: 0; }}

/* Capabilities: two-column index */
.caps {{ display: grid; grid-template-columns: 1fr 1fr; gap: 0 2.4rem; }}
.cap {{ display: grid; grid-template-columns: 14px 1fr; gap: 1rem; padding: 1.2rem 0; border-bottom: 1px solid rgba(38,38,38,.18); }}
.cap .dot {{ width: 14px; height: 14px; border-radius: 3px; margin-top: .35rem; }}
.stApp.stApp.stApp .cap h3 {{ font-family: var(--display) !important; font-weight: 500; font-size: 1.45rem; margin: 0 0 .35rem 0; padding: 0 !important; }}
.stApp.stApp.stApp .cap p {{ font-family: var(--serif) !important; margin: 0 0 .5rem 0; font-size: 1.02rem; line-height: 1.5; }}
.cap .tools {{ font-size: .82rem; color: var(--muted); line-height: 1.5; }}
.cap .where {{ font-size: .74rem; letter-spacing: .14em; text-transform: uppercase; color: var(--clay); margin-top: .45rem; }}

/* Lead story */
.lead {{ padding: 2.4rem; }}
.lead-grid {{ display: grid; grid-template-columns: 1.2fr 1fr; gap: 2.4rem; }}
.stApp.stApp.stApp .lead h3 {{ font-family: var(--display) !important; font-weight: 400; font-size: clamp(2.2rem, 4.4vw, 3.4rem); line-height: 1; margin: .6rem 0 1rem 0; padding: 0 !important; }}
.stApp.stApp.stApp .lead p.body {{ font-family: var(--serif) !important; font-size: 1.08rem; line-height: 1.62; margin: 0 0 1rem 0; column-gap: 2rem; }}
.review {{ background: rgba(255,255,255,.62); border: 1px solid rgba(255,255,255,.9); border-radius: 12px; padding: .9rem 1rem; margin-bottom: .7rem; display: grid; grid-template-columns: 1fr auto; gap: .8rem; }}
.stApp.stApp.stApp .review p {{ font-family: var(--serif) !important; font-style: italic; margin: 0; font-size: 1rem; line-height: 1.45; }}
.tag {{ font-size: .68rem; letter-spacing: .12em; text-transform: uppercase; padding: .22rem .55rem; border-radius: 999px; color: #fff; height: fit-content; white-space: nowrap; }}
.tag.neg {{ background: var(--orange); }}
.tag.pos {{ background: var(--green); }}
.tag.neu {{ background: var(--taupe); }}
.words {{ font-size: .84rem; color: var(--muted); margin: .1rem 0 1rem .2rem; }}
.words mark {{ background: rgba(234,97,29,.14); color: var(--ink); padding: 0 .3rem; border-radius: 4px; }}
.facts {{ display: grid; grid-template-columns: repeat(4, 1fr); margin-top: 2rem; border-top: 1px solid rgba(38,38,38,.25); }}
.facts div {{ padding: 1rem 1rem 0 0; }}
.stApp.stApp.stApp .facts b {{ display: block; font-family: var(--display) !important; font-size: 2.1rem; font-weight: 500; line-height: 1.05; }}
.facts span {{ font-size: .82rem; color: var(--muted); line-height: 1.4; display: block; margin-top: .3rem; }}

/* Article grid */
.stories {{ display: grid; grid-template-columns: 1fr 1fr; gap: 1.4rem; margin-top: 1.4rem; }}
.story {{ padding: 1.8rem 1.9rem 1.6rem 1.9rem; border-top: 6px solid var(--accent) !important; }}
.story .row {{ display: flex; justify-content: space-between; }}
.stApp.stApp.stApp .story h3 {{ font-family: var(--display) !important; font-weight: 400; font-size: 1.95rem; line-height: 1.05; margin: 1rem 0 .7rem 0; padding: 0 !important; }}
.stApp.stApp.stApp .story p {{ font-family: var(--serif) !important; font-size: 1.02rem; line-height: 1.55; color: var(--ink); margin: 0 0 1.1rem 0; }}
.story .nums {{ display: flex; gap: 2rem; margin-bottom: 1.1rem; }}
.stApp.stApp.stApp .story .nums b {{ display: block; font-family: var(--display) !important; font-size: 1.8rem; font-weight: 500; color: var(--accent); }}
.story .nums span {{ font-size: .8rem; color: var(--muted); }}

/* Dashboards */
.dash-notes {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 1.4rem; margin-bottom: 1.6rem; }}
.dash-notes div {{ border-top: 3px solid var(--accent); padding-top: .8rem; }}
.dash-notes b {{ display: block; font-weight: 600; margin-bottom: .3rem; }}
.stApp.stApp.stApp .dash-notes span {{ font-family: var(--serif) !important; color: var(--muted); font-size: .98rem; line-height: 1.5; }}
.st-key-bi {{ padding: 1.2rem; }}
.st-key-bi iframe {{ border-radius: 12px; }}

/* Live demo */
.st-key-demo {{ padding: 1.8rem 1.8rem 1rem 1.8rem; }}
.steps {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 1rem; margin: .6rem 0 1.4rem 0; }}
.steps div {{ background: rgba(255,255,255,.55); border: 1px solid rgba(255,255,255,.9); border-radius: 12px; padding: .9rem 1rem; border-left: 4px solid var(--accent); }}
.steps .kicker {{ font-size: .66rem; }}
.stApp.stApp.stApp .steps b {{ display: block; font-family: var(--display) !important; font-size: 2.2rem; font-weight: 500; line-height: 1.1; }}
.steps small {{ color: var(--muted); }}
.check {{ font-size: .95rem; padding: .45rem 0; border-bottom: 1px solid rgba(38,38,38,.12); display: flex; gap: .7rem; }}
.check .ok {{ color: var(--green); font-weight: 600; }}
.check .ko {{ color: var(--orange); font-weight: 600; }}
.stButton button, .stDownloadButton button {{ border-radius: 999px !important; border: 1px solid var(--ink) !important; background: rgba(255,255,255,.4) !important; }}
.stDownloadButton button:hover {{ background: var(--ink) !important; color: var(--paper) !important; }}
[data-testid="stExpander"] details {{ border-radius: 12px !important; background: rgba(255,255,255,.4); border: 1px solid rgba(255,255,255,.85) !important; }}
div[data-baseweb="input"], div[data-baseweb="base-input"] {{ background: rgba(255,255,255,.55) !important; }}

/* About */
.about {{ display: grid; grid-template-columns: 1.1fr 1fr; gap: 2.2rem; align-items: start; }}
.notes {{ padding: 2rem 2.2rem; }}
.note {{ padding: 1rem 0; border-bottom: 1px solid rgba(38,38,38,.15); }}
.note:last-child {{ border-bottom: none; padding-bottom: 0; }}
.note:first-child {{ padding-top: 0; }}
.stApp.stApp.stApp .note h4 {{ font-family: var(--display) !important; font-weight: 500; font-size: 1.35rem; margin: 0 0 .35rem 0; padding: 0 !important; }}
.stApp.stApp.stApp .note p {{ font-family: var(--serif) !important; color: var(--ink); font-size: 1.02rem; line-height: 1.55; margin: 0; }}
.path {{ width: 100%; border-collapse: collapse; }}
.path tr {{ border-bottom: 1px solid rgba(38,38,38,.18); }}
.path td {{ padding: .9rem .8rem .9rem 0; vertical-align: top; font-size: .95rem; }}
.path td.year {{ width: 26%; color: var(--clay); font-size: .78rem; letter-spacing: .14em; text-transform: uppercase; padding-top: 1.05rem; }}
.path td.what b {{ display: block; font-weight: 600; }}
.path td.what span {{ color: var(--muted); font-size: .9rem; }}

/* Contact and footer */
.contact {{ margin-top: 6rem; padding: 3rem 2.4rem; text-align: center; scroll-margin-top: 80px; }}
.stApp.stApp.stApp .contact h2 {{ font-family: var(--display) !important; font-weight: 400; font-size: clamp(2.6rem, 6vw, 4.6rem); text-transform: uppercase; margin: .6rem 0 .8rem 0; padding: 0 !important; line-height: 1; }}
.stApp.stApp.stApp .contact p {{ font-family: var(--serif) !important; font-style: italic; font-size: 1.15rem; color: var(--muted); margin: 0 0 1.6rem 0; }}
.stApp .contact .mail {{ font-family: var(--display) !important; font-size: clamp(1.5rem, 3.2vw, 2.3rem); text-decoration: none; color: var(--ink) !important; border-bottom: 2px solid var(--clay); }}
.foot {{ display: flex; justify-content: space-between; align-items: center; margin: 2.4rem 0 0 0; padding-top: .9rem; border-top: 1px solid var(--ink); font-size: .74rem; color: var(--muted); letter-spacing: .08em; }}

@media (max-width: 860px) {{
  .block-container {{ padding: 0 1rem 2rem 1rem; }}
  .mast-grid, .front, .lead-grid, .caps, .stories, .about, .dash-notes, .steps {{ grid-template-columns: 1fr; }}
  .facts {{ grid-template-columns: 1fr 1fr; }}
  .sec-head {{ grid-template-columns: 1fr; }}
  .stApp.stApp.stApp .sec-head .dek {{ text-align: left; }}
  .sections {{ gap: .9rem; }} .sections .date {{ display: none; }}
  .article, .lead {{ padding: 1.6rem 1.4rem; }}
  .figure {{ grid-template-columns: 92px 1fr; }}
  .foot {{ flex-direction: column; gap: .4rem; }}
  .inside {{ display: none; }}
}}
</style>
""")

# =============================================================================
# MASTHEAD + SECTION BAR
# =============================================================================
swatches = "".join(f"<i style='background:{c}'></i>" for c in (BLUE, ORANGE, PINK, GREEN, CLAY))
html(f"""
<header class="masthead" id="top">
<div class="mast-top"><span class="brand">Portfolio</span><span class="kicker muted">Hermosillo, Mexico</span></div>
<div class="mast-grid">
<div>
<h1>María<br>Carolina</h1>
<p class="tagline">Data science · Machine learning · Data engineering</p>
<div class="swatches">{swatches}</div>
</div>
<aside class="inside glass">
<span class="kicker">In this edition</span>
<a href="#capabilities"><em>A</em>Capabilities</a>
<a href="#work"><em>B</em>Selected work</a>
<a href="#dashboards"><em>C</em>Dashboards</a>
<a href="#demo"><em>D</em>Live demo</a>
<a href="#about"><em>E</em>About</a>
</aside>
</div>
</header>
<nav class="sections glass">
<a href="#front">Front page</a>
<a href="#capabilities">Capabilities</a>
<a href="#work">Work</a>
<a href="#dashboards">Dashboards</a>
<a href="#demo">Demo</a>
<a href="#about">About</a>
<a href="#contact">Contact</a>
<span class="date">{TODAY}</span>
</nav>
""")

# =============================================================================
# FRONT PAGE
# =============================================================================
figs = "".join(
    f"<div class='figure'><div class='sw' style='background:{c}'><b>{num}</b></div>"
    f"<div class='txt'><span class='kicker'>{name}</span><p>{text}</p></div></div>"
    for c, num, name, text in FIGURES
)
html(f"""
<section class="front" id="front">
<article class="article glass">
<div class="byline">By María Carolina González Bernal<br>{TODAY}</div>
<p class="body first">I work with data from the first messy file to the finished tool: cleaning it, testing what it says and building models and apps that other people can use.</p>
<p class="body">I recently completed an M.Sc. in Data Science, Big Data &amp; Business Analytics at Complutense University of Madrid. Before that I studied anthropology, which taught me to listen and to frame a question carefully before looking for an answer.</p>
<p class="body">The projects on this page cover natural language processing, machine learning, data pipelines, statistics and dashboards. Each one links to the code, a live app or a report.</p>
<div class="pull"><span class="mark">“</span><p>Clean inputs, honest validation and results people can read.</p></div>
<a class="btn btn-ink" href="#work">Read the work</a>
<a class="btn btn-line" href="#demo">Try the demo</a>
</article>
<aside class="figures">
<div class="head"><span class="kicker">Key figures</span></div>
{figs}
</aside>
</section>
""")

# =============================================================================
# CAPABILITIES
# =============================================================================
caps = "".join(
    f"<div class='cap'><span class='dot' style='background:{c}'></span><div>"
    f"<h3>{name}</h3><p>{what}</p><div class='tools'>{tools}</div><div class='where'>{where}</div></div></div>"
    for name, c, what, tools, where in CAPABILITIES
)
html(f"""
<section class="sec" id="capabilities">
<div class="sec-head"><div><span class="kicker muted">Section A</span><h2>Capabilities</h2></div>
<p class="dek">The areas I have worked in, each linked to a project.</p></div>
<div class="caps">{caps}</div>
</section>
""")

# =============================================================================
# WORK
# =============================================================================
html(f"""
<section class="sec" id="work">
<div class="sec-head"><div><span class="kicker muted">Section B</span><h2>Selected work</h2></div>
<p class="dek">Live apps, code and reports, with results measured on data the models had not seen.</p></div>
<article class="lead glass">
<div class="lead-grid">
<div>
<span class="kicker" style="color:var(--blue)">Lead story · NLP and deployment</span>
<h3>What 1.16 million diners say about Madrid's restaurants</h3>
<p class="body">A reputation tool for 10,056 restaurants. It summarises each restaurant, compares it with similar places, flags reputations that declined and classifies any review in Spanish or English, showing how much each word weighed in the decision.</p>
<p class="body">The data were split by restaurant, so the final test used places the model had never seen. The model is served through a FastAPI service with tests and tracked in MLflow.</p>
<a class="btn btn-ink" href="{LINKS['restaurants']}" target="_blank">Open the app</a>
<a class="btn btn-line" href="{LINKS['restaurants_repo']}" target="_blank">Code</a>
</div>
<div aria-hidden="true">
<div class="review"><p>“La paella llegó fría y el servicio fue lentísimo.”</p><span class="tag neg">Negative</span></div>
<p class="words">Strongest words: <mark>fría</mark> <mark>lentísimo</mark></p>
<div class="review"><p>“Best tapas we had in Madrid, the staff were lovely.”</p><span class="tag pos">Positive</span></div>
<div class="review"><p>“Correcto, sin más. Precio un poco alto.”</p><span class="tag neu">Neutral</span></div>
</div>
</div>
<div class="facts">
<div><b style="color:var(--blue)">110,912</b><span>test reviews from 996 unseen restaurants</span></div>
<div><b style="color:var(--orange)">0.879</b><span>recall on negative reviews</span></div>
<div><b style="color:var(--pink)">0.809 / 0.793</b><span>macro F1 in Spanish and English</span></div>
<div><b style="color:var(--green)">28,660</b><span>backtest evaluations of the alert rule</span></div>
</div>
</article>
<div class="stories">
<article class="story glass" style="--accent:{ORANGE}">
<div class="row"><span class="kicker muted">Machine learning · competition</span></div>
<h3>Which water pumps will fail next?</h3>
<p>60,000 water points in Tanzania with three possible outcomes. Feature engineering, target encoding fitted on training data only, and gradient boosting tuned with Optuna.</p>
<div class="nums"><div><b>0.8132</b><span>leaderboard</span></div><div><b>0.817</b><span>5-fold CV</span></div></div>
<a class="btn btn-line" href="{LINKS['pumps']}" target="_blank">Code</a>
</article>
<article class="story glass" style="--accent:{PINK}">
<div class="row"><span class="kicker muted">Python app · live</span></div>
<h3>Guess the Number, rebuilt as an app</h3>
<p>A console game turned into a Streamlit app with game modes, difficulty levels, scoring, saved results and a records screen with a leaderboard and charts.</p>
<div class="nums"><div><b>3</b><span>difficulty levels</span></div><div><b>6</b><span>modules</span></div></div>
<a class="btn btn-ink" href="{LINKS['guess']}" target="_blank">Play</a>
<a class="btn btn-line" href="{LINKS['guess_repo']}" target="_blank">Code</a>
</article>
<article class="story glass" style="--accent:{GREEN}">
<div class="row"><span class="kicker muted">Data engineering</span></div>
<h3>A server inventory, generated and checked</h3>
<p>Hostnames created from a naming convention, parsed into fields and validated. An improved version runs in the demo section below.</p>
<div class="nums"><div><b>1,500</b><span>records</span></div><div><b>5</b><span>quality checks</span></div></div>
<a class="btn btn-ink" href="#demo">Try it</a>
<a class="btn btn-line" href="{LINKS['hostnames']}" target="_blank">Report</a>
</article>
<article class="story glass" style="--accent:{CLAY}">
<div class="row"><span class="kicker muted">Statistics · health data</span></div>
<h3>Glucose tolerance in young and adult patients</h3>
<p>Two groups compared with normality checks, t-tests and ANOVA, plus a regression that predicts glucose 60 minutes after intake.</p>
<div class="nums"><div><b>0.634</b><span>R²</span></div><div><b>4.61</b><span>RMSE, mg/dL</span></div></div>
<a class="btn btn-line" href="{LINKS['glucose']}" target="_blank">Report</a>
</article>
</div>
</section>
""")

# =============================================================================
# DASHBOARDS (Tableau)
# =============================================================================
html(f"""
<section class="sec" id="dashboards">
<div class="sec-head"><div><span class="kicker muted">Section C</span><h2>Dashboards</h2></div>
<p class="dek">Easy Loans: a year of lending across Europe, in Tableau.</p></div>
<div class="dash-notes">
<div style="--accent:{BLUE}"><b>Loan operations</b><span>KPIs, deviation from the average, running total and date and country filters.</span></div>
<div style="--accent:{ORANGE}"><b>Merchant analysis</b><span>Top 10 merchants, merchants by country and an interactive map.</span></div>
<div style="--accent:{GREEN}"><b>Details</b><span>LOD and table calculations, a minimum-amount parameter and reset buttons.</span></div>
</div>
</section>
""")
live_views = {name: url for name, url in TABLEAU_DASHBOARDS.items() if url.strip()}
if live_views:
    with st.container(key="bi"):
        top_left, top_right = st.columns([3, 1], vertical_alignment="center")
        view = top_left.segmented_control("Dashboard", list(live_views), default=list(live_views)[0],
                                          label_visibility="collapsed") or list(live_views)[0]
        top_right.link_button("Open in Tableau Public ↗", TABLEAU_PROFILE, width="stretch")
        url = live_views[view]
        src = f"{url}{'&' if '?' in url else '?'}:showVizHome=no&:embed=true&:toolbar=bottom"
        if hasattr(st, "iframe"):
            st.iframe(src, height=860)
        else:
            components.iframe(src, height=860, scrolling=True)

# =============================================================================
# LIVE DEMO (hostname pipeline)
# =============================================================================
OS_MAP = {"L": ("Linux", 0.40), "S": ("Solaris", 0.30), "A": ("AIX", 0.20), "H": ("HP-UX", 0.10)}
ENV_MAP = {"D": ("Development", 0.10), "I": ("Integration", 0.10), "T": ("Testing", 0.25),
           "S": ("Staging", 0.25), "P": ("Production", 0.30)}
COUNTRY_MAP = {"NOR": ("Norway", 0.06), "FRA": ("France", 0.09), "ITA": ("Italy", 0.16),
               "ESP": ("Spain", 0.16), "GER": ("Germany", 0.23), "IRL": ("Ireland", 0.30)}


def _weighted(rng, mapping, n):
    codes = list(mapping)
    probs = np.array([mapping[c][1] for c in codes])
    return rng.choice(codes, size=n, p=probs / probs.sum())


@st.cache_data(show_spinner=False)
def generate_hostnames(n: int, seed: int, unique: bool) -> list[str]:
    """Extract: generate raw hostnames that follow the naming convention."""
    rng = np.random.default_rng(seed)
    hostnames, seen = [], set()
    while len(hostnames) < n:
        batch = n - len(hostnames)
        prefixes = np.char.add(np.char.add(_weighted(rng, OS_MAP, batch), _weighted(rng, ENV_MAP, batch)),
                               _weighted(rng, COUNTRY_MAP, batch))
        for p, node in zip(prefixes, rng.integers(1, 1000, size=batch)):
            name = f"{p}{node:03d}"
            if unique and name in seen:
                continue
            seen.add(name)
            hostnames.append(name)
    return hostnames


def parse_hostnames(hostnames: list[str]) -> pd.DataFrame:
    """Transform: decode each hostname into typed fields."""
    s = pd.Series(hostnames)
    return pd.DataFrame({
        "hostname": s,
        "os": s.str[0].map({k: v[0] for k, v in OS_MAP.items()}),
        "environment": s.str[1].map({k: v[0] for k, v in ENV_MAP.items()}),
        "country": s.str[2:5].map({k: v[0] for k, v in COUNTRY_MAP.items()}),
        "node": s.str[5:8].astype(int),
    })


def validate(df: pd.DataFrame) -> dict:
    """Validate: schema, format, completeness, range, uniqueness and distribution drift."""
    duplicates = int(df["hostname"].duplicated().sum())
    checks = {
        "Expected columns present": set(df.columns) == {"hostname", "os", "environment", "country", "node"},
        "Every hostname has 8 characters": bool(df["hostname"].str.len().eq(8).all()),
        "Every field parsed": bool(df.notna().all().all()),
        "Node numbers within 001–999": bool(df["node"].between(1, 999).all()),
        "No duplicate hostnames": duplicates == 0,
    }
    rows = []
    for field, mapping in (("os", OS_MAP), ("environment", ENV_MAP), ("country", COUNTRY_MAP)):
        observed = df[field].value_counts(normalize=True)
        for label, target in mapping.values():
            rows.append({"field": field, "category": label, "target": target,
                         "observed": float(observed.get(label, 0.0))})
    dist = pd.DataFrame(rows)
    dist["gap_pp"] = (dist["observed"] - dist["target"]).abs() * 100
    return {"checks": checks, "duplicates": duplicates, "distribution": dist}


PLOT_FONT = dict(family="Inter, Helvetica Neue, Arial, sans-serif", color=INK, size=13)

html("""
<section class="sec" id="demo">
<div class="sec-head"><div><span class="kicker muted">Section D</span><h2>Live demo</h2></div>
<p class="dek">A small data pipeline: generate a server inventory, parse it and check its quality.</p></div>
</section>
""")

with st.container(key="demo"):
    c1, c2, c3 = st.columns(3, gap="large")
    n_hosts = c1.slider("Servers to generate", 100, 5000, 1500, step=100)
    seed = c2.number_input("Random seed", min_value=0, max_value=9999, value=42, step=1)
    c3.write("")
    unique = c3.toggle("Block duplicate hostnames", value=True,
                       help="The original notebook did not include this check. Turn it off to see duplicates appear.")

    raw = generate_hostnames(n_hosts, int(seed), unique)
    data = parse_hostnames(raw)
    report = validate(data)
    passed = sum(report["checks"].values())

    html(f"""
    <div class="steps">
    <div style="--accent:{BLUE}"><span class="kicker">1 · Generate</span><b>{len(raw):,}</b><small>hostnames</small></div>
    <div style="--accent:{CLAY}"><span class="kicker">2 · Parse</span><b>{data.shape[1]}</b><small>structured fields</small></div>
    <div style="--accent:{GREEN}"><span class="kicker">3 · Validate</span><b>{passed}/{len(report['checks'])}</b><small>checks passed</small></div>
    </div>
    """)

    left, right = st.columns([1, 1.7], gap="large")
    with left:
        items = "".join(
            f"<div class='check'><span class='{'ok' if ok else 'ko'}'>{'✓' if ok else '✕'}</span>{name}</div>"
            for name, ok in report["checks"].items()
        )
        worst = report["distribution"]["gap_pp"].max()
        dup_note = (f"<p style='color:{ORANGE};margin:.8rem 0 0 0'>{report['duplicates']} duplicate hostnames found.</p>"
                    if report["duplicates"] else "")
        html(f"{items}{dup_note}<p style='color:{MUTED};margin:1rem 0'>Largest gap from the target mix: "
             f"<b style='color:{INK}'>{worst:.1f} percentage points</b>.</p>")
        st.download_button("Download the CSV", data.to_csv(index=False).encode("utf-8"),
                           file_name="hosts.csv", mime="text/csv", width="stretch")
    with right:
        field = st.segmented_control(
            "Target vs observed", ["os", "environment", "country"], default="environment",
            format_func=lambda f: {"os": "OS", "environment": "Environment", "country": "Country"}[f],
        ) or "environment"
        dist = report["distribution"].query("field == @field")
        fig = go.Figure()
        fig.add_bar(x=dist["category"], y=dist["target"] * 100, name="Target", marker_color=SAND)
        fig.add_bar(x=dist["category"], y=dist["observed"] * 100, name="Observed", marker_color=BLUE)
        fig.update_traces(marker_line_width=0)
        fig.update_layout(barmode="group", height=300, margin=dict(l=0, r=0, t=10, b=0), bargap=.3,
                          yaxis=dict(title="Share of servers (%)", gridcolor="rgba(38,38,38,.08)", zeroline=False),
                          legend=dict(orientation="h", y=1.12, x=0), plot_bgcolor="rgba(0,0,0,0)",
                          paper_bgcolor="rgba(0,0,0,0)", font=PLOT_FONT)
        st.plotly_chart(fig, width="stretch", config={"displayModeBar": False})

    pivot = data.groupby(["country", "environment"]).size().reset_index(name="servers")
    fig2 = px.bar(pivot, x="country", y="servers", color="environment", height=300,
                  color_discrete_sequence=[BLUE, ORANGE, PINK, GREEN, CLAY])
    fig2.update_traces(marker_line_width=0)
    fig2.update_layout(margin=dict(l=0, r=0, t=34, b=0), plot_bgcolor="rgba(0,0,0,0)",
                       paper_bgcolor="rgba(0,0,0,0)", font=PLOT_FONT, xaxis_title="", yaxis_title="Servers",
                       yaxis=dict(gridcolor="rgba(38,38,38,.08)"), legend_title_text="", bargap=.35,
                       title=dict(text="Servers by country and environment", font=dict(size=14)))
    st.plotly_chart(fig2, width="stretch", config={"displayModeBar": False})

    with st.expander("Preview the parsed data"):
        st.dataframe(data.head(50), width="stretch", hide_index=True)

# =============================================================================
# ABOUT
# =============================================================================
html(f"""
<section class="sec" id="about">
<div class="sec-head"><div><span class="kicker muted">Section E</span><h2>About</h2></div>
<p class="dek">How I like to work, and the path that brought me here.</p></div>
<div class="about">
<div class="notes glass">
<div class="note"><h4>Questions first</h4><p>Anthropology taught me to interview, observe and define the problem before choosing a method.</p></div>
<div class="note"><h4>Careful validation</h4><p>Leakage checks, untouched test sets and data quality tests, so results hold up outside the notebook.</p></div>
<div class="note"><h4>Languages</h4><p>Spanish (native), English (C1) and German (B1+, still learning). Open to relocation.</p></div>
</div>
<table class="path">
<tr><td class="year">2025–2026</td><td class="what"><b>M.Sc. Data Science, Big Data &amp; Business Analytics</b><span>Complutense University of Madrid</span></td></tr>
<tr><td class="year">2024–2025</td><td class="what"><b>Data Science Bootcamp</b><span>TripleTen</span></td></tr>
<tr><td class="year">2024</td><td class="what"><b>Survey data analysis, internship</b><span>Hermosillo City Hall</span></td></tr>
<tr><td class="year">2023</td><td class="what"><b>Social development research, internship</b><span>Ministry of Social Development of Sonora</span></td></tr>
<tr><td class="year">2019–2024</td><td class="what"><b>B.A. Anthropology</b><span>University of Sonora</span></td></tr>
</table>
</div>
</section>
""")

# =============================================================================
# CONTACT + FOOTER
# =============================================================================
html(f"""
<section class="contact glass" id="contact">
<span class="kicker muted">Contact</span>
<h2>Get in touch</h2>
<p>For Data Scientist, ML and Data Engineering roles, I would be glad to hear from you.</p>
<a class="mail" href="{LINKS['email']}">Carolinagles@gmail.com</a>
<div class="swatches" style="justify-content:center;margin-top:2rem">{swatches}</div>
</section>
<div class="foot"><span>María Carolina González Bernal · Portfolio</span><span>Built with Python, Streamlit and Plotly</span></div>
""")
