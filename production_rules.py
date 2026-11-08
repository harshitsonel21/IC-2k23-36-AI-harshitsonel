"""Simple production-rule system for a toy troubleshooting example."""
RULES = [
    (lambda facts: facts.get("power") is False, "Check the power cable."),
    (lambda facts: facts.get("power") is True and facts.get("screen") is False,
     "Check the display connection."),
    (lambda facts: facts.get("power") is True and facts.get("screen") is True,
     "The basic power and display checks passed."),
]

def infer(facts):
    """Return conclusions for all matching rules."""
    return [message for condition, message in RULES if condition(facts)]

if __name__ == "__main__":
    sample = {"power": True, "screen": False}
    print("Facts:", sample)
    print("Conclusions:", infer(sample))
