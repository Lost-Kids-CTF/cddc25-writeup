# Old Game

## Challenge (??? points, ??? solves)

They say this old game, a favourite of Star's, hides a secret...

nc cddc2025-challs-nlb-579269aea83cde66.elb.ap-southeast-1.amazonaws.com 6666

Flag format: CDDC2025{   }

## Summary

The challenge presents a terminal-based Minesweeper-style game where players can interact with the game by sending commands like `reveal`, `flag`, and directional movement commands.

## Analysis

The game is initialized with parameters:

```bash
-cols 10 -rows 10 -mines 99
```

That means nearly every cell is a mine. The game logic displays:

* `ROUND X/3 | MINES: 0/99`
* A 10x10 grid of cells
* A prompt to input commands (`>`)

Each round ends after 99 cells are flagged. After 3 such rounds, the flag is printed.

## Approach

The challenge does not penalize incorrect flagging, so we can first flag all cells on the board. Then we try to unflag and flag each cell, the moment we unflag a safe cell, the round ends (since all bomb cells are flagged and the single safe cell is currently not flagged) and we move to the next round.
