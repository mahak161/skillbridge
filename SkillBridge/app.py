import streamlit as st
import joblib
import numpy as np


# Load trained files
model = joblib.load("models/career_predictor.pkl")
encoder = joblib.load("models/label_encoder.pkl")
vectorizer = joblib.load("models/vectorizer.pkl")

st.set_page_config(
    page_title="SkillBridge ",
    page_icon="🚀",
    layout="wide"
)

st.markdown("""
<style>

/* =======================
   BACKGROUND
======================= */

.stApp{
    background: linear-gradient(
    135deg,
    #F8FAFC,
    #EEF2FF
    );
}

/* Hide Streamlit */
header{visibility:hidden;}
footer{visibility:hidden;}
#MainMenu{visibility:hidden;}

/* =======================
   SIDEBAR
======================= */

[data-testid="stSidebar"]{
    background:#0F172A;
}

[data-testid="stSidebar"] *{
    color:white;
}

/* Navigation Buttons */

[data-testid="stSidebarNav"] a{
    background:#1E293B;
    border-radius:18px;
    margin:10px;
    padding:14px;
    font-weight:700;
    transition:all .3s ease;
    border:1px solid #334155;
}

[data-testid="stSidebarNav"] a:hover{
    background:#2563EB;
    transform:translateX(6px);
}

/* =======================
   TITLE
======================= */

.main-title{
    text-align:center;
    font-size:70px;
    font-weight:900;

    background:linear-gradient(
    90deg,
    #2563EB,
    #06B6D4
    );

    -webkit-background-clip:text;
    -webkit-text-fill-color:transparent;

    animation:titlePop 1s ease;
}

.sub-title{
    text-align:center;
    color:#334155;
    font-size:24px;
    font-weight:600;
}

/* =======================
   BANNER
======================= */

.banner{
    background:linear-gradient(
    90deg,
    #2563EB,
    #14B8A6
    );
    color:white;
    padding:18px;
    border-radius:18px;
    text-align:center;
    font-size:18px;
    font-weight:700;
    margin-bottom:30px;

    animation:slideDown 0.8s ease;
}

/* =======================
   LABELS
======================= */

label{
    color:#0F172A !important;
    font-size:17px !important;
    font-weight:700 !important;
}

/* =======================
   ALL INPUT BOXES
======================= */

/* Selectbox */

div[data-baseweb="select"]{
    background:#1E293B !important;
    color:white !important;
    border-radius:16px !important;
    border:2px solid #334155 !important;
    transition:all 0.3s ease;
}

/* Text input */

.stTextInput input{
    background:#1E293B !important;
    color:white !important;
    border:2px solid #334155 !important;
    border-radius:16px !important;
    transition:all 0.3s ease;
}

.stTextInput input:hover{
    transform:translateY(-2px);
    box-shadow:0 0 15px rgba(37,99,235,0.4);
}

div[data-baseweb="select"]:hover{
    transform:translateY(-2px);
    box-shadow:0 0 15px rgba(37,99,235,0.4);
}

/* Multiselect */

[data-baseweb="tag"]{
    background:#2563EB !important;
    color:white !important;
    border-radius:12px !important;
}

/* =======================
   BUTTON
======================= */

.stButton button{
    background:linear-gradient(
    90deg,
    #2563EB,
    #14B8A6
    ) !important;

    color:white !important;
    border:none !important;
    border-radius:15px !important;
    height:55px !important;
    font-size:18px !important;
    font-weight:700 !important;

    transition:all .3s ease;
}

.stButton button:hover{
    transform:translateY(-4px);
}

/* =======================
   HEADING
======================= */

.pred-heading{
    text-align:center;
    color:#0F172A;
    font-size:42px;
    font-weight:800;
    margin-top:40px;
    margin-bottom:30px;
}

/* =======================
   CARDS
======================= */

.pred-card{
    background:white;
    border-radius:24px;
    padding:35px;
    min-height:250px;

    text-align:center;

    color:#0F172A;
    font-size:22px;
    font-weight:700;

    box-shadow:
    0px 10px 30px rgba(0,0,0,0.10);

    animation:cardPop .7s ease;
}

.pred-card:hover{
    transform:translateY(-8px);
    transition:.3s;
}

/* =======================
   ANIMATIONS
======================= */

@keyframes cardPop{
    from{
        opacity:0;
        transform:scale(.85);
    }
    to{
        opacity:1;
        transform:scale(1);
    }
}

@keyframes titlePop{
    0%{
        opacity:0;
        transform:translateY(-40px);
    }
    100%{
        opacity:1;
        transform:translateY(0);
    }
}

@keyframes slideDown{
    from{
        opacity:0;
        transform:translateY(-30px);
    }
    to{
        opacity:1;
        transform:translateY(0);
    }
}

</style>
""", unsafe_allow_html=True)

st.markdown("""
<h1 class="main-title">🚀 SkillBridge</h1>
<p class="sub-title">
Discover Your Ideal Tech Career Path
</p>
""", unsafe_allow_html=True)

st.markdown("""
<div class="banner">
🤖 Career Guidance • 📈 Market Trends • 🎯 Career Matching
</div>
""", unsafe_allow_html=True)

# User Inputs
education = st.selectbox(
    "🎓 Education Level",
    [
        "Bachelor of Technology (B.Tech)",
        "Bachelor of Engineering (B.E.)",
        "Bachelor of Computer Applications (BCA)",
        "Bachelor of Science (B.Sc)",
        "Master of Computer Applications (MCA)",
        "Master of Technology (M.Tech)",
        "Master of Engineering (M.E.)",
        "Master of Science (M.Sc)",
        "MBA",
        "Diploma",
        "Professional Degree",
        "Associate Degree",
        "Secondary School",
        "Higher Secondary",
        "Doctorate (PhD)",
        "Other"
    ]
)

experience = st.text_input(
    "Years of Professional Coding Experience",
    "2"
)

languages = st.multiselect(
    "💻 Programming Languages",
    [
        "Python","Java","JavaScript","TypeScript",
        "C","C++","C#","Go","Rust","PHP",
        "Ruby","Kotlin","Swift","SQL","R",
        "Dart","Scala","Perl","MATLAB"
    ]
)

languages_text = " ".join(languages)

tools = st.multiselect(
    "🛠 Tools & Technologies",
    [
        "Git","GitHub","Docker","Kubernetes",
        "AWS","Azure","GCP",
        "Linux","Jenkins","Terraform",
        "Postman","VS Code","IntelliJ",
        "Power BI","Tableau","Figma"
    ]
)

tools_text = " ".join(tools)

if st.button("Predict Career"):

    user_text = (
        education + " " +
        experience + " " +
        languages_text + " " +
        tools_text
    )

    user_vector = vectorizer.transform([user_text])

    # Get prediction probabilities
    probs = model.predict_proba(user_vector)[0]

    # Top 3 careers
    top3_idx = np.argsort(probs)[-3:][::-1]

    top3_careers = encoder.inverse_transform(top3_idx)

    st.markdown("""
<div class="pred-heading">
🎯 Top Career Matches
</div>
""", unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(f"""
        <div class='pred-card'>
        🥇<br><br>
        {top3_careers[0]}<br><br>
        {probs[top3_idx[0]]*100:.1f}%
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div class='pred-card'>
        🥈<br><br>
        {top3_careers[1]}<br><br>
        {probs[top3_idx[1]]*100:.1f}%
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown(f"""
        <div class='pred-card'>
        🥉<br><br>
        {top3_careers[2]}<br><br>
        {probs[top3_idx[2]]*100:.1f}%
        </div>
        """, unsafe_allow_html=True)