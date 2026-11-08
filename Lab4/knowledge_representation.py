"""Toy semantic network and forward-chaining rule engine."""
FACTS = {
    ("Tweety", "is_a", "Bird"),
    ("Bird", "has", "Wings"),
    ("Bird", "can", "LayEggs"),
}

RULES = [
    # If X is a Bird, infer that X has Wings.
    (("is_a", "Bird"), ("has", "Wings")),
    (("is_a", "Bird"), ("can", "LayEggs")),
]

def infer(subject, facts=FACTS):
    conclusions = set()
    for (relation, category), (new_relation, value) in RULES:
        if (subject, relation, category) in facts:
            conclusions.add((subject, new_relation, value))
    return conclusions

if __name__ == "__main__":
    print("Known facts:")
    for fact in sorted(FACTS): print(fact)
    print("\nInferred facts:")
    for fact in sorted(infer("Tweety")): print(fact)
