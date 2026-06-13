import streamlit as st

st.set_page_config(
    page_title="Career Roadmap",
    page_icon="🗺️",
    layout="wide"
)

# ==========================
# CSS
# ==========================

st.markdown("""
<style>

/* Background */
.stApp{
    background:linear-gradient(135deg,#F8FAFC,#EEF2FF);
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

/* Title */

.main-title{
    text-align:center;
    font-size:58px;
    font-weight:900;
    color:#38BDF8 !important;
    text-shadow:0px 2px 8px rgba(56,189,248,0.3);
    animation:pop 0.8s ease-out;
}

.sub-title{
    text-align:center;
    color:#475569;
    font-size:20px;
    margin-bottom:30px;
}

label{
    color:#0F172A !important;
    font-weight:700 !important;
}

/* Selectbox */

div[data-baseweb="select"]{
    background:white !important;
    border-radius:15px !important;
}

/* Button */

.stButton button{
    background:linear-gradient(
    90deg,
    #2563EB,
    #06B6D4
    );

    color:white;
    border:none;
    border-radius:14px;
    height:55px;
    font-size:18px;
    font-weight:700;
}

/* Section Heading */

.section-heading{
    color:#38BDF8;
    font-size:34px;
    font-weight:900;
    margin-bottom:20px;
    animation:pop 0.8s ease-out;
}

/* Roadmap Card */

.roadmap-card{
    background:white;
    border-radius:18px;
    padding:20px;
    margin-bottom:18px;

    box-shadow:
    0px 6px 20px rgba(0,0,0,0.08);

    animation:slideUp 0.8s ease;
}

.week-title{
    color:#2563EB;
    font-size:24px;
    font-weight:800;
    margin-bottom:10px;
}

.skill-item{
    background:#2563EB;
    color:white;
    padding:10px;
    border-radius:10px;
    margin:5px 0 25px 0;
}



@keyframes pop{

    0%{
        opacity:0;
        transform:scale(0.7);
    }

    100%{
        opacity:1;
        transform:scale(1);
    }
}

@keyframes slideUp{

    from{
        opacity:0;
        transform:translateY(30px);
    }

    to{
        opacity:1;
        transform:translateY(0px);
    }
}

</style>
""", unsafe_allow_html=True)

# ==========================
# HEADER
# ==========================

st.markdown("""
<h1 class='main-title'>
🗺️ Personalized Learning Roadmap
</h1>

<p class='sub-title'>
Get a custom 60-Day learning plan for your dream career
</p>
""", unsafe_allow_html=True)

# ==========================
# ROADMAP DATA
# ==========================

roadmaps = {

    "Data Scientist":{
       
        "weeks":[
            ["Python Basics","Functions","Pandas"],
            ["Statistics","Probability"],
            ["SQL Basics"],
            ["Data Cleaning"],
            ["Data Visualization"],
            ["Machine Learning"],
            ["Model Building"],
            ["Portfolio Project"]
        ]
    },

    "Data Analyst":{
       
        "weeks":[
            ["Excel"],
            ["Python Basics"],
            ["SQL"],
            ["Data Cleaning"],
            ["Power BI"],
            ["Tableau"],
            ["Dashboard Building"],
            ["Analytics Project"]
        ]
    },

    "AI Engineer":{
        
        "weeks":[
            ["Python"],
            ["Statistics"],
            ["Machine Learning"],
            ["Deep Learning"],
            ["Neural Networks"],
            ["NLP"],
            ["LLMs"],
            ["AI Project"]
        ]
    },

    "Machine Learning Engineer":{
        
        "weeks":[
            ["Python"],
            ["Statistics"],
            ["Machine Learning"],
            ["Scikit Learn"],
            ["Model Evaluation"],
            ["Deep Learning"],
            ["Deployment"],
            ["ML Project"]
        ]
    },

    "Backend Developer":{
        
        "weeks":[
            ["Python"],
            ["OOP"],
            ["SQL"],
            ["Flask"],
            ["FastAPI"],
            ["Docker"],
            ["AWS"],
            ["Backend Project"]
        ]
    },

    "Frontend Developer":{
       
        "weeks":[
            ["HTML"],
            ["CSS"],
            ["JavaScript"],
            ["Responsive Design"],
            ["React"],
            ["API Integration"],
            ["Portfolio Website"],
            ["Frontend Project"]
        ]
    },

    "Full Stack Developer":{
        
        "weeks":[
            ["HTML & CSS"],
            ["JavaScript"],
            ["React"],
            ["Backend Development"],
            ["Databases"],
            ["APIs"],
            ["Deployment"],
            ["Full Stack Project"]
        ]
    },

    "DevOps Engineer":{
        
        "weeks":[
            ["Linux"],
            ["Git"],
            ["Docker"],
            ["Kubernetes"],
            ["AWS"],
            ["CI/CD"],
            ["Monitoring"],
            ["DevOps Project"]
        ]
    },

    "Cloud Engineer":{
        
        "weeks":[
            ["Cloud Fundamentals"],
            ["AWS"],
            ["Azure"],
            ["Linux"],
            ["Docker"],
            ["Networking"],
            ["Deployment"],
            ["Cloud Project"]
        ]
    },

    "Cyber Security Analyst":{
        
        "weeks":[
            ["Networking"],
            ["Linux Security"],
            ["Cyber Security Basics"],
            ["Ethical Hacking Concepts"],
            ["Vulnerability Assessment"],
            ["Security Tools"],
            ["Incident Response"],
            ["Security Project"]
        ]
    },

    "Software Engineer":{
       
        "weeks":[
            ["Programming Basics"],
            ["OOP"],
            ["Data Structures"],
            ["Algorithms"],
            ["Git"],
            ["System Design"],
            ["Projects"],
            ["Interview Prep"]
        ]
    },

    "Android Developer":{
        
        "weeks":[
            ["Java/Kotlin"],
            ["Android Studio"],
            ["Layouts"],
            ["APIs"],
            ["Firebase"],
            ["State Management"],
            ["Testing"],
            ["Android App"]
        ]
    },

    "Web Developer":{
        
        "weeks":[
            ["HTML"],
            ["CSS"],
            ["JavaScript"],
            ["Bootstrap"],
            ["React Basics"],
            ["Projects"],
            ["Portfolio"],
            ["Website Deployment"]
        ]
    },

    "UI/UX Designer":{
        
        "weeks":[
            ["Design Principles"],
            ["Color Theory"],
            ["Typography"],
            ["Figma"],
            ["Wireframes"],
            ["Prototypes"],
            ["User Research"],
            ["UI/UX Project"]
        ]
    },

    "Business Analyst":{
        
        "weeks":[
            ["Excel"],
            ["SQL"],
            ["Business Analytics"],
            ["Power BI"],
            ["Requirements Gathering"],
            ["Data Visualization"],
            ["Case Studies"],
            ["BA Project"]
        ]
    },

    "Database Administrator":{
        
        "weeks":[
            ["SQL"],
            ["Database Design"],
            ["Normalization"],
            ["Optimization"],
            ["Backup & Recovery"],
            ["Security"],
            ["Administration"],
            ["Database Project"]
        ]
    },

    "Data Engineer":{
        
        "weeks":[
            ["Python"],
            ["SQL"],
            ["ETL"],
            ["Data Warehousing"],
            ["Apache Spark"],
            ["Pipelines"],
            ["Cloud Data Tools"],
            ["Data Project"]
        ]
    },

    "Product Manager":{
       
        "weeks":[
            ["Product Fundamentals"],
            ["Market Research"],
            ["User Stories"],
            ["Agile"],
            ["Roadmapping"],
            ["Analytics"],
            ["Case Studies"],
            ["PM Project"]
        ]
    },

    "QA Engineer":{
        
        "weeks":[
            ["Testing Basics"],
            ["Manual Testing"],
            ["Bug Reporting"],
            ["Automation"],
            ["Selenium"],
            ["API Testing"],
            ["Test Cases"],
            ["QA Project"]
        ]
    },

    "Game Developer":{
        
        "weeks":[
            ["C# Basics"],
            ["Unity"],
            ["Game Physics"],
            ["Animation"],
            ["Game Mechanics"],
            ["Level Design"],
            ["Optimization"],
            ["Game Project"]
        ]
    },

    "Blockchain Developer":{
        "weeks":[
            ["Blockchain Basics"],
            ["Cryptography"],
            ["Solidity"],
            ["Smart Contracts"],
            ["DApps"],
            ["DeFi"],
            ["Security"],
            ["Blockchain Project"]
        ]
    }

}

# ==========================
# INPUT
# ==========================

career = st.selectbox(
    "🎯 Select Career",
    list(roadmaps.keys())
)

# ==========================
# BUTTON
# ==========================

if st.button("🚀 Generate Roadmap"):

    data = roadmaps[career]

    for i, week in enumerate(data["weeks"], start=1):

        st.markdown(f"""
    <div class="roadmap-card">
        <div class="week-title">📅 Week {i}</div>
    </div>
    """, unsafe_allow_html=True)

        for skill in week:
            st.markdown(
            f"<div class='skill-item'>✅ {skill}</div>",
            unsafe_allow_html=True
        )
    st.success(
        "🎉 Roadmap Generated Successfully! Complete each week in sequence to become job-ready."
    )
    