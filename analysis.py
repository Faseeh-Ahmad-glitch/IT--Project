
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score
import logging

# ----------------------------------------------------------------
# UPI TRANSACTION ANALYTICS SYSTEM v2.0
# ----------------------------------------------------------------
# This module implements an end-to-end pipeline for financial
# behavioral modeling and user persona categorization.

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger('UPI_Analytics')

class UPIPipeline:
    def __init__(self, path):
        self.path = path
        self.df = None
        self.scaler = StandardScaler()
        self.features = ['Withdrawal', 'Balance']

    def ingest_data(self):
        logger.info("Initializing data ingestion...")
        self.df = pd.read_csv(self.path)
        self.df = self.df.dropna(subset=self.features, how='all').copy()
        for col in self.features:
            self.df[col] = pd.to_numeric(self.df[col], errors='coerce').fillna(0)
        logger.info(f"Ingestion complete. Shape: {self.df.shape}")

    def engineer_features(self):
        logger.info("Scaling features for K-Means sensitivity...")
        self.df_scaled = self.scaler.fit_transform(self.df[self.features])

    def identify_personas(self, k=3):
        logger.info(f"Running Unsupervised K-Means (k={k})...")
        model = KMeans(n_clusters=k, random_state=42, n_init=15)
        self.df['User_Persona'] = model.fit_predict(self.df_scaled)
        return self.df['User_Persona'].value_counts()

    def validate_segmentation(self):
        logger.info("Validating segments with Supervised Random Forest...")
        X = self.df[self.features]
        y = self.df['User_Persona']
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
        clf = RandomForestClassifier(n_estimators=100)
        clf.fit(X_train, y_train)
        preds = clf.predict(X_test)
        accuracy = accuracy_score(y_test, preds)
        logger.info(f"Validation Accuracy: {accuracy*100:.2f}%")
        return classification_report(y_test, preds)

    def export_artifacts(self):
        self.df.to_csv('MyTransaction_Processed.csv', index=False)
        plt.figure(figsize=(10,6))
        sns.scatterplot(data=self.df, x='Withdrawal', y='Balance', hue='User_Persona', palette='viridis')
        plt.title('Final User Persona Distribution')
        plt.savefig('persona_clusters.png')
        logger.info("Artifacts exported: CSV and PNG.")

if __name__ == '__main__':
    pipeline = UPIPipeline('MyTransaction.csv')
    pipeline.ingest_data()
    pipeline.engineer_features()
    counts = pipeline.identify_personas()
    print("Persona Counts:\n", counts)
    report = pipeline.validate_segmentation()
    print("Classification Report:\n", report)
    pipeline.export_artifacts()
