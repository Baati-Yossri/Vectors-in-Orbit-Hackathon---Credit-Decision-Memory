# 🧠 Credit Decision Memory  
**Similarity-Driven Risk & Anomaly Detection using Qdrant**

## 📌 Project Overview
This project implements **Use Case 3: Credit Decision Memory** — a decision-support system that assists bankers in evaluating loan applications by retrieving and analyzing similar historical cases instead of relying solely on black-box scoring models.

The system is **memory-based**, explainable, and designed for human-in-the-loop decisioning.

---

## 🎯 Problem Statement
Credit decisioning requires speed, accuracy, and audit-ready explanations.  
Traditional approaches often recompute risk from scratch and produce opaque scores without historical context.

Additionally, real-world credit datasets suffer from:
- Outcome imbalance
- Right-censoring (many loans are too recent to have known outcomes)

---

## 💡 Solution Concept
We built a **decision memory engine** that:
1. Converts loan applications into numerical vectors
2. Stores them in **Qdrant**
3. Retrieves similar historical loan cases
4. Analyzes their outcomes (repaid, defaulted, fraud)
5. Produces explainable, evidence-based recommendations

The system **does not auto-approve or reject loans**.

---

## 🏗️ Architecture
Loan Dataset → Vectorization → Qdrant Vector Store → Similarity Search → Explainable Decision Support

---

## 📂 Dataset
The dataset includes:
- Applicant financial profile
- Loan details (amount, tenure, purpose)
- Credit indicators
- Fraud signals
- Application dates

---

## ⚠️ Key Challenge: Outcome Imbalance
Initial analysis showed:
- ~78% Defaulted
- ~3% Repaid

This caused unintuitive similarity results.

---

## 🔍 Root Cause Identified
Most loans were requested in **2023–2025**, meaning many were still ongoing.
This is known as **right-censoring** in credit risk.

---

## ✅ Final Fix: Synthetic Time Shifting
To simulate mature loan lifecycles:
- Application dates were shifted **36 months into the past**
- Loan age was recomputed
- Outcomes were recalculated using lifecycle-aware logic

### Outcome Logic
- **Repaid**: loan age ≥ tenure, no fraud, no default
- **Defaulted**: fraud or early default
- **In_Progress**: ongoing loans

---

## 🧠 Why This Matters
This shows that:
- Memory-based systems depend on outcome quality
- Time-awareness is critical in credit decisioning
- Similarity search provides explainability, not blind automation

---

## 🧪 Tech Stack
- Python
- Pandas / NumPy
- Scikit-learn
- Qdrant
- Joblib

---

## ▶️ How to Run
```bash
python synthetic_time_shift.py
python vectorizing.py
python qdrant_ingest.py
python query_qdrant.py
```

---

## 📊 Output
- Similar historical loans
- Outcomes & fraud signals
- Banker-friendly explanations

---

## 🧾 Key Takeaway
**This project focuses on explainable decision memory, not prediction.**

---

## 🚀 Future Work
- Multimodal document embeddings
- Survival-analysis-aware similarity
- Portfolio-level risk analysis
