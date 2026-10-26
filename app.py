
import streamlit as st
import random
from collections import Counter

st.set_page_config(
    page_title="MatchPulse AI",
    page_icon="⚽",
    layout="wide"
)

# ---------- SESSION STATE ----------
if "minute" not in st.session_state:
    st.session_state.minute = 54

if "events" not in st.session_state:
    st.session_state.events = [
        {"minute": 48, "team": "HOME", "event": "Middle-third recovery", "player": "P-07"},
        {"minute": 50, "team": "HOME", "event": "Progressive pass", "player": "P-10"},
        {"minute": 51, "team": "AWAY", "event": "Counterattack", "player": "P-21"},
        {"minute": 52, "team": "HOME", "event": "High press recovery", "player": "P-07"},
        {"minute": 53, "team": "HOME", "event": "Shot on target", "player": "P-10"},
    ]

# Normalize older events so missing player IDs never cause a crash.
st.session_state.events = [
    {
        "minute": e.get("minute", 0),
        "team": e.get("team", "UNKNOWN"),
        "event": e.get("event", "Unspecified event"),
        "player": e.get("player", "Unknown"),
    }
    for e in st.session_state.events
]

events = st.session_state.events

# ---------- VISUAL DESIGN ----------
st.markdown("""
<style>
.stApp {
    background-color: #0b1220;
    color: #f1f5f9;
}
div[data-testid="stMetric"] {
    background: #16243a;
    padding: 14px;
    border-radius: 12px;
    border: 1px solid #2b405d;
}
</style>
""", unsafe_allow_html=True)

# ---------- EVENT ANALYSIS ----------
recent = events[-10:]
home = [e for e in recent if e["team"] == "HOME"]
away = [e for e in recent if e["team"] == "AWAY"]

def count_event(team_events, words):
    return sum(
        any(word in e["event"].lower() for word in words)
        for e in team_events
    )

home_recoveries = count_event(home, ["recovery"])
home_progressive = count_event(home, ["progressive"])
home_shots = count_event(home, ["shot"])
away_counters = count_event(away, ["counterattack"])
away_shots = count_event(away, ["shot"])

home_pressure = home_recoveries + home_progressive + home_shots
away_pressure = away_counters + away_shots

if home_pressure > away_pressure:
    control = "HOME"
elif away_pressure > home_pressure:
    control = "AWAY"
else:
    control = "BALANCED"

# ---------- HEADER ----------
st.title("⚽ MATCHPULSE AI")
st.caption("EXPLAINABLE • PERSONALIZED • REAL-TIME FOOTBALL INTELLIGENCE")

c1, c2, c3 = st.columns(3)
c1.metric("Match time", f"{st.session_state.minute}'")
c2.metric("Synthetic score", "HOME 2 — 1 AWAY")
c3.metric("Event-based control", control)

# ---------- MATCH STATE ----------
st.subheader("01 / MATCH STATE")
a, b, c, d = st.columns(4)
a.metric("Home pressure index", home_pressure)
b.metric("Away pressure index", away_pressure)
c.metric("Home recoveries", home_recoveries)
d.metric("Progressive passes", home_progressive)

st.caption(
    "Pressure indices are simple prototype scores derived from the "
    "latest 10 recorded events, not validated professional match metrics."
)

# ---------- EXPLAINABILITY ----------
st.subheader("02 / WHY IT MATTERS")

if control == "HOME":
    st.success(
        f"HOME CONTROL SIGNAL: In the latest {len(recent)} events, "
        f"the home side recorded {home_recoveries} recoveries, "
        f"{home_progressive} progressive passes and {home_shots} shot events. "
        "These actions suggest an active attacking phase, but do not alone "
        "prove overall match dominance."
    )
elif control == "AWAY":
    st.warning(
        f"AWAY PRESSURE SIGNAL: The away side recorded {away_counters} "
        f"counterattacks and {away_shots} shot events in this window. "
        "These events may indicate a threat during transitions."
    )
else:
    st.info(
        "BALANCED SIGNAL: The selected event indicators do not show a clear "
        "difference in pressure between the two teams."
    )

st.caption("All match events and scores are illustrative synthetic data.")

# ---------- AGENT WORKFLOW ----------
st.subheader("03 / MULTI-AGENT WORKFLOW")
st.write(
    "Prototype pipeline: each role receives shared event context and "
    "contributes to the next stage. These are currently Python-based roles, "
    "not independent LLM agents."
)

agent_rows = [
    ("1. Event Intelligence Agent", f"Normalized {len(events)} events"),
    ("2. Pattern Detection Agent", f"Compared event signals: {control}"),
    ("3. Explainability Agent", "Linked the signal to observed events"),
    ("4. Narrative Agent", "Prepared an evidence-based explanation"),
    ("5. Personalization Agent", "Adapts wording to the selected audience"),
    ("6. Recap Agent", "Summarizes the event history"),
]

for agent_name, agent_result in agent_rows:
    st.write(f"**{agent_name}** → {agent_result}")

# ---------- PERSONALIZATION ----------
st.subheader("04 / PERSONALIZED VIEW")
audience = st.selectbox(
    "Choose your viewing experience",
    ["Casual Fan", "Analyst", "Player Focus"]
)

if audience == "Casual Fan":
    st.info(
        f"The recent event signals currently favour {control.lower()} control. "
        "Watch for the next big chance."
    )
elif audience == "Analyst":
    st.info(
        f"Last {len(recent)} events — home recoveries: {home_recoveries}; "
        f"progressive passes: {home_progressive}; home shots: {home_shots}; "
        f"away counters: {away_counters}. Event-based signal: {control}."
    )
else:
    players = sorted(set(e["player"] for e in events))
    player = st.selectbox("Select synthetic player", players)
    player_events = [e for e in events if e["player"] == player]

    st.info(f"{player} has {len(player_events)} recorded actions.")
    for e in player_events:
        st.write(f"{e['minute']}' — {e['team']} — {e['event']}")

# ---------- LIVE SYNTHETIC EVENT FEED ----------
st.subheader("05 / SYNTHETIC LIVE EVENT FEED")

if st.button("▶ Advance match and generate event", type="primary"):
    team = random.choice(["HOME", "HOME", "AWAY"])
    event = random.choice([
        "Middle-third recovery",
        "Progressive pass",
        "Shot on target",
        "High press recovery",
        "Counterattack",
        "Tackle won",
        "Possession change",
    ])
    player = random.choice(["P-07", "P-10", "P-12", "P-21", "P-24"])

    st.session_state.minute += 1
    st.session_state.events.append({
        "minute": st.session_state.minute,
        "team": team,
        "event": event,
        "player": player,
    })

    st.rerun()

for e in reversed(st.session_state.events[-12:]):
    st.write(
        f"**{e['minute']}' · {e['team']} · {e['player']}** — {e['event']}"
    )

# ---------- RECAP ----------
st.subheader("06 / AUTOMATED MATCH RECAP")

if st.button("Generate match recap"):
    current_events = st.session_state.events
    home_events = [e for e in current_events if e["team"] == "HOME"]
    away_events = [e for e in current_events if e["team"] == "AWAY"]

    st.markdown(
        f"**Synthetic match recap through {st.session_state.minute} minutes**\n\n"
        f"- Recorded events: {len(current_events)}\n"
        f"- Home actions: {len(home_events)}\n"
        f"- Away actions: {len(away_events)}\n"
        f"- Home recoveries: {count_event(home_events, ['recovery'])}\n"
        f"- Home shot events: {count_event(home_events, ['shot'])}\n"
        f"- Current event-based control signal: {control}\n\n"
        "This recap summarizes the synthetic event history. It does not "
        "predict the final score or claim to describe a real match."
    )

st.caption("MatchPulse AI • Prototype v0.3 • Synthetic data only")

