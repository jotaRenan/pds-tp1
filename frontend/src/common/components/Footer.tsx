import Box from "@mui/material/Box";
import Container from "@mui/material/Container";
import Typography from "@mui/material/Typography";
import Link from "@mui/material/Link";
import { Divider, Grid, Stack } from "@mui/material";
import { Facebook, Twitter, Instagram, GitHub } from "@mui/icons-material";

export default function Footer() {
  return (
    <>
      <Divider variant="fullWidth" />
      <Container
        sx={{
          height: "10%",
          alignItems: "center",
          justifyContent: "center",
        }}
      >
        <Stack
          direction="row"
          spacing={2}
          alignItems="center"
          justifyContent="center"
          height="100%"
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
    </>
  );
}
