import { ThemeProvider } from "@emotion/react";
import { createTheme, CssBaseline, Grid } from "@mui/material";
import AlertProvider from "contexts/AlertContext";
import EventsProvider from "contexts/EventContext";
import Pages from "pages";

const theme = createTheme();

function App() {
  return (
    <ThemeProvider theme={theme}>
      <CssBaseline />
      <Grid width="100%" height="100vh" display="flex" flexDirection="column">
        <EventsProvider>
          <AlertProvider>
            <Pages />
          </AlertProvider>
        </EventsProvider>
      </Grid>
    </ThemeProvider>
  );
}

export default App;
