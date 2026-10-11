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
    ("stats", "Statistics with judgment",
     "The right test for the question, with honest uncertainty instead of overconfident claims.",
     "Hypothesis testing · ANOVA · Confidence intervals · Regression", "Glucose study · Restaurant NLP"),
    ("cloud", "Ready for scale",
     "Trained on distributed and cloud tools during my M.Sc. at Complutense University of Madrid.",
     "PySpark · Spark SQL · MLlib · Google Cloud · MongoDB · Snowflake", "M.Sc. coursework"),
]

# =============================================================================
# STYLE
# =============================================================================
BLUE = "#0071E3"
INK = "#1D1D1F"
SUB = "#6E6E73"
LINE = "#D2D2D7"
SOFT = "#F5F5F7"

html(f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');
:root {{ --ink:{INK}; --sub:{SUB}; --blue:{BLUE}; --line:{LINE}; --soft:{SOFT}; }}
html, body, .stApp, .stApp :is(h1,h2,h3,h4,h5,p,span,div,a,b,li,label,button,input,small,textarea):not([data-testid="stIconMaterial"]):not(.material-symbols-rounded) {{
  font-family: -apple-system, BlinkMacSystemFont, "SF Pro Display", "SF Pro Text", "Inter", "Helvetica Neue", Arial, sans-serif !important;
  -webkit-font-smoothing: antialiased;
}}
.stApp {{ background: #FBFBFD; }}
header[data-testid="stHeader"], #MainMenu, footer, [data-testid="stToolbar"], [data-testid="stDecoration"] {{ display: none !important; }}
.block-container {{ max-width: 1080px; padding: 0 1.4rem 4rem 1.4rem; }}
section.main > div {{ padding-top: 0; }}

/* Navigation: frosted glass bar */
.nav {{
  position: fixed; top: 0; left: 0; right: 0; z-index: 999; height: 52px;
  display: flex; align-items: center; justify-content: center; gap: 2.2rem;
  background: rgba(251,251,253,.72); backdrop-filter: saturate(180%) blur(20px);
  -webkit-backdrop-filter: saturate(180%) blur(20px); border-bottom: 1px solid rgba(0,0,0,.06);
  font-size: .82rem;
}}
.nav a {{ color: var(--ink); text-decoration: none; opacity: .8; }}
.nav a:hover {{ opacity: 1; }}
.nav .brand {{ font-weight: 600; opacity: 1; margin-right: 1rem; }}
.nav .cta {{ background: var(--blue); color: #fff; opacity: 1; padding: .3rem .85rem; border-radius: 980px; }}

/* Hero */
.hero {{ text-align: center; padding: 8.5rem 0 3.5rem 0; }}
.hero .hello {{ font-size: 1.35rem; font-weight: 600; color: var(--sub); margin: 0 0 .4rem 0; }}
.hero h1 {{
  font-size: clamp(3.4rem, 9vw, 6.6rem); line-height: 1.02; font-weight: 800; letter-spacing: -0.045em; margin: 0;
  background: linear-gradient(100deg, #1D1D1F 10%, #0071E3 55%, #7A5AF8 90%);
  -webkit-background-clip: text; background-clip: text; color: transparent;
  animation: rise .9s cubic-bezier(.2,.7,.2,1) both;
}}
.hero .tagline {{ font-size: clamp(1.5rem, 3.4vw, 2.3rem); font-weight: 600; letter-spacing: -0.02em; color: var(--ink); margin: 1.1rem auto .8rem auto; max-width: 30ch; line-height: 1.15; }}
.hero .lede {{ font-size: 1.15rem; color: var(--sub); max-width: 52ch; margin: 0 auto 2rem auto; line-height: 1.55; }}
@keyframes rise {{ from {{ opacity: 0; transform: translateY(18px); }} to {{ opacity: 1; transform: none; }} }}
@media (prefers-reduced-motion: reduce) {{ .hero h1 {{ animation: none; }} }}

.btn {{ display: inline-block; padding: .75rem 1.35rem; border-radius: 980px; font-size: 1rem; font-weight: 500; text-decoration: none !important; margin: .25rem .3rem; transition: background .2s, color .2s; }}
.btn-primary {{ background: var(--blue); color: #fff !important; }}
.btn-primary:hover {{ background: #0077ED; }}
.btn-ghost {{ color: var(--blue) !important; border: 1px solid var(--blue); }}
.btn-ghost:hover {{ background: var(--blue); color: #fff !important; }}
.btn:focus-visible, .nav a:focus-visible {{ outline: 3px solid rgba(0,113,227,.45); outline-offset: 2px; }}

/* Stats strip */
.stats {{ display: grid; grid-template-columns: repeat(4, 1fr); gap: 1rem; margin: 1rem 0 5rem 0; }}
.stat {{ text-align: center; padding: 1.3rem .5rem; }}
.stat b {{ display: block; font-size: clamp(2rem, 4.5vw, 3rem); font-weight: 700; letter-spacing: -0.03em; color: var(--ink); }}
.stat span {{ color: var(--sub); font-size: .95rem; }}

/* Section headings */
.section {{ text-align: center; margin: 0 auto 2.4rem auto; max-width: 720px; scroll-margin-top: 70px; }}
.section h2 {{ font-size: clamp(2.2rem, 5vw, 3.4rem); font-weight: 700; letter-spacing: -0.035em; line-height: 1.07; margin: 0 0 .7rem 0; color: var(--ink); }}
.section p {{ font-size: 1.2rem; color: var(--sub); line-height: 1.5; margin: 0; }}

/* Bento grid */
.bento {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 1.1rem; margin-bottom: 6rem; }}
.tile {{ background: #fff; border-radius: 28px; padding: 1.8rem 1.6rem; box-shadow: 0 2px 6px rgba(0,0,0,.04), 0 12px 32px rgba(0,0,0,.05); }}
.tile .icon {{ width: 46px; height: 46px; border-radius: 14px; display: grid; place-items: center; color: #fff; background: linear-gradient(135deg, #0071E3, #7A5AF8); }}
.tile .icon svg {{ width: 24px; height: 24px; }}
.tile h3 {{ font-size: 1.3rem; font-weight: 700; letter-spacing: -0.02em; margin: .7rem 0 .45rem 0; color: var(--ink); }}
.tile p {{ color: var(--sub); line-height: 1.5; margin: 0 0 1rem 0; font-size: .98rem; }}
.tile .tools {{ font-size: .85rem; color: var(--ink); line-height: 1.5; }}
.tile .proof {{ font-size: .82rem; color: var(--blue); margin-top: .6rem; }}

/* Featured project tiles */
.feature {{ border-radius: 32px; padding: 3rem 2.6rem; margin-bottom: 1.1rem; overflow: hidden; scroll-margin-top: 70px; }}
.feature.dark {{ background: radial-gradient(120% 140% at 85% 0%, #1E3A8A 0%, #0B1020 55%, #000 100%); color: #F5F5F7; }}
.feature.light {{ background: #fff; box-shadow: 0 2px 6px rgba(0,0,0,.04), 0 12px 32px rgba(0,0,0,.05); }}
.feature .kicker {{ font-size: 1rem; font-weight: 600; color: #6CB4FF; margin: 0 0 .5rem 0; }}
.feature.light .kicker {{ color: var(--blue); }}
.feature h3 {{ font-size: clamp(2rem, 4.4vw, 3rem); font-weight: 700; letter-spacing: -0.035em; line-height: 1.05; margin: 0 0 1rem 0; max-width: 18ch; }}
.feature.light h3 {{ color: var(--ink); }}
.feature .desc {{ font-size: 1.15rem; line-height: 1.55; max-width: 56ch; margin: 0 0 2rem 0; opacity: .82; }}
.feature.light .desc {{ color: var(--sub); opacity: 1; }}
.feature.dark .metrics {{ gap: 1.8rem; }}
.split {{ display: grid; grid-template-columns: 1.25fr 1fr; gap: 2.4rem; align-items: center; }}
.mock {{ display: flex; flex-direction: column; gap: .8rem; }}
.review {{ background: rgba(255,255,255,.08); border: 1px solid rgba(255,255,255,.14); backdrop-filter: blur(12px); border-radius: 18px; padding: 1rem 1.1rem; }}
.review p {{ margin: 0 0 .6rem 0; font-size: .98rem; line-height: 1.45; color: #F5F5F7; }}
.tag {{ font-size: .78rem; font-weight: 600; padding: .2rem .6rem; border-radius: 980px; }}
.tag.neg {{ background: rgba(255,69,58,.18); color: #FF6961; }}
.tag.pos {{ background: rgba(48,209,88,.18); color: #4CD964; }}
.tag.neu {{ background: rgba(255,214,10,.16); color: #FFD60A; }}
.alert {{ font-size: .88rem; color: #FFD60A; padding: .2rem .2rem; }}
.metrics {{ display: flex; flex-wrap: wrap; gap: 2.6rem; margin-bottom: 2rem; }}
.metrics div b {{ display: block; font-size: 2.3rem; font-weight: 700; letter-spacing: -0.03em; }}
.metrics div span {{ font-size: .9rem; opacity: .7; }}
.feature.light .metrics b {{ color: var(--ink); }}
.feature.light .metrics span {{ color: var(--sub); opacity: 1; }}
.feature .btn-ghost.on-dark {{ color: #fff !important; border-color: rgba(255,255,255,.6); }}
.feature .btn-ghost.on-dark:hover {{ background: #fff; color: #000 !important; }}
.trio {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 1.1rem; margin-bottom: 6rem; }}
.trio .feature {{ margin-bottom: 0; padding: 2.4rem 2rem; }}
.trio .feature h3 {{ font-size: clamp(1.45rem, 2.4vw, 1.8rem); }}
.trio .feature .desc {{ font-size: 1rem; }}
.trio .metrics {{ gap: 1.6rem; }}
.trio .metrics b {{ font-size: 1.9rem !important; }}

/* Live demo frame */
.demo-head {{ scroll-margin-top: 70px; }}
.st-key-demo {{ background: #fff; border-radius: 28px; padding: 2rem 2rem 1.2rem 2rem; box-shadow: 0 2px 6px rgba(0,0,0,.04), 0 12px 32px rgba(0,0,0,.05); }}
.check {{ font-size: .98rem; margin: .35rem 0; color: var(--ink); }}
.check .ok {{ color: #1A9E55; font-weight: 700; margin-right: .4rem; }}
.check .ko {{ color: #D93025; font-weight: 700; margin-right: .4rem; }}
.pipeline {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: .8rem; margin: .6rem 0 1.2rem 0; }}
.step {{ background: var(--soft); border-radius: 18px; padding: 1rem 1.1rem; }}
.step small {{ color: var(--sub); font-size: .82rem; }}
.step b {{ display: block; font-size: 1.6rem; font-weight: 700; letter-spacing: -0.02em; color: var(--ink); }}
.stButton button, .stDownloadButton button {{ border-radius: 980px !important; }}

/* Why me */
.why {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 2.4rem; margin: 0 0 6rem 0; }}
.why h4 {{ font-size: 1.25rem; font-weight: 700; letter-spacing: -0.02em; margin: 0 0 .5rem 0; color: var(--ink); }}
.why p {{ color: var(--sub); line-height: 1.55; margin: 0; }}
.journey {{ display: grid; grid-template-columns: repeat(5, 1fr); gap: 1rem; margin: -2rem 0 6rem 0; border-top: 2px solid var(--line); padding-top: 1.6rem; position: relative; }}
.stop {{ position: relative; }}
.stop::before {{ content: ""; position: absolute; top: -2.05rem; left: 0; width: 12px; height: 12px; border-radius: 50%; background: #fff; border: 2px solid var(--line); }}
.stop.now::before {{ background: var(--blue); border-color: var(--blue); box-shadow: 0 0 0 5px rgba(0,113,227,.15); }}
.stop .year {{ display: block; font-size: .85rem; color: var(--blue); font-weight: 600; margin-bottom: .3rem; }}
.stop b {{ display: block; font-size: .98rem; color: var(--ink); line-height: 1.3; margin-bottom: .25rem; }}
.stop small {{ color: var(--sub); font-size: .85rem; line-height: 1.35; }}

/* Contact */
.contact {{ background: #000; color: #F5F5F7; border-radius: 32px; text-align: center; padding: 4.5rem 1.5rem; scroll-margin-top: 70px; }}
.contact h2 {{ font-size: clamp(2.3rem, 5.4vw, 3.8rem); font-weight: 700; letter-spacing: -0.04em; line-height: 1.05; margin: 0 0 1rem 0; }}
.contact p {{ color: #A1A1A6; font-size: 1.2rem; max-width: 46ch; margin: 0 auto 2rem auto; line-height: 1.5; }}
.contact .btn-ghost {{ color: #fff !important; border-color: rgba(255,255,255,.6); }}
.foot {{ text-align: center; color: var(--sub); font-size: .82rem; margin-top: 2rem; }}

@media (max-width: 820px) {{
  .nav {{ gap: 1rem; font-size: .76rem; }} .nav .hide-sm {{ display: none; }}
  .stats {{ grid-template-columns: repeat(2, 1fr); }}
  .bento, .trio, .why, .pipeline, .split, .journey {{ grid-template-columns: 1fr; }}
  .feature {{ padding: 2.2rem 1.5rem; }}
  .journey {{ border-top: none; border-left: 2px solid var(--line); padding: 0 0 0 1.4rem; margin-top: 0; gap: 1.4rem; }}
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
<a class="hide-sm" href="#demo">Live demo</a>
<a class="hide-sm" href="#about">About</a>
<a class="cta" href="#contact">Let's talk</a>
</nav>
<div class="hero" id="top">
<p class="hello">Hi, I'm</p>
<h1>María Carolina.</h1>
<p class="tagline">I turn messy data into models and pipelines that ship.</p>
<p class="lede">Data Scientist with a data engineer's habits: clean inputs, honest validation and products people can actually click on.</p>
<a class="btn btn-primary" href="#work">See my work</a>
<a class="btn btn-ghost" href="#demo">Try the live pipeline</a>
</div>
<div class="stats">
<div class="stat"><b>1.16M</b><span>reviews modeled</span></div>
<div class="stat"><b>0.808</b><span>macro F1 on unseen data</span></div>
<div class="stat"><b>0.8132</b><span>DrivenData leaderboard</span></div>
<div class="stat"><b>3</b><span>languages: ES, EN, DE</span></div>
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
        dup_note = (f"<div class='check' style='color:#D93025'>{report['duplicates']} duplicate hostnames found.</div>"
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
                          yaxis=dict(title="Share of servers (%)", gridcolor="#EEE"),
                          legend=dict(orientation="h", y=1.12, x=0), plot_bgcolor="rgba(0,0,0,0)",
                          paper_bgcolor="rgba(0,0,0,0)", font=PLOT_FONT)
        st.plotly_chart(fig, width="stretch", config={"displayModeBar": False})

    pivot = data.groupby(["country", "environment"]).size().reset_index(name="servers")
    fig2 = px.bar(pivot, x="country", y="servers", color="environment", height=300,
                  color_discrete_sequence=[BLUE, "#7A5AF8", "#5AC8FA", "#1D1D1F", "#C7C7CC"])
    fig2.update_traces(marker_line_width=0)
    fig2.update_layout(margin=dict(l=0, r=0, t=30, b=0), plot_bgcolor="rgba(0,0,0,0)",
                       paper_bgcolor="rgba(0,0,0,0)", font=PLOT_FONT, xaxis_title="", yaxis_title="Servers",
                       yaxis=dict(gridcolor="#EEE"), legend_title_text="", bargap=.4,
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
<h2>Let's build something with your data.</h2>
<p>I'm looking for Data Scientist, ML and Data Engineering roles. Send me an email or find me on LinkedIn.</p>
<a class="btn btn-primary" href="{LINKS['email']}">Email me</a>
<a class="btn btn-ghost" href="{LINKS['linkedin']}" target="_blank">LinkedIn</a>
<a class="btn btn-ghost" href="{LINKS['github']}" target="_blank">GitHub</a>
<a class="btn btn-ghost" href="{LINKS['notion']}" target="_blank">Portfolio</a>
</div>
<p class="foot">Designed and built by María Carolina with Python, Streamlit and Plotly.</p>
""")
