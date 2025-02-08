from textual.app import App, ComposeResult
from textual.widgets import DirectoryTree, Footer, Header, TextArea, Label
from textual.containers import Horizontal, Container
from textual.screen import ModalScreen
from utilities.TerminalEmulator import TerminalEmulator
from utilities.File import OpenFile, GetFilePath


filePath = GetFilePath("main.py")


class Settings(ModalScreen[None]):
    BINDINGS = [("escape", "dismiss")]
    CSS_PATH = "css/settings.css"

    def action_pop_screen(self):
        self.push_screen(Bunny())

    def compose(self) -> ComposeResult:
        with Container(id="Modal"):
            yield Label("Hello, World! Press Escape to close.", id="modal-label")


class Bunny(App):
    CSS_PATH = "css/app.css"
    BINDINGS = [("ctrl+q", "quit", "Quit"), ("f12", "settings", "Open Settings")]

    def action_quit(self):
        """Quit the application."""
        self.exit()

    def action_settings(self) -> None:
        """Open the settings modal."""
        self.push_screen(Settings())

    def compose(self) -> ComposeResult:
        """Compose the layout of the application."""
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
