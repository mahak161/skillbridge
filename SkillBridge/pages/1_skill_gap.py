import streamlit as st

st.set_page_config(
    page_title="Skill Gap Detector",
    page_icon="📈",
    layout="wide"
)

# =========================
# CSS
# =========================
st.markdown("""
<style>

/* Background */
.stApp{
    background: linear-gradient(135deg,#F8FAFC,#EEF2FF);
}

/* Hide Streamlit */
header{visibility:hidden;}
footer{visibility:hidden;}
#MainMenu{visibility:hidden;}

/* Sidebar */
[data-testid="stSidebar"]{
    background:#0F172A;
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

[data-testid="stSidebarNav"] a:hover{
    background:#2563EB;
}

/* Headings */
.main-title{
    text-align:center;
    font-size:60px;
    font-weight:900;
    color:#0F172A !important;
    animation:titlePop 1s ease-out,
              floatTitle 3s ease-in-out infinite;
}

}

.sub-title{
    text-align:center;
    color:#334155;
    font-size:22px;
    font-weight:600;
}

/* Labels */
label{
    color:#0F172A !important;
    font-weight:700 !important;
}

/* Selectboxes */
div[data-baseweb="select"]{
    background:white !important;
    border-radius:16px !important;
}

/* Text input */
.stTextInput input{
    background:white !important;
    color:#0F172A !important;
    border-radius:16px !important;
    border:2px solid #CBD5E1 !important;
}

/* Selected skill tags */
[data-baseweb="tag"]{
    background:#2563EB !important;
    color:white !important;
    border-radius:12px !important;
}

/* Button */
.stButton button{
    background:linear-gradient(90deg,#2563EB,#06B6D4);
    color:white;
    border:none;
    border-radius:15px;
    font-weight:700;
    height:55px;
}

/* Cards */
.card{
    background:white;
    border-radius:20px;
    padding:25px;
    box-shadow:0px 8px 25px rgba(0,0,0,0.08);
}

.score-box{
    background:linear-gradient(90deg,#2563EB,#06B6D4);
    color:white;
    border-radius:20px;
    padding:25px;
    text-align:center;
    font-size:30px;
    font-weight:800;
    animation:scorePop 0.8s ease-out;
}

@keyframes scorePop{

    0%{
        opacity:0;
        transform:scale(0.7);
    }

    70%{
        transform:scale(1.08);
    }

    100%{
        opacity:1;
        transform:scale(1);
    }

}

@keyframes floatTitle{

    0%{
        transform:translateY(0px);
    }

    50%{
        transform:translateY(-6px);
    }

    100%{
        transform:translateY(0px);
    }

}

.required-heading{
    color:#38BDF8 !important;
    font-size:32px;
    font-weight:800;
    margin-bottom:15px;
}

.skill-box{
    background:#2563EB;
    color:white;
    padding:10px 15px;
    border-radius:12px;
    margin-bottom:6px;
    min-height:auto;
}

.skill-box:hover{
    transform:translateY(-4px);
    box-shadow:0 8px 20px rgba(37,99,235,0.25);
}

</style>
""", unsafe_allow_html=True)



# =========================
# HEADER
# =========================

st.markdown("""
<h1 class="main-title">📈 Skill Gap Detector</h1>
<p class="sub-title">
Identify missing skills and measure career readiness
</p>
""", unsafe_allow_html=True)

# =========================
# REQUIRED SKILLS
# =========================

required_skills = {

    "Data Scientist":[
        "Python",
        "Pandas",
        "SQL",
        "Statistics",
        "Machine Learning",
        "Git"
    ],

    "Data Analyst":[
        "Python",
        "SQL",
        "Power BI",
        "Tableau",
        "Statistics"
    ],

    "Full Stack Developer":[
        "JavaScript",
        "React",
        "Git",
        "SQL",
        "Docker"
    ],

    "Backend Developer":[
        "Python",
        "SQL",
        "Git",
        "Docker",
        "AWS"
    ],

    "Frontend Developer":[
        "JavaScript",
        "React",
        "Git",
        "HTML",
        "CSS"
    ],

    "DevOps Engineer":[
        "Docker",
        "Kubernetes",
        "AWS",
        "Git",
        "Linux"
    ],

    "Cloud Engineer":[
        "AWS",
        "Azure",
        "GCP",
        "Linux",
        "Docker"
    ],

    "AI Engineer":[
        "Python",
        "Machine Learning",
        "Deep Learning",
        "Git",
        "SQL"
    ]
}

# =========================
# INPUT SECTION
# =========================

col1, col2 = st.columns(2)

with col1:

    target_role = st.selectbox(
        "🎯 Target Career",
        [
            "Data Scientist",
            "Data Analyst",
            "Full Stack Developer",
            "Backend Developer",
            "Frontend Developer",
            "DevOps Engineer",
            "Cloud Engineer",
            "AI Engineer"
        ]
    )

with col2:

    skills = st.multiselect(
        "💻 Your Current Skills",
        [
            "Python",
            "Pandas",
            "NumPy",
            "SQL",
            "Statistics",
            "Machine Learning",
            "Deep Learning",
            "Git",
            "Docker",
            "AWS",
            "Power BI",
            "Tableau",
            "JavaScript",
            "React"
        ]
    )

# =========================
# BUTTON
# =========================

if st.button("Analyze Skill Gap"):

    needed = required_skills.get(
        target_role,
        []
    )

    matched = []
    missing = []

    for skill in needed:

        if skill in skills:
            matched.append(skill)
        else:
            missing.append(skill)

    if len(needed) > 0:
        readiness = int(
        (len(matched) / len(needed)) * 100
    )
    else:
        readiness = 0
    st.markdown("<br>", unsafe_allow_html=True)

    c1,c2 = st.columns([2,1])

    with c1:

        st.markdown("""
<h2 class='required-heading'>
📋 Required Skills
</h2>
""", unsafe_allow_html=True)

        for s in needed:

            if s in skills:
                display_skill = f"✅ {s}"
            else:
                display_skill = s

            st.markdown(
                f"""
                <div class='skill-box'>
                {display_skill}
                </div>
                """,
                unsafe_allow_html=True
            )
    with c2:

        st.markdown("<div style='margin-top:55px;'></div>", unsafe_allow_html=True)

        st.markdown(
            f"""
            <div class='score-box'>
            Readiness Score<br><br>
            {readiness}%
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown("<br>", unsafe_allow_html=True)

    st.info(
    """
✅ = You already have this skill

💡 Learn All Required skills to increase your readiness score and become job-ready for your target career.
"""
)