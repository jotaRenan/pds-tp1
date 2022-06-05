import { ThemeProvider } from "@emotion/react";
import { createTheme, CssBaseline, Grid } from "@mui/material";
import AlertProvider from "contexts/AlertContext";
import EventsProvider from "contexts/EventContext";
import Pages from "pages";
import { LocalizationProvider } from '@mui/x-date-pickers/LocalizationProvider';
import { AdapterDateFns } from '@mui/x-date-pickers/AdapterDateFns';

const theme = createTheme();

function App() {
  return (
    <ThemeProvider theme={theme}>
      <CssBaseline />
      <Grid width="100%" height="100vh" display="flex" flexDirection="column">
        <EventsProvider>
          <LocalizationProvider dateAdapter={AdapterDateFns}>
            <AlertProvider>
              <Pages />
            </AlertProvider>
          </LocalizationProvider>
        </EventsProvider>
      </Grid>
    </ThemeProvider>
  );
}

export default App;
