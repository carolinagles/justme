"""
Maria Carolina Gonzalez Bernal - Data Science & Data Engineering portfolio.
Run locally:  streamlit run app.py
All profile content lives in the PROFILE / PROJECTS / SKILLS blocks below,
so updating the app only means editing text, not code.
"""

import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

# ---------------------------------------------------------------------------
# Page setup and visual style
# ---------------------------------------------------------------------------
st.set_page_config(
    page_title="Maria Carolina Gonzalez Bernal | Data Scientist",
    page_icon="📊",
    layout="wide",
)

INK = "#1B2A2F"
TEAL = "#0F7C78"
AMBER = "#C98A1B"
MIST = "#E3ECEA"
GREY = "#5F6F73"

st.markdown(
    f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@400;500;600&family=IBM+Plex+Serif:wght@500;600&display=swap');
    html, body, [class*="css"], .stMarkdown, p, li, label {{
        font-family: 'IBM Plex Sans', system-ui, sans-serif;
    }}
    h1, h2, h3 {{
        font-family: 'IBM Plex Serif', Georgia, serif;
        color: {INK};
        letter-spacing: -0.01em;
    }}
    .block-container {{ padding-top: 3.5rem; max-width: 1150px; }}
    .chip {{ display:inline-block; border:1px solid #C9D6D3; border-radius:999px; padding:.18rem .7rem; margin:0 .35rem .45rem 0; font-size:.9rem; color:{INK}; background:white; }}
    div.hero-name {{
        font-family: 'IBM Plex Serif', Georgia, serif;
        font-size: 2.7rem; line-height: 1.1; color: {INK}; margin: 0;
    }}
    .hero-role {{ font-size: 1.15rem; color: {TEAL}; margin: .35rem 0 .9rem 0; font-weight: 500; }}
    .hero-text {{ font-size: 1.02rem; color: {INK}; max-width: 62ch; line-height: 1.6; }}
    .project-tools {{ color: {GREY}; font-size: .9rem; margin-top: -.4rem; }}
    .evidence {{
        border-left: 3px solid {TEAL}; padding: .2rem 0 .2rem .9rem; margin: .4rem 0 1rem 0;
        color: {INK};
    }}
    a {{ color: {TEAL}; }}
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------------------------------------------------------------------------
# Content (edit here)
# ---------------------------------------------------------------------------
PROFILE = {
    "name": "Maria Carolina Gonzalez Bernal",
    "role": "Data Scientist · Machine Learning · Data Engineering",
    "summary": (
        "I build machine learning solutions end to end, from clean data pipelines "
        "and hypothesis testing to deployed models people can actually use. "
        "M.Sc. in Data Science, Big Data & Business Analytics (Complutense University of Madrid). "
        "Based in Hermosillo, Mexico, and open to relocation to Germany."
    ),
    "email": "Carolinagles@gmail.com",
    "linkedin": "https://www.linkedin.com/in/carolinagles/",
    "github": "https://github.com/carolinagles",
    "notion": "https://www.notion.so/Hi-I-m-Maria-Carolina-207fea9d890080a99c11c189f1bd930d",
    "languages": [("Spanish", "Native"), ("English", "C1"), ("German", "B1+")],
}

PROJECTS = [
    {
        "title": "Restaurant Reputation Intelligence",
        "subtitle": "Sentiment analysis and competitive benchmarking for Madrid restaurants",
        "area": "NLP · MLOps",
        "tools": ["Python", "NLP", "TF-IDF", "LinearSVC", "MLflow", "FastAPI", "Streamlit", "LIME", "Parquet"],
        "metrics": [("Reviews", "1.16M"), ("Restaurants", "10,056"), ("Macro F1", "0.808"), ("Accuracy", "90.5%")],
        "bullets": [
            "Built a bilingual (Spanish/English) sentiment classifier on 1.16 million TripAdvisor reviews.",
            "Split the data by restaurant so no restaurant appears in both training and test, avoiding leakage.",
            "Compared a dummy baseline, logistic regression and LinearSVC; tuned regularization on validation only.",
            "Served the model through a versioned FastAPI REST API with automated pytest tests, "
            "tracked experiments in MLflow, and explained predictions with LIME.",
            "Built a Streamlit dashboard with reputation alerts and peer benchmarking across 55 competitive groups.",
        ],
        "links": [("Live demo", "https://madrid-restaurant-intelligence.streamlit.app/")],
    },
    {
        "title": "Water Pump Status Classification",
        "subtitle": "DrivenData “Pump It Up” competition",
        "area": "Machine Learning",
        "tools": ["Python", "LightGBM", "CatBoost", "Optuna", "Scikit-learn", "Target Encoding"],
        "metrics": [("Water points", "60k"), ("Classes", "3"), ("Leaderboard", "0.8132"), ("5-fold CV", "0.817")],
        "bullets": [
            "Predicted the operational status of water points in Tanzania (functional, needs repair, non functional).",
            "Engineered temporal, geospatial and binary features, including pump age and distance to the country center.",
            "Applied smoothed target encoding to high-cardinality variables, fitted on training data only.",
            "Tuned LightGBM and CatBoost with Optuna and selected the model with stratified 5-fold cross-validation.",
        ],
        "links": [("GitHub", "https://github.com/carolinagles/PumpItUp/blob/main/PumpItUp.ipynb")],
    },
    {
        "title": "Synthetic Server Inventory Generator",
        "subtitle": "Hostname data pipeline: generate, parse, validate, export",
        "area": "Data Engineering",
        "tools": ["Python", "Pandas", "NumPy", "Data Generation", "Data Validation", "Matplotlib", "Seaborn"],
        "metrics": [("Records", "1,500"), ("Fields parsed", "4"), ("Format", "CSV")],
        "bullets": [
            "Generated synthetic server records from an 8-character naming convention with weighted distributions.",
            "Parsed each hostname into structured fields (OS, environment, country, node) and exported a CSV dataset.",
            "Validated the output against the target distributions with grouped aggregations and charts.",
            "Try an improved version of this pipeline in the Live demo tab.",
        ],
        "links": [("Notion report", "https://app.notion.com/p/Hostnames-Generator-2b9fea9d8900807e9deadffe3bdb83ae")],
    },
    {
        "title": "Clinical Data Analysis: Glucose Tolerance",
        "subtitle": "Statistical comparison of young and adult patients",
        "area": "Statistics",
        "tools": ["Python", "SciPy", "Scikit-learn", "Seaborn"],
        "metrics": [("Records", "65"), ("R²", "0.634"), ("Precision", "±4.61 mg/dL")],
        "bullets": [
            "Checked normality with Shapiro-Wilk and compared cohorts with Welch's and paired t-tests and ANOVA.",
            "Reported 95% and 99% confidence intervals.",
            "Fitted a linear regression predicting post-intake glucose from baseline values.",
        ],
        "links": [("Notion report", "https://www.notion.so/Glucose-Levels-307fea9d89008006b054fb9422e09232")],
    },
]

SKILLS = {
    "Programming": ["Python", "SQL", "Git/GitHub"],
    "Machine Learning": ["Scikit-learn", "LightGBM", "CatBoost", "XGBoost", "Optuna", "PCA", "K-Means", "Time series"],
    "Deep Learning & NLP": ["TensorFlow/Keras", "CNNs", "Transfer learning", "Transformers", "spaCy", "NLTK", "TF-IDF", "Topic modeling"],
    "Big Data & Cloud": ["PySpark", "Spark SQL", "MLlib", "Google Cloud"],
    "MLOps & Deployment": ["MLflow", "FastAPI", "Streamlit", "pytest", "n8n"],
    "Data & Statistics": ["Pandas", "NumPy", "SciPy", "MongoDB", "Snowflake", "Hypothesis testing", "Regression"],
    "Visualization": ["Tableau", "Plotly", "Dash", "Matplotlib", "Seaborn"],
}

# Which skills each project actually demonstrates (used for the evidence map)
EVIDENCE = {
    "Python": [0, 1, 2, 3],
    "SQL": [],
    "Pandas": [0, 1, 2, 3],
    "Scikit-learn": [0, 1, 3],
    "LightGBM / CatBoost": [1],
    "Optuna": [1],
    "NLP / TF-IDF": [0],
    "MLflow": [0],
    "FastAPI / REST APIs": [0],
    "pytest": [0],
    "Streamlit": [0],
    "Data validation": [0, 2],
    "Feature engineering": [0, 1],
    "Leakage prevention": [0, 1],
    "Hypothesis testing": [0, 3],
    "Data visualization": [0, 1, 2, 3],
}

EDUCATION = [
    ("M.Sc. Data Science, Big Data & Business Analytics", "Complutense University of Madrid (online)", "10/2025 – 10/2026",
     "Coursework: Machine Learning, Deep Learning, Text Mining, Apache Spark, Google Cloud, Model Deployment"),
    ("Data Science Bootcamp", "TripleTen", "07/2024 – 04/2025", ""),
    ("B.A. Anthropology", "University of Sonora, Mexico", "2019 – 2024",
     "Field research and interview methods: I am used to asking the right questions before touching the data."),
]

EXPERIENCE = [
    ("Administrative Process Analyst (Intern)", "Hermosillo City Hall", "02/2024 – 08/2024",
     "Analyzed citizen survey data to identify community needs and support improvements in public services."),
    ("Social Development Research Intern", "Ministry of Social Development of Sonora", "06/2023 – 09/2023",
     "Conducted structured interviews and contributed to reports used to design social programs."),
]

# ---------------------------------------------------------------------------
# Hostname pipeline (live demo)
# ---------------------------------------------------------------------------
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
    """Step 1 - Extract: generate raw hostnames following the naming convention."""
    rng = np.random.default_rng(seed)
    hostnames, seen = [], set()
    while len(hostnames) < n:
        batch = n - len(hostnames)
        prefixes = (np.char.add(np.char.add(_weighted(rng, OS_MAP, batch), _weighted(rng, ENV_MAP, batch)),
                                _weighted(rng, COUNTRY_MAP, batch)))
        nodes = rng.integers(1, 1000, size=batch)
        for p, node in zip(prefixes, nodes):
            name = f"{p}{node:03d}"
            if unique and name in seen:
                continue
            seen.add(name)
            hostnames.append(name)
    return hostnames


def parse_hostnames(hostnames: list[str]) -> pd.DataFrame:
    """Step 2 - Transform: decode each hostname into typed, structured fields."""
    s = pd.Series(hostnames, name="hostname")
    df = pd.DataFrame({"hostname": s})
    df["os"] = s.str[0].map({k: v[0] for k, v in OS_MAP.items()})
    df["environment"] = s.str[1].map({k: v[0] for k, v in ENV_MAP.items()})
    df["country"] = s.str[2:5].map({k: v[0] for k, v in COUNTRY_MAP.items()})
    df["node"] = s.str[5:8].astype(int)
    return df


def validate(df: pd.DataFrame) -> dict:
    """Step 3 - Validate: schema, uniqueness, nulls and distribution drift vs targets."""
    checks = {
        "Expected columns present": set(df.columns) == {"hostname", "os", "environment", "country", "node"},
        "Hostnames are 8 characters": bool(df["hostname"].str.len().eq(8).all()),
        "No unparsed values": bool(df.notna().all().all()),
        "Node range 001–999": bool(df["node"].between(1, 999).all()),
    }
    duplicates = int(df["hostname"].duplicated().sum())
    checks["No duplicate hostnames"] = duplicates == 0

    rows = []
    for field, mapping in (("os", OS_MAP), ("environment", ENV_MAP), ("country", COUNTRY_MAP)):
        observed = df[field].value_counts(normalize=True)
        for _, (label, target) in mapping.items():
            rows.append({"field": field, "category": label, "target": target,
                         "observed": float(observed.get(label, 0.0))})
    dist = pd.DataFrame(rows)
    dist["abs_diff_pp"] = (dist["observed"] - dist["target"]).abs() * 100
    return {"checks": checks, "duplicates": duplicates, "distribution": dist}


# ---------------------------------------------------------------------------
# Layout
# ---------------------------------------------------------------------------
left, right = st.columns([3, 2], gap="large")
with left:
    st.markdown(f"<div class='hero-name'>{PROFILE['name']}</div>", unsafe_allow_html=True)
    st.markdown(f"<p class='hero-role'>{PROFILE['role']}</p>", unsafe_allow_html=True)
    st.markdown(f"<p class='hero-text'>{PROFILE['summary']}</p>", unsafe_allow_html=True)
    b1, b2, b3, b4 = st.columns(4)
    b1.link_button("LinkedIn", PROFILE["linkedin"], width="stretch")
    b2.link_button("GitHub", PROFILE["github"], width="stretch")
    b3.link_button("Portfolio", PROFILE["notion"], width="stretch")
    b4.link_button("Email me", f"mailto:{PROFILE['email']}", width="stretch")

with right:
    st.markdown("##### What I bring")
    m1, m2 = st.columns(2)
    m1.metric("Reviews modeled", "1.16M")
    m2.metric("Best macro F1 (NLP)", "0.808")
    m3, m4 = st.columns(2)
    m3.metric("DrivenData leaderboard", "0.8132")
    m4.metric("Languages", "3", help="Spanish (native), English (C1), German (B1+)")

st.write("")
tab_projects, tab_demo, tab_skills, tab_background = st.tabs(
    ["Projects", "Live demo: data pipeline", "Skills", "Background"]
)

# ---- Projects --------------------------------------------------------------
with tab_projects:
    areas = ["All"] + sorted({p["area"] for p in PROJECTS})
    area = st.radio("Filter by area", areas, horizontal=True, label_visibility="collapsed")
    for p in PROJECTS:
        if area != "All" and p["area"] != area:
            continue
        with st.container(border=True):
            head, links = st.columns([4, 1])
            head.subheader(p["title"])
            head.caption(p["subtitle"])
            for label, url in p["links"]:
                links.link_button(label, url, width="stretch")
            st.markdown(f"<p class='project-tools'>{' · '.join(p['tools'])}</p>", unsafe_allow_html=True)
            cols = st.columns(len(p["metrics"]))
            for col, (label, value) in zip(cols, p["metrics"]):
                col.metric(label, value)
            st.markdown("\n".join(f"- {b}" for b in p["bullets"]))

# ---- Live demo -------------------------------------------------------------
with tab_demo:
    st.subheader("Generate, parse and validate a server inventory")
    st.write(
        "This is a working version of my hostname project. Each hostname encodes the operating system, "
        "environment, country and node number, for example `LPGER042`. Choose the settings, and the app "
        "runs the pipeline and checks the result."
    )
    c1, c2, c3 = st.columns(3)
    n_hosts = c1.slider("Number of servers", 100, 5000, 1500, step=100)
    seed = c2.number_input("Random seed", min_value=0, max_value=9999, value=42, step=1)
    unique = c3.toggle("Enforce unique hostnames", value=True,
                       help="The original notebook did not check this. Turn it off to see duplicates appear.")

    raw = generate_hostnames(n_hosts, int(seed), unique)
    data = parse_hostnames(raw)
    report = validate(data)

    s1, s2, s3 = st.columns(3)
    s1.metric("1 · Generated", f"{len(raw):,} hostnames")
    s2.metric("2 · Parsed", f"{data.shape[1]} columns")
    passed = sum(report["checks"].values())
    s3.metric("3 · Checks passed", f"{passed}/{len(report['checks'])}",
              delta=None if report["duplicates"] == 0 else f"{report['duplicates']} duplicates",
              delta_color="inverse")

    v1, v2 = st.columns([1, 2], gap="large")
    with v1:
        st.markdown("**Data quality checks**")
        for name, ok in report["checks"].items():
            st.markdown(f"{'✅' if ok else '❌'} {name}")
        worst = report["distribution"]["abs_diff_pp"].max()
        st.markdown(
            f"<div class='evidence'>Largest gap between target and observed share: "
            f"<b>{worst:.1f} percentage points</b>.</div>",
            unsafe_allow_html=True,
        )
        st.download_button("Download CSV", data.to_csv(index=False).encode("utf-8"),
                           file_name="hosts.csv", mime="text/csv", width="stretch")
    with v2:
        field = st.segmented_control("Compare target vs observed", ["os", "environment", "country"],
                                     default="environment", format_func=lambda f: {"os": "OS", "environment": "Environment", "country": "Country"}[f])
        field = field or "environment"
        dist = report["distribution"].query("field == @field")
        fig = go.Figure()
        fig.add_bar(x=dist["category"], y=dist["target"] * 100, name="Target", marker_color=MIST)
        fig.add_bar(x=dist["category"], y=dist["observed"] * 100, name="Observed", marker_color=TEAL)
        fig.update_layout(barmode="group", height=330, margin=dict(l=10, r=10, t=10, b=10),
                          yaxis_title="Share of servers (%)", legend=dict(orientation="h", y=1.1),
                          plot_bgcolor="white", font=dict(family="IBM Plex Sans, Arial, sans-serif", color=INK), paper_bgcolor="rgba(0,0,0,0)")
        st.plotly_chart(fig, width="stretch")

    st.markdown("**Hosts by country and environment**")
    pivot = data.groupby(["country", "environment"]).size().reset_index(name="servers")
    fig2 = px.bar(pivot, x="country", y="servers", color="environment", barmode="stack",
                  color_discrete_sequence=[TEAL, AMBER, "#7FA7A3", INK, "#B7C9C6"], height=360)
    fig2.update_layout(margin=dict(l=10, r=10, t=10, b=10), plot_bgcolor="white",
                       font=dict(family="IBM Plex Sans, Arial, sans-serif", color=INK), paper_bgcolor="rgba(0,0,0,0)", xaxis_title="", yaxis_title="Servers")
    st.plotly_chart(fig2, width="stretch")

    with st.expander("Preview the parsed dataset"):
        st.dataframe(data.head(50), width="stretch", hide_index=True)

# ---- Skills ----------------------------------------------------------------
with tab_skills:
    st.subheader("Skills backed by projects")
    st.write("Each filled cell links a skill to a project where I used it, so you can check the evidence.")
    short = ["Restaurant NLP", "Pump It Up", "Hostname pipeline", "Glucose study"]
    skills_list = [s for s, idx in EVIDENCE.items() if idx]
    matrix = [[1 if j in EVIDENCE[s] else 0 for j in range(len(short))] for s in skills_list]
    heat = go.Figure(go.Heatmap(
        z=matrix, x=short, y=skills_list, colorscale=[[0, "#F2F5F4"], [1, TEAL]],
        showscale=False, xgap=3, ygap=3,
        hovertemplate="%{y} in %{x}<extra></extra>",
    ))
    heat.update_layout(height=34 * len(skills_list) + 60, margin=dict(l=10, r=10, t=10, b=10),
                       plot_bgcolor="white", font=dict(family="IBM Plex Sans, Arial, sans-serif", color=INK), paper_bgcolor="rgba(0,0,0,0)",
                       yaxis=dict(autorange="reversed"), xaxis=dict(side="top"))
    st.plotly_chart(heat, width="stretch")

    st.subheader("Full toolkit")
    cols = st.columns(2, gap="large")
    for i, (group, items) in enumerate(SKILLS.items()):
        with cols[i % 2]:
            st.markdown(f"**{group}**")
            st.markdown("".join(f"<span class='chip'>{it}</span>" for it in items), unsafe_allow_html=True)

# ---- Background ------------------------------------------------------------
with tab_background:
    e, x = st.columns(2, gap="large")
    with e:
        st.subheader("Education")
        for degree, school, dates, note in EDUCATION:
            st.markdown(f"**{degree}**  \n{school} · {dates}")
            if note:
                st.caption(note)
    with x:
        st.subheader("Experience")
        for role, org, dates, note in EXPERIENCE:
            st.markdown(f"**{role}**  \n{org} · {dates}")
            st.caption(note)
        st.subheader("Languages")
        for lang, level in PROFILE["languages"]:
            st.markdown(f"**{lang}** — {level}")

st.divider()
st.caption(f"Built with Streamlit, Pandas and Plotly · {PROFILE['email']}")
