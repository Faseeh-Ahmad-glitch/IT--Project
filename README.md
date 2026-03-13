# UPI Transaction Analysis & User Persona Modeling

## Executive Summary
This repository contains the complete implementation of a financial behavior analysis project. By leveraging UPI transaction data, we perform granular data preprocessing, unsupervised clustering for persona identification, and supervised learning for behavior prediction.

## Detailed Project Report Findings
Optimizing Digital Wallet Ecosystems via Hybrid Machine Learning: A Discovery-Driven Analysis of Raw UPI Transaction Logs
Faseeh Ahmad 
IPM06175
Integrated Program in Management, IIM Rohtak
2024-29
IT Applications
Dr. Karan Verma
March 12, 2026
Abstract
As a part of this assignment, I have addressed the problem of working with financially unlabelled data in the form of constructing a hybrid machine-learning pipeline on a raw dataset (1,418 UPI trades in 2023). I applied K-means unsupervised clustering to extract behavioral personas using data of withdrawal and balance. The Random Forest classifier based on those personas then used the ground truth as a ground truth. This indicates that banks may automate the user segmentation so as to enhance service delivery and risk management.
Introduction
Transactional data in the rapidly developing Indian FinTech market typically comes in logs in their raw form and with no fixed categories. Traditional supervised learning involves labels but it is seen in this project that it is actually possible to use unsupervised learning to find labels yourself. By merging the two strategies we are essentially simulating the way banks work in real life, in which you would have to guess what users want by simply looking at what they do rather than any explicit tags.
Problem Statement	
The Labeling Deficit: The bulk of raw UPI logs are simply accumulated in some unspecified Other or Misc. categories, so applying any standard controlled classification is like attempting to find a solution without any guidance on the part of the professor.
The Insight Gap: FinTech folks lack clear user segmentation and, therefore, are unable to determine whether a customer is a high-value premium customer or a debt-stricken person who simply misses an office hour you can request clarification.
Economic Risk: Inefficient marketing investment and poor risk evaluation will translate to a greater burn rate of digital wallet startups i.e. we are burning more money t

## Methodology
### 1. Data Acquisition & Cleaning
- **Source:** UPI Transactions Dataset.
- **Preprocessing:** Handling of non-numeric 'Withdrawal' and 'Balance' entries, removal of null records, and feature scaling using `StandardScaler`.

### 2. Persona Segmentation (Unsupervised Learning)
- **Algorithm:** K-Means Clustering.
- **Optimization:** Defined 3 distinct clusters representing:
    - **Low-Activity Users:** Small balances, infrequent withdrawals.
    - **Transactors:** Regular withdrawal patterns with moderate liquidity.
    - **High-Net-Worth/High-Volume:** Outlier behavior with significant account balances.

### 3. Classification Model (Supervised Learning)
- **Algorithm:** Random Forest Classifier.
- **Result:** Achieved 100% accuracy in mapping transactions to the identified personas, demonstrating high feature reliability.

## Visualizations & Artifacts
- **Cluster Map:** `persona_clusters.png` illustrates the clear separation between identified groups.
- **Processed Data:** `MyTransaction_Processed.csv` includes the categorical labels for further analysis.
- **Automation Script:** `analysis.py` allows for reproducible results on new data.

## How to Run
1. Ensure dependencies are installed: `pandas`, `scikit-learn`, `seaborn`.
2. Run `python analysis.py`.
