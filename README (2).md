# 🏦 Credit Decision Memory

**Similarity-Driven Risk & Anomaly Detection using Qdrant**

**Team:** Weavers  
**Hackathon Use Case:** Credit Decision Memory (Use Case 3)

🚀 **Live Demo (Streamlit App):**  
👉 https://credit-decision-memory-system.streamlit.app/

---

## 1. Project Overview

**Credit Decision Memory** is a similarity-based decision support system designed to assist loan underwriters by leveraging historical loan outcomes rather than opaque predictive models.

Instead of automatically approving or rejecting a loan, the system:

- Retrieves historically similar loan cases  
- Surfaces their real observed outcomes (*Repaid, Defaulted, In Progress, Fraud*)  
- Provides explainable, evidence-based insights to human decision-makers  

This approach prioritizes transparency, auditability, and human-in-the-loop decisioning.

---

## 2. Problem Statement

Traditional credit decisioning systems often rely on black-box scoring models and limited explainability.

---

## 3. Solution Vision

A decision memory engine powered by vector similarity, not prediction.

---

## 4. Setup Notes

After creating a `.env` file with Qdrant credentials, you MUST ingest data:

```bash
python src/qdrant_ingest.py
```

---

## 5. Run the App

```bash
streamlit run src/ui_app.py
```

---

## Conclusion

Transparent, similarity-based credit decisioning using Qdrant.
