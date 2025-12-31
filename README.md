## Overview

This project is an *AI-powered decision analysis system* designed to evaluate problems and their proposed solutions using intelligent agents. Users submit a *problem statement and decision* through a modern web interface, and the system leverages *AI reasoning* to generate structured insights and analysis.

## Architecture & Flow

The frontend is built with *Next.js*, providing a *responsive and user-friendly interface* for data entry and result visualization. When a user submits a problem and solution, the data is sent to a *FastAPI backend*, which handles request validation and business logic.

All submissions are securely stored in a *MySQL database*, enabling *persistence, traceability, and future analysis*. After submission, users can trigger an *AI-based evaluation* of the decision.

## AI Decision Analysis

The analysis is performed by an *AI agent built using LangChain and LangGraph*. These frameworks allow the system to model *reasoning workflows, decision paths, and contextual evaluation*. The agent processes the stored problem and solution to generate insights such as:

* Strengths
* Weaknesses
* Risks
* Actionable recommendations

## Results & Visualization

Once the analysis is complete, the results are returned to the frontend and displayed in a *clear, structured, and intuitive format*. This helps users understand the *quality, implications, and reasoning* behind a decision.

## Tech Stack

### Frontend
* Next.js
* React
* Tailwind CSS (optional)

### Backend
* FastAPI
* Python

### Database
* MySQL

### AI & Agents
* LangChain
* LangGraph
* Large Language Models (LLMs)

### Infrastructure & Tooling
* REST APIs
* JSON-based data exchange
* Git & GitHub

## Use Cases

* Decision support systems
* Policy and strategy evaluation
* Problem–solution validation
* AI-assisted reasoning tools
