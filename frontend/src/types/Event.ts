import EventResult from "./EventResult";
import Team from "./Team";

export default interface Event {
  id: string;
  description: string;
  start: string;
  location: string;
  home_team: Team;
  away_team: Team;
  result: EventResult;
}
