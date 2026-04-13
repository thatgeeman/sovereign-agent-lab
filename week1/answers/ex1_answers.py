"""
Exercise 1 — Answers
====================
Fill this in after running exercise1_context.py.
Run `python grade.py ex1` to check for obvious issues before submitting.
"""

# ── Part A ─────────────────────────────────────────────────────────────────

# The exact answer the model gave for each condition.
# Copy-paste from your terminal output (the → "..." part).

PART_A_PLAIN_ANSWER = "The Haymarket Vaults"
PART_A_XML_ANSWER = "The Albanach"
PART_A_SANDWICH_ANSWER = "The Albanach"

# Was each answer correct? True or False.
# Correct = contains "Haymarket" or "Albanach" (both satisfy all constraints).

PART_A_PLAIN_CORRECT = True  # True or False
PART_A_XML_CORRECT = True
PART_A_SANDWICH_CORRECT = True

# Explain what you observed. Minimum 30 words.

PART_A_EXPLANATION = """
In part A, all approaches got the answer correct. 
However providing the options as an XML shows a primcay bias for these models and the 
answer that appears first is selected by the LLM. 
The same is true for sandwich (XML+query repeat).
"""

# ── Part B ─────────────────────────────────────────────────────────────────

PART_B_PLAIN_ANSWER = "The Haymarket Vaults"
PART_B_XML_ANSWER = "The Albanach"
PART_B_SANDWICH_ANSWER = "The Albanach"

PART_B_PLAIN_CORRECT = True
PART_B_XML_CORRECT = True
PART_B_SANDWICH_CORRECT = True

# Did adding near-miss distractors change any results? True or False.
PART_B_CHANGED_RESULTS = False

# Which distractor was more likely to cause a wrong answer, and why?
# Minimum 20 words.
PART_B_HARDEST_DISTRACTOR = """
The distractor did not seem to affect the answers and remained the 
same as the Baseline approach (Partt A). The most likely distractor 
would have been 'The Holyrood Arms' as it satisfies all criterion except being available
and sits close to 'The Haymarket Vaults'. This would've been a perfect example of 
attention "blurs" adjacent similar items, but ws not observed in this case.
This may be due to the small amount of text. With larger text/corpus, this may become 
even more visible.
"""

# ── Part C ─────────────────────────────────────────────────────────────────

# Did the exercise run Part C (small model)?
# Check outputs/ex1_results.json → "part_c_was_run"
PART_C_WAS_RUN = True  # True or False

PART_C_PLAIN_ANSWER = "The Haymarket Vaults"
PART_C_XML_ANSWER = "The Haymarket Vaults"
PART_C_SANDWICH_ANSWER = "The Haymarket Vaults"

# Explain what Part C showed, or why it wasn't needed. Minimum 30 words.
PART_C_EXPLANATION = """
WSith the small model, the answer is the same acroos all data formats.
Even with XML and sandwich approaches. It goes to show that if the data
is structured properly the model (however small) may find it easier to 
retrieve the answer from the haystack. Value of XML is seen. The primacy bias is 
not anymore visible with these models and seem to work consistenly with small models.
"""

# ── Core lesson ────────────────────────────────────────────────────────────

# Complete this sentence. Minimum 40 words.
# "Context formatting matters most when..."

CORE_LESSON = """
Context formatting matters most for smaller models. For larger capacity models, the 
effect seems to be smaller. Hoever as the corpus or text grows, it may be also be important
for larger and smaller models, as 
attention "blurs" for adjacent similar items may become more prominent.
"""
