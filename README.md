# **Rock, Paper, Scissors: A Secure Game with Secret Bit Positions**

This Python project implements a **secure version** of the classic **Rock, Paper, Scissors** game. Players use a **secret bit position** to **hide their choices**, 
preventing the opponent from knowing their selection until the game result is revealed. This ensures there is **no cheating**, as the players cannot guess each other's choices.

### **How It Works:**
1. **Players choose** their move (Rock, Paper, or Scissors).
2. **Each player hides their choice** using a **secret bit position** from their input string.
3. The game uses the **bit position** to **map** the player's choice to a valid game option (Rock, Paper, or Scissors) using modulo arithmetic (`% 3`).
4. The game then resolves the winner based on standard **Rock, Paper, Scissors** rules:
   - **Rock beats Scissors**
   - **Paper beats Rock**
   - **Scissors beat Paper**
5. If the **bit position** entered by a player is **out of range** (greater than the length of their input string), the program will display an **error message**: `Invalid bit position!`.

### **Key Features:**
- **Cheating Prevention**: The secret bit position ensures that **no player can predict** the other's move.
- **Error Handling**: If a player enters an **invalid bit position**, the program will notify them and ask for a valid position.
- **Fair Play**: Each player’s choice is obfuscated by the secret bit position, ensuring the game remains **fair and unbiased**.
- **Interactive Gameplay**: Players input their choices and bit positions, and the game continues until they choose to stop.

### **Example Workflow:**

1. **First Game Round:**
    ```
    Player one, Enter your Choice: 789
    Player two, Enter your Choice: 456
    Player one, Enter the secret bit position: 2
    Player two, Enter the secret bit position: 1
    Draw
    Do you want to continue? (y/n): y
    ```

2. **Second Game Round (Invalid Bit Position):**
    ```
    Player one, Enter your Choice: 12
    Player two, Enter your Choice: 8
    Player one, Enter the secret bit position: 4
    Player two, Enter the secret bit position: 5
    Invalid bit position!
    Do you want to continue? (y/n): y
    ```

3. **Third Game Round:**
    ```
    Player one, Enter your Choice: 789
    Player two, Enter your Choice: 456
    Player one, Enter the secret bit position: 2
    Player two, Enter the secret bit position: 0
    Player one wins!!
    Do you want to continue? (y/n): n
    ```

This workflow demonstrates how the game progresses, including handling invalid bit positions and displaying results for each round.
