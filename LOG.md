# Log

One entry for each recipe, selection or Track B model you train, newest at
the bottom. The numbers come from `experiments.csv`. "Why" and "what it means"
are in your own words: your agent asks you for them and does not make them up.
End the log with your plan for what to try next.

<!-- The form of an entry:

## <date> <tag> (Track A or B)
- changed: what is different from the run before
- why: your reason
- validation: 0.000 (before: 0.000)
- what it means: what you think the result says
-->

## 2026-11-09 drop_nonstreet (Track A)

- changed: the starter recipe again (the left-right flip is back, nothing else in `recipe.py` differs from `baseline`) on a smaller selection. 85 training photos dropped with the reason "not a street scene": osaka 14, tokyo 22, seoul 12, busan 24, taipei 13, taken from the five suspect sheets of baseline seed 0. `selection.csv` went from 44,257 to 44,172 rows.
- why: my rule, written before I chose which photos to look at: drop training photos you could not see while walking a street — nature only, inside a room (museum, restaurant, office), exhibits, food, maps, a plane in the sky. Keep walkable covered spaces such as shopping arcades, underground malls and stations. Street photos that are just hard to tell from another city stay in.
- expected before seeing the result: little or no change, because 85 photos are only about 0.2% of the training set, and I only looked at the 48 most doubtful photos per city from every fourth training photo.
- validation: pending — the run is on Colab.
