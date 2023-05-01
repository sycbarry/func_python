"""
Recursion and Complexity.
"""

def vote(
    voters: dict,
    politicians: dict,
    voter: str,
    politician: str)
    -> dict:
    voters[voter] = politician
    if politician in politicians:
        politicians[politician] += 1
    else:
        politicians[politician] = 1
    return voters,politicians

def voted_for(voters: dict, voter: str)
    -> str:
    return '%s voted for %s' % (voter, voters.get(voter, None))

def voters(politicians: dict, politician: str)
    -> str:
    return "%s receied %d vote(s)" % (politician, politicians.get(politician, 0))
