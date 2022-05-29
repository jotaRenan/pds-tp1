import Table from "@mui/material/Table";
import TableBody from "@mui/material/TableBody";
import TableCell from "@mui/material/TableCell";
import TableContainer from "@mui/material/TableContainer";
import TableHead from "@mui/material/TableHead";
import TableRow from "@mui/material/TableRow";
import Paper from "@mui/material/Paper";
import { Button } from "@mui/material";
import Event from "types/Event";
import { height } from "@mui/system";

interface EventsTableProps {
  events: Event[];
  bet?: boolean;
}

export default function EventsTable({ events, bet }: EventsTableProps) {
  return (
    <TableContainer component={Paper} sx={{ height: "90%" }}>
      <Table sx={{ height: "100%" }}>
        <TableHead>
          <TableRow>
            <TableCell></TableCell>
            <TableCell align="right">1</TableCell>
            <TableCell align="right">X</TableCell>
            <TableCell align="right">2</TableCell>
            {bet && <TableCell align="right" width="15%"></TableCell>}
          </TableRow>
        </TableHead>
        <TableBody>
          {events.map((event) => (
            <TableRow
              key={JSON.stringify(event)}
              sx={{ "&:last-child td, &:last-child th": { border: 0 } }}
            >
              <TableCell component="th" scope="row">
                {event.home_team.name} x {event.away_team.name}
              </TableCell>
              <TableCell align="right">{event.result.home}</TableCell>
              <TableCell align="right">{event.result.draw}</TableCell>
              <TableCell align="right">{event.result.away}</TableCell>
              {bet && (
                <TableCell align="right">
                  <Button variant="contained">Apostar</Button>
                </TableCell>
              )}
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </TableContainer>
  );
}

EventsTable.defaultProps = {
  bet: false,
};
