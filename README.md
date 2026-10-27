# ⚽ MatchPulse AI
### Explainable, Personalized Real-Time Football Intelligence

MatchPulse AI is a Python and Streamlit prototype that turns football match events into understandable match insights. It is designed to help fans move beyond the scoreline and understand **what is happening, why it matters, and what to watch next**.

Instead of presenting match indicators alone, MatchPulse AI combines event-based signals, rule-based Python processing, explanations, and audience personalization in one interactive experience.

## 🚀 Try the Demo

- **Live application:** [Open MatchPulse AI](https://matchpulse-ai-cwybrfk52mftmgnrzy7irz.streamlit.app/)
- **Hackathon demo video:** [Watch the 1-minute, 53-second walkthrough](https://youtu.be/7frj1zlVs-g)
- **Source code:** [View the GitHub repository](https://github.com/olufemi-builds/matchpulse-ai)

## 🎯 The Problem

Football fans can access scores and statistics from many platforms, but numbers alone do not always explain the story of a match.

A fan may see a team leading or trailing without understanding the pressure building, the events influencing the match, or why a particular development matters.

MatchPulse AI explores how explainable football intelligence can make match information more accessible and relevant to different audiences.

## 💡 The Solution

MatchPulse AI provides an interactive match experience that connects match-state indicators with event-based explanations and personalized narratives.

The prototype demonstrates how a structured Python workflow can process synthetic football events, identify relevant signals, explain those signals, and present a readable match recap.

## ✨ Key Features

- **Match-state indicators:** View the selected match state and home/away pressure signals.
- **Explainable insights:** Read explanations connecting displayed insights to the available event signals.
- **Six-role Python workflow:** Demonstrates a structured, role-based processing approach for organizing match intelligence.
- **Audience personalization:** Explore a Casual Fan experience designed to present insights in an accessible way.
- **Synthetic event feed:** Inspect demonstration events used to illustrate the match-analysis workflow.
- **Match recap:** View a generated summary of the demonstration match.
- **Interactive Streamlit interface:** Explore the prototype through a browser without installing the application locally.

## 🧠 How It Works

The prototype follows a structured processing flow:

1. **Normalize:** Prepare event information for consistent processing.
2. **Detect:** Evaluate event signals and identify relevant match developments.
3. **Explain:** Turn detected signals into readable, evidence-based explanations.
4. **Personalize:** Present insights for the selected audience experience.
5. **Recap:** Summarize the demonstration match in a concise narrative.

These stages describe the implemented Python-based workflow. The six-role design organizes processing responsibilities; it should not be interpreted as six independent AI agents.

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Match-event processing and rule-based logic |
| Streamlit | Interactive web application |
| Synthetic demonstration data | Illustrates match events and analytical outputs |
| GitHub | Source code and project version control |
| Streamlit Community Cloud | Hosted demo application |

## ▶️ Run Locally

### Prerequisites

- Python 3.10 or a compatible Python version
- pip
- Git

### 1. Clone the repository

```bash
git clone https://github.com/olufemi-builds/matchpulse-ai.git
cd matchpulse-ai
```

### 2. Install Streamlit

```bash
python -m pip install streamlit
```

### 3. Launch the application

```bash
streamlit run app.py
```

Streamlit will provide a local URL where you can open the application in your browser.

## 📊 Data and Prototype Scope

**Transparency matters.** This version uses synthetic football events and rule-based Python processing to demonstrate the concept.

- The application does not currently consume live Premier League match data.
- The role-based workflow is implemented in Python; it does not currently represent six independent LLM agents.
- Match indicators and explanations should be interpreted within the context of the demonstration data.
- The prototype demonstrates a potential approach to explainable and personalized football intelligence rather than a production-ready live analytics platform.

## 🔭 Future Development

Potential next steps include:

- Integrating a reliable live football data provider.
- Expanding match-event validation and analytical evidence.
- Introducing independently orchestrated AI agents where they add measurable value.
- Supporting additional audience profiles and personalization preferences.
- Evaluating explanation quality against real match events.
- Adding historical match comparisons and more advanced tactical context.

These are proposed enhancements, not claims about features already implemented.

## 🏆 Hackathon Project

**Event:** Inside the Game: Developer Hackathon

**Project:** MatchPulse AI — Explainable, Personalized Real-Time Football Intelligence

The project explores how structured event processing, explainability, and audience-aware presentation can help football fans understand the story behind a match.

## 👨‍💻 Author

**Olufemi Olamoyegun**

Data & Analytics Practitioner | Low-Code Analytics | Python | Business Intelligence

- [GitHub](https://github.com/olufemi-builds)
- [Live Demo](https://matchpulse-ai-cwybrfk52mftmgnrzy7irz.streamlit.app/)
- [Demo Video](https://youtu.be/7frj1zlVs-g)

---

*MatchPulse AI is a hackathon prototype. Its current outputs are illustrative and depend on synthetic demonstration data.*
