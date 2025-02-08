import os
def TerminalEmulator():
    # Get the current working directory and return it formatted as a prompt
    current_dir = os.getcwd()
    return current_dir + ">"
