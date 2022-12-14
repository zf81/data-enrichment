# Packages
import pandas as pd

#Loading in the data 
patients = pd.read_csv('data/Hospital_Inpatient_Discharges__SPARCS_De-Identified___2015.csv')
neighborhood = pd.read_csv('data/NY_2015_ADI_9 Digit Zip Code_v3.1.csv')

list(patients)

list(neighborhood)

# Clean up column names 
patients.columns = patients.columns.str.replace('[^A-Za-z0-9]+', '_')

df_patients_small = patients[['Zip_Code_3_digits','CCS_Diagnosis_Code','CCS_Diagnosis_Description','Total_Charges','Total_Costs']]
print(df_patients_small.sample(10).to_markdown())
list(df_patients_small)
df_patients_small.shape

df_neighborhood_small = neighborhood[['ZIPID']]
print(df_neighborhood_small.sample(10).to_markdown())
list(df_neighborhood_small)
df_neighborhood_small.shape 

combined_df = df_patients_small.merge(df_neighborhood_small, how='left', left_on='Zip_Code_3_digits', right_on='ZIPID')
combined_df = pd.merge(df_patients_small, df_neighborhood_small, how='left', left_on='Zip_Code_3_digits', right_on='ZIPID')

# Combined the two dataframes
combined_df.columns

# Saving to csv
combined_df.to_csv('data/combined_df.csv')
combined_df.shape

patient_zip = pd.read_csv('data/patient_zip.csv')

# Concat
neighborhood_small_sample = df_neighborhood_small.sample(10)
patients_small_sample = df_patients_small.sample(10)

concat = pd.concat([neighborhood_small_sample, patients_small_sample])