"""Write track_a/selection.csv: a random half of the training photos.

Every city keeps half of its training photos, drawn with one fixed seed, so the
same command always writes the same file. Photos that `curate.py drop` already
took out (track_a/dropped.csv) stay out: this script never puts back a photo
that was dropped for a reason.

    python scripts/make_selection.py            half of every city, seed 0
    python scripts/make_selection.py --seed 1   the same, with another draw

The recipe is not touched: this only changes which photos official.py trains on.
Print the result with `uv run python src/curate.py count`.
"""

import argparse
import csv
import random
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

import rules  # noqa: E402
from rules import CITIES  # noqa: E402

TRAIN = ROOT / "data" / "starter" / "train"
SELECTION = ROOT / "track_a" / "selection.csv"
DROPPED = ROOT / "track_a" / "dropped.csv"


def dropped_paths():
    """Paths that curate.py drop took out of the selection, with their reasons."""
    if not DROPPED.exists():
        return set()
    with open(DROPPED, newline="", encoding="utf-8") as f:
        return {r["path"] for r in csv.DictReader(f)}


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--seed", type=int, default=0, help="the seed for the draw (default 0)")
    args = ap.parse_args()

    every = [f"{city}/{path.name}" for path, city in rules.list_photos(TRAIN)]
    dropped = dropped_paths()
    rng = random.Random(args.seed)
    chosen = []
    for city in CITIES:
        mine = [p for p in every if p.split("/")[0] == city]
        rng.shuffle(mine)
        half = mine[:len(mine) // 2]
        kept = [p for p in half if p not in dropped]
        chosen += kept
        print(f"{city:8s} {len(kept):6d} of {len(mine):6d} photos"
              f"  ({len(half) - len(kept)} of the half were already dropped)")
    chosen.sort()
    SELECTION.parent.mkdir(parents=True, exist_ok=True)
    with open(SELECTION, "w", newline="", encoding="utf-8") as f:
        f.write("path\n" + "".join(p + "\n" for p in chosen))
    print(f"wrote {SELECTION.relative_to(ROOT).as_posix()}: {len(chosen)} photos, seed {args.seed}")


if __name__ == "__main__":
    main()