from textual.app import App, ComposeResult
from textual.widgets import DirectoryTree, Footer, Header, TextArea
from textual.containers import Horizontal
from terminalEmulator import TerminalEmulator
from File import OpenFile, GetFilePath


filePath = GetFilePath("main.py")

class Bunny(App):

    CSS = """
        #file-viewer{
            width: 20%;
        }
        #terminal{
            height: 20%;
        }
    """

    def compose(self) -> ComposeResult:
        yield Header("Bunny", name="Bunny", icon="🐰")

        with Horizontal():
            yield DirectoryTree(path=".", id="file-viewer")
            yield TextArea(OpenFile(filePath), language="Python")

        # Add the terminal section using TextArea with the current directory as the prompt
        yield TextArea(TerminalEmulator(), classes="terminal-box", id="terminal")

        # Footer section
        yield Footer()


if __name__ == "__main__":
    Bunny().run()
