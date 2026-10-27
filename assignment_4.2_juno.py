"""Exercise 4.2 — Working with a dictionary

WHAT THE PROGRAM MUST DO
    Describe one real object from your field using a dictionary of at least five fields,
    then read it, change it, remove one field, and display every field with its value.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What object did you describe, which five fields did you choose, and why those?
       A field you would never actually use does not count.

WHAT THE AI CANNOT KNOW
    Your object and your fields. A campaign, a customer, a product, a store, a supplier.
    Choose something you would genuinely have to describe in your job.

CHECK IT YOURSELF
    Ask your program for a field that does not exist. Note what happens in a comment,
    then make it survive that case.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: Details about one example marketing campaign, stored as key-value pairs.
# 2. Process: Read a field, update the campaign's clicks, remove a temporary field,
#    safely try to read a field that is not present, and display all remaining fields.
# 3. Out: The selected campaign details, the missing-field message, and each
#    remaining field with its value.
# 4. The object is a marketing campaign. Its name, channel, budget, impressions, and
#    clicks describe its identity, planned spend, and performance.


# Your code below
# Create a campaign dictionary with five useful fields and a temporary note.
campaign = {
    "name": "Winter Sale",
    "channel": "Meta Ads",
    "budget_eur": 2500,
    "impressions": 283000,
    "clicks": 4838,
    "draft_note": "Check the final creative",
}

# Read values by their field names.
print("Campaign:", campaign["name"])
print("Channel:", campaign["channel"])

# Update an existing value by assigning a new value to its key.
campaign["clicks"] = 5000
print("Updated clicks:", campaign["clicks"])

# pop() removes the temporary field and returns the removed value.
removed_note = campaign.pop("draft_note")
print("Removed temporary note:", removed_note)

# Bracket lookup for a missing key would raise KeyError; get() safely returns a default.
missing_value = campaign.get("cost_per_conversion", "Not available")
print("Cost per conversion:", missing_value)

# Display every remaining field and its value.
print("All campaign fields:")
for field, value in campaign.items():
    print(field, "=", value)
