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
graph TD;
    Start((Start))-->1(Player_1 chooses a sign);
    1-->|Repeat until right sign|1.1(Player_1 chooses a sign [X,0]);
    1.1-->2(Player_1 chooses a position on the board);
    2-->|Repeat until right position|2.1(Player_1 chooses a right position [1,2,3,4,5,6,7,8,9]);
    2.1-->|Check if position is empty or occupied|2.2(We check if the position is empty or already occupied by an X or a 0);
    2.2--|If position is not empty|->2.1;
    2.2--|If position is empty|->3(Check for winner);
    3-->|If there is a winner|End(End);
    3-->|If no winner|4(Player_2 chooses a sign);
    4-->|Repeat until right sign|4.1(Player_2 chooses a sign [X,0]);
    4.1-->5(Player_2 chooses a position on the board);
    5-->|Repeat until right position|5.1(Player_2 chooses a right position [1,2,3,4,5,6,7,8,9]);
    5.1-->|Check if position is empty or occupied|5.2(We check if the position is empty or already occupied by an X or a 0);
    5.2--|If position is not empty|->5.1;
    5.2--|If position is empty|->6(Check for winner);
    6-->|If there is a winner|End;
    6-->|If no winner|1;
```
