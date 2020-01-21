# boxesandgrids
CS165a Programming Assignment 1

I used [sampleboxesandgrids.py](sampleboxesandgrids.py) for this assignment.

The algorithm is pretty simple - since each possible move has a score value, it simply evaluates the best move based on the best possible overall score delta, by tracking the score deltas separately for player 1 and player 2 across possible board states. It doesn't traverse the whole tree, due to the heuristic tracking the possible score deltas at every step, so it completes very quickly; it's also smarter than a generic greedy algorithm like the one implemented in player 1's AI, as player 2 pretty predictably goes 29-7 against player 1 using this implementation.

Otherwise, it's a relatively standard implementation of minmax/alpha beta pruning. 
