"""
María Carolina - Data Science & Data Engineering portfolio (Streamlit).
Run locally:  streamlit run app.py

Content lives in the CONTENT section below. Styling lives in CSS.
"""

import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="María Carolina | Data Scientist", page_icon="✦", layout="wide")


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
    "pumps": "https://github.com/carolinagles/PumpItUp/blob/main/PumpItUp.ipynb",
    "hostnames": "https://app.notion.com/p/Hostnames-Generator-2b9fea9d8900807e9deadffe3bdb83ae",
    "glucose": "https://www.notion.so/Glucose-Levels-307fea9d89008006b054fb9422e09232",
}

ICON = {
    "ml": '<path d="M4 19V9M10 19V5M16 19v-7M22 19H2"/>',
    "nlp": '<path d="M4 5h16v10H9l-5 4z"/><path d="M8 9h8M8 12h5"/>',
    "pipe": '<circle cx="5" cy="6" r="2"/><circle cx="19" cy="18" r="2"/><path d="M7 6h6a4 4 0 0 1 4 4v6"/><path d="M5 8v10h10"/>',
    "ship": '<path d="M12 3l8 4.5v9L12 21l-8-4.5v-9z"/><path d="M12 12l8-4.5M12 12v9M12 12L4 7.5"/>',
    "stats": '<path d="M3 20h18"/><path d="M5 20c2-8 4-12 7-12s5 4 7 12"/><path d="M12 8v12" stroke-dasharray="2 2"/>',
    "cloud": '<path d="M7 18h10a4 4 0 0 0 .5-7.97A6 6 0 0 0 6 11a3.5 3.5 0 0 0 1 7z"/>',
}

# Tableau Public: publish the workbook, then paste each dashboard's share link here.
# Example: "https://public.tableau.com/views/EasyLoans2023/LOANOPERATIONS"
# While a link is empty, the app shows the project tile without the embedded dashboard.
TABLEAU_DASHBOARDS = {
    "Loan operations": "",
    "Merchant analysis": "",
}
TABLEAU_PROFILE = ""  # e.g. "https://public.tableau.com/app/profile/your.name"

CAPABILITIES = [
    ("ml", "Machine learning that holds up",
     "Models judged on data they have never seen. Gradient boosting, careful validation, tuned with Optuna.",
     "Scikit-learn · LightGBM · CatBoost · XGBoost · Optuna", "Pump It Up · Restaurant NLP"),
    ("nlp", "Language, understood",
     "Text classification in Spanish and English, from TF-IDF baselines to Transformers.",
     "TF-IDF · Transformers · spaCy · NLTK · LIME", "Restaurant NLP"),
    ("pipe", "Pipelines you can trust",
     "Data that is generated, parsed, validated and exported without silent errors.",
     "Pandas · NumPy · Pandera · Parquet · SQL", "Hostname pipeline · Restaurant NLP"),
    ("ship", "From notebook to product",
     "Models served behind an API, tested, versioned and wrapped in a dashboard.",
     "FastAPI · MLflow · pytest · Streamlit", "Restaurant NLP"),
    ("stats", "Statistics people can read",
     "The right test for the question, then a dashboard a manager understands in seconds.",
     "Hypothesis testing · ANOVA · Regression · Tableau · Plotly", "Glucose study · Easy Loans dashboards"),
    ("cloud", "Ready for scale",
     "Trained on distributed and cloud tools during my M.Sc. at Complutense University of Madrid.",
     "PySpark · Spark SQL · MLlib · Google Cloud · MongoDB · Snowflake", "M.Sc. coursework"),
]

# =============================================================================
# STYLE
# =============================================================================
BLUE = "#7C74E8"   # soft violet accent
INK = "#1F2347"
SUB = "#5E6388"
LINE = "#D5DAF5"
SOFT = "#F1F3FD"

html(f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;0,700;1,500;1,600&family=Inter:wght@400;500;600;700&display=swap');
:root {{
  --ink:{INK}; --sub:{SUB}; --violet:{BLUE}; --line:{LINE}; --soft:{SOFT};
  --plum:#2E3270; --sky:#8FB4F5; --lilac:#B9A9F5; --pearl:#F8F9FF;
  --glass: rgba(255,255,255,.42); --glass-strong: rgba(255,255,255,.62);
  --edge: rgba(255,255,255,.75);
  --shadow: 0 1px 0 rgba(255,255,255,.9) inset, 0 -1px 0 rgba(110,120,210,.08) inset, 0 12px 40px rgba(46,50,112,.10);
  --serif: "Cormorant Garamond", "Iowan Old Style", "Palatino Linotype", Georgia, serif;
}}
html, body, .stApp, .stApp :is(h1,h2,h3,h4,h5,p,span,div,a,b,li,label,button,input,small,textarea):not([data-testid="stIconMaterial"]):not(.material-symbols-rounded) {{
  font-family: -apple-system, BlinkMacSystemFont, "SF Pro Text", "Inter", "Helvetica Neue", Arial, sans-serif !important;
  -webkit-font-smoothing: antialiased;
}}
.stApp.stApp.stApp.stApp :is(h1,h2,h3,h4,b,em) :is(span,em) {{ font-family: inherit !important; }}
/* Soft lavender and periwinkle light, so the glass has something to refract */
.stApp {{
  background:
    radial-gradient(42vw 42vw at 8% 4%, rgba(190,178,255,.55), transparent 60%),
    radial-gradient(40vw 40vw at 94% 12%, rgba(158,196,255,.60), transparent 60%),
    radial-gradient(46vw 46vw at 72% 68%, rgba(205,194,255,.45), transparent 62%),
    radial-gradient(38vw 38vw at 10% 84%, rgba(170,206,255,.45), transparent 60%),
    linear-gradient(180deg, #F5F4FF 0%, #EEF3FF 50%, #F3F1FD 100%);
  background-attachment: fixed;
}}
header[data-testid="stHeader"], #MainMenu, footer, [data-testid="stToolbar"], [data-testid="stDecoration"] {{ display: none !important; }}
.block-container {{ max-width: 1080px; padding: 0 1.4rem 4rem 1.4rem; }}

/* Liquid glass recipe */
.glass, .tile, .feature.light, .st-key-demo, .st-key-bi, .scoreboard, .nav {{
  background: var(--glass);
  backdrop-filter: blur(26px) saturate(170%); -webkit-backdrop-filter: blur(26px) saturate(170%);
  border: 1px solid var(--edge); box-shadow: var(--shadow); position: relative;
}}
.tile::before, .feature.light::before {{
  content: ""; position: absolute; inset: 0; border-radius: inherit; pointer-events: none;
  background: linear-gradient(135deg, rgba(255,255,255,.65) 0%, rgba(255,255,255,0) 38%, rgba(255,255,255,0) 70%, rgba(255,255,255,.25) 100%);
  mix-blend-mode: soft-light;
}}

/* Navigation */
.nav {{
  position: fixed; top: 12px; left: 50%; transform: translateX(-50%); z-index: 999; height: 48px;
  display: flex; align-items: center; gap: 1.9rem; padding: 0 .6rem 0 1.4rem; border-radius: 980px;
  font-size: .84rem; width: max-content; max-width: calc(100vw - 24px);
}}
.nav a {{ color: var(--ink); text-decoration: none; opacity: .78; }}
.nav a:hover {{ opacity: 1; }} .stApp.stApp.stApp .nav .brand {{ font-family: var(--serif) !important; font-size: 1.15rem; font-weight: 700; opacity: 1; margin-right: .4rem; color: var(--plum); }}
.nav .cta {{ background: var(--plum); color: #fff; opacity: 1; padding: .42rem 1rem; border-radius: 980px; }}

/* Hero with faint court lines */
.hero {{ position: relative; text-align: center; padding: 8.8rem 0 3rem 0; }}
.hero .court {{ position: absolute; inset: 4.5rem 0 0 0; width: 100%; height: 100%; opacity: .55; pointer-events: none; z-index: 0; }}
.hero > *:not(.court) {{ position: relative; z-index: 1; }} .stApp.stApp.stApp .hero .hello {{ font-family: var(--serif) !important; font-style: italic; font-size: 1.6rem; color: var(--sub); margin: 0 0 .2rem 0; }} .stApp.stApp.stApp .hero h1 {{
  font-family: var(--serif) !important; font-weight: 600; font-size: clamp(3.6rem, 10vw, 7.2rem);
  line-height: .98; letter-spacing: -0.02em; margin: 0; color: var(--plum);
  animation: rise 1s cubic-bezier(.2,.7,.2,1) both;
}}
.hero h1 em {{ font-style: italic; color: var(--violet); }}
.hero .tagline {{ font-size: clamp(1.35rem, 3vw, 2rem); font-weight: 600; letter-spacing: -0.02em; color: var(--ink); margin: 1.3rem auto .8rem auto; max-width: 30ch; line-height: 1.2; }}
.hero .lede {{ font-size: 1.12rem; color: var(--sub); max-width: 52ch; margin: 0 auto 2rem auto; line-height: 1.6; }}
@keyframes rise {{ from {{ opacity: 0; transform: translateY(16px); }} to {{ opacity: 1; transform: none; }} }}
@media (prefers-reduced-motion: reduce) {{ .hero h1 {{ animation: none; }} }}

.btn {{ display: inline-block; padding: .78rem 1.4rem; border-radius: 980px; font-size: 1rem; font-weight: 500; text-decoration: none !important; margin: .25rem .3rem; transition: background .25s, color .25s, box-shadow .25s; }}
.btn-primary {{ background: var(--plum); color: #fff !important; box-shadow: 0 6px 20px rgba(46,50,112,.28); }}
.btn-primary:hover {{ background: #3B4090; }}
.btn-ghost {{ color: var(--plum) !important; background: rgba(255,255,255,.45); border: 1px solid rgba(255,255,255,.85); backdrop-filter: blur(14px); box-shadow: var(--shadow); }}
.btn-ghost:hover {{ background: rgba(255,255,255,.75); }}
.btn:focus-visible, .nav a:focus-visible {{ outline: 3px solid rgba(124,116,232,.45); outline-offset: 2px; }}

/* Scoreboard: a centre-court results board in frosted glass */
.scoreboard {{
  display: grid; grid-template-columns: repeat(4, 1fr); margin: 1.4rem 0 5.5rem 0; border-radius: 26px; overflow: hidden;
}}
.scoreboard .cell {{ text-align: center; padding: 1.6rem .6rem 1.4rem .6rem; border-right: 1px solid rgba(46,50,112,.10); }}
.scoreboard .cell:last-child {{ border-right: none; }} .stApp.stApp.stApp .scoreboard b {{ display: block; font-family: var(--serif) !important; font-weight: 600; font-size: clamp(2.2rem, 4.6vw, 3.2rem); color: var(--plum); letter-spacing: -0.01em; line-height: 1.1; }}
.scoreboard span {{ color: var(--sub); font-size: .9rem; }}

/* Section headings */
.section {{ text-align: center; margin: 0 auto 2.4rem auto; max-width: 720px; scroll-margin-top: 80px; }} .stApp.stApp.stApp .section h2 {{ font-family: var(--serif) !important; font-weight: 600; font-size: clamp(2.5rem, 5.6vw, 3.9rem); letter-spacing: -0.015em; line-height: 1.02; margin: 0 0 .7rem 0; color: var(--plum); }}
.section p {{ font-size: 1.15rem; color: var(--sub); line-height: 1.55; margin: 0; }}

/* Capability tiles */
.bento {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 1.1rem; margin-bottom: 6rem; }}
.tile {{ border-radius: 28px; padding: 1.8rem 1.6rem; }}
.tile .icon {{ width: 46px; height: 46px; border-radius: 15px; display: grid; place-items: center; color: var(--plum);
  background: rgba(255,255,255,.7); border: 1px solid rgba(255,255,255,.9); box-shadow: 0 4px 14px rgba(46,50,112,.12); }}
.tile .icon svg {{ width: 24px; height: 24px; }}
.tile h3 {{ font-size: 1.22rem; font-weight: 650; letter-spacing: -0.015em; margin: .8rem 0 .45rem 0; color: var(--ink); }}
.tile p {{ color: var(--sub); line-height: 1.55; margin: 0 0 1rem 0; font-size: .97rem; }}
.tile .tools {{ font-size: .85rem; color: var(--ink); line-height: 1.55; }}
.tile .proof {{ font-size: .82rem; color: var(--violet); margin-top: .7rem; font-weight: 500; }}
.tile .proof::before {{ content: ""; display: inline-block; width: 7px; height: 7px; border-radius: 50%; background: linear-gradient(135deg, var(--sky), var(--lilac)); margin-right: .45rem; vertical-align: middle; }}

/* Feature tiles */
.feature {{ border-radius: 32px; padding: 3rem 2.6rem; margin-bottom: 1.1rem; overflow: hidden; scroll-margin-top: 80px; position: relative; }}
.feature.dark {{
  background: radial-gradient(110% 130% at 92% 0%, #9AA8FF 0%, #5C64CF 38%, #33378A 72%, #24275C 100%); color: #F8F9FF;
  border: 1px solid rgba(255,255,255,.35); box-shadow: 0 1px 0 rgba(255,255,255,.35) inset, 0 24px 60px rgba(46,50,112,.30);
}}
.feature .kicker {{ font-size: .95rem; font-weight: 600; color: #D9DEFF; margin: 0 0 .6rem 0; }}
.feature.light .kicker {{ color: var(--violet); }} .stApp.stApp.stApp .feature h3 {{ font-family: var(--serif) !important; font-weight: 600; font-size: clamp(2.2rem, 4.6vw, 3.2rem); letter-spacing: -0.01em; line-height: 1.02; margin: 0 0 1rem 0; max-width: 18ch; }}
.feature.light h3 {{ color: var(--plum); }}
.feature .desc {{ font-size: 1.1rem; line-height: 1.6; max-width: 56ch; margin: 0 0 2rem 0; opacity: .85; }}
.feature.light .desc {{ color: var(--sub); opacity: 1; }}
.feature.dark .metrics {{ gap: 1.5rem; }}
.stApp.stApp.stApp.stApp .feature.dark .metrics div b {{ font-size: 2.15rem; }}
.split {{ display: grid; grid-template-columns: 1.25fr 1fr; gap: 2.4rem; align-items: center; }}
.mock {{ display: flex; flex-direction: column; gap: .8rem; }}
.review {{ background: rgba(255,255,255,.12); border: 1px solid rgba(255,255,255,.28); backdrop-filter: blur(16px); border-radius: 20px; padding: 1rem 1.1rem; box-shadow: 0 1px 0 rgba(255,255,255,.3) inset; }}
.review p {{ margin: 0 0 .6rem 0; font-size: .98rem; line-height: 1.45; color: #F7F5FF; }}
.tag {{ font-size: .78rem; font-weight: 600; padding: .2rem .65rem; border-radius: 980px; }}
.tag.neg {{ background: rgba(255,170,190,.22); color: #FFD0DA; }}
.tag.pos {{ background: rgba(170,210,255,.24); color: #D6E8FF; }}
.tag.neu {{ background: rgba(215,200,255,.24); color: #E6DDFF; }}
.alert {{ font-size: .88rem; color: #E6DDFF; padding: .2rem; font-style: italic; }}
.metrics {{ display: flex; flex-wrap: wrap; gap: 2.4rem; margin-bottom: 2rem; }} .stApp.stApp.stApp .metrics div b {{ display: block; font-family: var(--serif) !important; font-size: 2.5rem; font-weight: 600; line-height: 1.05; }}
.metrics div span {{ font-size: .88rem; opacity: .75; }}
.feature.light .metrics b {{ color: var(--plum); }}
.feature.light .metrics span {{ color: var(--sub); opacity: 1; }}
.trio {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 1.1rem; margin-bottom: 6rem; }}
.trio .feature {{ margin-bottom: 0; padding: 2.3rem 1.9rem; }}
.stApp.stApp.stApp.stApp .trio .feature h3 {{ font-size: clamp(1.55rem, 2.2vw, 1.85rem); }}
.trio .feature .desc {{ font-size: .98rem; }}
.trio .metrics {{ gap: 1.6rem; }}
.trio .metrics b {{ font-size: 2.1rem !important; }}

/* Dashboards */
.bi {{ margin-bottom: 1.1rem; }}
.bi-list {{ display: flex; flex-direction: column; gap: .8rem; }}
.bi-list div {{ background: rgba(255,255,255,.55); border: 1px solid rgba(255,255,255,.85); border-radius: 20px; padding: 1rem 1.2rem; }}
.bi-list b {{ display: block; color: var(--ink); font-size: 1rem; margin-bottom: .2rem; }}
.bi-list span {{ color: var(--sub); font-size: .92rem; line-height: 1.45; }}
.st-key-bi {{ border-radius: 28px; padding: 1.4rem; }}
.st-key-bi iframe {{ border-radius: 18px; }}

/* Live demo */
.demo-head {{ scroll-margin-top: 80px; }}
.st-key-demo {{ border-radius: 30px; padding: 2rem 2rem 1.2rem 2rem; }}
.check {{ font-size: .98rem; margin: .38rem 0; color: var(--ink); }}
.check .ok {{ color: var(--violet); font-weight: 700; margin-right: .45rem; }}
.check .ko {{ color: #C9577A; font-weight: 700; margin-right: .45rem; }}
.pipeline {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: .8rem; margin: .6rem 0 1.2rem 0; }}
.step {{ background: rgba(255,255,255,.55); border: 1px solid rgba(255,255,255,.9); border-radius: 20px; padding: 1rem 1.1rem; }}
.step small {{ color: var(--sub); font-size: .82rem; }} .stApp.stApp.stApp .step b {{ display: block; font-family: var(--serif) !important; font-size: 2rem; font-weight: 600; color: var(--plum); line-height: 1.1; }}
.stButton button, .stDownloadButton button {{ border-radius: 980px !important; background: rgba(255,255,255,.6) !important; border: 1px solid rgba(255,255,255,.9) !important; }}
[data-testid="stExpander"] details {{ border-radius: 18px; background: rgba(255,255,255,.45); border: 1px solid rgba(255,255,255,.85); }}
div[data-baseweb="input"], div[data-baseweb="base-input"] {{ background: rgba(255,255,255,.6) !important; border-radius: 12px; }}

/* Why me */
.why {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 2.4rem; margin: 0 0 6rem 0; }} .stApp.stApp.stApp .why h4 {{ font-family: var(--serif) !important; font-size: 1.6rem; font-weight: 600; line-height: 1.1; margin: 0 0 .5rem 0; color: var(--plum); }}
.why p {{ color: var(--sub); line-height: 1.6; margin: 0; }}
.journey {{ display: grid; grid-template-columns: repeat(5, 1fr); gap: 1rem; margin: -2rem 0 6rem 0; border-top: 2px solid rgba(255,255,255,.95); padding-top: 1.6rem; position: relative; box-shadow: 0 -1px 0 rgba(46,50,112,.12); }}
.stop {{ position: relative; }}
.stop::before {{ content: ""; position: absolute; top: -2.05rem; left: 0; width: 12px; height: 12px; border-radius: 50%; background: #fff; border: 2px solid rgba(46,50,112,.25); }}
.stop.now::before {{ background: var(--violet); border-color: var(--violet); box-shadow: 0 0 0 5px rgba(124,116,232,.22); }}
.stop .year {{ display: block; font-size: .85rem; color: var(--violet); font-weight: 600; margin-bottom: .3rem; }}
.stop b {{ display: block; font-size: .98rem; color: var(--ink); line-height: 1.3; margin-bottom: .25rem; }}
.stop small {{ color: var(--sub); font-size: .85rem; line-height: 1.35; }}

/* Contact */
.contact {{
  background: radial-gradient(110% 150% at 12% 0%, #9AA8FF 0%, #5C64CF 40%, #33378A 75%, #24275C 100%);
  color: #F8F9FF; border-radius: 34px; text-align: center; padding: 4.6rem 1.5rem; scroll-margin-top: 80px;
  border: 1px solid rgba(255,255,255,.25); box-shadow: 0 1px 0 rgba(255,255,255,.35) inset, 0 24px 60px rgba(46,50,112,.30);
}} .stApp.stApp.stApp .contact .small {{ font-family: var(--serif) !important; font-style: italic; font-size: 1.5rem; color: #D9DEFF; margin: 0 0 .3rem 0; }} .stApp.stApp.stApp .contact h2 {{ font-family: var(--serif) !important; font-weight: 600; font-size: clamp(2.6rem, 6vw, 4.2rem); line-height: 1.02; margin: 0 0 1rem 0; }}
.contact p {{ color: rgba(248,249,255,.8); font-size: 1.15rem; max-width: 46ch; margin: 0 auto 2rem auto; line-height: 1.55; }}
.contact .btn-primary {{ background: #fff; color: var(--plum) !important; }}
.contact .btn-ghost {{ color: #fff !important; background: rgba(255,255,255,.12); border-color: rgba(255,255,255,.4); box-shadow: none; }}
.contact .btn-ghost:hover {{ background: rgba(255,255,255,.22); }}
.foot {{ text-align: center; color: var(--sub); font-size: .82rem; margin-top: 2rem; }}

@media (max-width: 820px) {{
  .nav {{ gap: .9rem; font-size: .76rem; padding: 0 .4rem 0 1rem; }} .nav .hide-sm {{ display: none; }}
  .scoreboard {{ grid-template-columns: repeat(2, 1fr); }}
  .scoreboard .cell:nth-child(2) {{ border-right: none; }}
  .scoreboard .cell:nth-child(-n+2) {{ border-bottom: 1px solid rgba(46,50,112,.10); }}
  .bento, .trio, .why, .pipeline, .split, .journey {{ grid-template-columns: 1fr; }}
  .feature {{ padding: 2.2rem 1.5rem; }}
  .journey {{ border-top: none; border-left: 2px solid rgba(255,255,255,.95); padding: 0 0 0 1.4rem; margin-top: 0; gap: 1.4rem; box-shadow: none; }}
  .stop::before {{ top: .15rem; left: -1.92rem; }}
}}
</style>
""")

# =============================================================================
# NAV + HERO
# =============================================================================
html(f"""
<nav class="nav">
<a class="brand" href="#top">María Carolina</a>
<a href="#skills">What I do</a>
<a href="#work">Work</a>
<a class="hide-sm" href="#dashboards">Dashboards</a>
<a class="hide-sm" href="#demo">Live demo</a>
<a class="hide-sm" href="#about">About</a>
<a class="cta" href="#contact">Let's talk</a>
</nav>
<div class="hero" id="top">
<svg class="court" viewBox="0 0 1000 520" preserveAspectRatio="xMidYMid meet" aria-hidden="true" fill="none" stroke="#FFFFFF" stroke-width="3"><rect x="80" y="40" width="840" height="440" rx="4"/><line x1="80" y1="95" x2="920" y2="95"/><line x1="80" y1="425" x2="920" y2="425"/><line x1="260" y1="95" x2="260" y2="425"/><line x1="740" y1="95" x2="740" y2="425"/><line x1="260" y1="260" x2="740" y2="260"/><line x1="500" y1="30" x2="500" y2="490" stroke-width="5" stroke-dasharray="2 9"/></svg>
<p class="hello">Hi, I'm</p>
<h1>María <em>Carolina.</em></h1>
<p class="tagline">I turn messy data into models and pipelines that ship.</p>
<p class="lede">Data Scientist with a data engineer's habits: clean inputs, honest validation and products people can actually click on.</p>
<a class="btn btn-primary" href="#work">See my work</a>
<a class="btn btn-ghost" href="#demo">Try the live pipeline</a>
</div>
<div class="scoreboard">
<div class="cell"><b>1.16M</b><span>reviews modeled</span></div>
<div class="cell"><b>0.808</b><span>macro F1 on unseen data</span></div>
<div class="cell"><b>0.8132</b><span>DrivenData leaderboard</span></div>
<div class="cell"><b>3</b><span>languages: ES, EN, DE</span></div>
</div>
""")

# =============================================================================
# CAPABILITIES (bento)
# =============================================================================
tiles = "".join(
    f"<div class='tile'><div class='icon'><svg viewBox='0 0 24 24' fill='none' stroke='currentColor' stroke-width='1.7' stroke-linecap='round' stroke-linejoin='round'>{ICON[icon]}</svg></div><h3>{title}</h3><p>{text}</p>"
    f"<div class='tools'>{tools}</div><div class='proof'>Proven in: {proof}</div></div>"
    for icon, title, text, tools, proof in CAPABILITIES
)
html(f"""
<div class="section" id="skills">
<h2>What I bring to your team.</h2>
<p>Six things I do well, each one backed by real work you can open and check.</p>
</div>
<div class="bento">{tiles}</div>
""")

# =============================================================================
# FEATURED WORK
# =============================================================================
html(f"""
<div class="section" id="work">
<h2>Work that ships.</h2>
<p>Not just notebooks. Deployed apps, tested APIs and results measured the honest way.</p>
</div>
<div class="feature dark"><div class="split"><div>
<p class="kicker">NLP · MLOps · Live app</p>
<h3>What 1.16 million diners really think.</h3>
<p class="desc">A bilingual sentiment engine for Madrid's restaurants. It reads Spanish and English reviews, flags restaurants whose reputation is slipping, and benchmarks each one against true competitors. Served through a tested FastAPI service, tracked in MLflow, explained with LIME.</p>
<div class="metrics">
<div><b>1.16M</b><span>reviews</span></div>
<div><b>10,056</b><span>restaurants</span></div>
<div><b>0.808</b><span>macro F1</span></div>
<div><b>90.5%</b><span>accuracy on unseen restaurants</span></div>
</div>
<a class="btn btn-primary" href="{LINKS['restaurants']}" target="_blank">Open the live app</a>
</div>
<div class="mock" aria-hidden="true">
<div class="review"><p>“La paella llegó fría y el servicio fue lentísimo.”</p><span class="tag neg">Negative</span></div>
<div class="review"><p>“Best tapas we had in Madrid, the staff were lovely.”</p><span class="tag pos">Positive</span></div>
<div class="review"><p>“Correcto, sin más. Precio un poco alto.”</p><span class="tag neu">Neutral</span></div>
<div class="alert">Reputation alert: rating down 0.8 in six months</div>
</div>
</div></div>
<div class="trio">
<div class="feature light">
<p class="kicker">Machine learning · Competition</p>
<h3>Which water pumps will fail next?</h3>
<p class="desc">60,000 water points in Tanzania, three outcomes. Feature engineering, leak-free target encoding and tuned gradient boosting.</p>
<div class="metrics"><div><b>0.8132</b><span>leaderboard</span></div><div><b>0.817</b><span>5-fold CV</span></div></div>
<a class="btn btn-ghost" href="{LINKS['pumps']}" target="_blank">View on GitHub</a>
</div>
<div class="feature light">
<p class="kicker">Data engineering</p>
<h3>A server inventory, built and checked.</h3>
<p class="desc">Generates hostnames from a naming convention, parses them into fields and validates every output. Try it right here below.</p>
<div class="metrics"><div><b>5</b><span>quality checks</span></div><div><b>1,500</b><span>records</span></div></div>
<a class="btn btn-ghost" href="#demo">Try it live</a>
</div>
<div class="feature light">
<p class="kicker">Statistics · Health data</p>
<h3>Reading blood sugar the careful way.</h3>
<p class="desc">Young vs adult patients compared with the right tests, plus a regression that predicts post-meal glucose.</p>
<div class="metrics"><div><b>0.634</b><span>R²</span></div><div><b>±4.61</b><span>mg/dL</span></div></div>
<a class="btn btn-ghost" href="{LINKS['glucose']}" target="_blank">Read the report</a>
</div>
</div>
""")

# =============================================================================
# BUSINESS INTELLIGENCE (Tableau)
# =============================================================================
live_views = {name: url for name, url in TABLEAU_DASHBOARDS.items() if url.strip()}
profile_btn = (f"<a class='btn btn-ghost' href='{TABLEAU_PROFILE}' target='_blank'>See it on Tableau Public</a>"
               if TABLEAU_PROFILE else "")
html(f"""
<div class="section" id="dashboards">
<h2>Dashboards people act on.</h2>
<p>Numbers are only useful when a manager can read them in ten seconds.</p>
</div>
<div class="feature light bi">
<div class="split"><div>
<p class="kicker">Business intelligence · Tableau</p>
<h3>Easy Loans: a year of lending, at a glance.</h3>
<p class="desc">Two interactive dashboards on 2023 loan operations across Europe. Track volume and running totals over time, spot which operations sit above or below the average, and find the top merchants in every country on a map.</p>
<div class="metrics">
<div><b>2</b><span>dashboards</span></div>
<div><b>7</b><span>linked views</span></div>
<div><b>LOD</b><span>and table calculations</span></div>
</div>
{profile_btn}
</div>
<div class="bi-list">
<div><b>Loan operations</b><span>KPIs, deviation from the average, running total, date and country filters</span></div>
<div><b>Merchant analysis</b><span>Top 10 merchants, merchants by country, interactive map</span></div>
<div><b>Built for the user</b><span>Minimum-amount parameter and one-click reset buttons</span></div>
</div>
</div>
</div>
""")
if live_views:
    with st.container(key="bi"):
        view = st.segmented_control("Dashboard", list(live_views), default=list(live_views)[0],
                                    label_visibility="collapsed") or list(live_views)[0]
        url = live_views[view]
        sep = "&" if "?" in url else "?"
        src = f"{url}{sep}:showVizHome=no&:embed=true&:toolbar=bottom"
        if hasattr(st, "iframe"):
            st.iframe(src, height=860)
        else:
            components.iframe(src, height=860, scrolling=True)
        st.caption("Interactive: filter by date and country, hover for details, click a bar or map point to cross-filter.")
html("<div style='height:6rem'></div>")

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


PLOT_FONT = dict(family="-apple-system, BlinkMacSystemFont, Inter, Helvetica Neue, Arial, sans-serif", color=INK)

html("""
<div class="section demo-head" id="demo">
<h2>Don't take my word for it.</h2>
<p>This pipeline runs live. Generate a server inventory, then watch it get parsed and checked.</p>
</div>
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
    <div class="pipeline">
    <div class="step"><small>1. Generate</small><b>{len(raw):,}</b><small>hostnames</small></div>
    <div class="step"><small>2. Parse</small><b>{data.shape[1]}</b><small>structured fields</small></div>
    <div class="step"><small>3. Validate</small><b>{passed}/{len(report['checks'])}</b><small>checks passed</small></div>
    </div>
    """)

    left, right = st.columns([1, 1.7], gap="large")
    with left:
        items = "".join(
            f"<div class='check'><span class='{'ok' if ok else 'ko'}'>{'✓' if ok else '✕'}</span>{name}</div>"
            for name, ok in report["checks"].items()
        )
        worst = report["distribution"]["gap_pp"].max()
        dup_note = (f"<div class='check' style='color:#C9577A'>{report['duplicates']} duplicate hostnames found.</div>"
                    if report["duplicates"] else "")
        html(f"{items}{dup_note}<p style='color:{SUB};margin-top:1rem'>Largest gap from the target mix: "
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
        fig.add_bar(x=dist["category"], y=dist["target"] * 100, name="Target", marker_color=LINE)
        fig.add_bar(x=dist["category"], y=dist["observed"] * 100, name="Observed", marker_color=BLUE)
        fig.update_traces(marker_line_width=0)
        fig.update_layout(barmode="group", height=300, margin=dict(l=0, r=0, t=10, b=0), bargap=.35,
                          yaxis=dict(title="Share of servers (%)", gridcolor="rgba(46,50,112,.08)"),
                          legend=dict(orientation="h", y=1.12, x=0), plot_bgcolor="rgba(0,0,0,0)",
                          paper_bgcolor="rgba(0,0,0,0)", font=PLOT_FONT)
        st.plotly_chart(fig, width="stretch", config={"displayModeBar": False})

    pivot = data.groupby(["country", "environment"]).size().reset_index(name="servers")
    fig2 = px.bar(pivot, x="country", y="servers", color="environment", height=300,
                  color_discrete_sequence=["#2E3270", BLUE, "#8FB4F5", "#B9A9F5", "#D5DAF5"])
    fig2.update_traces(marker_line_width=0)
    fig2.update_layout(margin=dict(l=0, r=0, t=30, b=0), plot_bgcolor="rgba(0,0,0,0)",
                       paper_bgcolor="rgba(0,0,0,0)", font=PLOT_FONT, xaxis_title="", yaxis_title="Servers",
                       yaxis=dict(gridcolor="rgba(46,50,112,.08)"), legend_title_text="", bargap=.4,
                       title=dict(text="Servers by country and environment", font=dict(size=15)))
    st.plotly_chart(fig2, width="stretch", config={"displayModeBar": False})

    with st.expander("Peek at the parsed data"):
        st.dataframe(data.head(50), width="stretch", hide_index=True)

html("<div style='height:5rem'></div>")

# =============================================================================
# WHY ME
# =============================================================================
html(f"""
<div class="section" id="about">
<h2>Why work with me.</h2>
<p>A data scientist who started out studying people.</p>
</div>
<div class="why">
<div><h4>I ask the right question first.</h4><p>My background in anthropology trained me to interview, observe and frame problems before touching the data. It makes my models answer what the business actually needs.</p></div>
<div><h4>I care about the boring parts.</h4><p>Leakage checks, validation sets, data quality tests. The parts that decide whether a model survives contact with real users.</p></div>
<div><h4>I'm ready for Germany.</h4><p>Spanish native, English C1 and German B1+ and improving. Open to relocation and comfortable working across time zones.</p></div>
</div>
<div class="journey">
<div class="stop"><span class="year">2019–2024</span><b>B.A. Anthropology</b><small>University of Sonora</small></div>
<div class="stop"><span class="year">2023</span><b>Social development research</b><small>Ministry of Social Development of Sonora</small></div>
<div class="stop"><span class="year">2024</span><b>Survey data analysis</b><small>Hermosillo City Hall</small></div>
<div class="stop"><span class="year">2024–2025</span><b>Data Science Bootcamp</b><small>TripleTen</small></div>
<div class="stop now"><span class="year">2025–2026</span><b>M.Sc. Data Science, Big Data &amp; Business Analytics</b><small>Complutense University of Madrid</small></div>
</div>
""")

# =============================================================================
# CONTACT
# =============================================================================
html(f"""
<div class="contact" id="contact">
<p class="small">Game, set, match.</p>
<h2>Let's build something with your data.</h2>
<p>I'm looking for Data Scientist, ML and Data Engineering roles. Send me an email or find me on LinkedIn.</p>
<a class="btn btn-primary" href="{LINKS['email']}">Email me</a>
<a class="btn btn-ghost" href="{LINKS['linkedin']}" target="_blank">LinkedIn</a>
<a class="btn btn-ghost" href="{LINKS['github']}" target="_blank">GitHub</a>
<a class="btn btn-ghost" href="{LINKS['notion']}" target="_blank">Portfolio</a>
</div>
<p class="foot">Designed and built by María Carolina with Python, Streamlit and Plotly.</p>
""")
