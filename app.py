import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# Color 
with open("cm.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


plt.rcParams.update({
    'figure.facecolor': '#ffffff',
    'axes.facecolor': '#ffffff',
    'axes.edgecolor': '#c5d5e8',
    'axes.labelcolor': '#1a3a6e',
    'xtick.color': '#4a6fa5',
    'ytick.color': '#4a6fa5',
    'text.color': '#2c3e50',
    'grid.color': '#e8f0fa',
    'grid.linestyle': '--',
    'grid.alpha': 0.6,
    'axes.prop_cycle': plt.cycler(color=[
        '#1f5fa6', '#2e86de', '#54a0ff',
        '#a8c8f0', '#1a3a6e', '#c5d5e8'
    ])
})

# =========================
# CONFIG
# =========================
st.set_page_config(
    page_title="COVID & Happiness Dashboard",
    layout="wide"
)

st.title("🌍 COVID-19 & Happiness Analysis Dashboard")


# =========================
# LOAD DATA
# =========================
@st.cache_data
def load_data():
    df = pd.read_csv("data/merged_data.csv")
    df.columns = df.columns.str.strip()

    if "Total Cases" not in df.columns:
        df["Total Cases"] = df.iloc[:, -1]

    df["log_cases"] = np.log1p(df["Total Cases"])
    return df

@st.cache_data
def load_corr():
    return pd.read_csv("data/data_merge.csv", index_col=0)

merged_data = load_data()
data_merge = load_corr()

data_merge_numeric = data_merge.reset_index()

# =========================
# SAFETY CHECK
# =========================
if "Total Cases" not in merged_data.columns:
    st.error("Missing column: Total Cases")
    st.stop()

# =========================
# ROW 1
# =========================
st.subheader("📊 Row 1")

col1, col2, col3 = st.columns(3)

with col1:
    top_happy = merged_data.sort_values("Ladder score", ascending=False).head(10)

    fig, ax = plt.subplots(figsize=(3, 2))
    sns.barplot(
        x=top_happy["Ladder score"],
        y=top_happy["Country name"],
        ax=ax
    )
    ax.set_title("Happiest", fontsize=9)
    st.pyplot(fig)

with col2:
    fig, ax = plt.subplots(figsize=(3, 2))
    sns.histplot(merged_data["Total Cases"], ax=ax)
    ax.set_title("COVID distribution", fontsize=9)
    st.pyplot(fig)

with col3:
    st.subheader("🗓 Top 10 COVID Countries")
    top8 = pd.DataFrame({
        "Country": [
            "US", "India", "France", "Germany", "Brazil",
            "Japan", "South Korea", "Italy"
        ],
        "Total Cases": [
            103802702, 44690738, 39866718, 38249060, 37076053,
            33320438, 30615522, 25603510
        ]
    })
    st.dataframe(
        top8.style.format({"Total Cases": "{:,}"}),
        use_container_width=True,
        height=315,
        column_config={
            "Country": st.column_config.TextColumn(width="small"),
            "Total Cases": st.column_config.NumberColumn(width="small"),
        }
    )

# =========================
# ROW 2
# =========================
st.subheader("📊 Row 2")

col1, col2, col3 = st.columns(3)

with col1:
    fig, ax = plt.subplots(figsize=(3, 2))
    sns.scatterplot(
        data=merged_data,
        x="Logged GDP per capita",
        y="Ladder score",
        ax=ax
    )
    ax.set_title("GDP vs Happiness", fontsize=9)
    st.pyplot(fig)

with col2:
    fig, ax = plt.subplots(figsize=(3, 2))
    sns.scatterplot(
        data=merged_data,
        x="Social support",
        y="Ladder score",
        ax=ax
    )
    ax.set_title("Social support", fontsize=9)
    st.pyplot(fig)

with col3:
    fig, ax = plt.subplots(figsize=(3, 2))
    sns.scatterplot(
        data=merged_data,
        x="Healthy life expectancy",
        y="Ladder score",
        ax=ax
    )
    ax.set_title("Life expectancy", fontsize=9)
    st.pyplot(fig)


# =========================
# ROW 3 (CORRELATION + EXTRA)
# =========================
st.subheader("📊 Row 3")

col1, col2, col3 = st.columns(3)

with col1:
    corr = data_merge_numeric.corr(numeric_only=True)

    fig, ax = plt.subplots(figsize=(3, 2))
    sns.heatmap(
        corr,
        cmap="coolwarm",
        annot=False,   # IMPORTANT: keep small
        ax=ax
    )
    ax.set_title("Correlation", fontsize=9)
    st.pyplot(fig)

with col2:
    fig, ax = plt.subplots(figsize=(3, 2))
    sns.scatterplot(
        data=merged_data,
        x="Ladder score",
        y="log_cases",
        ax=ax
    )
    ax.set_title("Happiness vs COVID", fontsize=9)
    st.pyplot(fig)

with col3:
    st.markdown("### 🧠 Insights")

    st.markdown("""
    - Le PIB par habitant est fortement corrélé au bonheur
    - Le soutien social améliore significativement le bien-être  
    - Les cas de COVID-19 sont plus élevés dans les pays développés
    - Les modèles de régression ont une performance limitée pour expliquer le bonheur.
    """)