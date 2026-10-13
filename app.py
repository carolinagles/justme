"""
María Carolina · Data Science & Data Engineering portfolio (Streamlit).
Run locally:  streamlit run app.py

Design: Swiss / International Typographic Style (strict grid, large grotesk type,
hairline rules) with liquid-glass panels and a warm palette:
luminous blue, energy orange, pop pink, meadowland green and clay on paper.

Content lives in the CONTENT section. Styling lives in STYLE.
"""

import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="María Carolina · Data Scientist", page_icon="●", layout="wide")


def html(block: str) -> None:
    """Render raw HTML. Lines are left-stripped so Markdown never turns them into code blocks."""
    clean = "\n".join(line.strip() for line in block.strip().splitlines() if line.strip())
    st.markdown(clean, unsafe_allow_html=True)


# =============================================================================
# PALETTE
# =============================================================================
PAPER = "#F1ECE8"
INK = "#262626"
MUTED = "#6B625A"
BLUE = "#566F97"     # luminous blue
ORANGE = "#EA611D"   # energy orange
PINK = "#D684A8"     # pop pink
GREEN = "#88886C"    # meadowland green
CLAY = "#B97E54"     # clay
SAND = "#CFB79F"
TAUPE = "#AF9A87"
STONE = "#BEB9B6"

# =============================================================================
# CONTENT
# =============================================================================
EMAIL = "Carolinagles@gmail.com"

TABLEAU_DASHBOARDS = {
    "Loan operations": "https://public.tableau.com/views/EasyLoans_17918449786600/LOANOPERATIONS",
    "Merchant analysis": "https://public.tableau.com/views/EasyLoans-TopMerchants/MERCHANTANALYSIS",
}
TABLEAU_PROFILE = "https://public.tableau.com/app/profile/maria.carolina.gonzalez.bernal"

FIGURES = [
    (BLUE, "0.808", "Macro F1 on 996 restaurants the model never saw"),
    (ORANGE, "0.879", "Recall on negative reviews"),
    (PINK, "0.8132", "DrivenData “Pump It Up” leaderboard"),
    (GREEN, "55", "Peer groups covering 96.7% of comparable restaurants"),
    (CLAY, "4.0×", "Lift of the Critical alert in a historical backtest"),
]

# area, colour, what it involves, tools, where it shows up
CAPABILITIES = [
    ("Machine learning", BLUE,
     "Models evaluated on data they have not seen, split by group to avoid leakage.",
     "Scikit-learn, LightGBM, CatBoost, XGBoost, Optuna", "Restaurant intelligence · Pump It Up"),
    ("Natural language", ORANGE,
     "Spanish and English text classification, with each prediction explained word by word.",
     "TF-IDF, LinearSVC, Transformers, spaCy, NLTK", "Restaurant intelligence"),
    ("Data engineering", PINK,
     "Data generated, parsed, validated and exported with explicit checks.",
     "Pandas, NumPy, Pandera, Parquet, SQL", "Hostname pipeline · Restaurant intelligence"),
    ("Deployment", GREEN,
     "Models served behind a tested API and wrapped in small apps.",
     "FastAPI, MLflow, pytest, Streamlit", "Restaurant intelligence · Guess the Number"),
    ("Statistics and BI", CLAY,
     "Choosing the right test, then showing results in dashboards that are quick to read.",
     "Hypothesis testing, ANOVA, regression, Tableau, Plotly", "Glucose study · Easy Loans"),
    ("Big data and cloud", TAUPE,
     "Distributed and cloud tools studied in my M.Sc. at Complutense University of Madrid.",
     "PySpark, Spark SQL, MLlib, Google Cloud, MongoDB, Snowflake", "M.Sc. coursework"),
]

# Smaller projects shown as cards. "areas" drives the filter.
PROJECTS = [
    {"title": "Which water pumps will fail next?", "color": ORANGE,
     "kicker": "Machine learning · Competition", "areas": ["Machine learning"],
     "text": "60,000 water points in Tanzania with three possible outcomes. Feature engineering, "
             "target encoding fitted on training data only, and gradient boosting tuned with Optuna.",
     "nums": [("0.8132", "leaderboard"), ("0.817", "5-fold CV")],
     "links": [("Code", "https://github.com/carolinagles/PumpItUp/blob/main/PumpItUp.ipynb", False)]},
    {"title": "Guess the Number, rebuilt as an app", "color": PINK,
     "kicker": "Python app · Live", "areas": ["Apps"],
     "text": "A console game turned into a Streamlit app with game modes, difficulty levels, scoring, "
             "saved results and a records screen with a leaderboard and charts.",
     "nums": [("3", "difficulty levels"), ("6", "modules")],
     "links": [("Play", "https://guessthenumberrrr.streamlit.app/", True),
               ("Code", "https://github.com/carolinagles/guessthenumberrrr", False)]},
    {"title": "A server inventory, generated and checked", "color": GREEN,
     "kicker": "Data engineering", "areas": ["Data engineering"],
     "text": "Hostnames created from a naming convention, parsed into fields and validated. "
             "An improved version runs in the live demo below.",
     "nums": [("1,500", "records"), ("5", "quality checks")],
     "links": [("Try it", "#demo", True),
               ("Report", "https://app.notion.com/p/Hostnames-Generator-2b9fea9d8900807e9deadffe3bdb83ae", False)]},
    {"title": "Glucose tolerance in young and adult patients", "color": CLAY,
     "kicker": "Statistics · Health data", "areas": ["Statistics and BI"],
     "text": "Two groups compared with normality checks, t-tests and ANOVA, plus a regression "
             "that predicts glucose 60 minutes after intake.",
     "nums": [("0.634", "R²"), ("4.61", "RMSE, mg/dL")],
     "links": [("Report", "https://www.notion.so/Glucose-Levels-307fea9d89008006b054fb9422e09232", False)]},
]
FEATURED_AREAS = ["Machine learning", "Natural language", "Apps"]
RESTAURANT_APP = "https://madrid-restaurant-intelligence.streamlit.app/"
RESTAURANT_REPO = "https://github.com/carolinagles/madrid-restaurant-intelligence"

# =============================================================================
# STYLE
# =============================================================================
html(f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter+Tight:wght@500;600;700;800&family=Inter:wght@400;500;600&display=swap');
:root {{
  --paper:{PAPER}; --ink:{INK}; --muted:{MUTED};
  --blue:{BLUE}; --orange:{ORANGE}; --pink:{PINK}; --green:{GREEN}; --clay:{CLAY}; --sand:{SAND};
  --display: "Inter Tight", "Helvetica Neue", Helvetica, Arial, sans-serif;
  --text: "Inter", "Helvetica Neue", Helvetica, Arial, sans-serif;
  --glass: rgba(255,255,255,.44);
  --glass-edge: rgba(255,255,255,.82);
  --glass-shadow: 0 1px 0 rgba(255,255,255,.95) inset, 0 -1px 0 rgba(38,38,38,.04) inset, 0 16px 40px rgba(80,58,40,.10);
  --rule: rgba(38,38,38,.85);
  --hair: rgba(38,38,38,.14);
}}
html, body, .stApp, .stApp :is(h1,h2,h3,h4,p,span,div,a,b,li,label,button,input,small,td,th):not([data-testid="stIconMaterial"]):not(.material-symbols-rounded) {{
  font-family: var(--text) !important; -webkit-font-smoothing: antialiased; }}
.stApp.stApp.stApp :is(h1,h2,h3,h4,b) :is(span) {{ font-family: inherit !important; }}
[data-testid="stHeaderActionElements"] {{ display: none !important; }}
header[data-testid="stHeader"], #MainMenu, footer, [data-testid="stToolbar"], [data-testid="stDecoration"] {{ display: none !important; }}

/* Paper with soft light in the palette, so the glass has something to refract */
.stApp {{
  color: var(--ink); overflow-x: hidden;
  background:
    radial-gradient(36vw 30vw at 90% 8%, rgba(86,111,151,.16), transparent 70%),
    radial-gradient(30vw 26vw at 4% 38%, rgba(234,97,29,.08), transparent 70%),
    radial-gradient(34vw 28vw at 96% 60%, rgba(214,132,168,.12), transparent 70%),
    radial-gradient(32vw 28vw at 10% 88%, rgba(136,136,108,.13), transparent 70%),
    radial-gradient(26vw 22vw at 55% 98%, rgba(185,126,84,.12), transparent 70%),
    {PAPER};
  background-attachment: fixed;
}}
.block-container {{ max-width: 1180px; padding: 0 2rem 2rem 2rem; }}
a {{ color: inherit; }}
::selection {{ background: var(--blue); color: #fff; }}
a:focus-visible, button:focus-visible {{ outline: 2px solid var(--blue); outline-offset: 3px; }}

/* Liquid glass */
.glass, .st-key-demo, .st-key-bi, .st-key-work_filter {{
  background: var(--glass);
  backdrop-filter: blur(24px) saturate(160%); -webkit-backdrop-filter: blur(24px) saturate(160%);
  border: 1px solid var(--glass-edge); box-shadow: var(--glass-shadow); border-radius: 18px; position: relative;
}}
.glass::before {{
  content: ""; position: absolute; inset: 0; border-radius: inherit; pointer-events: none;
  background: linear-gradient(135deg, rgba(255,255,255,.6) 0%, rgba(255,255,255,0) 32%, rgba(255,255,255,0) 70%, rgba(255,255,255,.25) 100%);
}}
.glass > * {{ position: relative; }}
.glass.tinted {{
  background: linear-gradient(140deg, rgba(86,111,151,.94) 0%, rgba(86,111,151,.84) 55%, rgba(110,132,168,.80) 100%);
  border-color: rgba(255,255,255,.45); color: #fff;
  box-shadow: 0 1px 0 rgba(255,255,255,.45) inset, 0 20px 48px rgba(60,78,110,.25);
}}
.glass.tinted::before {{ background: linear-gradient(135deg, rgba(255,255,255,.28) 0%, rgba(255,255,255,0) 35%, rgba(255,255,255,0) 75%, rgba(255,255,255,.12) 100%); }}

/* Small type */
.label {{ font-size: .8rem; color: var(--muted); }}
.dot {{ display: inline-block; width: 10px; height: 10px; border-radius: 50%; vertical-align: middle; margin-right: .5rem; }}

/* Navigation */
.nav {{ position: fixed; top: 12px; left: 50%; transform: translateX(-50%); z-index: 999; width: min(1140px, calc(100vw - 24px));
  height: 52px; display: flex; align-items: center; gap: 1.8rem; padding: 0 .5rem 0 1.2rem; font-size: .88rem; border-radius: 14px; }}
.stApp .nav a {{ text-decoration: none; color: var(--ink) !important; }}
.stApp .nav a:not(.brand):not(.cta):hover {{ color: var(--blue) !important; }}
.nav .brand {{ font-weight: 600; margin-right: auto; display: flex; align-items: center; gap: .55rem; }}
.nav .brand i {{ width: 12px; height: 12px; border-radius: 50%; background: var(--orange); display: inline-block; }}
.stApp .nav a.cta {{ background: var(--ink); color: var(--paper) !important; padding: .5rem .95rem; border-radius: 10px; }}
.stApp .nav a.cta:hover {{ background: var(--blue); }}

/* Hero */
.hero {{ padding: 8rem 0 0 0; }}
.hero .meta {{ display: grid; grid-template-columns: repeat(4, 1fr); gap: 1.5rem; border-top: 1px solid var(--rule); padding-top: .8rem; }}
.hero .meta div {{ font-size: .92rem; line-height: 1.45; }}
.hero .meta .label {{ display: block; margin-bottom: .2rem; }}
.stApp.stApp.stApp .hero h1 {{ font-family: var(--display) !important; font-weight: 800; font-size: clamp(4rem, 15.5vw, 14.5rem);
  line-height: .84; letter-spacing: -0.055em; margin: 2.4rem 0 0 -0.05em; padding: 0 !important; color: var(--ink); }}
.hero h1 .second {{ display: block; }}
.hero h1 .dot2 {{ color: var(--orange); }}
.hero .statement {{ display: grid; grid-template-columns: 1fr 3fr; gap: 1.5rem; margin-top: 2.4rem; padding-top: 1rem; border-top: 1px solid var(--rule); }}
.stApp.stApp.stApp .hero p.lead {{ font-family: var(--display) !important; font-size: clamp(1.6rem, 3.2vw, 2.5rem); font-weight: 600;
  line-height: 1.1; letter-spacing: -0.03em; margin: 0; max-width: 26ch; }}
.hero p.sub {{ font-size: 1.05rem; color: var(--muted); line-height: 1.6; margin: 1rem 0 1.6rem 0; max-width: 56ch; }}

.btn {{ display: inline-block; padding: .8rem 1.2rem; font-size: .92rem; font-weight: 500; text-decoration: none !important;
  border: 1px solid var(--ink); border-radius: 10px; margin: 0 .5rem .5rem 0; transition: background .15s, color .15s, border-color .15s; }}
.btn-solid {{ background: var(--ink); color: var(--paper) !important; }}
.btn-solid:hover {{ background: var(--blue); border-color: var(--blue); color: #fff !important; }}
.btn-line {{ color: var(--ink) !important; background: rgba(255,255,255,.35); }}
.btn-line:hover {{ background: var(--ink); color: var(--paper) !important; }}

/* Key figures */
.figures {{ margin-top: 4.5rem; padding: 2rem 2rem 1.6rem 2rem; }}
.figures .top {{ display: grid; grid-template-columns: 2fr 1fr; gap: 1.5rem; align-items: end; padding-bottom: 1.6rem; }}
.stApp.stApp.stApp .figures .big {{ font-family: var(--display) !important; font-weight: 800; font-size: clamp(3.2rem, 9.5vw, 8rem);
  line-height: .85; letter-spacing: -0.05em; margin: 0; color: var(--blue); }}
.figures .top p {{ margin: 0; font-size: 1rem; line-height: 1.5; color: var(--ink); }}
.figures .row {{ display: grid; grid-template-columns: repeat(5, 1fr); border-top: 1px solid var(--rule); }}
.figures .cell {{ padding: 1rem 1rem 0 0; }}
.figures .cell i {{ display: block; width: 26px; height: 6px; border-radius: 3px; margin-bottom: .7rem; }}
.stApp.stApp.stApp .figures .cell b {{ display: block; font-family: var(--display) !important; font-size: clamp(1.7rem, 3vw, 2.4rem); font-weight: 700; letter-spacing: -0.03em; line-height: 1; }}
.figures .cell span {{ display: block; font-size: .82rem; color: var(--muted); line-height: 1.4; margin-top: .45rem; }}

/* Section scaffold: label column + content column */
.sec {{ display: grid; grid-template-columns: 1fr 3fr; gap: 1.5rem; border-top: 1px solid var(--rule); padding-top: 1rem; margin-top: 7rem; scroll-margin-top: 84px; }}
.sec .tag {{ font-size: .9rem; font-weight: 500; }}
.stApp.stApp.stApp .sec h2 {{ font-family: var(--display) !important; font-weight: 700; font-size: clamp(2.4rem, 5.2vw, 4.2rem);
  line-height: .95; letter-spacing: -0.045em; margin: 0 0 1rem 0; padding: 0 !important; }}
.sec p.intro {{ font-size: 1.08rem; color: var(--muted); line-height: 1.55; max-width: 56ch; margin: 0 0 2rem 0; }}

/* Capabilities: scannable index inside glass */
.caps {{ padding: .4rem 1.6rem; }}
.index, .path {{ border: none !important; }}
.index td, .index th, .path td {{ border-left: none !important; border-right: none !important; border-top: none !important; }}
.index {{ width: 100%; border-collapse: collapse; }}
.index tr {{ border-bottom: 1px solid var(--hair); }}
.index tr:last-child {{ border-bottom: none; }}
.index td {{ vertical-align: top; padding: 1.1rem 1rem 1.15rem 0; font-size: .94rem; line-height: 1.5; }}
.stApp.stApp.stApp .index td.name {{ font-family: var(--display) !important; font-size: 1.25rem; font-weight: 600; letter-spacing: -0.02em; width: 25%; line-height: 1.2; }}
.index td.what {{ width: 37%; }}
.index td.tools {{ width: 22%; color: var(--muted); font-size: .88rem; }}
.index td.proof {{ width: 16%; font-size: .82rem; color: var(--muted); }}

/* Featured project */
.feature {{ padding: 2.4rem; }}
.feature .grid2 {{ display: grid; grid-template-columns: 1.15fr 1fr; gap: 2.6rem; align-items: start; }}
.feature .label {{ color: rgba(255,255,255,.82); }}
.stApp.stApp.stApp .feature h3 {{ font-family: var(--display) !important; font-size: clamp(2.1rem, 4.2vw, 3.4rem); font-weight: 700;
  line-height: .98; letter-spacing: -0.04em; margin: .7rem 0 1.1rem 0; padding: 0 !important; }}
.feature p {{ font-size: 1.02rem; line-height: 1.6; color: rgba(255,255,255,.92); margin: 0 0 1.1rem 0; max-width: 54ch; }}
.feature .btn {{ border-color: rgba(255,255,255,.9); }}
.feature .btn-solid {{ background: #fff; color: var(--blue) !important; }}
.feature .btn-solid:hover {{ background: var(--ink); border-color: var(--ink); color: #fff !important; }}
.feature .btn-line {{ color: #fff !important; background: rgba(255,255,255,.1); }}
.feature .btn-line:hover {{ background: #fff; color: var(--blue) !important; }}
.review {{ background: rgba(255,255,255,.88); color: var(--ink); border-radius: 12px; padding: .9rem 1rem; margin-bottom: .65rem;
  display: grid; grid-template-columns: 1fr auto; gap: .8rem; align-items: start; box-shadow: 0 6px 18px rgba(30,40,70,.12); }}
.feature .review p {{ color: var(--ink) !important; margin: 0 !important; font-size: .95rem; line-height: 1.45; }}
.pill {{ font-size: .72rem; font-weight: 600; padding: .22rem .55rem; border-radius: 999px; color: #fff; white-space: nowrap; }}
.pill.neg {{ background: var(--orange); }} .pill.pos {{ background: var(--green); }} .pill.neu {{ background: {TAUPE}; }}
.words {{ font-size: .84rem; color: rgba(255,255,255,.88); margin: .1rem 0 .9rem .2rem; }}
.words mark {{ background: rgba(255,255,255,.2); color: #fff; padding: 0 .3rem; border-radius: 4px; }}
.facts {{ display: grid; grid-template-columns: repeat(4, 1fr); border-top: 1px solid rgba(255,255,255,.5); margin-top: 2.2rem; }}
.facts div {{ padding: .9rem 1rem 0 0; }}
.stApp.stApp.stApp .facts b {{ display: block; font-family: var(--display) !important; font-size: 1.9rem; font-weight: 700; letter-spacing: -0.03em; }}
.facts span {{ font-size: .82rem; color: rgba(255,255,255,.85); line-height: 1.4; display: block; margin-top: .25rem; }}

/* Filter */
.st-key-work_filter {{ padding: .55rem .7rem; margin: 1.6rem 0 1.2rem 0; border-radius: 14px; }}
.st-key-work_filter [data-testid="stMarkdownContainer"] p {{ margin: 0; }}

/* Project cards */
.cards {{ display: grid; grid-template-columns: 1fr 1fr; gap: 1.2rem; }}
.card {{ padding: 1.6rem 1.7rem 1.3rem 1.7rem; display: flex; flex-direction: column; }}
.card .bar {{ height: 5px; width: 44px; border-radius: 3px; margin-bottom: 1rem; }}
.stApp.stApp.stApp .card h3 {{ font-family: var(--display) !important; font-size: clamp(1.5rem, 2.3vw, 1.95rem); font-weight: 700;
  line-height: 1.05; letter-spacing: -0.03em; margin: .5rem 0 .8rem 0; padding: 0 !important; }}
.card p {{ color: var(--muted); font-size: .98rem; line-height: 1.55; margin: 0 0 1.2rem 0; }}
.card .nums {{ display: flex; gap: 2rem; margin: auto 0 1.2rem 0; border-top: 1px solid var(--hair); padding-top: .9rem; }}
.stApp.stApp.stApp .card .nums b {{ display: block; font-family: var(--display) !important; font-size: 1.7rem; font-weight: 700; letter-spacing: -0.03em; }}
.card .nums span {{ font-size: .8rem; color: var(--muted); }}
.empty {{ padding: 1.4rem 1.6rem; color: var(--muted); }}

/* Dashboards */
.dash-list {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 1.5rem; margin-bottom: 1.6rem; }}
.dash-list div {{ border-top: 1px solid var(--rule); padding-top: .8rem; }}
.dash-list b {{ display: block; font-weight: 600; margin-bottom: .3rem; }}
.dash-list span {{ color: var(--muted); font-size: .92rem; line-height: 1.5; }}
.st-key-bi {{ padding: 1.1rem; }}
.st-key-bi iframe {{ border-radius: 12px; }}

/* Live demo */
.st-key-demo {{ padding: 1.7rem 1.7rem .9rem 1.7rem; }}
.steps {{ display: grid; grid-template-columns: repeat(3, 1fr); border-top: 1px solid var(--rule); margin: .8rem 0 1.4rem 0; }}
.steps div {{ padding: .85rem 1rem 0 0; }}
.steps i {{ display: block; width: 22px; height: 5px; border-radius: 3px; margin-bottom: .55rem; }}
.stApp.stApp.stApp .steps b {{ display: block; font-family: var(--display) !important; font-size: 2.3rem; font-weight: 700; letter-spacing: -0.03em; line-height: 1.05; }}
.steps span {{ font-size: .84rem; color: var(--muted); }}
.check {{ font-size: .95rem; padding: .45rem 0; border-bottom: 1px solid var(--hair); display: flex; gap: .7rem; }}
.check .ok {{ color: var(--green); font-weight: 700; }}
.check .ko {{ color: var(--orange); font-weight: 700; }}
.stButton button, .stDownloadButton button, .stLinkButton a {{ border-radius: 10px !important; border: 1px solid var(--ink) !important; background: rgba(255,255,255,.4) !important; }}
.stDownloadButton button:hover {{ background: var(--ink) !important; color: var(--paper) !important; }}
[data-testid="stExpander"] details {{ border-radius: 12px !important; background: rgba(255,255,255,.4); border: 1px solid rgba(255,255,255,.85) !important; }}
div[data-baseweb="input"], div[data-baseweb="base-input"] {{ background: rgba(255,255,255,.6) !important; }}

/* About */
.cols {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 1.5rem; }}
.cols div {{ border-top: 1px solid var(--rule); padding-top: .9rem; }}
.stApp.stApp.stApp .cols h4 {{ font-family: var(--display) !important; font-size: 1.3rem; font-weight: 600; letter-spacing: -0.02em; margin: 0 0 .55rem 0; padding: 0 !important; }}
.cols p {{ color: var(--muted); font-size: .97rem; line-height: 1.55; margin: 0; }}
.timeline {{ margin-top: 2.6rem; padding: .3rem 1.6rem; }}
.path {{ width: 100%; border-collapse: collapse; }}
.path tr {{ border-bottom: 1px solid var(--hair); }}
.path tr:last-child {{ border-bottom: none; }}
.path td {{ padding: .85rem 1rem .85rem 0; font-size: .95rem; vertical-align: top; }}
.path td.year {{ width: 18%; color: var(--muted); }}
.path td.what {{ width: 46%; font-weight: 500; }}
.path td.where {{ color: var(--muted); }}
.path tr.now td.year {{ color: var(--blue); font-weight: 600; }}

/* Contact */
.contact {{ margin-top: 7rem; padding: 3.2rem 2.4rem 2rem 2.4rem; scroll-margin-top: 84px; }}
.stApp.stApp.stApp .contact h2 {{ font-family: var(--display) !important; font-weight: 800; font-size: clamp(3.6rem, 11vw, 9rem); line-height: .86;
  letter-spacing: -0.055em; margin: 0 0 2rem -0.04em; padding: 0 !important; color: #fff; }}
.contact .rowc {{ display: grid; grid-template-columns: 1fr 3fr; gap: 1.5rem; border-top: 1px solid rgba(255,255,255,.5); padding-top: 1rem; }}
.contact p {{ color: rgba(255,255,255,.88); margin: 0; font-size: .98rem; line-height: 1.5; }}
.stApp .contact .mail {{ font-family: var(--display) !important; font-size: clamp(1.4rem, 3vw, 2.2rem); font-weight: 600; text-decoration: none; color: #fff !important; border-bottom: 2px solid rgba(255,255,255,.8); }}
.foot {{ display: flex; justify-content: space-between; font-size: .8rem; color: var(--muted); margin: 1.4rem .2rem 0 .2rem; }}

@media (max-width: 860px) {{
  .block-container {{ padding: 0 1rem 2rem 1rem; }}
  .nav {{ gap: 1rem; padding: 0 .4rem 0 .9rem; font-size: .8rem; }} .nav .hide-sm {{ display: none; }}
  .hero .meta {{ grid-template-columns: 1fr 1fr; row-gap: 1rem; }}
  .stApp.stApp.stApp.stApp .hero h1 {{ font-size: 20vw; }}
  .hero .statement, .sec, .figures .top, .feature .grid2, .cards, .cols, .dash-list, .contact .rowc, .steps {{ grid-template-columns: 1fr; }}
  .figures .row {{ grid-template-columns: 1fr 1fr; }}
  .facts {{ grid-template-columns: 1fr 1fr; }}
  .index td.tools, .index td.proof {{ display: none; }}
  .index td.name {{ width: 40%; }}
  .feature, .figures, .contact {{ padding: 1.6rem 1.3rem; }}
  .foot {{ flex-direction: column; gap: .3rem; }}
}}
</style>
""")

# =============================================================================
# NAV + HERO + KEY FIGURES
# =============================================================================
figure_cells = "".join(
    f"<div class='cell'><i style='background:{c}'></i><b>{num}</b><span>{text}</span></div>"
    for c, num, text in FIGURES
)
html(f"""
<nav class="nav glass">
<a class="brand" href="#top"><i></i>María Carolina</a>
<a href="#work">Work</a>
<a href="#capabilities">Capabilities</a>
<a class="hide-sm" href="#dashboards">Dashboards</a>
<a class="hide-sm" href="#demo">Live demo</a>
<a class="hide-sm" href="#about">About</a>
<a class="cta" href="#contact">Contact</a>
</nav>
<section class="hero" id="top">
<div class="meta">
<div><span class="label">Role</span>Data Scientist<br>ML and Data Engineering</div>
<div><span class="label">Education</span>M.Sc. Data Science<br>Complutense University of Madrid</div>
<div><span class="label">Location</span>Hermosillo, Mexico<br>Open to relocation</div>
<div><span class="label">Languages</span>Spanish, English C1<br>German B1+</div>
</div>
<h1>María<span class="second">Carolina<span class="dot2">.</span></span></h1>
<div class="statement">
<div class="label">About this page</div>
<div>
<p class="lead">I like turning messy data into tools that people can use.</p>
<p class="sub">This page collects my projects in machine learning, natural language processing, data pipelines, statistics and dashboards. Each one links to the code, a live app or a report.</p>
<a class="btn btn-solid" href="#work">See the projects</a>
<a class="btn btn-line" href="#demo">Try the live demo</a>
</div>
</div>
</section>
<div class="figures glass">
<div class="top">
<p class="big">1,157,800</p>
<p>Spanish and English restaurant reviews from Madrid, cleaned and classified in my main project, covering 10,056 restaurants.</p>
</div>
<div class="row">{figure_cells}</div>
</div>
""")

# =============================================================================
# WORK
# =============================================================================
html(f"""
<section class="sec" id="work">
<div class="tag">Selected work</div>
<div>
<h2>Projects.</h2>
<p class="intro">Live apps, code and reports. Model results are measured on data the models had not seen.</p>
</div>
</section>
<article class="feature glass tinted">
<div class="grid2">
<div>
<span class="label">Main project · NLP, machine learning and deployment</span>
<h3>What 1.16 million diners say about Madrid's restaurants</h3>
<p>A reputation tool for 10,056 restaurants. It summarises each restaurant, compares it with similar places, flags reputations that declined and classifies any review in Spanish or English, showing how much each word weighed in the decision.</p>
<p>The data were split by restaurant, so the final test used places the model had never seen. The model is served through a FastAPI service with tests and tracked in MLflow.</p>
<a class="btn btn-solid" href="{RESTAURANT_APP}" target="_blank">Open the app ↗</a>
<a class="btn btn-line" href="{RESTAURANT_REPO}" target="_blank">Code</a>
</div>
<div aria-hidden="true">
<div class="review"><p>“La paella llegó fría y el servicio fue lentísimo.”</p><span class="pill neg">Negative</span></div>
<p class="words">Words that weighed most: <mark>fría</mark> <mark>lentísimo</mark></p>
<div class="review"><p>“Best tapas we had in Madrid, the staff were lovely.”</p><span class="pill pos">Positive</span></div>
<div class="review"><p>“Correcto, sin más. Precio un poco alto.”</p><span class="pill neu">Neutral</span></div>
</div>
</div>
<div class="facts">
<div><b>110,912</b><span>test reviews from 996 unseen restaurants</span></div>
<div><b>0.809 / 0.793</b><span>macro F1 in Spanish and English</span></div>
<div><b>0.905</b><span>accuracy on the test set</span></div>
<div><b>28,660</b><span>backtest evaluations of the alert rule</span></div>
</div>
</article>
""")

with st.container(key="work_filter"):
    area = st.segmented_control(
        "Filter projects", ["All", "Machine learning", "Data engineering", "Statistics and BI", "Apps"],
        default="All", label_visibility="collapsed",
    ) or "All"


def project_card(p: dict) -> str:
    nums = "".join(f"<div><b style='color:{p['color']}'>{n}</b><span>{l}</span></div>" for n, l in p["nums"])
    buttons = ""
    for label, url, primary in p["links"]:
        style = "btn-solid" if primary else "btn-line"
        target = "" if url.startswith("#") else ' target="_blank"'
        buttons += f"<a class='btn {style}' href='{url}'{target}>{label}</a>"
    return (f"<article class='card glass'><div class='bar' style='background:{p['color']}'></div>"
            f"<span class='label'>{p['kicker']}</span><h3>{p['title']}</h3><p>{p['text']}</p>"
            f"<div class='nums'>{nums}</div><div>{buttons}</div></article>")


shown = [p for p in PROJECTS if area == "All" or area in p["areas"]]
if shown:
    html(f"<div class='cards'>{''.join(project_card(p) for p in shown)}</div>")
else:
    html("<div class='empty glass'>The main project above covers this area.</div>")

# =============================================================================
# CAPABILITIES
# =============================================================================
rows = "".join(
    f"<tr><td class='name'><span class='dot' style='background:{c}'></span>{name}</td><td class='what'>{what}</td>"
    f"<td class='tools'>{tools}</td><td class='proof'>{proof}</td></tr>"
    for name, c, what, tools, proof in CAPABILITIES
)
html(f"""
<section class="sec" id="capabilities">
<div class="tag">Capabilities</div>
<div>
<h2>Areas I work in.</h2>
<p class="intro">What each area involves, the tools I use and the project where you can see it.</p>
<div class="caps glass"><table class="index">{rows}</table></div>
</div>
</section>
""")

# =============================================================================
# DASHBOARDS (Tableau)
# =============================================================================
html(f"""
<section class="sec" id="dashboards">
<div class="tag">Business intelligence</div>
<div>
<h2>Dashboards.</h2>
<p class="intro">Easy Loans: a year of lending across Europe in two interactive Tableau dashboards. Filter by date and country, hover for details and click to cross-filter.</p>
<div class="dash-list">
<div><b><span class="dot" style="background:{BLUE}"></span>Loan operations</b><span>KPIs, deviation from the average, running total, date and country filters.</span></div>
<div><b><span class="dot" style="background:{ORANGE}"></span>Merchant analysis</b><span>Top 10 merchants, merchants by country and an interactive map.</span></div>
<div><b><span class="dot" style="background:{GREEN}"></span>Details</b><span>LOD and table calculations, a minimum-amount parameter and reset buttons.</span></div>
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
<div class="tag">Live demo</div>
<div>
<h2>A small pipeline you can try.</h2>
<p class="intro">Generate a server inventory, then see it parsed into fields and checked for quality.</p>
</div>
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
    <div><i style="background:{BLUE}"></i><span>1 · Generate</span><b>{len(raw):,}</b><span>hostnames</span></div>
    <div><i style="background:{CLAY}"></i><span>2 · Parse</span><b>{data.shape[1]}</b><span>structured fields</span></div>
    <div><i style="background:{GREEN}"></i><span>3 · Validate</span><b>{passed}/{len(report['checks'])}</b><span>checks passed</span></div>
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
html("""
<section class="sec" id="about">
<div class="tag">About</div>
<div>
<h2>About me.</h2>
<p class="intro">How I like to work, and the path that brought me here.</p>
<div class="cols">
<div><h4>Questions first</h4><p>Anthropology taught me to interview, observe and define the problem before choosing a method.</p></div>
<div><h4>Careful validation</h4><p>Separate test data, leakage checks and quality tests, to understand what a model can and cannot do.</p></div>
<div><h4>Languages</h4><p>Spanish (native), English (C1) and German (B1+), which I keep studying.</p></div>
</div>
<div class="timeline glass">
<table class="path">
<tr class="now"><td class="year">2025–2026</td><td class="what">M.Sc. Data Science, Big Data &amp; Business Analytics</td><td class="where">Complutense University of Madrid</td></tr>
<tr><td class="year">2024–2025</td><td class="what">Data Science Bootcamp</td><td class="where">TripleTen</td></tr>
<tr><td class="year">2024</td><td class="what">Survey data analysis, internship</td><td class="where">Hermosillo City Hall</td></tr>
<tr><td class="year">2023</td><td class="what">Social development research, internship</td><td class="where">Ministry of Social Development of Sonora</td></tr>
<tr><td class="year">2019–2024</td><td class="what">B.A. Anthropology</td><td class="where">University of Sonora</td></tr>
</table>
</div>
</div>
</section>
""")

# =============================================================================
# CONTACT + FOOTER
# =============================================================================
html(f"""
<section class="contact glass tinted" id="contact">
<h2>Let's talk.</h2>
<div class="rowc">
<p>Open to Data Scientist, ML and Data Engineering roles. I would be glad to hear from you.</p>
<div><a class="mail" href="mailto:{EMAIL}">{EMAIL}</a></div>
</div>
</section>
<div class="foot"><span>María Carolina González Bernal</span><span>Built with Python, Streamlit and Plotly</span></div>
""")
