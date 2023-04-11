Here is the core structural logic of how the game should work:

    1. Player_1 chooses a sign:
    1.1 This step is repeated until the player chooses a right sign [X,0]
    2. Player_1 chooses a position on the board:
    2.1 This step is repeated until the player chooses a right position [1,2,3,4,5,6,7,8,9]
    2.2 We check if the position is empty or already occupied by an X or a 0. If so, we go back to step 2.1
    3. After we have successfully placed the sign, we check for a winner
    4. If no winner, steps 2 and 3 are repeated for Player_2
    5. If no winner, steps 2 and 3 are repeated for Player_1
    6. If no winner, steps 2 and 3 are repeated for Player_2.....
    .....
    ....
    
### FlowChart
Here is a simple flow chart:

```mermaid
flowchart LR
    A(Player 1 or 2 chooses a sign)
    B{Sign is correct?}
    C(Player 1 or 2 chooses a board position)
    D{Position is correct and available?}
    E(Place the sign on the board)
    F{Check winner}
    G(There is a winner!)
    H(Check space left on board)
    I(There is space left)
    J(It's a draw!)
    
    A --> B
    B -->|No| A
    B -->|Yes| C
    C --> D
    D -->|No| C
    D -->|Yes| E    
    E --> F
    F -->|Yes| G
    F -->|No| H
    H --> I
    I --> |Yes| C 
    I --> |No| J   
```
