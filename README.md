# Bunny

**TUI-based Code Editor** built using Python's Textual framework.

Bunny is a terminal-based user interface (TUI) for editing code, viewing directories, and running terminal commands. It combines a code editor, directory viewer, and terminal within a single, easy-to-use interface. It’s designed for users who prefer a text-based interface over traditional graphical user interfaces (GUIs).

![Bunny Logo](./images/Screenshot%202025-01-19%20103239.png)


---

## Download the Latest Release

You can download the latest release of Bunny from the following link:

- [Latest Release (v1.0.0-alpha)](https://github.com/LNC-Network/Bunny/releases/download/v1.0.0-alpha)

---

## Building and Running from Source

To build or run Bunny from the source code, follow these steps:

### Prerequisites

Make sure you have Python 3.x installed on your system, as well as `pip` (Python's package manager).

### Install Required Dependencies

You need to install the required libraries first:

```bash
pip install textual
pip install pyinstaller
```

### Build the Executable
After the dependencies are installed, you can build the executable file using PyInstaller. Run the following command to bundle Bunny into a single executable file:

```bash
pyinstaller --onefile main.py
```
This will generate an executable in the ```dist/``` folder, which you can then distribute.

