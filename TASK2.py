import random
 # Rock, Paper, Scissors Game
R = "\033[31m"  # Red
G = "\033[32m"  # Green
Y = "\033[33m"  # Yellow
B = "\033[34m"  # Blue
C = "\033[36m"  # Cyan
W = "\033[37m"  # White
RESET = "\033[0m" # Resets all formatting

# GAME RULES
# Store game elements and outcomes in dictionaries for briefness and clarity.
# Each element can win against one and lose against another.
# The game will be played until one player reaches the target score.
GAME_ELEMENTS = ["ROCK", "PAPER", "SCISSORS"]
OUTCOMES = {
    ("ROCK", "SCISSORS"): "win",
    ("PAPER", "ROCK"): "win",
    ("SCISSORS", "PAPER"): "win",
    ("ROCK", "PAPER"): "lose",
    ("PAPER", "SCISSORS"): "lose",
    ("SCISSORS", "ROCK"): "lose"
}
MESSAGES = {
    "intro": f"{C}--- Quick Play: Rock, Paper, Scissors! ---{RESET}",
    "prompt_rounds": f"{Y}Target Score? {RESET}",
    "prompt_choice": f"{C}Your move ({'/'.join(GAME_ELEMENTS)}) or 'Q' to quit: {RESET}",
    "invalid_round": f"{R}Must be a positive number. Try again.{RESET}",
    "invalid_choice": f"{R}Invalid move. Choose from {', '.join(GAME_ELEMENTS)}.{RESET}",
    "tie": f"{Y}It's a tie!{RESET}",
    "win": f"{G}You win this round!{RESET}",
    "lose": f"{R}Computer wins this round!{RESET}",
    "player_reveals": f"You show: {B}",
    "computer_reveals": f"Comp shows: {R}",
    "final_score": f"{W}Final Score:{RESET}",
    "player_won_game": f"{G} VICTORY! YOU ARE THE UNDISPUTED CHAMPION!{RESET}",
    "computer_won_game": f"{R} :( COMPUTER IS THE CHAMPION!{RESET}",
    "game_quit": f"{Y}Game halted. Hope to play again soon!{RESET}",
    "thanks": f"{C}Thanks for playing! Until our next match!{RESET}"
}

# ___ Core Game Functions ___

def get_valid_int_input(prompt):
    #Gets and validates a positive integer input.
    while True:
        try:
            value = int(input(prompt).strip())
            if value > 0:
                return value
            print(MESSAGES["invalid_round"])
        except ValueError:
            print(MESSAGES["invalid_round"])

def get_player_move(valid_options):
    # Tells the player to input their move and checks the valid options.
    while True:
        move = input(MESSAGES["prompt_choice"]).strip().upper()
        if move == 'Q' or move in valid_options:
            return move
        print(MESSAGES["invalid_choice"])

def determine_round_result(player_move, computer_move):
    #Determines if player wins, loses, or ties the round.
    if player_move == computer_move:
        return "tie"
    # Use the pre-defined OUTCOMES dictionary
    if (player_move, computer_move) in OUTCOMES:
        return OUTCOMES[(player_move, computer_move)]
    # This else handles the case where player_move beats computer_move indirectly
    # e.g., if (comp_move, player_move) is in OUTCOMES, then player_move lost
    # but since we already checked direct player wins, it must be a loss.
    return "lose" # Should not be reached if OUTCOMES covers all specific wins/losses and ties are handled.

def display_scores(player_s, comp_s, target_s):
    #Prints current scores concisely.
    print(f"{W}Score:{RESET} You {G}{player_s}{RESET} | Comp {R}{comp_s}{RESET} (First to {target_s})")

# *** Main Game Loop ***

def play_game():
    #Manages the overall flow of the Rock-Paper-Scissors game.
    print(MESSAGES["intro"])

    player_score = 0
    computer_score = 0
    target_score = get_valid_int_input(MESSAGES["prompt_rounds"])

    while player_score < target_score and computer_score < target_score:
        display_scores(player_score, computer_score, target_score)

        player_move = get_player_move(GAME_ELEMENTS)
        if player_move == 'Q':
            break

        computer_move = random.choice(GAME_ELEMENTS)

        print(f"{MESSAGES['player_reveals']}{player_move}{RESET}")
        print(f"{MESSAGES['computer_reveals']}{computer_move}{RESET}")

        result_type = determine_round_result(player_move, computer_move)
        print(MESSAGES[result_type]) # It will print the outcome message.

        if result_type == "win":
            player_score += 1
        elif result_type == "lose":
            computer_score += 1
        
        print("-" * 30) # Separator

    # *** Game End Summary ***
    print(f"\n{MESSAGES['final_score']}")
    display_scores(player_score, computer_score, target_score)

    if player_score >= target_score:
        print(MESSAGES["player_won_game"])
    elif computer_score >= target_score:
        print(MESSAGES["computer_won_game"])
    else: # Game terminated due to 'Q'
        print(MESSAGES["game_quit"])

    print(MESSAGES["thanks"])

# *** Let's Run the Game ***
if __name__ == '__main__':
    play_game()