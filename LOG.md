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
- what it means: b1 uses the same model, image size and augmentation as the Track A baseline, but 4 epochs is only about 177,000 photos instead of 250,000. Its score is about 0.01 below baseline, more than the 0.003 seed noise, so I think it is lower mainly because it trained on fewer photos.

## 2026-11-09 no_flip (Track A)

- changed: removed the left-right flip (`T.RandomHorizontalFlip()`) from `train_transform`. The rest of the starter recipe is unchanged and the photos are still all training photos, so this is baseline without the flip.
- why: a flip turns signs into mirror writing and puts traffic on the wrong side, and Japan drives on the left while Korea and Taiwan drive on the right, so I thought it destroys clues.
- validation: 0.4926 (before: 0.4942 and 0.4971 from baseline seeds 0 and 1); seoul 0.5828, busan 0.3827, tokyo 0.6145, osaka 0.3492, taipei 0.5337.
- what it means: 0.4926 is within the seed noise of baseline, so removing the flip did not help; maybe signs and traffic direction are a small part of most photos.

## 2026-11-09 drop_nonstreet (Track A)

- changed: the starter recipe again (the left-right flip is back, nothing else in `recipe.py` differs from `baseline`) on a smaller selection. 85 training photos dropped with the reason "not a street scene": osaka 14, tokyo 22, seoul 12, busan 24, taipei 13, taken from the five suspect sheets of baseline seed 0. `selection.csv` went from 44,257 to 44,172 rows.
- why: my rule, written before I chose which photos to look at: drop training photos you could not see while walking a street — nature only, inside a room (museum, restaurant, office), exhibits, food, maps, a plane in the sky. Keep walkable covered spaces such as shopping arcades, underground malls and stations. Street photos that are just hard to tell from another city stay in.
- expected before seeing the result: little or no change, because 85 photos are only about 0.2% of the training set, and I only looked at the 48 most doubtful photos per city from every fourth training photo.
- validation: 0.4891 (before: 0.4942 and 0.4971 from baseline seeds 0 and 1); seoul 0.5815, busan 0.3799, tokyo 0.6236, osaka 0.3477, taipei 0.5127.
- what it means: as I predicted, removing 85 photos (0.2%) did not help. It came out about 0.005 below baseline, but with only one seed and per-city swings of 0.02-0.04 between seeds, I cannot tell whether that is a real drop or noise. To see a real effect I would have to apply the rule to all training photos, not only the 48 most doubtful per city.

## 2026-11-10 half (Track A)

- changed: the starter recipe unchanged (the recipe hash `17ac485223fa` is still the same as baseline), but on a random half of the photos: `scripts/make_selection.py` seeded 0 kept half of every city's training photos and left the 85 already-dropped photos out, so `selection.csv` went from 44,172 rows to 22,088 rows (seoul 5632, busan 2581, tokyo 6670, osaka 3590, taipei 3615). The budget is still 249,984 photos through the network, so each photo was seen about 11 times instead of about 6. This run took the CPU of this computer, not Colab's GPU.
- why: to see whether the amount of training photos matters, without collecting new photos: if half the photos gives a much lower score, more photos would probably help.
- validation: 0.4798 (before: 0.4942 and 0.4971 from baseline seeds 0 and 1); seoul 0.5906, busan 0.377, tokyo 0.5826, osaka 0.3463, taipei 0.5025.
- what it means: half scored about 0.015 below baseline, about three times the 0.005 that I treat as possible noise, so I think the amount of photos really matters, and collecting more photos is the most promising next step. Caveats: one seed only, and this run used the CPU while baseline used Colab's GPU.
- biggest difference: this is the change that made the biggest difference, in the wrong direction: flip and cleaning changed nothing measurable, the amount of data did.

## Plan

- half: collecting more photos is the most promising next step, because the amount of training photos is the one thing that moved the score.
- drop_nonstreet: apply the rule to all training photos, not only the 48 most doubtful per city.
