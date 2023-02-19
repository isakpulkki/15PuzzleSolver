# Week 4

* Pattern database builder implemented
* IDA* algorithm almost implemented

## What I have done

Implemented a pattern database that uses different groups of numbers to calculate heuristics by considering only different permutations within those groups. Also created a hashing function for the puzzle to enable faster access to nodes visited and closed for updating values. Also implemented parallel processing for faster searching, since the permutations are independent of each other.

## Encountered problems

Encountered a long wait time when using a (6, 6, 3) grouping for the pattern database builder, with 5765760 permutations, leading to the adoption of a (5, 5, 5) grouping that only had 524160 permutations, computed as nPr(16, 5).

## What to do next

The program is almost complete, with the IDA* algorithm being the only remaining task to use the additive pattern database and provide the GUI program with a list of directions. This will be completed next week.

## Hours used

I used about 12 hours in total coding the application and researching about data structures and algorithms.