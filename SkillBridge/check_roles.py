import pandas as pd

df = pd.read_csv(
    r"C:\Users\MAHAK\Downloads\skill.datasets\stack-overflow-developer-survey-2024\survey_results_public.csv"
)

df = df[
    [
        "EdLevel",
        "YearsCodePro",
        "LanguageHaveWorkedWith",
        "ToolsTechHaveWorkedWith",
        "DevType"
    ]
]

df = df.dropna()

print(df["DevType"].value_counts().head(20))