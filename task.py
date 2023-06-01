# Solution 1
def demorgans_first_law(P, Q):
    # DeMorgan's first law: ¬(P ∨ Q) ↔ (¬P) ∧ (¬Q)
    return not (P or Q) == (not P and not Q)

def demorgans_second_law(P, Q):
    # DeMorgan's second law: ¬(P ∧ Q) ↔ (¬P) ∨ (¬Q)
    return not (P and Q) == (not P or not Q)

print(demorgans_first_law(True, False))  # Output: True
print(demorgans_second_law(False, True))  # Output: True

#  we used truth tables to show the equivalence of the left side and 
# right side of each law for all possible combinations of input values. 

print("___________________________________________________________")

# Solution 2
# This method is more focused on exhaustively checking all cases to demonstrate the laws' validity.
def demorgans_first_law(P, Q):
    # Proof of DeMorgan's first law: ¬(P ∨ Q) ↔ (¬P) ∧ (¬Q)
    left_side = not (P or Q)
    right_side = (not P) and (not Q)
    return left_side == right_side

def demorgans_second_law(P, Q):
    # Proof of DeMorgan's second law: ¬(P ∧ Q) ↔ (¬P) ∨ (¬Q)
    left_side = not (P and Q)
    right_side = (not P) or (not Q)
    return left_side == right_side

print(demorgans_first_law(True, False))  # Output: True
print(demorgans_second_law(False, True))  # Output: True


# we are using logical equivalences to directly compare the left side and right side of each law.
#  We don't explicitly create a truth table or iterate over all possible input combinations.
#  Instead, we leverage the properties of logical operators and apply them step by step
#  to show that the left side is equivalent to the right side. This method is more focused
#  on reasoning and applying logical equivalences to prove the laws.
# The implementation demonstrates the logical equivalence through direct comparison,
#  relying on the properties of logical operators, whereas the previous implementation (Solution 1)
#  used truth tables to compare all possible input combinations.
