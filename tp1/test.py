import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LogisticRegression

print("✅ Tous les modules sont importés avec succès par [mets ton nom ici]")

# Mini test : graphique seaborn
df = pd.read_csv("donnevrai.csv")  

print(df.head())  

sns.boxplot(x="danger", y="vitesse", data=df)
plt.title("Exemple graphique : vitesse selon danger")
plt.show()

print("✅ Le graphique seaborn s'affiche correctement !")
