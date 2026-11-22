# tiny-chess-01 — a ≤4 KiB Python chess engine

[![make.fun · tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/uec-mizushima/tiny-chess-01/rank.svg)](https://make.fun/bounty/tiny-chess-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![reward](https://make.fun/badge/tiny-chess-01/uec-mizushima/tiny-chess-01/reward.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)

`main.py` (3,917 bytes) is a complete, deterministic chess engine for the
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

## Protocol

The engine talks to the competition environment over HTTP
(`MAKEFUN_ENV_URL`): it fetches the game state, replays the move list
to rebuild the board and the repetition history, computes its move and
posts it back, until the environment reports the trial is done.

## Local verification performed

- Perft against known node counts (start position, Kiwipete and two
  standard test positions, depths 1–4): all exact.
- Sanity and tactics checks (mate in 1, hanging-piece captures): all
  found; repeated searches of the same position return the same move.
- End-to-end games against the kit's real environment server, run as
  `python3 -P -s main.py`: clean exits, no illegal moves.
- Local trials against the kit's practice gauntlet (six house engines,
  Elo anchors 855–1596): 5 wins, 1 draw, 0 losses on practice set 0.

## License

MIT — see `LICENSE`.
