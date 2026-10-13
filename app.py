"""
María Carolina · Data Science & Data Engineering portfolio (Streamlit).
Run locally:  streamlit run app.py

Design: Swiss / International Typographic Style. Strict grid, large grotesk type,
hairline rules, one signal colour (International Klein Blue) and no decoration
that does not carry information.

Content lives in the CONTENT section. Styling lives in STYLE.
"""

import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="María Carolina · Data Scientist", page_icon="■", layout="wide")


def html(block: str) -> None:
    """Render raw HTML. Lines are left-stripped so Markdown never turns them into code blocks."""
    clean = "\n".join(line.strip() for line in block.strip().splitlines() if line.strip())
    st.markdown(clean, unsafe_allow_html=True)


# =============================================================================
# CONTENT
# =============================================================================
LINKS = {
    "email": "mailto:Carolinagles@gmail.com",
    "linkedin": "https://www.linkedin.com/in/carolinagles/",
    "github": "https://github.com/carolinagles",
    "notion": "https://www.notion.so/Hi-I-m-Maria-Carolina-207fea9d890080a99c11c189f1bd930d",
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

# name, what it means for a team, tools, where it is proven
CAPABILITIES = [
    ("Machine learning",
     "Models judged on data they have never seen, split by group so nothing leaks.",
     "Scikit-learn, LightGBM, CatBoost, XGBoost, Optuna",
     "Restaurant intelligence, Pump It Up"),
    ("Natural language",
     "Spanish and English text classified, with every prediction explained word by word.",
     "TF-IDF, LinearSVC, Transformers, spaCy, NLTK",
     "Restaurant intelligence"),
    ("Data engineering",
     "Inputs generated, parsed, validated and exported without silent errors.",
     "Pandas, NumPy, Pandera, Parquet, SQL",
     "Hostname pipeline, Restaurant intelligence"),
    ("From notebook to product",
     "Models served behind a tested API and wrapped in apps people use.",
     "FastAPI, MLflow, pytest, Streamlit",
     "Restaurant intelligence, Guess the Number"),
    ("Statistics and BI",
     "The right test for the question, then a dashboard a manager reads in seconds.",
     "Hypothesis testing, ANOVA, regression, Tableau, Plotly",
     "Glucose study, Easy Loans"),
    ("Scale and cloud",
     "Distributed and cloud tools from my M.Sc. at Complutense University of Madrid.",
     "PySpark, Spark SQL, MLlib, Google Cloud, MongoDB, Snowflake",
     "M.Sc. coursework"),
]

# =============================================================================
# STYLE
# =============================================================================
BLUE = "#002FA7"      # International Klein Blue
INK = "#0E0E0E"
GREY = "#5F5F5A"
RULE = "#0E0E0E"
PAPER = "#F4F4F1"
TINT = "#E6EAF6"

html(f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter+Tight:wght@500;600;700;800&family=Inter:wght@400;500;600&family=IBM+Plex+Mono:wght@400;500&display=swap');
:root {{ --ink:{INK}; --grey:{GREY}; --blue:{BLUE}; --paper:{PAPER}; --tint:{TINT};
  --display: "Inter Tight", "Helvetica Neue", Helvetica, Arial, sans-serif;
  --text: "Inter", "Helvetica Neue", Helvetica, Arial, sans-serif;
  --mono: "IBM Plex Mono", ui-monospace, Menlo, monospace; }}
html, body, .stApp, .stApp :is(h1,h2,h3,h4,p,span,div,a,b,li,label,button,input,small,td,th):not([data-testid="stIconMaterial"]):not(.material-symbols-rounded) {{
  font-family: var(--text) !important; -webkit-font-smoothing: antialiased; }}
.stApp.stApp.stApp :is(h1,h2,h3,h4,b) :is(span) {{ font-family: inherit !important; }}
.stApp {{ background: var(--paper); color: var(--ink); overflow-x: hidden; }}
header[data-testid="stHeader"], #MainMenu, footer, [data-testid="stToolbar"], [data-testid="stDecoration"] {{ display: none !important; }}
.block-container {{ max-width: 1180px; padding: 0 2rem 0 2rem; }}
a {{ color: inherit; }}
[data-testid="stHeaderActionElements"], .stApp h1 a[href^="#"] svg {{ display: none !important; }}
::selection {{ background: var(--blue); color: #fff; }}

/* Type helpers */
.stApp.stApp.stApp .display, .stApp.stApp.stApp .display * {{ font-family: var(--display) !important; }}
.stApp.stApp.stApp .mono, .stApp.stApp.stApp .mono * {{ font-family: var(--mono) !important; }}
.label {{ font-size: .78rem; color: var(--grey); letter-spacing: .01em; }}

/* Navigation */
.nav {{ position: fixed; top: 0; left: 0; right: 0; z-index: 999; background: rgba(244,244,241,.94);
  border-bottom: 1px solid {RULE}; height: 54px; display: flex; align-items: center; }}
.nav .inner {{ width: 100%; max-width: 1180px; margin: 0 auto; padding: 0 2rem; display: flex; align-items: center; gap: 2rem; font-size: .88rem; }}
.nav .brand {{ font-weight: 600; margin-right: auto; text-decoration: none; display: flex; align-items: center; gap: .6rem; }}
.nav .brand i {{ width: 14px; height: 14px; background: var(--blue); display: inline-block; }}
.stApp .nav a {{ text-decoration: none; color: var(--ink) !important; }}
.stApp .nav a.cta {{ color: var(--paper) !important; }}
.stApp .nav a:not(.brand):not(.cta):hover {{ color: var(--blue) !important; }}
.nav .cta {{ background: var(--ink); color: var(--paper); padding: .45rem .9rem; }}
.nav .cta:hover {{ background: var(--blue); color: #fff !important; }}
a:focus-visible, button:focus-visible {{ outline: 2px solid var(--blue); outline-offset: 3px; }}

/* Hero */
.hero {{ padding: 7.5rem 0 0 0; }}
.hero .meta {{ display: grid; grid-template-columns: repeat(4, 1fr); gap: 1.5rem; border-top: 1px solid {RULE}; padding-top: .8rem; }}
.hero .meta div {{ font-size: .9rem; line-height: 1.4; }}
.hero .meta .label {{ display: block; margin-bottom: .2rem; }}
.stApp.stApp.stApp .hero h1 {{ font-family: var(--display) !important; font-weight: 800; font-size: clamp(4rem, 16vw, 15rem);
  line-height: .84; letter-spacing: -0.055em; margin: 2.4rem 0 0 -0.05em; padding: 0 !important; color: var(--ink); }}
.hero h1 .second {{ display: block; }}
.hero h1 .dot {{ color: var(--blue); }}
.hero .statement {{ display: grid; grid-template-columns: 1fr 3fr; gap: 1.5rem; margin: 2.4rem 0 0 0; padding-top: 1rem; border-top: 1px solid {RULE}; }}
.stApp.stApp.stApp .hero .statement p.lead {{ font-family: var(--display) !important; font-size: clamp(1.6rem, 3.4vw, 2.6rem); font-weight: 600;
  line-height: 1.08; letter-spacing: -0.03em; margin: 0; max-width: 26ch; }}
.hero .statement p.sub {{ font-size: 1.05rem; color: var(--grey); line-height: 1.55; margin: 1.1rem 0 1.6rem 0; max-width: 52ch; }}

.btn {{ display: inline-block; padding: .85rem 1.25rem; font-size: .95rem; font-weight: 500; text-decoration: none !important;
  border: 1px solid var(--ink); margin: 0 .5rem .5rem 0; transition: background .15s, color .15s, border-color .15s; }}
.btn-solid {{ background: var(--ink); color: var(--paper) !important; }}
.btn-solid:hover {{ background: var(--blue); border-color: var(--blue); color: #fff !important; }}
.btn-line {{ color: var(--ink) !important; }}
.btn-line:hover {{ background: var(--ink); color: var(--paper) !important; }}
.btn .arrow {{ margin-left: .5rem; }}

/* Full-bleed blue band */
.band {{ width: 100vw; position: relative; left: 50%; margin-left: -50vw; background: var(--blue); color: #fff; }}
.band .inner {{ max-width: 1180px; margin: 0 auto; padding: 3.2rem 2rem; }}
.counter {{ display: grid; grid-template-columns: 3fr 1fr; gap: 1.5rem; align-items: end; margin-top: 4.5rem; }}
.stApp.stApp.stApp .counter .big {{ font-family: var(--display) !important; font-weight: 800; font-size: clamp(3.6rem, 12vw, 10rem);
  line-height: .85; letter-spacing: -0.05em; margin: 0; }}
.counter p {{ font-size: 1.05rem; line-height: 1.45; margin: 0; color: rgba(255,255,255,.88); }}
.figures {{ display: grid; grid-template-columns: repeat(4, 1fr); border-top: 1px solid rgba(255,255,255,.55); margin-top: 2.4rem; }}
.figures div {{ padding: .9rem 1rem 0 0; }}
.stApp.stApp.stApp .figures b {{ display: block; font-family: var(--display) !important; font-size: clamp(1.8rem, 3.6vw, 2.8rem); font-weight: 700; letter-spacing: -0.03em; }}
.figures span {{ font-size: .86rem; color: rgba(255,255,255,.8); }}

/* Section scaffold: label column + content column */
.sec {{ display: grid; grid-template-columns: 1fr 3fr; gap: 1.5rem; border-top: 1px solid {RULE}; padding-top: 1rem; margin-top: 7rem; scroll-margin-top: 70px; }}
.sec .label {{ font-size: .9rem; color: var(--ink); font-weight: 500; }}
.stApp.stApp.stApp :is(.sec, .contact) h2 {{ padding: 0 !important; }}
.stApp.stApp.stApp .sec h2 {{ font-family: var(--display) !important; font-weight: 700; font-size: clamp(2.4rem, 5.4vw, 4.4rem);
  line-height: .95; letter-spacing: -0.045em; margin: 0 0 1rem 0; }}
.sec p.intro {{ font-size: 1.1rem; color: var(--grey); line-height: 1.55; max-width: 56ch; margin: 0 0 2.4rem 0; }}

/* Capability index */
.index {{ width: 100%; border-collapse: collapse; }}
.index tr {{ border-top: 1px solid {RULE}; }}
.index tr:last-child {{ border-bottom: 1px solid {RULE}; }}
.index td {{ vertical-align: top; padding: 1.1rem 1rem 1.2rem 0; font-size: .95rem; line-height: 1.5; }}
.stApp.stApp.stApp .index td.name {{ font-family: var(--display) !important; font-size: 1.35rem; font-weight: 600; letter-spacing: -0.02em; width: 24%; line-height: 1.15; }}
.index td.what {{ width: 36%; color: var(--ink); }}
.index td.tools {{ width: 24%; color: var(--grey); }}
.index td.proof {{ width: 16%; color: var(--blue); font-size: .86rem; }}
.index tr:hover td.name {{ color: var(--blue); }}

/* Featured project (inside a band) */
.feature {{ display: grid; grid-template-columns: 1.15fr 1fr; gap: 3rem; align-items: start; }}
.feature .label {{ color: rgba(255,255,255,.8); }}
.stApp.stApp.stApp .feature h3 {{ font-family: var(--display) !important; font-size: clamp(2.2rem, 4.6vw, 3.8rem); font-weight: 700;
  line-height: .95; letter-spacing: -0.04em; margin: .6rem 0 1.2rem 0; }}
.feature p {{ font-size: 1.05rem; line-height: 1.55; color: rgba(255,255,255,.9); margin: 0 0 1.4rem 0; max-width: 54ch; }}
.feature .btn {{ border-color: #fff; }}
.feature .btn-solid {{ background: #fff; color: var(--blue) !important; }}
.feature .btn-solid:hover {{ background: var(--ink); border-color: var(--ink); color: #fff !important; }}
.feature .btn-line {{ color: #fff !important; }}
.feature .btn-line:hover {{ background: #fff; color: var(--blue) !important; }}
.review {{ background: #fff; color: var(--ink); padding: 1rem 1.1rem; margin-bottom: .7rem; display: grid; grid-template-columns: 1fr auto; gap: 1rem; align-items: start; }}
.review p {{ color: var(--ink) !important; margin: 0 !important; font-size: .95rem; line-height: 1.45; }}
.tag {{ font-size: .74rem; padding: .18rem .5rem; border: 1px solid var(--ink); white-space: nowrap; }}
.tag.neg {{ background: var(--ink); color: #fff; }}
.tag.pos {{ border-color: var(--blue); color: var(--blue); }}
.why-word {{ font-size: .84rem; color: rgba(255,255,255,.85); margin: .2rem 0 1.4rem 0; line-height: 1.5; }}
.why-word mark {{ background: rgba(255,255,255,.18); color: #fff; padding: 0 .25rem; }}
.facts {{ display: grid; grid-template-columns: repeat(4, 1fr); border-top: 1px solid rgba(255,255,255,.55); margin-top: 2.6rem; }}
.facts div {{ padding: .9rem 1rem 0 0; }}
.stApp.stApp.stApp .facts b {{ display: block; font-family: var(--display) !important; font-size: 2rem; font-weight: 700; letter-spacing: -0.03em; }}
.facts span {{ font-size: .84rem; color: rgba(255,255,255,.82); line-height: 1.35; display: block; }}

/* Project grid */
.grid {{ display: grid; grid-template-columns: 1fr 1fr; gap: 0 1.5rem; margin-top: 3rem; }}
.card {{ border-top: 1px solid {RULE}; padding: 1rem 0 2.6rem 0; }}
.card .row {{ display: flex; justify-content: space-between; gap: 1rem; }}
.stApp.stApp.stApp .card h3 {{ font-family: var(--display) !important; font-size: clamp(1.6rem, 2.6vw, 2.2rem); font-weight: 700;
  line-height: 1; letter-spacing: -0.035em; margin: 1.4rem 0 .9rem 0; max-width: 18ch; }}
.card p {{ color: var(--grey); font-size: 1rem; line-height: 1.55; margin: 0 0 1.2rem 0; max-width: 46ch; }}
.card .nums {{ display: flex; gap: 2.2rem; margin-bottom: 1.4rem; }}
.stApp.stApp.stApp .card .nums b {{ display: block; font-family: var(--display) !important; font-size: 1.9rem; font-weight: 700; letter-spacing: -0.03em; }}
.card .nums span {{ font-size: .82rem; color: var(--grey); }}

/* Dashboards */
.dash-list {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 1.5rem; margin-bottom: 2rem; }}
.dash-list div {{ border-top: 1px solid {RULE}; padding-top: .8rem; }}
.dash-list b {{ display: block; font-weight: 600; margin-bottom: .3rem; }}
.dash-list span {{ color: var(--grey); font-size: .92rem; line-height: 1.45; }}
.st-key-bi {{ border: 1px solid {RULE}; padding: 1.2rem; background: #fff; }}

/* Live demo */
.st-key-demo {{ border: 1px solid {RULE}; padding: 1.6rem 1.6rem .8rem 1.6rem; background: #fff; }}
.steps {{ display: grid; grid-template-columns: repeat(3, 1fr); border-top: 1px solid {RULE}; margin: .8rem 0 1.4rem 0; }}
.steps div {{ padding: .8rem 1rem 0 0; }}
.stApp.stApp.stApp .steps b {{ display: block; font-family: var(--display) !important; font-size: 2.4rem; font-weight: 700; letter-spacing: -0.03em; line-height: 1.05; }}
.steps span {{ font-size: .84rem; color: var(--grey); }}
.check {{ font-size: .95rem; padding: .45rem 0; border-bottom: 1px solid #DCDCD7; display: flex; gap: .7rem; }}
.check .ok {{ color: var(--blue); font-weight: 600; }}
.check .ko {{ color: #B3261E; font-weight: 600; }}
.stButton button, .stDownloadButton button {{ border-radius: 0 !important; border: 1px solid var(--ink) !important; background: transparent !important; }}
.stDownloadButton button:hover {{ background: var(--ink) !important; color: var(--paper) !important; }}
[data-testid="stExpander"] details {{ border-radius: 0 !important; border: 1px solid #CFCFCA !important; }}
div[data-baseweb="input"], div[data-baseweb="base-input"], div[data-baseweb="select"] > div {{ border-radius: 0 !important; }}
[data-testid="stSegmentedControl"] button, [data-testid="stBaseButton-segmented_control"], [data-testid="stBaseButton-segmented_controlActive"] {{ border-radius: 0 !important; }}

/* About */
.cols {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 1.5rem; }}
.cols div {{ border-top: 1px solid {RULE}; padding-top: .9rem; }}
.stApp.stApp.stApp .cols h4 {{ font-family: var(--display) !important; font-size: 1.35rem; font-weight: 600; letter-spacing: -0.02em; margin: 0 0 .6rem 0; line-height: 1.15; }}
.cols p {{ color: var(--grey); font-size: .98rem; line-height: 1.55; margin: 0; }}
.path {{ width: 100%; border-collapse: collapse; margin-top: 3rem; }}
.path tr {{ border-top: 1px solid {RULE}; }}
.path tr:last-child {{ border-bottom: 1px solid {RULE}; }}
.path td {{ padding: .8rem 1rem .8rem 0; font-size: .95rem; vertical-align: top; }}
.path td.year {{ width: 18%; color: var(--grey); }}
.path td.what {{ width: 46%; font-weight: 500; }}
.path td.where {{ color: var(--grey); }}
.path tr.now td {{ color: var(--blue); }}

/* Contact */
.contact {{ margin-top: 7rem; }}
.contact .inner {{ padding: 4rem 2rem 3rem 2rem; }}
.stApp.stApp.stApp .contact h2 {{ font-family: var(--display) !important; font-weight: 800; font-size: clamp(4rem, 13vw, 10.5rem); line-height: .86; letter-spacing: -0.055em; margin: 0 0 2.2rem -0.04em; }}
.contact .rowc {{ display: grid; grid-template-columns: 1fr 3fr; gap: 1.5rem; border-top: 1px solid rgba(255,255,255,.55); padding-top: 1rem; }}
.contact .mail {{ font-size: clamp(1.4rem, 3vw, 2.2rem); font-weight: 500; text-decoration: none; border-bottom: 2px solid #fff; color: #fff; }}
.contact .links {{ margin-top: 1.6rem; display: flex; gap: 1.8rem; flex-wrap: wrap; font-size: .95rem; }}
.contact .links a {{ color: #fff; text-decoration: none; border-bottom: 1px solid rgba(255,255,255,.5); }}
.contact .links a:hover {{ border-bottom-color: #fff; }}
.contact p {{ color: rgba(255,255,255,.85); margin: 0; font-size: .95rem; line-height: 1.5; }}
.foot {{ display: flex; justify-content: space-between; font-size: .8rem; color: rgba(255,255,255,.75); margin-top: 3.5rem; }}

@media (max-width: 860px) {{
  .block-container {{ padding: 0 1.1rem; }}
  .nav .inner {{ padding: 0 1.1rem; gap: 1rem; }} .nav .hide-sm {{ display: none; }}
  .hero .meta, .figures, .facts {{ grid-template-columns: 1fr 1fr; row-gap: 1rem; }}
  .hero .statement, .sec, .counter, .feature, .grid, .cols, .dash-list, .contact .rowc, .steps {{ grid-template-columns: 1fr; }}
  .index td.tools, .index td.proof {{ display: none; }}
  .index td.name {{ width: 40%; }}
  .band .inner {{ padding: 2.4rem 1.1rem; }}
  .stApp.stApp.stApp.stApp .hero h1 {{ font-size: 21vw; }}
}}
</style>
""")

# =============================================================================
# NAV + HERO
# =============================================================================
html(f"""
<nav class="nav"><div class="inner">
<a class="brand" href="#top"><i></i>María Carolina</a>
<a href="#capabilities">Capabilities</a>
<a href="#work">Work</a>
<a class="hide-sm" href="#dashboards">Dashboards</a>
<a class="hide-sm" href="#demo">Live demo</a>
<a class="hide-sm" href="#about">About</a>
<a class="cta" href="#contact">Contact</a>
</div></nav>
<section class="hero" id="top">
<div class="meta">
<div><span class="label">Role</span>Data Scientist<br>ML and Data Engineering</div>
<div><span class="label">Education</span>M.Sc. Data Science<br>Complutense University of Madrid</div>
<div><span class="label">Based in</span>Hermosillo, Mexico<br>Open to relocation to Germany</div>
<div><span class="label">Languages</span>Spanish, English C1<br>German B1+</div>
</div>
<h1>María<span class="second">Carolina<span class="dot">.</span></span></h1>
<div class="statement">
<div class="label">Statement</div>
<div>
<p class="lead">I turn messy data into models and pipelines that ship.</p>
<p class="sub">Data scientist with a data engineer's habits: clean inputs, honest validation and products people can actually use.</p>
<a class="btn btn-solid" href="#work">See the work<span class="arrow">→</span></a>
<a class="btn btn-line" href="#demo">Try the live pipeline</a>
</div>
</div>
</section>
<div class="band"><div class="inner">
<div class="counter" style="margin-top:0">
<p class="big">1,157,800</p>
<p>Restaurant reviews in Spanish and English, read by one model and turned into decisions for 10,056 restaurants in Madrid.</p>
</div>
<div class="figures">
<div><b>0.808</b><span>macro F1 on unseen restaurants</span></div>
<div><b>0.879</b><span>recall on negative reviews</span></div>
<div><b>0.8132</b><span>DrivenData leaderboard</span></div>
<div><b>4.0×</b><span>lift of my validated alerts</span></div>
</div>
</div></div>
""")

# =============================================================================
# CAPABILITIES
# =============================================================================
rows = "".join(
    f"<tr><td class='name'>{name}</td><td class='what'>{what}</td>"
    f"<td class='tools'>{tools}</td><td class='proof'>{proof}</td></tr>"
    for name, what, tools, proof in CAPABILITIES
)
html(f"""
<section class="sec" id="capabilities">
<div class="label">Capabilities</div>
<div>
<h2>What I bring to a data team.</h2>
<p class="intro">Six things I do well. Each one points to work you can open and check.</p>
<table class="index">{rows}</table>
</div>
</section>
""")

# =============================================================================
# WORK
# =============================================================================
html(f"""
<section class="sec" id="work">
<div class="label">Selected work</div>
<div>
<h2>Work that ships.</h2>
<p class="intro">Deployed apps, tested APIs and results measured the honest way.</p>
</div>
</section>
<div class="band"><div class="inner">
<div class="feature">
<div>
<span class="label">NLP, MLOps, live app</span>
<h3>What 1.16 million diners really think.</h3>
<p>A reputation tool for Madrid's restaurants. It diagnoses each restaurant, compares it with true peers, flags reputations that slipped and classifies any review in Spanish or English, showing the exact weight of every word.</p>
<p>Split by restaurant so the model never saw its test set. Served through a tested FastAPI service and tracked in MLflow.</p>
<a class="btn btn-solid" href="{LINKS['restaurants']}" target="_blank">Open the live app<span class="arrow">→</span></a>
<a class="btn btn-line" href="{LINKS['restaurants_repo']}" target="_blank">Code</a>
</div>
<div aria-hidden="true">
<div class="review"><p>“La paella llegó fría y el servicio fue lentísimo.”</p><span class="tag neg">Negative</span></div>
<p class="why-word">Strongest words: <mark>fría</mark> <mark>lentísimo</mark></p>
<div class="review"><p>“Best tapas we had in Madrid, the staff were lovely.”</p><span class="tag pos">Positive</span></div>
<div class="review"><p>“Correcto, sin más. Precio un poco alto.”</p><span class="tag">Neutral</span></div>
</div>
</div>
<div class="facts">
<div><b>110,912</b><span>test reviews from 996 unseen restaurants</span></div>
<div><b>0.809 / 0.793</b><span>macro F1 in Spanish / English</span></div>
<div><b>55</b><span>peer groups, 96.7% of comparable restaurants</span></div>
<div><b>28,660</b><span>backtest evaluations of the alert rule</span></div>
</div>
</div></div>
<div class="grid">
<div class="card">
<div class="row"><span class="label">Machine learning, competition</span><span class="label">2025</span></div>
<h3>Which water pumps will fail next?</h3>
<p>60,000 water points in Tanzania and three outcomes. Feature engineering, leak-free target encoding and tuned gradient boosting.</p>
<div class="nums"><div><b>0.8132</b><span>leaderboard</span></div><div><b>0.817</b><span>5-fold CV</span></div></div>
<a class="btn btn-line" href="{LINKS['pumps']}" target="_blank">View on GitHub</a>
</div>
<div class="card">
<div class="row"><span class="label">Python app, live</span><span class="label">2025</span></div>
<h3>Guess the Number, rebuilt as a product.</h3>
<p>A console game turned into a full Streamlit app: game modes, difficulty levels, scoring, saved results and a records screen with a leaderboard and charts.</p>
<div class="nums"><div><b>3</b><span>difficulty levels</span></div><div><b>6</b><span>modules</span></div></div>
<a class="btn btn-solid" href="{LINKS['guess']}" target="_blank">Play it<span class="arrow">→</span></a>
<a class="btn btn-line" href="{LINKS['guess_repo']}" target="_blank">Code</a>
</div>
<div class="card">
<div class="row"><span class="label">Data engineering</span><span class="label">2024</span></div>
<h3>A server inventory, built and checked.</h3>
<p>Hostnames generated from a naming convention, parsed into fields and validated. An improved version runs live further down this page.</p>
<div class="nums"><div><b>1,500</b><span>records</span></div><div><b>5</b><span>quality checks</span></div></div>
<a class="btn btn-line" href="#demo">Try it live</a>
<a class="btn btn-line" href="{LINKS['hostnames']}" target="_blank">Report</a>
</div>
<div class="card">
<div class="row"><span class="label">Statistics, health data</span><span class="label">2025</span></div>
<h3>Reading blood sugar the careful way.</h3>
<p>Young and adult patients compared with the right tests, plus a regression that predicts glucose 60 minutes after intake.</p>
<div class="nums"><div><b>0.634</b><span>R²</span></div><div><b>4.61</b><span>RMSE, mg/dL</span></div></div>
<a class="btn btn-line" href="{LINKS['glucose']}" target="_blank">Read the report</a>
</div>
</div>
""")

# =============================================================================
# DASHBOARDS (Tableau)
# =============================================================================
html(f"""
<section class="sec" id="dashboards">
<div class="label">Business intelligence</div>
<div>
<h2>Dashboards people act on.</h2>
<p class="intro">Easy Loans: a year of lending across Europe in two interactive Tableau dashboards. Filter by date and country, hover for details, click to cross-filter.</p>
<div class="dash-list">
<div><b>Loan operations</b><span>KPIs, deviation from the average, running total, date and country filters.</span></div>
<div><b>Merchant analysis</b><span>Top 10 merchants, merchants by country and an interactive map.</span></div>
<div><b>Built for the user</b><span>LOD and table calculations, a minimum-amount parameter and one-click resets.</span></div>
</div>
</div>
</section>
""")
live_views = {name: url for name, url in TABLEAU_DASHBOARDS.items() if url.strip()}
if live_views:
    with st.container(key="bi"):
        top_left, top_right = st.columns([3, 1], vertical_alignment="center")
        view = top_left.segmented_control("Dashboard", list(live_views), default=list(live_views)[0],
                                          label_visibility="collapsed") or list(live_views)[0]
        top_right.link_button("Tableau Public profile ↗", TABLEAU_PROFILE, width="stretch")
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
    rows_ = []
    for field, mapping in (("os", OS_MAP), ("environment", ENV_MAP), ("country", COUNTRY_MAP)):
        observed = df[field].value_counts(normalize=True)
        for label, target in mapping.values():
            rows_.append({"field": field, "category": label, "target": target,
                          "observed": float(observed.get(label, 0.0))})
    dist = pd.DataFrame(rows_)
    dist["gap_pp"] = (dist["observed"] - dist["target"]).abs() * 100
    return {"checks": checks, "duplicates": duplicates, "distribution": dist}


PLOT_FONT = dict(family="Inter, Helvetica Neue, Helvetica, Arial, sans-serif", color=INK, size=13)

html("""
<section class="sec" id="demo">
<div class="label">Live demo</div>
<div>
<h2>Don't take my word for it.</h2>
<p class="intro">This pipeline runs live. Generate a server inventory, then watch it get parsed and checked.</p>
</div>
</section>
""")

with st.container(key="demo"):
    c1, c2, c3 = st.columns(3, gap="large")
    n_hosts = c1.slider("Servers to generate", 100, 5000, 1500, step=100)
    seed = c2.number_input("Random seed", min_value=0, max_value=9999, value=42, step=1)
    c3.write("")
    unique = c3.toggle("Block duplicate hostnames", value=True,
                       help="My original notebook missed this check. Turn it off to see duplicates slip in.")

    raw = generate_hostnames(n_hosts, int(seed), unique)
    data = parse_hostnames(raw)
    report = validate(data)
    passed = sum(report["checks"].values())

    html(f"""
    <div class="steps">
    <div><span>Generate</span><b>{len(raw):,}</b><span>hostnames</span></div>
    <div><span>Parse</span><b>{data.shape[1]}</b><span>structured fields</span></div>
    <div><span>Validate</span><b>{passed}/{len(report['checks'])}</b><span>checks passed</span></div>
    </div>
    """)

    left, right = st.columns([1, 1.7], gap="large")
    with left:
        items = "".join(
            f"<div class='check'><span class='{'ok' if ok else 'ko'}'>{'✓' if ok else '✕'}</span>{name}</div>"
            for name, ok in report["checks"].items()
        )
        worst = report["distribution"]["gap_pp"].max()
        dup_note = (f"<p style='color:#B3261E;margin:.8rem 0 0 0'>{report['duplicates']} duplicate hostnames found.</p>"
                    if report["duplicates"] else "")
        html(f"{items}{dup_note}<p style='color:{GREY};margin:1rem 0'>Largest gap from the target mix: "
             f"<b style='color:{INK}'>{worst:.1f} percentage points</b>.</p>")
        st.download_button("Download the CSV ↓", data.to_csv(index=False).encode("utf-8"),
                           file_name="hosts.csv", mime="text/csv", width="stretch")
    with right:
        field = st.segmented_control(
            "Target vs observed", ["os", "environment", "country"], default="environment",
            format_func=lambda f: {"os": "OS", "environment": "Environment", "country": "Country"}[f],
        ) or "environment"
        dist = report["distribution"].query("field == @field")
        fig = go.Figure()
        fig.add_bar(x=dist["category"], y=dist["target"] * 100, name="Target", marker_color="#CFCFCA")
        fig.add_bar(x=dist["category"], y=dist["observed"] * 100, name="Observed", marker_color=BLUE)
        fig.update_traces(marker_line_width=0)
        fig.update_layout(barmode="group", height=300, margin=dict(l=0, r=0, t=10, b=0), bargap=.3,
                          yaxis=dict(title="Share of servers (%)", gridcolor="#E4E4DF", zeroline=False),
                          legend=dict(orientation="h", y=1.12, x=0), plot_bgcolor="rgba(0,0,0,0)",
                          paper_bgcolor="rgba(0,0,0,0)", font=PLOT_FONT)
        st.plotly_chart(fig, width="stretch", config={"displayModeBar": False})

    pivot = data.groupby(["country", "environment"]).size().reset_index(name="servers")
    fig2 = px.bar(pivot, x="country", y="servers", color="environment", height=300,
                  color_discrete_sequence=[BLUE, INK, "#7F97D6", "#9A9A94", "#CFCFCA"])
    fig2.update_traces(marker_line_width=0)
    fig2.update_layout(margin=dict(l=0, r=0, t=34, b=0), plot_bgcolor="rgba(0,0,0,0)",
                       paper_bgcolor="rgba(0,0,0,0)", font=PLOT_FONT, xaxis_title="", yaxis_title="Servers",
                       yaxis=dict(gridcolor="#E4E4DF"), legend_title_text="", bargap=.35,
                       title=dict(text="Servers by country and environment", font=dict(size=14)))
    st.plotly_chart(fig2, width="stretch", config={"displayModeBar": False})

    with st.expander("Peek at the parsed data"):
        st.dataframe(data.head(50), width="stretch", hide_index=True)

# =============================================================================
# ABOUT
# =============================================================================
html("""
<section class="sec" id="about">
<div class="label">About</div>
<div>
<h2>Why work with me.</h2>
<p class="intro">A data scientist who started out studying people.</p>
<div class="cols">
<div><h4>I ask the right question first.</h4><p>Anthropology trained me to interview, observe and frame a problem before touching the data, so my models answer what the business actually needs.</p></div>
<div><h4>I care about the unglamorous parts.</h4><p>Leakage checks, untouched test sets and data quality tests. They decide whether a model survives contact with real users.</p></div>
<div><h4>I'm ready for Germany.</h4><p>Spanish native, English C1 and German B1+ and improving. Open to relocation and used to working across time zones.</p></div>
</div>
<table class="path">
<tr class="now"><td class="year">2025–2026</td><td class="what">M.Sc. Data Science, Big Data &amp; Business Analytics</td><td class="where">Complutense University of Madrid</td></tr>
<tr><td class="year">2024–2025</td><td class="what">Data Science Bootcamp</td><td class="where">TripleTen</td></tr>
<tr><td class="year">2024</td><td class="what">Survey data analysis, internship</td><td class="where">Hermosillo City Hall</td></tr>
<tr><td class="year">2023</td><td class="what">Social development research, internship</td><td class="where">Ministry of Social Development of Sonora</td></tr>
<tr><td class="year">2019–2024</td><td class="what">B.A. Anthropology</td><td class="where">University of Sonora</td></tr>
</table>
</div>
</section>
""")

# =============================================================================
# CONTACT
# =============================================================================
html(f"""
<div class="band contact" id="contact"><div class="inner">
<h2>Let's talk.</h2>
<div class="rowc">
<p>Looking for Data Scientist, ML and Data Engineering roles in Germany and remote.</p>
<div>
<a class="mail" href="{LINKS['email']}">Carolinagles@gmail.com</a>
<div class="links">
<a href="{LINKS['linkedin']}" target="_blank">LinkedIn ↗</a>
<a href="{LINKS['github']}" target="_blank">GitHub ↗</a>
<a href="{TABLEAU_PROFILE}" target="_blank">Tableau Public ↗</a>
<a href="{LINKS['notion']}" target="_blank">Notion portfolio ↗</a>
</div>
</div>
</div>
<div class="foot"><span>María Carolina González Bernal</span><span>Built with Python, Streamlit and Plotly</span></div>
</div></div>
""")
