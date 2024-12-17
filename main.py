from textual.app import App, ComposeResult
from textual.containers import Horizontal, Vertical
from textual.widgets import Digits, Input
from textual.reactive import reactive


class Score(Digits):
    """A widget to display and update a score using Digits."""
    value = reactive(0)

    def __init__(self, initial_value: int, *args, **kwargs):
        super().__init__(str(initial_value), *args, **kwargs)
        self.value = initial_value

    def watch_value(self) -> None:
        self.update(str(self.value))

    def update_score(self, amount: str) -> None:
        try:
            self.value += int(amount)
        except ValueError:
            pass  # Ignore invalid inputs


class RummyScoreBoard(App):
    CSS = """
    Vertical {
        align: center middle;
    }

    Input {
        margin-top: 1;
        width: 20;
        height: 3;
        border: tall $accent;
    }

    Digits {
        color: cyan;
        text-style: bold;
        margin-bottom: 1;
    }

    Horizontal {
        align: center middle;
        margin: 2;
        background: $surface;
    }
    """

    def compose(self) -> ComposeResult:
        self.score1 = Score(0)
        self.score2 = Score(0)

        with Horizontal():
            with Vertical():
                yield self.score1
                self.input1 = Input(placeholder="Enter +/- points")
                yield self.input1

            with Vertical():
                yield self.score2
                self.input2 = Input(placeholder="Enter +/- points")
                yield self.input2

    def on_input_submitted(self, event: Input.Submitted) -> None:
        """Handle score updates based on input."""
        if event.input is self.input1:
            self.score1.update_score(event.value)
            self.input1.clear()
        elif event.input is self.input2:
            self.score2.update_score(event.value)
            self.input2.clear()


if __name__ == "__main__":
    app = RummyScoreBoard()
    app.run()
