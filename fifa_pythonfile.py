import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
# % matplotlib inline
df = pd.read_csv("FullData.csv")
df.head(7)


# Analyzing this huge dataset is a tedious task as it involves quite a few pre-processing steps.
# There might be a lot of redundant and unwanted columns, which can be removed.
# Therefore you can delete certain columns if needed, by writing the below code:


del df['National_Kit'] #deletes the column National_Kit
df.head()

plt.figure(figsize=(15, 32))

sns.countplot(y=df.Nationality, palette="Set2")  # Plot all the nations on Y Axis

plt.figure(figsize=(15,6))
sns.countplot(x="Age",data=df)

plt.show()