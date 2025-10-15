# InvestScan-AI

### A Generative AI-powered assistant for reconciling investment records and application receipts.

---

## Overview

**InvestScan-AI** is an intelligent system designed to **analyze, consolidate, and cross-check investment documents** such as financial application receipts or statements.  
The goal is to ensure a **complete and accurate view of an investor’s financial portfolio** by detecting mismatches between recorded investments and actual supporting documents.

---

## User Story

> *As an investor who stores (or sometimes loses) financial application receipts and keeps track of my investments in a unified platform,  
> I want to know whether there are any investment receipts not registered in my investment database (and vice versa),  
> so that I can have a truthful and consolidated view of my financial assets.*

---

## Project Objectives

### Career Objective
To **practice Generative AI applications** that could be useful in a **banking context**, particularly in **corporate or investment banking** environments.

### Learning Objective
To build an **end-to-end NLP-based application**, incorporating:
- **Text and file processing**  
- **Named Entity Recognition (NER)**  
- **Prompt engineering** and **LLM-based extraction**

### Product Objective
To design a functional, usable, and scalable system that:
- Processes and consolidates **textual financial data**
- Runs **on-demand or automatically** when new receipts become available
- Enables **data quality evaluation and reconciliation**

---

## System Components

### 1. **File Reading**
- Reads investment documents in **PDF format**.  
- Implemented as a **function or class method**.

### 2. **File Type Detection**
- Determines whether the PDF contains **text** or **image-based** content (for OCR).  
- Implemented as a **function or class method**.

### 3. **Temporary Text Extraction**
- Creates a **temporary text variable** with the file’s content.  
- Implemented as a **function or class method**.

### 4. **Information Extraction**
- Extracts key financial fields, such as:
  - Purchase date  
  - Issuer  
  - Invested amount  
  - Maturity date (if applicable)  
  - Expected return or yield (if applicable)
- Uses a combination of **NER** and **LLM-based extraction**.  
- Implemented as a **function or class method**.

### 5. **Support Database Management**
- Updates or creates an **auxiliary database** to store processed information.  
- Implemented as a **function or class method**.

### 6. **Receipt-to-Investment Matching**
- Checks whether each document has a **matching record** in the investment database.  
- Returns a **DataFrame** of unmatched entries (expected: empty).  
- Implemented as a **function or class method**.

### 7. **Investment-to-Receipt Matching**
- Scans the investment database to verify that each investment has a corresponding receipt.  
- Returns a **DataFrame** of unmatched investments.  
- Expected results: some assets (e.g., stocks, funds, CRIs/CRAs) may not have receipts.  
- Implemented as a **function or class method**.

### 8. **Data Quality Evaluation**
- Evaluates the quality of extracted and consolidated information.  
- May rely on manual checks or predefined criteria (e.g., data type, string length).  
- Implemented as a **function or class**.

### 9. **Main Application Script**
- Executes the reconciliation **on-demand**.  
- If a receipt already exists in the database, it is **not reprocessed**.  
- The investment-to-receipt check can be run in each execution.  
- Designed as a **standalone Python script** or **Streamlit app**.

---

## Technologies (Planned / Potential)
- **Python 3.13+**
- **Streamlit** – for on-demand execution UI
- **Pandas / SQLite** – for structured data management
- **pdfminer / PyPDF2 / pytesseract** – for file reading and OCR
- **spaCy / Hugging Face / OpenAI / Mistral SDK** – for NER and LLM-based extraction
- **dotenv** – for environment variable management

---

## Planned Workflow

```mermaid
flowchart TD
    A[PDF Receipts] --> B[File Type Detection]
    B --> C[Text Extraction]
    C --> D[Information Extraction (NER + LLM)]
    D --> E[Support Database Update]
    E --> F[Cross-Check with Investment Database]
    F --> G[Report Missing Records]
    G --> H[Quality Evaluation]
    H --> I[Main Execution / Streamlit UI]
```


### Author
Matheus Rosso
<br>
Data Scientist & Economist | Focused on Generative AI Applications in Finance
