import Footer from "./components/Footer";
import Header from "./components/Header";

interface DefaultProps {
  children: JSX.Element;
}

export default function Common({ children }: DefaultProps) {
  return (
    <>
      <Header />
      {children}
      <Footer />
    </>
  );
}
