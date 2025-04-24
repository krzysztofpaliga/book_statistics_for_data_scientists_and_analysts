import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
data = pd.read('./diabetes.csv')
data = pd.read_csv('./diabetes.csv')
X = data.drop('Outcome', axis =1)
y = data['Outcome']
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
pca = PCA(n_components = 2)
X_pca = pca.fit_transform(X_scaled)
explained_variance_ratio = pca.explained_variance_ratio
explained_variance_ratio = pca.explained_variance_ratio_
pl.bar(range(len(explained_variance_ratio)), explained_variance_ratio)
plt.bar(range(len(explained_variance_ratio)), explained_variance_ratio)
plt.xlabel('Principal Component')
plt.ylabel('Explained Variance Ratio')
plt.title('Explained Variance Ratio for Each Principal Component')
plt.savefig('skew_negative.jpg', dpi=600, bbox_inches='tight')
plt.show()
%history -f ipython.py
