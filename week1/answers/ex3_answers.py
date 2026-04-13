"""
Exercise 3 — Answers
====================
Fill this in after completing the three Rasa conversations.

CALM vs Old Rasa — what changed
---------------------------------
The old open-source Rasa approach used:
  - nlu.yml: intent training examples
  - rules.yml: explicit dialogue rules
  - FormValidationAction: Python class to parse slot values

Rasa Pro CALM uses:
  - flows.yml: natural language descriptions of what each flow does
  - from_llm slots: the LLM extracts values from conversation
  - ONE custom action: ActionValidateBooking for the business rules

The conversation is the same from the manager's perspective.
The machinery underneath is completely different.

CONVERSATION SCRIPTS
---------------------
Conversation 1 (happy path):
  You:    calling to confirm a booking
  Agent:  [asks guest count]
  You:    160 guests
  Agent:  [asks vegan count]
  You:    about 50 need vegan
  Agent:  [asks deposit]
  You:    £200 deposit
  Agent:  [confirms or escalates?]

Conversation 2 (deposit too high):
  Same as above but use a deposit above £300 (e.g. "£500 deposit").

Conversation 3 (out of scope):
  Start normally, then when asked for vegan count say something like
  "can you arrange parking for the speakers?" and observe what happens.
  Does CALM handle this differently than the old rules approach?
"""

# ── Conversation 1: Happy path ─────────────────────────────────────────────

CONVERSATION_1_TRACE = """
2026-04-14 01:06:36 INFO     root  - Rasa server is up and running.
Bot loaded. Type a message and press enter (use '/stop' to exit):
Your input ->  calling to confirm a booking
How many guests are you confirming for tonight's event?
Your input ->  160
And how many of those guests will need vegan meals?
Your input ->  50 need that
What deposit amount in GBP are you proposing to secure the booking?
Your input ->  200 is that enough
Thank you — booking confirmed. 160 guests, 50 requiring vegan meals, £200 deposit accepted. I'll send written confirmation to the organiser shortly.
Is there anything else I can help you with?
Your input ->  no thats it
Okay, I'll be around in case you need further help.
"""

CONVERSATION_1_OUTCOME = "confirmed"  # "confirmed" or "escalated"

# ── Conversation 2: Deposit too high ───────────────────────────────────────

CONVERSATION_2_TRACE = """
2026-04-14 01:11:10 INFO     root  - Rasa server is up and running.
Bot loaded. Type a message and press enter (use '/stop' to exit):
Your input ->   calling to confirm a booking
How many guests are you confirming for tonight's event?
Your input ->  160 approx
And how many of those guests will need vegan meals?
Your input ->  50 need it thats
What deposit amount in GBP are you proposing to secure the booking?
Your input ->  £500 deposit
I need to check one thing with the organiser before I can confirm. The issue is: a deposit of £500 exceeds the organiser's authorised limit of £300. Can I call you back within 15 minutes?
Is there anything else I can help you with?
Your input ->  no
"""

CONVERSATION_2_OUTCOME = "escalated"  # "confirmed" or "escalated"
CONVERSATION_2_REASON = "he issue is: a deposit of £500 exceeds the organiser's authorised limit of £300."  # the reason the agent gave for escalating

# ── Conversation 3: Out of scope ───────────────────────────────────────────

CONVERSATION_3_TRACE = """
Your input ->  calling to confirm a booking
How many guests are you confirming for tonight's event?
Your input ->  160 guests
And how many of those guests will need vegan meals?
Your input ->  can you arrange parking for the speakers?
I can only help with confirming tonight's venue booking. For anything else, please contact the event organiser directly.
Would you like to continue with confirm booking?
"""

# Describe what CALM did after the out-of-scope message. Min 20 words.
CONVERSATION_3_WHAT_HAPPENED = """
It picked the utter_out_of_scope flow in the execution flow. as described in th e
flows.yaml. It tries to forward out of scope requests to manager and tries to 
brinf the remainig/missing parts of the conversation in order.
"""

# Compare Rasa CALM's handling of the out-of-scope request to what
# LangGraph did in Exercise 2 Scenario 3. Min 40 words.
OUT_OF_SCOPE_COMPARISON = """
In comaprison, LangGraph was true to its core and did not know what to do. 
It responded with "I don't have access to that information"
However Rasa decided to not expose any limitations and confidently passes it on to a 
human intervention/escalation if the user needs more info.
"""

# ── Task B: Cutoff guard ───────────────────────────────────────────────────

TASK_B_DONE = True  # True or False

# List every file you changed.
TASK_B_FILES_CHANGED = ["actions/actions.py"]

# How did you test that it works? Min 20 words.
TASK_B_HOW_YOU_TESTED = """
The code only executes when 
time is above 16.45 and to test it I changed the if statement to True.
"""

# ── CALM vs Old Rasa ───────────────────────────────────────────────────────

# In the old open-source Rasa (3.6.x), you needed:
#   ValidateBookingConfirmationForm with regex to parse "about 160" → 160.0
#   nlu.yml intent examples to classify "I'm calling to confirm"
#   rules.yml to define every dialogue path
#
# In Rasa Pro CALM, you need:
#   flow descriptions so the LLM knows when to trigger confirm_booking
#   from_llm slot mappings so the LLM extracts values from natural speech
#   ONE action class (ActionValidateBooking) for the business rules
#
# What does this simplification cost? What does it gain?
# Min 30 words.

CALM_VS_OLD_RASA = """
Simple regex parsing is risky to get numbers wrong. sometimes the number could be 
written in text as 'one hundred sixty' instead of 160 and it may not be caught with regex.

Hoever LLM is more capable of capturing those differnet forms. Similary the LLM mode can 
capture several variations of the same text than trying to classify several variations of 
'im calling to confirm' in the old Rasa. 
Python still is used for ActionValidateBooking which validates the numerical values 
collected in all three slots. This action runs after guest_count, vegan_count, and 
deposit_amount_gbp are all collected and runs the deterministic business rule checks. 
"""

# ── The setup cost ─────────────────────────────────────────────────────────

# CALM still required: config.yml, domain.yml, flows.yml, endpoints.yml,
# rasa train, two terminals, and a Rasa Pro licence.
# The old Rasa ALSO needed nlu.yml, rules.yml, and a FormValidationAction.
#
# CALM is simpler. But it's still significantly more setup than LangGraph.
# That setup bought you something specific.
# Min 40 words.

SETUP_COST_VALUE = """
The setup cost bought a hard behavioural boundary. CALM cannot improvise a response
that is not defined in flows.yml, and it cannot call a tool that was not declared there.
In Conversation 3, when the manager asked about parking mid-booking, CALM responded:
"I can only help with confirming tonight's venue booking" and returned to the open slot —
it did not attempt to reason about the request, look anything up, or offer a workaround.
LangGraph would have tried to handle the question, possibly hallucinating an answer or
calling a tool in a way the task never anticipated. For the confirmation use case, this 
is a feature, not a limitation. The CALM agent
cannot talk itself into accepting a £500 deposit by reasoning "it's only £200 over,
probably fine." It cannot go off-script when Rod's legal and financial constraints are
at stake. Every path through the conversation is auditable you can read flows.yml and
actions.py and know exactly what the agent can and cannot do. The setup cost (config.yml,
domain.yml, flows.yml, endpoints.yml, licence, two terminals, retrain cycle) is the
price of that guarantee. LangGraph is cheaper to start but the guarantee does not exist.
"""
