import Team from "./Team";

export interface NewEvent {
    description: string;
    start: string;
    location: string;
    home_team: Team;
    away_team: Team;
}