import { Route, BrowserRouter, Routes, Navigate } from "react-router-dom";

import EventDetails from "./EventDetails";
import Home from "./Home";
import NewEvent from "./NewEvent";
import NotFound from "./NotFound";

const Pages = () => {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/404" element={<NotFound />} />
        <Route path="/" element={<Home />} />
        <Route path="/inicio" element={<Home />} />
        <Route path="/eventos" element={<Home />} />
        <Route path="/eventos/:id" element={<EventDetails />} />
        <Route path="/apostar/:id" element={<EventDetails bet />} />
        <Route path="/cadastrar-evento" element={<NewEvent />} />
        <Route path="*" element={<Navigate replace to="/404" />} />
      </Routes>
    </BrowserRouter>
  );
};

export default Pages;
