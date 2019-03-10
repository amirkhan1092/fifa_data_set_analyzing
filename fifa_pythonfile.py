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

# weights
a = 0.5
b = 1
c = 2
d = 3

# GoalKeeping Characterstics
df['gk_Shot_Stopper'] = (
                                    b * df.Reactions + b * df.Composure + a * df.Speed + a * df.Strength + c * df.Jumping + b * df.GK_Positioning + c * df.GK_Diving + d * df.GK_Reflexes + b * df.GK_Handling) / (
                                    2 * a + 4 * b + 2 * c + 1 * d)
df['gk_Sweeper'] = (
                               b * df.Reactions + b * df.Composure + b * df.Speed + a * df.Short_Pass + a * df.Long_Pass + b * df.Jumping + b * df.GK_Positioning + b * df.GK_Diving + d * df.GK_Reflexes + b * df.GK_Handling + d * df.GK_Kicking + c * df.Vision) / (
                               2 * a + 4 * b + 3 * c + 2 * d)

# Based on the above parameters,
# I’ll be predicting my best goalkeeper as per the dataset. Let us now plot these parameters:

plt.figure(figsize=(15, 6))
# Generate sequential data and plot
sd = df.sort_values('gk_Shot_Stopper', ascending=False)[:5]
x1 = np.array(list(sd['Name']))
y1 = np.array(list(sd['gk_Shot_Stopper']))
sns.barplot(x1, y1, palette="colorblind")
plt.ylabel("Shot Stopping Score")

plt.show()
