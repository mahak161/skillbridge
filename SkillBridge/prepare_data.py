import pandas as pd

df = pd.read_csv(
    r"C:\Users\MAHAK\Downloads\skill.datasets\stack-overflow-developer-survey-2024\survey_results_public.csv"
)

# Keep only required columns
df = df[
    [
        "EdLevel",
        "YearsCodePro",
        "LanguageHaveWorkedWith",
        "ToolsTechHaveWorkedWith",
        "DevType"
    ]
]

# Remove missing values
df = df.dropna()

print(df.head())

print("\nRows after cleaning:", len(df))