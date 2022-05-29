import { Route, BrowserRouter, Routes } from "react-router-dom";

import Bet from "./Bet/Bet";
import Home from "./Home";
import NewEvent from "./NewEvent";

const Pages = () => {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="*" element={<Home />} /> {/* Precisa ser 404 depois */}
        <Route path="/" element={<Home />} />
        <Route path="/inicio" element={<Home />} />
        <Route path="/eventos" element={<Home />} />
        <Route path="/apostar" element={<Bet />} />
        <Route path="/cadastrar-evento" element={<NewEvent />} />
      </Routes>
    </BrowserRouter>
  );
};

export default Pages;
