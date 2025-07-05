#Password generators empower users to create the robust, unpredictable, and unique passwords necessary to protect their digital identity
# and sensitive information from ever-evolving cyber threats.
# User Input: Prompt the user to specify the desired length of the password.
# Generate Password: Use a combination of random characters to generate a password of the specified length.
# Display the Password: Print the generated password on the screen.

# Password Generator Application
import tkinter as tk
from tkinter import ttk  
import tkinter.messagebox as msg
import random
import string # Essential for character sets

# Constants and Configuration
APP_WIDTH = 550
APP_HEIGHT = 300
MIN_PASS_LENGTH = 4
MAX_PASS_LENGTH = 80

# Character sets for password generation
CHAR_SETS = {
    "uppercase": string.ascii_uppercase,
    "lowercase": string.ascii_lowercase,
    "digits": string.digits,
    "special_chars": string.punctuation # Comprehensive punctuation
}

#  Password Generation Logic 

def generate_password(length, strength):
    """
    Generates a password of specified length and strength.
    Ensures complexity requirements are met directly.
    """
    all_chars = []
    guaranteed_chars = [] # Characters to ensure are in the password

    # Always include letters for 'low' and above
    all_chars.extend(list(CHAR_SETS["uppercase"]))
    all_chars.extend(list(CHAR_SETS["lowercase"]))

    if strength == "low":
        pass # Only letters

    elif strength == "medium":
        all_chars.extend(list(CHAR_SETS["digits"]))
        # Guarantee at least one uppercase, one lowercase, one digit
        guaranteed_chars.append(random.choice(CHAR_SETS["uppercase"]))
        guaranteed_chars.append(random.choice(CHAR_SETS["lowercase"]))
        guaranteed_chars.append(random.choice(CHAR_SETS["digits"]))

    elif strength == "high":
        all_chars.extend(list(CHAR_SETS["digits"]))
        all_chars.extend(list(CHAR_SETS["special_chars"]))
        # Guarantee at least one uppercase, one lowercase, one digit, one special char
        guaranteed_chars.append(random.choice(CHAR_SETS["uppercase"]))
        guaranteed_chars.append(random.choice(CHAR_SETS["lowercase"]))
        guaranteed_chars.append(random.choice(CHAR_SETS["digits"]))
        guaranteed_chars.append(random.choice(CHAR_SETS["special_chars"]))

    # If the length is less than the number of guaranteed chars,
    # the password might not meet the minimum length requirement for complexity
    # This case should ideally be handled by UI constraints (min length based on strength)
    # For now, we'll just use min(length, len(guaranteed_chars))
    if len(guaranteed_chars) > length:
        return "Error: Length too short for selected strength."

    # Generate remaining characters
    remaining_length = length - len(guaranteed_chars)
    if remaining_length < 0: remaining_length = 0 # Safety check

    random_chars = [random.choice(all_chars) for _ in range(remaining_length)]

    # Combine guaranteed and random characters, then shuffle to mix
    final_password_list = guaranteed_chars + random_chars
    random.shuffle(final_password_list)

    return "".join(final_password_list)

# GUI Setup Functions 

def create_main_window():
    """Initializes and configures the main Tkinter window."""
    root = tk.Tk()
    root.title("SecurePass Generator") # Unique title
    root.resizable(False, False)

    # Center the window
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    set_x = int((screen_width / 2) - (APP_WIDTH / 2))
    set_y = int((screen_height / 2) - (APP_HEIGHT / 2))
    root.geometry(f'{APP_WIDTH}x{APP_HEIGHT}+{set_x}+{set_y}')

    # Apply a modern theme (e.g., 'clam', 'alt', 'default', 'winnative', 'xpnative')
    style = ttk.Style()
    style.theme_use('clam') # 'clam' often looks cleaner

    return root

def setup_ui_elements(root):
    """Sets up all widgets and their layout using grid."""
    # Main container frame (optional, but good for structure)
    main_frame = ttk.Frame(root, padding="15 15 15 15")
    main_frame.grid(row=0, column=0, sticky="nsew")
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)

    #  Title Label
    title_label = ttk.Label(main_frame, text="Password Forge", font=("Arial", 20, "bold"))
    title_label.grid(row=0, column=0, columnspan=3, pady=(0, 20))

    #  Password Length Input 
    length_label = ttk.Label(main_frame, text="Length:", font=("Arial", 12))
    length_label.grid(row=1, column=0, sticky="w", padx=(0, 10))

    length_entry = ttk.Entry(main_frame, width=5, font=("Arial", 12))
    length_entry.insert(0, "12") # Default length
    length_entry.grid(row=1, column=1, sticky="w")

    # Password Strength Selection
    strength_label = ttk.Label(main_frame, text="Strength:", font=("Arial", 12))
    strength_label.grid(row=2, column=0, sticky="w", pady=(15, 0), padx=(0, 10))

    strength_var = tk.StringVar(value="high") # Default to high
    radio_frame = ttk.Frame(main_frame)
    radio_frame.grid(row=2, column=1, columnspan=2, sticky="w", pady=(15, 0))

    ttk.Radiobutton(radio_frame, text="Low (aA)", variable=strength_var, value="low").pack(side="left", padx=(0, 15))
    ttk.Radiobutton(radio_frame, text="Medium (aA1)", variable=strength_var, value="medium").pack(side="left", padx=(0, 15))
    ttk.Radiobutton(radio_frame, text="High (aA1#)", variable=strength_var, value="high").pack(side="left", padx=(0, 15))

    #  Generated Password Output 
    output_label = ttk.Label(main_frame, text="Generated Password:", font=("Arial", 12))
    output_label.grid(row=3, column=0, sticky="w", pady=(20, 5))

    # Use an Entry widget for the output password, making it read-only
    generated_pass_entry = ttk.Entry(main_frame, width=45, font=("Courier New", 12), state="readonly")
    generated_pass_entry.grid(row=4, column=0, columnspan=3, sticky="ew")

    #  Generate Button
    generate_button = ttk.Button(main_frame, text="FORGE PASSWORD",
                                 command=lambda: on_generate_button_click(
                                     length_entry, strength_var, generated_pass_entry
                                 ))
    generate_button.grid(row=5, column=0, columnspan=3, pady=(20, 0))

    # Configure columns for responsiveness (optional but good practice with grid)
    main_frame.grid_columnconfigure(0, weight=0) # Labels minimal width
    main_frame.grid_columnconfigure(1, weight=1) # Entry/Radiobuttons expand
    main_frame.grid_columnconfigure(2, weight=0) # Remaining space (optional for alignment)

    # Return elements that need to be accessed by event handlers
    return length_entry, strength_var, generated_pass_entry

def on_generate_button_click(length_entry, strength_var, generated_pass_entry):
    #Event handler for the Generate button.
    try:
        length = int(length_entry.get())
        strength = strength_var.get()

        if not (MIN_PASS_LENGTH <= length <= MAX_PASS_LENGTH):
            msg.showwarning("Input Error", f"Password length must be between {MIN_PASS_LENGTH} and {MAX_PASS_LENGTH}.")
            return

        # Clear previous password
        generated_pass_entry.config(state="normal")
        generated_pass_entry.delete(0, tk.END)

        new_password = generate_password(length, strength)

        # Insert new password and make read-only again
        generated_pass_entry.insert(0, new_password)
        generated_pass_entry.config(state="readonly")

    except ValueError:
        msg.showwarning("Input Error", "Please enter a valid number for password length.")
    except Exception as e:
        msg.showerror("An Error Occurred", f"An unexpected error happened: {e}")

# Main Application Execution
if __name__ == "__main__":
    app_root = create_main_window()
    length_entry_widget, strength_var_widget, generated_pass_entry_widget = setup_ui_elements(app_root)
    app_root.mainloop()