#Link to dashboard: https://uc-data-dashboard-szqjxtrzepcvsf6vkuspf5.streamlit.app/

"""
UCLA vs. Berkeley — Admit Rate, Fall 2020-2025
Run with: streamlit run admissions_dashboard.py

Data source: UC Information Center, via the Bay Area modeling table
(school-level admissions data, 2020-2025). Admit rates are computed as
total admits / total applicants per campus per year — not an average
of per-school rates. Scope is Bay Area public high schools only, not
all UC applicants statewide.
"""

import pandas as pd
import plotly.graph_objects as go
import streamlit as st

# ----------------------------------------------------------------------
# Page setup + dark theme
# ----------------------------------------------------------------------
st.set_page_config(
    page_title="UCLA vs. Berkeley — Admit Rate, 2020-2025",
    layout="centered",
)

BG = "#0b0d10"
PANEL = "#14171b"
LINE = "#242830"
INK = "#eceae4"
MUTED = "#8a8f98"
UCLA = "#5fa8dd"
CAL = "#f2b632"
ACCENT = "#e8593f"

st.markdown(
    f"""
    <link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,400;9..144,500;9..144,600&family=IBM+Plex+Mono:wght@400;500;600&display=swap" rel="stylesheet">
    <style>
        .stApp {{
            background-color: {BG};
            color: {INK};
            font-family: 'Fraunces', Georgia, serif;
        }}
        .block-container {{
            max-width: 820px;
            padding-top: 3rem;
            padding-bottom: 4rem;
        }}
        .kicker {{
            font-family: 'IBM Plex Mono', monospace;
            font-size: 11px; letter-spacing: 0.1em;
            color: {MUTED}; margin-bottom: 16px;
        }}
        h1.title {{
            font-family: 'Fraunces', Georgia, serif;
            font-size: clamp(28px, 4.6vw, 40px);
            font-weight: 500; line-height: 1.15;
            margin: 0 0 16px; letter-spacing: -0.01em;
            max-width: 20ch;
        }}
        p.sub {{
            font-family: 'IBM Plex Mono', monospace;
            font-size: 13px; color: {MUTED};
            max-width: 62ch; line-height: 1.7;
        }}
        .question {{
            border: 1px solid {LINE};
            background: {PANEL};
            padding: 22px 24px;
            margin: 28px 0 0;
        }}
        .question .label {{
            font-family: 'IBM Plex Mono', monospace;
            font-size: 10px; letter-spacing: 0.1em;
            color: {ACCENT}; margin-bottom: 10px;
        }}
        .question .q {{
            font-family: 'Fraunces', Georgia, serif;
            font-size: 17px; line-height: 1.5;
            margin: 0 0 18px; max-width: 56ch;
        }}
        .scope {{
            font-family: 'IBM Plex Mono', monospace;
            font-size: 11px; color: {MUTED};
            display: flex; gap: 24px; flex-wrap: wrap;
        }}
        .scope b {{ color: {INK}; font-weight: 600; }}
        .divider {{ height: 1px; background: {LINE}; margin: 3rem 0; }}
        h2.section {{
            font-family: 'Fraunces', Georgia, serif;
            font-size: 19px; font-weight: 500; margin: 0 0 6px;
        }}
        p.note {{
            font-family: 'IBM Plex Mono', monospace;
            font-size: 12px; color: {MUTED};
            max-width: 60ch; line-height: 1.7; margin: 0 0 20px;
        }}
        .stat-pair {{
            display: flex; border-top: 1px solid {LINE};
            border-bottom: 1px solid {LINE}; margin-bottom: 10px;
        }}
        .stat {{ flex: 1; padding: 22px 0; }}
        .stat.right {{ border-left: 1px solid {LINE}; padding-left: 32px; }}
        .stat.left {{ padding-right: 32px; }}
        .stat .who {{
            font-family: 'IBM Plex Mono', monospace;
            font-size: 11px; letter-spacing: 0.06em; color: {MUTED};
            margin-bottom: 8px;
        }}
        .stat .drop {{ font-size: 34px; font-weight: 600; line-height: 1; }}
        .stat.ucla-c .drop {{ color: {UCLA}; }}
        .stat.cal-c .drop {{ color: {CAL}; }}
        .stat .from-to {{
            font-family: 'IBM Plex Mono', monospace;
            font-size: 12px; color: {MUTED}; margin-top: 8px;
        }}
        .callout {{
            font-family: 'IBM Plex Mono', monospace;
            font-size: 12.5px; color: {INK};
            background: {PANEL};
            border-left: 2px solid {ACCENT};
            padding: 14px 18px; max-width: 60ch;
            line-height: 1.7; margin: 20px 0 0;
        }}
        .callout b {{ color: {ACCENT}; }}
        .legend-note {{
            font-family: 'IBM Plex Mono', monospace;
            font-size: 11px; color: {MUTED}; margin-top: -8px;
        }}
        footer {{ visibility: hidden; }}
        .my-footer {{
            margin-top: 3rem;
            font-family: 'IBM Plex Mono', monospace;
            font-size: 10.5px; color: {MUTED};
            border-top: 1px solid {LINE};
            padding-top: 18px; line-height: 1.7;
        }}
    </style>
    """,
    unsafe_allow_html=True,
)

# ----------------------------------------------------------------------
# Data (from bay_area_modeling_table.csv, aggregated: sum then divide)
# ----------------------------------------------------------------------
ucla = pd.DataFrame([
    {"year": 2020, "applicants": 14836, "admits": 1808, "enrollees": 848},
    {"year": 2021, "applicants": 17991, "admits": 1365, "enrollees": 596},
    {"year": 2022, "applicants": 19610, "admits": 1633, "enrollees": 873},
    {"year": 2023, "applicants": 18912, "admits": 1494, "enrollees": 794},
    {"year": 2024, "applicants": 19009, "admits": 1498, "enrollees": 791},
    {"year": 2025, "applicants": 18516, "admits": 1514, "enrollees": 773},
])
cal = pd.DataFrame([
    {"year": 2020, "applicants": 14303, "admits": 2524, "enrollees": 1427},
    {"year": 2021, "applicants": 17296, "admits": 2539, "enrollees": 1497},
    {"year": 2022, "applicants": 19752, "admits": 2440, "enrollees": 1513},
    {"year": 2023, "applicants": 19461, "admits": 2492, "enrollees": 1518},
    {"year": 2024, "applicants": 19485, "admits": 2674, "enrollees": 1670},
    {"year": 2025, "applicants": 19531, "admits": 2248, "enrollees": 1404},
])
for df in (ucla, cal):
    df["admit_rate"] = df.admits / df.applicants * 100
    df["yield_rate"] = df.enrollees / df.admits * 100

# ----------------------------------------------------------------------
# Header
# ----------------------------------------------------------------------
st.markdown('<div class="kicker">UC Information Center · Bay Area public high schools</div>', unsafe_allow_html=True)
st.markdown('<h3 class="title">How has the UC admit rate for Bay Area public high school applicants to UCLA and Berkeley changed from fall 2020 to fall 2025?', unsafe_allow_html=True)
st.markdown(
    '<p class="sub">UCLA and Berkeley admit rates for Bay Area public high school '
    'applicants, fall 2020 through fall 2025 — spanning the shift to test-blind '
    'admissions.</p>',
    unsafe_allow_html=True,
)
st.markdown(
    """
    <div class="question">
        <div class="label">QUESTION</div>
        <p class="q">How has the UC admit rate for Bay Area public high school
        applicants to UCLA and Berkeley changed from fall 2020 to fall 2025,
        across the shift to test-blind admissions?</p>
        <div class="scope">
            <span>Population: <b>Bay Area public high school applicants</b></span>
            <span>Metric: <b>admit rate (admits &divide; applicants)</b></span>
            <span>Window: <b>fall 2020 &ndash; fall 2025</b></span>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# ----------------------------------------------------------------------
# Section 1 — admit rate, six-year change
# ----------------------------------------------------------------------
st.markdown('<h2 class="section">Admit rate, six-year change</h2>', unsafe_allow_html=True)
st.markdown(
    '<p class="note">Both campuses cut their admit rate roughly in half — not '
    'because fewer students got in, but because far more applied.</p>',
    unsafe_allow_html=True,
)

st.markdown(
    f"""
    <div class="stat-pair">
        <div class="stat left ucla-c">
            <div class="who">UCLA</div>
            <div class="drop">12.2% &rarr; 8.2%</div>
            <div class="from-to">2020 admits / applicants &rarr; 2025</div>
        </div>
        <div class="stat right cal-c">
            <div class="who">BERKELEY</div>
            <div class="drop">17.6% &rarr; 11.5%</div>
            <div class="from-to">2020 admits / applicants &rarr; 2025</div>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

fig = go.Figure()
fig.add_trace(go.Scatter(
    x=cal.year, y=cal.admit_rate, mode="lines+markers", name="Berkeley",
    line=dict(color=CAL, width=2.5), marker=dict(size=7, color=CAL),
))
fig.add_trace(go.Scatter(
    x=ucla.year, y=ucla.admit_rate, mode="lines+markers", name="UCLA",
    line=dict(color=UCLA, width=2.5), marker=dict(size=7, color=UCLA),
))
fig.add_vline(x=2021, line_width=1, line_dash="dash", line_color=ACCENT)
fig.add_annotation(
    x=2021, y=1.02, yref="paper", showarrow=False,
    text="fall 2021 — SAT/ACT dropped",
    font=dict(family="IBM Plex Mono", size=11, color=ACCENT),
)
fig.update_layout(
    plot_bgcolor=BG, paper_bgcolor=BG,
    font=dict(family="IBM Plex Mono", size=12, color=MUTED),
    margin=dict(l=10, r=10, t=40, b=10),
    height=340,
    xaxis=dict(showgrid=False, tickmode="linear", dtick=1, color=MUTED),
    yaxis=dict(showgrid=True, gridcolor=LINE, ticksuffix="%", color=MUTED, rangemode="tozero"),
    legend=dict(orientation="h", y=-0.2, font=dict(color=MUTED)),
    hovermode="x unified",
)
st.plotly_chart(fig, use_container_width=True, config={"displayModeBar": False})

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# ----------------------------------------------------------------------
# Section 2 — applicant volume
# ----------------------------------------------------------------------
st.markdown('<h2 class="section">Why: applicant volume outran admits</h2>', unsafe_allow_html=True)
st.markdown(
    '<p class="note">Applicants per campus, fall 2020 vs. fall 2025, '
    'Bay Area public high schools only.</p>',
    unsafe_allow_html=True,
)

col1, col2 = st.columns(2)
with col1:
    fig_a = go.Figure(go.Bar(
        x=[ucla.applicants.iloc[0], ucla.applicants.iloc[-1]],
        y=["2020", "2025"], orientation="h",
        marker_color=UCLA, text=[f"{v:,}" for v in [ucla.applicants.iloc[0], ucla.applicants.iloc[-1]]],
        textposition="outside", textfont=dict(family="IBM Plex Mono", color=MUTED),
    ))
    fig_a.update_layout(
        title=dict(text="UCLA", font=dict(family="IBM Plex Mono", size=12, color=UCLA)),
        plot_bgcolor=BG, paper_bgcolor=BG, height=180,
        margin=dict(l=10, r=60, t=40, b=10),
        xaxis=dict(visible=False), yaxis=dict(color=MUTED, tickfont=dict(family="IBM Plex Mono")),
    )
    st.plotly_chart(fig_a, use_container_width=True, config={"displayModeBar": False})
with col2:
    fig_b = go.Figure(go.Bar(
        x=[cal.applicants.iloc[0], cal.applicants.iloc[-1]],
        y=["2020", "2025"], orientation="h",
        marker_color=CAL, text=[f"{v:,}" for v in [cal.applicants.iloc[0], cal.applicants.iloc[-1]]],
        textposition="outside", textfont=dict(family="IBM Plex Mono", color=MUTED),
    ))
    fig_b.update_layout(
        title=dict(text="Berkeley", font=dict(family="IBM Plex Mono", size=12, color=CAL)),
        plot_bgcolor=BG, paper_bgcolor=BG, height=180,
        margin=dict(l=10, r=60, t=40, b=10),
        xaxis=dict(visible=False), yaxis=dict(color=MUTED, tickfont=dict(family="IBM Plex Mono")),
    )
    st.plotly_chart(fig_b, use_container_width=True, config={"displayModeBar": False})

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# ----------------------------------------------------------------------
# Section 3 — yield rate
# ----------------------------------------------------------------------
st.markdown('<h2 class="section">Yield rate held steady — or rose</h2>', unsafe_allow_html=True)
st.markdown(
    '<p class="note">Of students admitted, the share who enrolled. Unlike '
    'admit rate, yield didn\'t collapse.</p>',
    unsafe_allow_html=True,
)

fig_y = go.Figure()
fig_y.add_trace(go.Bar(x=ucla.year, y=ucla.yield_rate, name="UCLA", marker_color=UCLA))
fig_y.add_trace(go.Bar(x=cal.year, y=cal.yield_rate, name="Berkeley", marker_color=CAL))
fig_y.update_layout(
    barmode="group",
    plot_bgcolor=BG, paper_bgcolor=BG,
    font=dict(family="IBM Plex Mono", size=12, color=MUTED),
    margin=dict(l=10, r=10, t=20, b=10),
    height=300,
    xaxis=dict(showgrid=False, tickmode="linear", dtick=1, color=MUTED),
    yaxis=dict(showgrid=True, gridcolor=LINE, ticksuffix="%", color=MUTED),
    legend=dict(orientation="h", y=-0.2, font=dict(color=MUTED)),
)
st.plotly_chart(fig_y, use_container_width=True, config={"displayModeBar": False})

st.markdown(
    """
    <div class="callout">
        Berkeley's admit rate fell the most in the single year the testing rule
        changed <b>(17.6% &rarr; 14.7%, fall 2021)</b> — but its yield rate kept
        climbing through 2025. Fewer offers went out; the ones that did were taken.
    </div>
    """,
    unsafe_allow_html=True,
)

# ----------------------------------------------------------------------
# Footer
# ----------------------------------------------------------------------
st.markdown(
    """
    <div class="my-footer">
        Source: UC Information Center, via the Bay Area modeling table
        (school-level admissions data, 2020&ndash;2025). Admit rates computed as
        total admits &divide; total applicants per campus per year &mdash; not an
        average of per-school rates. Scope is Bay Area public high schools only,
        not all UC applicants statewide.
    </div>
    """,
    unsafe_allow_html=True,
)

