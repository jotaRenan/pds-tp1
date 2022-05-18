class EventOdds:
    def __init__(self, *, home: float, away: float, draw: float) -> None:
        self.home = home
        self.away = away
        self.draw = draw

    def __repr__(self) -> str:
        return f"Home odds: {self.home}, away odds: {self.away}, draw odds: {self.draw}"
