
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

df = pd.read_csv('MyTransaction.csv').dropna(subset=['Withdrawal', 'Balance'], how='all').copy()
df['Withdrawal'] = pd.to_numeric(df['Withdrawal'], errors='coerce').fillna(0)
df['Balance'] = pd.to_numeric(df['Balance'], errors='coerce').fillna(0)

scaler = StandardScaler()
X_scaled = scaler.fit_transform(df[['Withdrawal', 'Balance']])
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
df['User_Persona'] = kmeans.fit_predict(X_scaled)
df.to_csv('MyTransaction_Processed.csv', index=False)
print('Processing complete.')
