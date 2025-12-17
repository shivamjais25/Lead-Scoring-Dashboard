import streamlit as st
import pandas as pd

# -----------------------------
# Sample / Dummy Data
# -----------------------------
data = [
    {
        "Name": "Gagan Kapoor",
        "Title": "Data Scientist",
        "Company": "Google",
        "Person_Location": "Gurugram, Haryana, India",
        "Company_HQ": "Mountain View, California",
        "Work_Mode": "Remote",
        "Email": "gagankapoor@gmail.com",
        "LinkedIn": "https://www.linkedin.com/in/gagan-kapoor-5621141a5/"
    },
    {
        "Name": "Kanishk Gupta",
        "Title": "Software Engineer 2",
        "Company": "Microsoft",
        "Person_Location": "West Delhi, Delhi, India",
        "Company_HQ": "WA 98052, USA",
        "Work_Mode": "Remote",
        "Email": "KanishkGupta@gmail.com",
        "LinkedIn": "https://www.linkedin.com/in/kanishkgupta2000/"
    },
    {
        "Name": "Liang Cao",
        "Title": "Senior Software Engineer",
        "Company": "Meta",
        "Person_Location": "Seattle, Washington, United States",
        "Company_HQ": "Menlo Park, California",
        "Work_Mode": "Hybrid",
        "Email": "LiangCao@gmail.com",
        "LinkedIn": "https://www.linkedin.com/in/liang-cao-060727251/"
    },
    {
        "Name": "Jayant Sohane",
        "Title": "Full-Stack Developer",
        "Company": "Tesla",
        "Person_Location": "San Francisco Bay Area",
        "Company_HQ": "Austin, Texas, United States",
        "Work_Mode": "Remote",
        "Email": "JayantSohane@gmail.com",
        "LinkedIn": "https://www.linkedin.com/in/jayant-sohane/"
    },
    {
        "Name": "Snehil Srivastava",
        "Title": "Data Engineer",
        "Company": "Amazon",
        "Person_Location": "Gurugram, Haryana, India",
        "Company_HQ": "Seattle, Washington",
        "Work_Mode": "Remote",
        "Email": "SnehilSrivastava@gmail.com",
        "LinkedIn": "https://www.linkedin.com/in/snehil-srivastava-42315b173/"
    }
]

df = pd.DataFrame(data)

# -----------------------------
# Scoring Weights (Config)
# -----------------------------
WEIGHTS = {
    "senior_role": 30,
    "mid_role": 20,
    "big_tech_company": 30,
    "india_location": 10,
    "us_hub_location": 20,
    "remote": 20,
    "hybrid": 10
}

BIG_TECH = ["google", "microsoft", "meta", "amazon", "tesla"]
US_HUBS = ["bay area", "san francisco", "seattle", "austin"]

# -----------------------------
# Scoring Function
# -----------------------------
def calculate_score(row):
    score = 0

    title = row["Title"].lower()
    location = row["Person_Location"].lower()
    company = row["Company"].lower()
    work_mode = row["Work_Mode"].lower()

    # Role seniority
    if "senior" in title:
        score += WEIGHTS["senior_role"]
    elif any(x in title for x in ["engineer", "scientist", "developer"]):
        score += WEIGHTS["mid_role"]

    # Company strength
    if company in BIG_TECH:
        score += WEIGHTS["big_tech_company"]

    # Location scoring
    if any(hub in location for hub in US_HUBS):
        score += WEIGHTS["us_hub_location"]
    elif "india" in location:
        score += WEIGHTS["india_location"]

    # Work mode
    if work_mode == "remote":
        score += WEIGHTS["remote"]
    elif work_mode == "hybrid":
        score += WEIGHTS["hybrid"]

    return min(score, 100)


# Apply scoring
df["Probability_Score"] = df.apply(calculate_score, axis=1)

# Rank
df = df.sort_values(by="Probability_Score", ascending=False)
df.insert(0, "Rank", range(1, len(df) + 1))

# -----------------------------
# Streamlit UI
# -----------------------------
st.set_page_config(page_title="Lead Ranking & Scoring Dashboard", layout="wide")

st.title("📊 Tech Professional Lead Ranking & Scoring Dashboard")
st.write(
    "This mini-dashboard demonstrates how professional leads can be identified, enriched, and ranked using transparent, configurable business criteria such as role seniority, company tier, location, and work mode."
)

# Search Filter
search_term = st.text_input("Search by Name, Location, Company, or Title")

if search_term:
    filtered_df = df[df.apply(lambda row: search_term.lower() in row.astype(str).str.lower().to_string(), axis=1)]
else:
    filtered_df = df

# Display Table
st.dataframe(filtered_df, use_container_width=True)

# Download Button
csv = filtered_df.to_csv(index=False).encode('utf-8')
st.download_button(
    label="Download CSV",
    data=csv,
    file_name="lead_scoring_results.csv",
    mime="text/csv"
)

st.caption("Demo built using Python + Streamlit with dummy data and transparent scoring logic.")
