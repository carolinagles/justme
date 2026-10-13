"""
María Carolina · Data Science & Data Engineering portfolio (Streamlit).
Run locally:  streamlit run app.py

Design: Swiss typography and grid with liquid-glass panels.
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

st.set_page_config(page_title="María Carolina · Data Scientist", page_icon="◦", layout="wide")


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
:root {{ --paper:{PAPER}; --ink:{INK}; --muted:#59534E; --blue:{BLUE}; --orange:{ORANGE}; --pink:{PINK}; --green:{GREEN}; --clay:{CLAY}; --sand:{SAND}; --taupe:{TAUPE}; --sans:Helvetica Neue,Helvetica,Arial,sans-serif; }}
html {{scroll-behavior:smooth;}}
body,.stApp,.stApp :is(h1,h2,h3,h4,p,span,div,a,b,li,label,button,input,small,td,th) {{font-family:var(--sans); -webkit-font-smoothing:antialiased;}}
.stApp {{color:var(--ink); background:radial-gradient(ellipse at 95% 8%,#566F9726,transparent 36%),radial-gradient(ellipse at 5% 40%,#D684A82B,transparent 34%),radial-gradient(ellipse at 90% 73%,#88886C28,transparent 35%),{PAPER}; background-attachment:fixed;}}
header[data-testid="stHeader"],#MainMenu,footer,[data-testid="stToolbar"] {{display:none;}}
.block-container {{max-width:1240px;padding:2rem 2.5rem 3rem;}}
a {{color:inherit;}} ::selection {{background:var(--blue);color:white;}}
a:focus-visible,button:focus-visible {{outline:3px solid var(--blue);outline-offset:5px;}}
.kicker {{font-size:.7rem;letter-spacing:.12em;text-transform:uppercase;font-weight:600;}} .muted {{color:var(--muted);}}
.glass,.st-key-demo,.st-key-bi {{background:linear-gradient(135deg,#ffffff99,#ffffff40);border:1px solid #ffffffe0;border-radius:24px;box-shadow:inset 0 1px 1px white,inset 0 -1px 1px #ffffff80,0 12px 40px #2626260c;backdrop-filter:blur(26px) saturate(145%);-webkit-backdrop-filter:blur(26px) saturate(145%);}}
.mast-top {{display:flex;justify-content:space-between;gap:1rem;padding-bottom:1rem;border-bottom:1px solid #26262630;}} .brand {{font-weight:600;font-size:.85rem;}}
.mast-grid {{display:grid;grid-template-columns:1.7fr 1fr;gap:4rem;align-items:end;padding:4.5rem 0 3rem;}}
.stApp .masthead h1 {{font-family:var(--sans);font-size:clamp(3.4rem,8vw,6.8rem);font-weight:600;letter-spacing:-.075em;line-height:.96;margin:0;padding:0;}}
.tagline {{font-size:.85rem;margin-top:1.8rem;line-height:1.6;color:var(--muted);}}
.hero-note {{font-size:1.2rem;line-height:1.6;max-width:32ch;}} .hero-note p {{margin-bottom:1.4rem;}}
.swatches {{display:flex;gap:7px;margin-top:1.3rem;}} .swatches i {{width:28px;height:6px;border-radius:10px;}}
.sections {{display:flex;gap:1.7rem;align-items:center;flex-wrap:wrap;padding:.85rem 1.3rem;margin-bottom:2rem;border-radius:999px;}}
.sections a {{font-size:.82rem;text-decoration:none;padding:.4rem 0;}} .sections a:hover {{color:var(--blue);}}
.btn {{display:inline-flex;align-items:center;justify-content:center;min-height:44px;padding:.7rem 1.2rem;border:1px solid #26262635;border-radius:999px;text-decoration:none!important;font-size:.82rem;font-weight:500;margin:.25rem .3rem .25rem 0;transition:transform .2s,background .2s;}}
.btn:hover {{transform:translateY(-2px);background:#ffffffb0;}} .btn-ink {{background:var(--ink);color:white!important;}} .btn-ink:hover {{background:var(--blue);}}
.front {{display:grid;grid-template-columns:1.3fr 1fr;gap:2rem;}} .article {{padding:2rem;}} .article .body {{font-size:1rem;line-height:1.7;margin:0;max-width:60ch;}}
.figures {{display:grid;grid-template-columns:repeat(2,1fr);gap:.8rem;}} .figure {{padding:1.2rem;background:#ffffff55;border:1px solid #ffffffb0;border-radius:18px;}} .figure .sw {{background:none!important;}} .figure .sw b {{font-size:2rem;letter-spacing:-.06em;}} .figure .txt p {{display:none;}} .figure .txt .kicker {{font-size:.65rem;color:var(--muted);}} .figures .head {{display:none;}}
.sec {{margin-top:5rem;scroll-margin-top:24px;}} .sec-head {{display:grid;grid-template-columns:1fr auto;align-items:end;gap:2rem;padding-bottom:1.2rem;border-bottom:1px solid #26262630;margin-bottom:1.7rem;}}
.stApp .sec-head h2 {{font-size:clamp(2rem,4vw,3.4rem);font-weight:500;letter-spacing:-.055em;padding:0;margin:.5rem 0 0;line-height:1.1;}} .dek {{max-width:36ch;font-size:.9rem;line-height:1.5;color:var(--muted);margin:0;}}
.caps {{display:grid;grid-template-columns:repeat(3,1fr);gap:1.5rem;}} .cap {{display:grid;grid-template-columns:10px 1fr;gap:.8rem;border-top:1px solid #26262625;padding:1.2rem 0;}} .dot {{width:9px;height:9px;border-radius:50%;margin-top:.4rem;}}
.stApp .cap h3 {{font-size:1.1rem;font-weight:600;letter-spacing:-.025em;margin:0 0 .6rem;padding:0;}} .cap p {{font-size:.9rem;line-height:1.6;}} .tools,.where {{font-size:.75rem;line-height:1.6;color:var(--muted);}} .where {{margin-top:.6rem;}}
.lead {{padding:2.5rem;}} .lead-grid {{display:grid;grid-template-columns:1.25fr 1fr;gap:3rem;}}
.stApp .lead h3 {{font-size:clamp(1.8rem,3vw,2.6rem);font-weight:500;letter-spacing:-.05em;line-height:1.1;margin:1rem 0; padding:0;}}
.body,.story p {{font-size:.95rem;line-height:1.65;}}
.review {{background:#ffffff75;border:1px solid white;border-radius:16px;padding:1rem;margin:.6rem 0;display:flex;flex-direction:column;gap:.8rem;}} .review p {{font-size:.9rem;line-height:1.5;margin:0;}} .tag {{font-size:.65rem;font-weight:600;align-self:flex-start;padding:.3rem .6rem;border-radius:999px;}} .neg {{background:#EA611D25;color:#85300B;}} .pos {{background:#88886C30;color:#45452E;}} .neu {{background:#AF9A8730;color:#554437;}} .words {{font-size:.75rem;color:var(--muted);}} mark {{background:#EA611D20;padding:.15rem .3rem;border-radius:4px;}}
.facts {{display:grid;grid-template-columns:repeat(4,1fr);gap:1rem;border-top:1px solid #26262620;margin-top:2rem;padding-top:1.5rem;}} .facts b {{display:block;font-size:1.5rem;letter-spacing:-.04em;}} .facts span {{display:block;font-size:.75rem;color:var(--muted);margin-top:.4rem;line-height:1.5;}}
.stories {{display:grid;grid-template-columns:1fr 1fr;gap:1.2rem;margin-top:1.2rem;}} .story {{padding:2rem;border-top:3px solid var(--accent);}} .story h3 {{font-size:1.65rem;font-weight:500;letter-spacing:-.04em;line-height:1.2;margin:1rem 0;}} .nums {{display:flex;gap:2rem;margin-bottom:1rem;}} .nums b {{display:block;font-size:1.7rem;letter-spacing:-.04em;}} .nums span {{font-size:.75rem;color:var(--muted);}}
.dash-notes {{display:grid;grid-template-columns:repeat(3,1fr);gap:2rem;margin-bottom:1.5rem;}} .dash-notes div {{border-top:2px solid var(--accent);padding-top:.8rem;}} .dash-notes b {{display:block;font-size:.9rem;margin-bottom:.4rem;}} .dash-notes span {{font-size:.85rem;line-height:1.5;color:var(--muted);}}
.st-key-bi,.st-key-demo {{padding:1.5rem;}} .steps {{display:grid;grid-template-columns:repeat(3,1fr);gap:1rem;margin:1.5rem 0;}} .steps div {{background:#ffffff70;border:1px solid white;border-radius:16px;padding:1rem;border-left:3px solid var(--accent);}} .steps b {{display:block;font-size:2rem;font-weight:500;letter-spacing:-.05em;}} .steps small {{color:var(--muted);}}
.check {{font-size:.85rem;padding:.65rem 0;border-bottom:1px solid #26262615;display:flex;gap:.6rem;}} .ok {{color:#45452E;}} .ko {{color:#85300B;}}
.stButton button,.stDownloadButton button,.stLinkButton a {{border-radius:999px!important;min-height:44px;}} [data-testid="stExpander"] details {{background:#ffffff55;border-radius:16px;border:1px solid white;}}
.about {{display:grid;grid-template-columns:1fr 1fr;gap:2rem;}} .notes {{padding:2rem;}} .note {{padding:1rem 0;border-bottom:1px solid #26262620;}} .note:first-child {{padding-top:0;}} .note:last-child {{border:0;padding-bottom:0;}} .note h4 {{font-size:1rem;font-weight:600;padding:0;margin-bottom:.5rem;}} .note p {{font-size:.9rem;line-height:1.65;margin:0;}}
.path {{width:100%;border-collapse:collapse;}} .path tr {{border-bottom:1px solid #26262620;}} .path td {{padding:1rem .6rem;font-size:.85rem;vertical-align:top;}} .year {{white-space:nowrap;color:var(--muted);}} .what b,.what span {{display:block;line-height:1.5;}} .what span {{color:var(--muted);margin-top:.3rem;}}
.contact {{padding:2.5rem;margin-top:5rem;}} .contact h2 {{font-size:2.5rem;font-weight:500;letter-spacing:-.05em;padding:0;margin:.8rem 0;}} .contact p {{font-size:.95rem;color:var(--muted);}} .mail {{font-size:clamp(1rem,3vw,1.7rem);text-decoration:none;border-bottom:1px solid #26262640;overflow-wrap:anywhere;}} .foot {{padding:2rem 0;font-size:.7rem;color:var(--muted);}}
@media(max-width:800px) {{.block-container {{padding:1.2rem;}} .mast-grid,.front,.lead-grid,.about {{grid-template-columns:1fr;gap:1.5rem;}} .mast-grid {{padding:3rem 0 2rem;}} .hero-note {{max-width:48ch;font-size:1rem;}} .caps {{grid-template-columns:1fr 1fr;}} .sec-head {{grid-template-columns:1fr;gap:.8rem;}} .sections {{border-radius:20px;gap:.4rem 1.2rem;}} .facts {{grid-template-columns:1fr 1fr;}} .lead,.story,.article,.notes {{padding:1.5rem;}} }}
@media(max-width:520px) {{.stories,.caps,.dash-notes {{grid-template-columns:1fr;}} .steps {{gap:.5rem;}} .steps div {{padding:.7rem;}} .steps .kicker {{font-size:.6rem;}} .mast-top .kicker {{font-size:.6rem;}} .sec {{margin-top:3.5rem;}} }}
@media(prefers-reduced-motion:reduce) {{html {{scroll-behavior:auto;}} .btn {{transition:none;}} .btn:hover {{transform:none;}}}}
</style>
""")

# =============================================================================
# MASTHEAD + SECTION BAR
# =============================================================================
swatches = "".join(f"<i style='background:{c}'></i>" for c in (BLUE, ORANGE, PINK, GREEN, CLAY))
html(f"""
<header class="masthead" id="front">
<div class="mast-top"><span class="brand">MC / Portfolio</span><span class="kicker muted">Hermosillo, Mexico · Open to relocation</span></div>
<div class="mast-grid"><div><h1>María<br>Carolina.</h1><p class="tagline">Data science / Machine learning / Data engineering</p><div class="swatches">{swatches}</div></div>
<div class="hero-note"><p>I explore data and build tools that make the findings easier to use.</p><a class="btn btn-ink" href="#work">Explore projects ↗</a><a class="btn btn-line" href="#contact">Contact</a></div></div>
</header>
<nav class="sections glass" aria-label="Portfolio sections"><a href="#work">01 / Work</a><a href="#capabilities">02 / Skills</a><a href="#dashboards">03 / Dashboards</a><a href="#demo">04 / Demo</a><a href="#about">05 / About</a></nav>
""")

# =============================================================================
# FRONT PAGE
# =============================================================================
figs = "".join(
    f"<div class='figure'><div class='sw' style='background:{c}'><b>{num}</b></div>"
    f"<div class='txt'><span class='kicker'>{name}</span><p>{text}</p></div></div>"
    for c, num, name, text in FIGURES[:4]
)
html(f"""
<section class="front" aria-label="Introduction and project results">
<article class="article glass"><span class="kicker muted">A little context</span><p class="body" style="margin-top:1rem">My background is in anthropology and data science. My projects bring together data preparation, analysis and small applications, with a growing focus on data engineering.</p></article>
<aside class="figures" aria-label="Selected project results">{figs}</aside></section>
""")

# =============================================================================
# WORK
# =============================================================================
html(f"""
<section class="sec" id="work">
<div class="sec-head"><div><span class="kicker muted">01 / Work</span><h2>Selected work</h2></div>
<p class="dek">A selection of applications, notebooks and analyses.</p></div>
<article class="lead glass">
<div class="lead-grid">
<div>
<span class="kicker" style="color:var(--blue)">Featured project · NLP / Deployment</span>
<h3>Madrid Restaurant Intelligence</h3>
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
<h3>Water pump classification</h3>
<p>60,000 water points in Tanzania with three possible outcomes. Feature engineering, target encoding fitted on training data only, and gradient boosting tuned with Optuna.</p>
<div class="nums"><div><b>0.8132</b><span>leaderboard</span></div><div><b>0.817</b><span>5-fold CV</span></div></div>
<a class="btn btn-line" href="{LINKS['pumps']}" target="_blank">Code</a>
</article>
<article class="story glass" style="--accent:{PINK}">
<div class="row"><span class="kicker muted">Python app · live</span></div>
<h3>Guess the Number</h3>
<p>A console game turned into a Streamlit app with game modes, difficulty levels, scoring, saved results and a records screen with a leaderboard and charts.</p>
<div class="nums"><div><b>3</b><span>difficulty levels</span></div><div><b>6</b><span>modules</span></div></div>
<a class="btn btn-ink" href="{LINKS['guess']}" target="_blank">Play</a>
<a class="btn btn-line" href="{LINKS['guess_repo']}" target="_blank">Code</a>
</article>
<article class="story glass" style="--accent:{GREEN}">
<div class="row"><span class="kicker muted">Data engineering</span></div>
<h3>Hostname data pipeline</h3>
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
# CAPABILITIES
# =============================================================================
caps = "".join(
    f"<div class='cap'><span class='dot' style='background:{c}'></span><div>"
    f"<h3>{name}</h3><p>{what}</p><div class='tools'>{tools}</div><div class='where'>{where}</div></div></div>"
    for name, c, what, tools, where in CAPABILITIES
)
html(f"""
<section class="sec" id="capabilities">
<div class="sec-head"><div><span class="kicker muted">02 / Skills</span><h2>Capabilities</h2></div>
<p class="dek">Tools and methods used across my projects.</p></div>
<div class="caps">{caps}</div>
</section>
""")

# =============================================================================
# DASHBOARDS (Tableau)
# =============================================================================
html(f"""
<section class="sec" id="dashboards">
<div class="sec-head"><div><span class="kicker muted">03 / Dashboards</span><h2>Dashboards</h2></div>
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
<div class="sec-head"><div><span class="kicker muted">04 / Demo</span><h2>Live demo</h2></div>
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
<div class="sec-head"><div><span class="kicker muted">05 / About</span><h2>About</h2></div>
<p class="dek">How I like to work, and the path that brought me here.</p></div>
<div class="about">
<div class="notes glass">
<div class="note"><h4>Questions first</h4><p>Anthropology taught me to interview, observe and define the problem before choosing a method.</p></div>
<div class="note"><h4>Careful validation</h4><p>I use separate test data and quality checks to understand what a model can and cannot do.</p></div>
<div class="note"><h4>Languages</h4><p>Spanish (native), English (C1) and German (B1+, learning).</p></div>
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
<p>Interested in opportunities in data science and data engineering.</p>
<a class="mail" href="{LINKS['email']}">Carolinagles@gmail.com</a>

</section>
<div class="foot">María Carolina González Bernal</div>
""")
