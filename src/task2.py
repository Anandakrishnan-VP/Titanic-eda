import pandas as pd
df=pd.read_csv("cleaned_tds.csv") #using cleaned dataset
#Genertaing summary statistics
print(df.describe())
print(df.describe(include="object"))
#Histograms and boxplots for numeric features
import matplotlib.pyplot as plt
import seaborn as sns
#numric_cols=df.select_dtypes(include=["int64","float64"]).columns
numerical_cols=["Age","Fare","SibSp","Parch"]
#histograms
plt.figure(figsize=(15, 8))
for i, col in enumerate(numerical_cols):
    plt.subplot(2,2,i+1)
    sns.histplot(data=df[col])
    plt.title(f"Histogram of {col}")
plt.tight_layout()
plt.show()
#boxplots
plt.figure(figsize=(15, 8))
for i, col in enumerate(numerical_cols):
    plt.subplot(2,2,i+1)
    sns.boxplot(data=df[col])
    plt.title(f"Boxplot of {col}")
plt.tight_layout()
plt.show()
#correlation matrix
correleation_matrix=df.corr(numeric_only=True)
plt.figure(figsize=(10,8))
sns.heatmap(correleation_matrix, annot=True, cmap="coolwarm", linewidths=0.5)
plt.title("Correleation Matrix")
plt.show()
 
    
    