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

## 2026-11-09 baseline (Track A)

- changed: nothing. The starter recipe on all training photos (44,257), first with seed 0 and then with seed 1.
- why: to have a reference, and to see how much the score moves by chance when only the seed changes.
- validation: 0.4942 with seed 0 and 0.4971 with seed 1 (seed 0 per city: seoul 0.5717, busan 0.3914, tokyo 0.6406, osaka 0.3228, taipei 0.5444).
- what it means: the two seeds differ by about 0.003, so a change has to move the score by more than that before I believe it.

## 2026-11-09 b1 (Track B)

- changed: `train_b.py` as it came — resnet18 at 224 px, 4 epochs, batch 64, no balancing, on every photo in `data/starter/train`.
- why: to have a valid Track B submission and a reference for later Track B changes.
- validation: 0.4835 (seoul 0.591, busan 0.3791, tokyo 0.5986, osaka 0.3369, taipei 0.5118).
- what it means: not answered yet.

## 2026-11-09 no_flip (Track A)

- changed: removed the left-right flip (`T.RandomHorizontalFlip()`) from `train_transform`. The rest of the starter recipe is unchanged and the photos are still all training photos, so this is baseline without the flip.
- why: a flip turns signs into mirror writing and puts traffic on the wrong side, and Japan drives on the left while Korea and Taiwan drive on the right, so I thought it destroys clues.
- validation: 0.4926 (before: 0.4942 and 0.4971 from baseline seeds 0 and 1); seoul 0.5828, busan 0.3827, tokyo 0.6145, osaka 0.3492, taipei 0.5337.
- what it means: 0.4926 is within the seed noise of baseline, so removing the flip did not help; maybe signs and traffic direction are a small part of most photos.

## 2026-11-09 drop_nonstreet (Track A)

- changed: the starter recipe again (the left-right flip is back, nothing else in `recipe.py` differs from `baseline`) on a smaller selection. 85 training photos dropped with the reason "not a street scene": osaka 14, tokyo 22, seoul 12, busan 24, taipei 13, taken from the five suspect sheets of baseline seed 0. `selection.csv` went from 44,257 to 44,172 rows.
- why: my rule, written before I chose which photos to look at: drop training photos you could not see while walking a street — nature only, inside a room (museum, restaurant, office), exhibits, food, maps, a plane in the sky. Keep walkable covered spaces such as shopping arcades, underground malls and stations. Street photos that are just hard to tell from another city stay in.
- expected before seeing the result: little or no change, because 85 photos are only about 0.2% of the training set, and I only looked at the 48 most doubtful photos per city from every fourth training photo.
- validation: pending — the run is on Colab.
