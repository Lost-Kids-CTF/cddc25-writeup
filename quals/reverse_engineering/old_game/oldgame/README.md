# Old Game

## Build
```
./build.sh 
./run.sh
nc localhost 6666
```

## Parameters
```
  -cols int
    	Number of Columns  (default 15)
  -rows int
    	Number of Rows (default 15)
  -mines int
    	Number of Mines (default 40)
```

## Play Guides
```

    ROUND 1/3 | MINES: 0/50

    [□] □  □  □  □  □  □  □  □  □  □  □  □  □  □
     □  □  □  □  □  □  □  □  □  □  □  □  □  □  □
     □  □  □  □  □  □  □  □  □  □  □  □  □  □  □
     □  □  □  □  □  □  □  □  □  □  □  □  □  □  □
     □  □  □  □  □  □  □  □  □  □  □  □  □  □  □
     □  □  □  □  □  □  □  □  □  □  □  □  □  □  □
     □  □  □  □  □  □  □  □  □  □  □  □  □  □  □
     □  □  □  □  □  □  □  □  □  □  □  □  □  □  □
     □  □  □  □  □  □  □  □  □  □  □  □  □  □  □
     □  □  □  □  □  □  □  □  □  □  □  □  □  □  □
     □  □  □  □  □  □  □  □  □  □  □  □  □  □  □
     □  □  □  □  □  □  □  □  □  □  □  □  □  □  □
     □  □  □  □  □  □  □  □  □  □  □  □  □  □  □
     □  □  □  □  □  □  □  □  □  □  □  □  □  □  □
     □  □  □  □  □  □  □  □  □  □  □  □  □  □  □
> help

Commands:
  up, down, left, right - Move cursor
  reveal - Reveal current cell
  flag - Toggle flag on current cell
  quit - Exit game
  help - Show this help message
>
```

## Challenge
```
./oldgame -cols 10 -rows 10 -mines 99
```

