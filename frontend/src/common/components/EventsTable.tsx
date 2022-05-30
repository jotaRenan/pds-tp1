import Table from "@mui/material/Table";
import TableBody from "@mui/material/TableBody";
import TableCell from "@mui/material/TableCell";
import TableContainer from "@mui/material/TableContainer";
import TableHead from "@mui/material/TableHead";
import TableRow from "@mui/material/TableRow";
import Paper from "@mui/material/Paper";
import { Button } from "@mui/material";
import Event from "types/Event";
import { useNavigate } from "react-router-dom";

interface EventsTableProps {
  events: Event[];
  bet?: boolean;
  clickable?: boolean;
}

export default function EventsTable({
  events,
  bet,
  clickable,
}: EventsTableProps) {
  const navigate = useNavigate();

  return (
    <TableContainer component={Paper} sx={{ maxHeight: "75%" }}>
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
              hover
              key={JSON.stringify(event)}
              sx={{
                "&:last-child td, &:last-child th": { border: 0 },
                cursor: "pointer",
              }}
              onClick={() => clickable && navigate(`/eventos/${event.id}`)}
            >
              <TableCell component="th" scope="row">
                {event.home_team.name} x {event.away_team.name}
              </TableCell>
              <TableCell align="right">{event.result.home}</TableCell>
              <TableCell align="right">{event.result.draw}</TableCell>
              <TableCell align="right">{event.result.away}</TableCell>
              {bet && (
                <TableCell align="right">
                  <Button
                    variant="contained"
                    onClick={(e) => {
                      e.stopPropagation();
                      navigate(`/apostar/${event.id}`);
                    }}
                  >
                    Apostar
                  </Button>
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
  clickable: false,
};
