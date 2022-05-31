
import React from 'react';
import { Container } from "@mui/system";
import Footer from "./components/Footer";
import Header from "./components/Header";

interface DefaultProps {
  children: JSX.Element;
}

export default function Common({ children }: DefaultProps) {
  return (
    <>
      <Header />
      <Container
        sx={{
          height: "80%",
          maxHeight: "80%",
          alignItems: "center",
          justifyContent: "center",
        }}
        maxWidth="lg"
      >
        {children}
      </Container>
      <Footer />
    </>
  );
}
