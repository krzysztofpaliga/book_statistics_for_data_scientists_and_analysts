import pandas as pd
from sklearn import datasets
faces = datasets.fetch_olivetti_faces()
df = pd.DataFrame(faces.data)
df['target'] = faces.target
print(f'{df.head(3)}')
print('\n')
import matplotlib.pyplot as plt
plt.imshow(df.iloc[0, :-1].values.reshape(64, 64), cmap='gray')
plt.title(f'Image of person {df.iloc[0, -1]}")
plt.title(f'Image of person {df.iloc[0, -1]}')
plt.show()
%history -f ipython.py
