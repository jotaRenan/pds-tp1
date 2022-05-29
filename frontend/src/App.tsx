import { ThemeProvider } from "@emotion/react";
import { createTheme, CssBaseline, Grid } from "@mui/material";
import { Container } from "@mui/system";
import Pages from "pages";

const theme = createTheme();

function App() {
  return (
    <ThemeProvider theme={theme}>
      <CssBaseline />
      <Grid width="100%" height="100vh" display="flex" flexDirection="column">
        <Pages />
      </Grid>
    </ThemeProvider>
  );
}

export default App;
