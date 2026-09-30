# Eric Reid
#IC4
#September 30, 2026
# Python for Health Analytics
# Purpose is to clean and process the eye health dataset



import pandas as pd
import numpy as np

#Load csv
df = pd.read_csv("eye_health_behavioral_risk_factors_dataset_2022_brfss.csv")


print(df.shape,
      df.dtypes,
      df.isna().sum(),
      df.nunique(),
      sep="\n")



print("Duplicates: ", df.duplicated().sum())

df = df.dropna(axis=1, how="all")
df = df.drop(columns = [c for c in df.columns if c.endswith("ID")])

df = df.dropna(subset=["Data_Value"]) #Drop rows with no value in the column "Data_Value"
df.drop(columns=["Geolocation", "Data_Value_Footnote_Symbol", \
                 "Data_Value_Footnote", "StateAbbr", "NonWeightedSample", "Geographic Level", "Numerator"])


df.columns = df.columns.str.lower().str.replace(" ", "_")  # Make column headers snake_case
df["error"] = (df["high_confidence_limit"] - df["low_confidence_limit"]) / 2 # Create new column "ci_width" and calculate
df["prevalence_level"] = np.select([df["data_value"] < 5, df["data_value"] <= 7],\
                                    ["Low", "Medium"], "High")  #Create prevalence level description

df.to_csv("eye_health_2022_clean.csv", index=False)
print(pd.read_csv("eye_health_2022_clean.csv").shape == df.shape)
print(pd.read_csv("eye_health_2022_clean.csv").shape)  # Print saved file dimensions
print(pd.read_csv("eye_health_2022_clean.csv").head)  #Print dataframe head (first 5 lines)
