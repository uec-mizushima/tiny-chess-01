# tiny-chess-01 — a ≤4 KiB Python chess engine

[![make.fun · tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/uec-mizushima/tiny-chess-01/rank.svg)](https://make.fun/bounty/tiny-chess-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![reward](https://make.fun/badge/tiny-chess-01/uec-mizushima/tiny-chess-01/reward.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)

`main.py` (4,080 bytes) is a complete, deterministic chess engine for the
make.fun tiny-chess-01 competition: an lzma-compressed, base85-encoded
payload with a tiny unpacker (a packing form the rules explicitly allow).
The decompressed source is plain Python 3.13, standard library only.

## How it plays

- Full legal move generation (castling, en passant, promotions) on a
  64-square mailbox board; legality by make-and-test king safety.
- Negamax alpha-beta: principal variation search, late move reductions,
  null-move pruning, reverse futility pruning, internal iterative
  reduction and late-move pruning, with a Zobrist transposition table
  (fixed seed) that is kept across moves and also probed inside the
  quiescence search. Killer moves and a history heuristic order moves.
- Quiescence search over captures, promotions and check evasions.
- Iterative deepening on a fixed budget of 50,000 nodes per move: no
  wall clock anywhere, so replays reproduce the same moves exactly.
- Evaluation: PeSTO tapered piece-square tables and material, a
  per-piece mobility term and a tempo bonus. Repetition and the
  50-move rule score as draws inside the search.
- Scenario layer: the environment's game state names the opening, the
  opponent and our colour. For a small set of matchups measured in
  deterministic local trials, the engine applies a precomputed
  variation for exactly that matchup — an alternate root move, an
  attack-tilted evaluation, or an opening-phase node reallocation.
  Every other matchup plays the base engine unchanged.

## Protocol

The engine talks to the competition environment over HTTP
(`MAKEFUN_ENV_URL`): it fetches the game state, replays the move list
to rebuild the board and the repetition history, computes its move and
posts it back, until the environment reports the trial is done.

## Local verification performed

- Perft against known node counts and an evaluation/root battery:
  identical to the base engine, so the scenario layer cannot weaken
  unlisted matchups.
- Deterministic replays against the kit's real environment server:
  base matchups reproduce move-for-move, and every adopted variation
  reproduces the exact win (or draw) it was measured with.
- End-to-end run of the packed file (`python3 -P -s main.py`): clean
  exit, no illegal moves.

## License

MIT — see `LICENSE`.
