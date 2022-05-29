import Box from "@mui/material/Box";
import Container from "@mui/material/Container";
import Typography from "@mui/material/Typography";
import Link from "@mui/material/Link";
import { Grid, Paper, Stack } from "@mui/material";
import { Facebook, Twitter, Instagram, GitHub } from "@mui/icons-material";

export default function Footer() {
  return (
    <Box
      component="footer"
      sx={{ bgcolor: "background.paper", py: 6, height: "30%" }}
    >
      <Container maxWidth="lg">
        <Grid
          direction="row"
          spacing={1}
          alignItems="center"
          justifyContent={"center"}
          container
        >
          <Grid item xs={4}>
            <Paper elevation={0} sx={{ p: 8, bgcolor: "grey.200" }}>
              <Typography variant="h6" gutterBottom>
                Texto
              </Typography>
            </Paper>
          </Grid>
          <Grid item xs={4}>
            <Paper elevation={0} sx={{ p: 8, bgcolor: "grey.200" }}>
              <Typography variant="h6" gutterBottom>
                Texto
              </Typography>
            </Paper>
          </Grid>
          <Grid item xs={4}>
            <Paper elevation={0} sx={{ p: 8, bgcolor: "grey.200" }}>
              <Typography variant="h6" gutterBottom>
                Texto
              </Typography>
            </Paper>
          </Grid>
        </Grid>
        <Stack
          marginTop={"10px"}
          direction="row"
          spacing={1}
          alignItems="center"
          justifyContent={"center"}
        >
          <Typography
            variant="subtitle1"
            align="center"
            color="text.secondary"
            component="p"
          >
            BETinho ®
          </Typography>
          <Link display="block" variant="body1" href={"https://twitter.com/"}>
            <Twitter />
          </Link>
          <Link
            display="block"
            variant="body1"
            href={"https://www.facebook.com/"}
          >
            <Facebook />
          </Link>
          <Link
            display="block"
            variant="body1"
            href={"https://www.instagram.com/"}
          >
            <Instagram />
          </Link>
          <Link
            display="block"
            variant="body1"
            href={"https://github.com/jotaRenan/pds-tp1"}
          >
            <GitHub />
          </Link>
        </Stack>
      </Container>
    </Box>
  );
}
