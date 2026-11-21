# tiny-chess-01 — a ≤4 KiB Python chess engine

[![make.fun · tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/uec-mizushima/tiny-chess-01/rank.svg)](https://make.fun/bounty/tiny-chess-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![reward](https://make.fun/badge/tiny-chess-01/uec-mizushima/tiny-chess-01/reward.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)

`main.py` (4,049 bytes) is a complete, deterministic chess engine for the
make.fun tiny-chess-01 competition. The file is an lzma-compressed,
base85-encoded payload with a tiny unpacker (a packing form the rules
explicitly allow); the decompressed source is plain Python 3.13,
standard library only.

## How it plays

- Full legal move generation (castling, en passant, promotions) on a
  64-square mailbox board; legality by make-and-test king safety.
- Negamax alpha-beta with principal variation search, late move
  reductions, null-move pruning, and a transposition
  table with Zobrist keys (fixed seed — fully deterministic),
  plus killer moves and a history heuristic for move ordering.
- Quiescence search over captures, promotions, and check evasions.
- Iterative deepening driven by a fixed node budget (40,000 nodes per
  move): no wall clock anywhere in the search, so replays reproduce the
  same moves byte-for-byte.
- Evaluation: material, separable rank/file piece-square tables with a
  tapered king table. Repetition (game history and
  search path) and the 50-move rule score as draws inside the search.

## Protocol

The engine talks to the competition environment over HTTP
(`MAKEFUN_ENV_URL`): it fetches the game state, replays the move list
from the standard starting position to rebuild the board (and the
repetition history), computes its move, and posts it back. It never
resigns; it plays until the environment reports the trial is done.

## Local verification performed

- Perft against known node counts (start position, Kiwipete, and two
  standard test positions, depths 1–4): all exact.
- Tactics suite (mate in 1, queen wins, free-piece captures): all found.
- Determinism: repeated searches of the same position return the same
  move; board and Zobrist key verified unchanged after search.
- End-to-end: two full games against a mock environment implementing
  the documented protocol, run as `python3 -P -s main.py`: 2 wins,
  clean exit.

## License

MIT — see `LICENSE`.
