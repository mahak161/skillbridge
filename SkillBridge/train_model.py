import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
import joblib

# Load data
df = pd.read_csv(
    r"C:\Users\MAHAK\Downloads\skill.datasets\stack-overflow-developer-survey-2024\survey_results_public.csv"
)

# Keep needed columns
df = df[
    [
        "EdLevel",
        "YearsCodePro",
        "LanguageHaveWorkedWith",
        "ToolsTechHaveWorkedWith",
        "DatabaseHaveWorkedWith",
        "PlatformHaveWorkedWith",
        "WebframeHaveWorkedWith",
        "DevType"
    ]
]

df = df.dropna()

allowed_roles = [
    "Developer, full-stack",
    "Developer, back-end",
    "Developer, front-end",
    "Developer, desktop or enterprise applications",
    "Developer, mobile",
    "Developer, embedded applications or devices",
    "DevOps specialist",
    "Data engineer",
    "Data scientist or machine learning specialist",
    "Cloud infrastructure engineer",
    "Developer, game or graphics",
    "Developer, QA or test",
    "Developer, AI"
]

df = df[df["DevType"].isin(allowed_roles)]

# Keep top careers only
top_roles = df["DevType"].value_counts().head(10).index

df = df[df["DevType"].isin(top_roles)]

# Combine inputs into one text field
df["features"] = (
    df["EdLevel"].astype(str) + " " +
    df["YearsCodePro"].astype(str) + " " +
    df["LanguageHaveWorkedWith"].astype(str) + " " +
    df["ToolsTechHaveWorkedWith"].astype(str) + " " +
    df["DatabaseHaveWorkedWith"].astype(str) + " " +
    df["PlatformHaveWorkedWith"].astype(str) + " " +
    df["WebframeHaveWorkedWith"].astype(str)
)

# Encode career labels
encoder = LabelEncoder()
y = encoder.fit_transform(df["DevType"])

from sklearn.feature_extraction.text import TfidfVectorizer

vectorizer = TfidfVectorizer(max_features=5000)

X = vectorizer.fit_transform(df["features"])

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


model = LogisticRegression(
    max_iter=2000
)

model.fit(X_train, y_train)

accuracy = model.score(X_test, y_test)

print("Accuracy:", round(accuracy * 100, 2), "%")

joblib.dump(model, "models/career_predictor.pkl")
joblib.dump(encoder, "models/label_encoder.pkl")
joblib.dump(vectorizer, "models/vectorizer.pkl")

print("Model Saved Successfully!")
import os

print("Career:", os.path.getsize("models/career_predictor.pkl"))
print("Encoder:", os.path.getsize("models/label_encoder.pkl"))
print("Vectorizer:", os.path.getsize("models/vectorizer.pkl"))

from sklearn.metrics import classification_report

y_pred = model.predict(X_test)

print(classification_report(y_test, y_pred))