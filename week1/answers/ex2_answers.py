"""
Exercise 2 — Answers
====================
Fill this in after running exercise2_langgraph.py.
Run `python grade.py ex2` to check for obvious issues.
"""

# ── Task A ─────────────────────────────────────────────────────────────────

# List of tool names called during Task A, in order of first appearance.
# Look at [TOOL_CALL] lines in your terminal output.
# Example: ["check_pub_availability", "get_edinburgh_weather"]

TASK_A_TOOLS_CALLED = [
    "check_pub_availability",
    "check_pub_availability",
    "calculate_catering_cost",
    "get_edinburgh_weather",
    "generate_event_flyer",
]

# Which venue did the agent confirm? Must be one of:
# "The Albanach", "The Haymarket Vaults", or "none"
TASK_A_CONFIRMED_VENUE = "The Albanach"

# Total catering cost the agent calculated. Float, e.g. 5600.0
# Write 0.0 if the agent didn't calculate it.
TASK_A_CATERING_COST_GBP = 5600

# Did the weather tool return outdoor_ok = True or False?
TASK_A_OUTDOOR_OK = True

# Optional — anything unexpected.
# If you used a non-default model via RESEARCH_MODEL env var, note it here.
# Example: "Used nvidia/nemotron-3-super-120b-a12b for the agent loop."
TASK_A_NOTES = (
    "I set the FLYER_IMAGE_MODEL env var as 'black-forest-labs/flux-schnell' for image generation"
)

# ── Task B ─────────────────────────────────────────────────────────────────
#
# The scaffold ships with a working generate_event_flyer that has two paths:
#
#   - Live mode: if FLYER_IMAGE_MODEL is set in .env, the tool calls that
#     model and returns a real image URL.
#   - Placeholder mode: otherwise (the default) the tool returns a
#     deterministic placehold.co URL with mode="placeholder".
#
# Both paths return success=True. Both count as "implemented" for grading.
# This is not the original Task B — the original asked you to write a direct
# FLUX image call, but Nebius removed FLUX on 2026-04-13. See CHANGELOG.md
# §Changed for why we pivoted the task.

# Did your run of the flyer tool produce a success=True result?
# (This will be True for both live and placeholder mode — both are valid.)
TASK_B_IMPLEMENTED = True  # True or False

# Which path did your run take? "live" or "placeholder"
# Look for the "mode" field in the TOOL_RESULT output of Task B.
# If you didn't set FLYER_IMAGE_MODEL in .env, you will get "placeholder".
TASK_B_MODE = "live"

# The image URL returned by the tool. Copy exactly from your terminal output.
# In placeholder mode this will be a placehold.co URL.
# In live mode it will be a provider CDN URL.
TASK_B_IMAGE_URL = "https://pictures-storage.storage.eu-north1.nebius.cloud/text2img-68645e20-4d3a-40ea-9a4f-8fe55cc1cc3c_00001_.webp"

# The prompt sent to the image model. Copy from terminal output.
TASK_B_PROMPT_USED = "Professional event flyer for Edinburgh AI Meetup, tech professionals, modern venue at The Haymarket Vaults, Edinburgh. 160 guests tonight. Warm lighting, Scottish architecture background, clean modern typography."

# Why did the agent's behaviour NOT change when Nebius removed FLUX?
# One sentence. This is the point of the lesson.
TASK_B_WHY_AGENT_SURVIVED = """
Because of the fallback image provider via a placeholder function/tool that was implemented.
"""

# ── Task C ─────────────────────────────────────────────────────────────────

# Scenario 1: first choice unavailable
# Quote the specific message where the agent changed course. Min 20 words.
SCENARIO_1_PIVOT_MOMENT = """
The specific message after the tool calls that made the agent change course was:
'The first tool response said The Bow Bar's capacity is 80, which is too small, so they didn't meet the requirements. Then I checked The Albanach next.'
"""

SCENARIO_1_FALLBACK_VENUE = "The Albanach"

# Scenario 2: impossible constraint (300 guests)
# Did the agent recommend a pub name not in the known venues list?
SCENARIO_2_HALLUCINATED = False  # True or False

# Paste the final [AI] message.
SCENARIO_2_FINAL_ANSWER = """
<think>
Okay, let's see. The user is looking for a venue in Edinburgh that can accommodate 
300 people with vegan options. They provided four known venues: The Albanach, The 
Haymarket Vaults, The Guilford Arms, and The Bow Bar. I checked each one using the 
check_pub_availability function.\n\nFirst, The Albanach had a capacity of 180 and 
vegan options, but that's under 300. Then The Haymarket Vaults with 160, also too small. 
The Guilford Arms had 200 capacity but no vegan options. Finally, The Bow Bar has 80 
capacity and vegan, but it's full. None of them meet both the capacity and vegan 
requirements. So I need to inform the user that none of the known venues can handle 
their request. Maybe suggest looking for other options outside the known list or 
adjusting the requirements.
</think>
\n\nNone of the known Edinburgh venues meet 
the requirements for 300 guests with vegan options. The maximum capacity among the 
checked venues is 200 (The Guilford Arms), which still falls short while also lacking 
vegan options. Would you like to:\n1. Expand the search to non-listed venues?\n2. 
Adjust the guest count or dietary requirements?\n3. Check availability for a different 
date?
"""

# Scenario 3: out of scope (train times)
# Did the agent try to call a tool?
SCENARIO_3_TRIED_A_TOOL = False  # True or False

SCENARIO_3_RESPONSE = """
<think>
Okay, the user is asking about the last train time from Edinburgh Waverley to London tonight. 
Let me check the tools provided.\n\nLooking at the available functions: check_pub_availability, 
get_edinburgh_weather, calculate_catering_cost, generate_event_flyer. 
None of these are related to train schedules. 
The functions are for checking pub availability, weather, catering costs, and generating flyers. 
\n\nSince there's no tool for train times, I can't use any of the provided functions to answer 
this. I need to inform the user that I don't have access to that information and suggest they 
check a train service website or app.
</think>
\n\nI don't have access to real-time train 
schedules or transportation data. For the most accurate information about the last train 
from Edinburgh Waverley to London, I recommend checking:\n1. The National Rail website 
(https://www.nationalrail.co.uk)\n2. Train service apps like Citymapper or Trainline\n3. 
The specific train operator's website (e.g., LNER)\n\nWould you like help with anything 
related to Edinburgh pubs, weather, or event planning instead?
"""

# Would this behaviour be acceptable in a real booking assistant? Min 30 words.
SCENARIO_3_ACCEPTABLE = """
Its a safe behavior but user experience wise an actual user may expect the tool to also get the 
full information about transportation schedules as well as the "booking assistant" 
should help in bookings, not just reservations for pubs.
"""

# ── Task D ─────────────────────────────────────────────────────────────────

# Paste the Mermaid output from `python exercise2_langgraph.py task_d` here.
TASK_D_MERMAID_OUTPUT = """
---
config:
  flowchart:
    curve: linear
---
graph TD;
        __start__([<p>__start__</p>]):::first
        agent(agent)
        tools(tools)
        __end__([<p>__end__</p>]):::last
        __start__ --> agent;
        agent -.-> __end__;
        agent -.-> tools;
        tools --> agent;
        classDef default fill:#f2f0ff,line-height:1.2
        classDef first fill-opacity:0
        classDef last fill:#bfb6fc
"""

# Compare the LangGraph graph to exercise3_rasa/data/flows.yml. Min 30 words.
TASK_D_COMPARISON = """
The langgraph method is a flexible agentic flow for performing tool calls and 
arriving at a final answer. It could get stuck or not even complete (due to max_tries)
in a loop and not compolete the user requests. However it seems that Rasa CALM is a 
framework to query the the user for specific things in a deterministic manner and in a 
giver order. 
"""

# ── Reflection ─────────────────────────────────────────────────────────────

# The most unexpected thing the agent did. Min 40 words.
# Must reference a specific behaviour from your run.

MOST_SURPRISING = """
Most suprising bit was in the thinking block. 
I would've expected it wouldve been easier for the LLM to first select by meets_all_constraints.
However it seems the agent still reasons again about the 
availability and vegan filter, although the tool call should've confirmed it. 
The thought process is wasting tokens. Hoever it seems most of the times
the agent checks for count first and then verifies the availabiliuty.
"""
