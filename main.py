from textual.app import App, ComposeResult
from textual.widgets import DirectoryTree, Footer, Header, TextArea, Static
from textual.containers import Horizontal, Vertical


class Bunny(App):
    """A Textual-based TUI resembling VS Code with a directory viewer, editor, and terminal."""

    CSS = """
        #file-viewer{
            width: 20%;
        }
    """

    def compose(self) -> ComposeResult:

        yield Header("Bunny", name="Bunny", icon="🐰")

        with Horizontal():
            yield DirectoryTree(".", id="file-viewer")
            yield TextArea()

        # Bottom panel: Terminal
        yield Static("Terminal", classes="terminal-box")

        yield Footer()


if __name__ == "__main__":
    Bunny().run()
