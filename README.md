# AI Resume Matcher

---

## Overview

**Resume-Matcher** is an intelligent developer tool designed to evaluate and enhance the recruitment process by matching resumes with job descriptions using advanced NLP techniques. It leverages large language models and sentence embeddings to provide accurate similarity scores and personalized feedback, helping recruiters and developers automate candidate assessments.

---

## Why AI Resume Matcher?

This project aims to simplify and improve candidate-job matching through AI. The core features include:

- **Semantic Matching:** Uses Sentence Transformers to measure relevance between resumes and job descriptions.
- **AI-Driven Insights:** Generates tailored feedback on skill gaps and improvement areas using OpenAI's API.
- **API Integration:** Provides streamlined REST APIs for automated candidate evaluation.
- **Personalized Recommendations:** Supports recruiters with data-driven suggestions to optimize resumes.
- **Scalable Architecture:** Built with FastAPI and Uvicorn for robust deployment in production environments.

---

## Getting Started

Follow these instructions to get the project up and running locally.

---

## Prerequisites

Make sure you have the following installed:

- **Programming Language:** Python 3.8+
- **Package Manager:** pip
- **Frontend:** Node.js & npm
- **API Key:** OpenAI API key

---

## Installation

Build Resume-Matcher from source and install dependencies:

1. **Clone the repository:**

   ```bash
   git clone https://github.com/aditisha019/Resume-Matcher.git

2. **Navigate to the project directory:**

   ```bash
   cd Resume-Matcher

3. **Install backend dependencies:**

   ```bash
   cd backend
   pip install -r requirements.txt

4. **Install frontend dependencies:**

   ```bash
   cd ../frontend
   npm install

## Usage

Run the project locally:
1. **Start the backend server:**

   ```bash
   cd backend
   uvicorn main:app --reload

2. **Start the frontend app:**

   ```bash
   cd ../frontend
   npm start

3. Open your browser at http://localhost:3000.

## Testing

This project uses pytest for backend testing. To run tests:

```bash
cd backend
pytest

