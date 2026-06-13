import streamlit as st
import pandas as pd
import plotly.express as px

# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(
    page_title="Market Intelligence Dashboard",
    page_icon="📊",
    layout="wide"
)

# ==========================================
# CUSTOM CSS
# ==========================================

st.markdown("""
<style>

/* ======================
BACKGROUND
====================== */

.stApp{
    background:linear-gradient(
    135deg,
    #F8FAFC,
    #E0F2FE,
    #DBEAFE
    );
}

/* ======================
HIDE STREAMLIT
====================== */

header{
    visibility:hidden;
}

footer{
    visibility:hidden;
}

#MainMenu{
    visibility:hidden;
}

/* ======================
SIDEBAR
====================== */

[data-testid="stSidebar"]{
    background:#071330;
}

[data-testid="stSidebar"] *{
    color:white;
}

[data-testid="stSidebarNav"] a{
    background:#1E293B;
    border-radius:18px;
    margin:10px;
    padding:14px;
    font-weight:700;
    border:1px solid #334155;
}

/* ======================
MAIN TITLE
====================== */

.main-title{
    text-align:center;
    font-size:58px;
    font-weight:900;
    color:#38BDF8 !important;
    opacity:1 !important;
}

.sub-title{
    text-align:center;
    font-size:20px;
    color:#334155;
    margin-bottom:40px;
}

/* ======================
SECTION TITLES
====================== */

.section-title{
    color:#38BDF8;
    font-size:38px;
    font-weight:900;
    margin-top:10px;
    margin-bottom:15px;
}

/* ======================
LABELS
====================== */

label{
    color:#0F172A !important;
    font-size:18px !important;
    font-weight:700 !important;
}

/* ======================
SELECTBOX
====================== */

div[data-baseweb="select"]{
    background:white !important;
    border-radius:16px !important;
    border:2px solid #BAE6FD !important;
}

/* ======================
BUTTON
====================== */

.stButton button{

    width:100%;
    height:58px;

    background:linear-gradient(
    90deg,
    #2563EB,
    #38BDF8
    );

    color:white;
    border:none;

    border-radius:16px;

    font-size:19px;
    font-weight:800;
}

/* ======================
METRIC CARDS
====================== */

.metric-card{

    background:white;

    border-radius:22px;

    padding:28px;

    text-align:center;

    box-shadow:
    0px 8px 25px rgba(0,0,0,0.08);

    border:1px solid #E2E8F0;
}

.metric-title{
    color:#64748B;
    font-size:18px;
    font-weight:700;
}

.metric-value{
    color:#2563EB;
    font-size:40px;
    font-weight:900;
    margin-top:10px;
}

/* ======================
CHART BOX
====================== */

.chart-box{

    background:white;

    padding:20px;

    border-radius:20px;

    margin-top:20px;

    box-shadow:
    0px 8px 25px rgba(0,0,0,0.08);
}

/* ======================
FUTURE BOX
====================== */

.future-box{

    background:linear-gradient(
    90deg,
    #2563EB,
    #38BDF8
    );

    color:white;

    border-radius:18px;

    padding:18px;

    margin-top:20px;

    font-size:17px;

    font-weight:600;

    line-height:1.6;

    box-shadow:
    0px 8px 25px rgba(37,99,235,0.25);
}

.future-title{
    font-size:24px;
    font-weight:800;
    margin-bottom:10px;
}

.future-text{
    color:white !important;
    font-size:18px;
    line-height:1.7;
}

/* ======================
REMOVE WHITE TEXT ISSUE
====================== */

.js-plotly-plot .plotly .gtitle{
    fill:#38BDF8 !important;
}

.js-plotly-plot .plotly text{
    fill:#0F172A !important;
}

</style>
""", unsafe_allow_html=True)

# ==========================================
# HEADER
# ==========================================

st.markdown("""
<h1 class="main-title">
📊 Market Intelligence Dashboard
</h1>
""", unsafe_allow_html=True)

st.markdown("""
<p class='sub-title'>
Analyze market demand, salary trends, hiring growth and future opportunities
</p>
""", unsafe_allow_html=True)

# ==========================================
# MARKET DATA
# ==========================================

market_data = {

    "Python":{
        "demand":92,
        "growth":[45,58,66,79,92],
        "salary":[4,6,8,11,15],
        "future":"Python will continue dominating AI, automation, backend development and data science careers."
    },

    "SQL":{
        "demand":85,
        "growth":[40,52,61,74,85],
        "salary":[3,5,7,9,12],
        "future":"SQL remains one of the most important skills for data analytics and database management."
    },

    "Power BI":{
        "demand":72,
        "growth":[25,35,49,61,72],
        "salary":[3,5,6,8,10],
        "future":"Power BI professionals are highly demanded in business intelligence and analytics."
    },

    "Machine Learning":{
        "demand":88,
        "growth":[35,48,60,76,88],
        "salary":[6,9,13,18,24],
        "future":"Machine Learning jobs are rapidly increasing because of AI adoption."
    },

    "Data Science":{
        "demand":90,
        "growth":[40,54,69,81,90],
        "salary":[6,9,13,18,25],
        "future":"Data Science careers are growing across healthcare, finance and AI industries."
    },

    "React":{
        "demand":81,
        "growth":[30,44,57,70,81],
        "salary":[4,6,9,12,16],
        "future":"React continues to dominate frontend development and startup hiring."
    },

    "AWS":{
        "demand":86,
        "growth":[38,50,63,74,86],
        "salary":[5,8,11,15,20],
        "future":"AWS and cloud computing skills remain among the highest-paying tech skills."
    },

    "Cyber Security":{
        "demand":83,
        "growth":[28,40,55,69,83],
        "salary":[5,8,12,16,21],
        "future":"Cyber security demand is increasing because companies need stronger digital protection."
    },

    "AI Engineering":{
        "demand":93,
        "growth":[45,59,73,84,93],
        "salary":[8,12,17,24,32],
        "future":"AI Engineering is expected to become one of the highest-paying careers globally."
    },

    "Java":{
        "demand":80,
        "growth":[30,44,55,67,80],
        "salary":[4,6,8,11,15],
        "future":"Java remains strong in enterprise software and Android development."
    },

    "C++":{
        "demand":68,
        "growth":[20,30,42,56,68],
        "salary":[4,6,9,12,16],
        "future":"C++ is still important in gaming, systems programming and competitive coding."
    },

    "UI/UX Design":{
        "demand":70,
        "growth":[24,35,46,59,70],
        "salary":[3,5,7,10,13],
        "future":"UI/UX design is becoming essential for modern digital products."
    },

    "Blockchain":{
        "demand":67,
        "growth":[18,28,40,54,67],
        "salary":[7,10,15,20,28],
        "future":"Blockchain development is growing in fintech and Web3 applications."
    },

    "DevOps":{
        "demand":82,
        "growth":[30,42,56,69,82],
        "salary":[5,8,12,16,21],
        "future":"DevOps engineers are highly demanded for cloud deployment pipelines."
    },

    "Cloud Computing":{
        "demand":89,
        "growth":[38,50,65,78,89],
        "salary":[6,9,13,18,24],
        "future":"Cloud computing skills are becoming mandatory in enterprise technology."
    },

    "Docker":{
        "demand":76,
        "growth":[25,36,50,64,76],
        "salary":[4,7,10,13,18],
        "future":"Docker is essential for containerization and DevOps."
    },

    "Kubernetes":{
        "demand":79,
        "growth":[22,34,49,63,79],
        "salary":[6,9,12,17,22],
        "future":"Kubernetes demand is increasing with cloud-native applications."
    },

    "Android Development":{
        "demand":75,
        "growth":[28,40,52,64,75],
        "salary":[4,6,8,11,15],
        "future":"Android developers continue to be highly demanded in app industries."
    },

    "Data Analytics":{
        "demand":84,
        "growth":[36,48,61,73,84],
        "salary":[4,6,8,11,14],
        "future":"Data analytics remains one of the safest and fastest-growing careers."
    },

    "Deep Learning":{
        "demand":82,
        "growth":[24,38,52,67,82],
        "salary":[7,10,14,20,28],
        "future":"Deep Learning is becoming critical in advanced AI systems."
    }
}

# ==========================================
# SKILL ANALYSIS
# ==========================================

st.markdown("""
<div class='section-title'>
 Skill Analysis
</div>
""", unsafe_allow_html=True)

skill = st.selectbox(
    "Select one skill you are good at",
    list(market_data.keys())
)

# ==========================================
# BUTTON
# ==========================================

if st.button("🚀 Generate Market Analysis"):

    # Selected skill data
    data = market_data[skill]

    # ==========================================
    # METRIC CARDS
    # ==========================================

    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-title">Current Demand</div>
            <div class="metric-value">{data['demand']}%</div>
        </div>
        """, unsafe_allow_html=True)

    with c2:

        growth_percent = data["growth"][-1] - data["growth"][0]

        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-title">Previous Growth</div>
            <div class="metric-value">+{growth_percent}%</div>
        </div>
        """, unsafe_allow_html=True)

    with c3:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-title">Expected Salary</div>
            <div class="metric-value">₹{data['salary'][-1]} LPA</div>
        </div>
        """, unsafe_allow_html=True)
    # ==========================================
    # DEMAND GROWTH
    # ==========================================

    st.markdown("""
    <div class='section-title'>
    📈 Skill Demand Growth
    </div>
    """, unsafe_allow_html=True)

    growth_df = pd.DataFrame({
        "Year":[2021,2022,2023,2024,2025],
        "Demand":data["growth"]
    })

    fig1 = px.bar(
        growth_df,
        x="Year",
        y="Demand",
        text="Demand",
        title=f"{skill} Market Demand Growth"
    )

    fig1.update_layout(
        plot_bgcolor="white",
        paper_bgcolor="white",
        font_color="#0F172A",
        title_font_color="#38BDF8",
        title_font_size=26
    )

    fig1.update_traces(
        marker_color="#38BDF8",
        textposition="outside"
    )

    st.plotly_chart(
        fig1,
        use_container_width=True
    )

    # ==========================================
    # SALARY GROWTH
    # ==========================================

    st.markdown("""
    <div class='section-title'>
    💰 Salary Growth By Experience
    </div>
    """, unsafe_allow_html=True)

    salary_df = pd.DataFrame({

        "Experience":[
            "0-1 Years",
            "1-3 Years",
            "3-5 Years",
            "5-8 Years",
            "8+ Years"
        ],

        "Salary":data["salary"]
    })

    fig2 = px.line(
        salary_df,
        x="Experience",
        y="Salary",
        markers=True,
        title=f"{skill} Salary Trend"
    )

    fig2.update_layout(
        plot_bgcolor="white",
        paper_bgcolor="white",
        font_color="#0F172A",
        title_font_color="#38BDF8",
        title_font_size=26
    )

    fig2.update_traces(
        line_color="#2563EB",
        marker=dict(size=12)
    )

    st.plotly_chart(
        fig2,
        use_container_width=True
    )

    # ==========================================
    # HIRING DISTRIBUTION
    # ==========================================

    st.markdown("""
    <div class='section-title'>
    🌍 Hiring Distribution
    </div>
    """, unsafe_allow_html=True)

    hiring_df = pd.DataFrame({

        "Industry":[
            "IT Services",
            "Finance",
            "Healthcare",
            "E-Commerce",
            "Startups"
        ],

        "Hiring":[45,20,12,13,10]
    })

    fig3 = px.pie(
        hiring_df,
        names="Industry",
        values="Hiring",
        title=f"{skill} Industry Hiring Distribution"
    )

    fig3.update_layout(
        paper_bgcolor="white",
        font_color="#0F172A",
        title_font_color="#38BDF8",
        title_font_size=26
    )

    st.plotly_chart(
        fig3,
        use_container_width=True
    )

    

    
    # ==========================================
    # FUTURE TRENDS
    # ==========================================
    st.markdown(
f"""
<div class="future-box">

<div class="future-title">
🔮 Future Trends
</div>

<div class="future-text">
{data['future']}
</div>

</div>
""",
unsafe_allow_html=True
)