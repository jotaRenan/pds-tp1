import { Route, BrowserRouter, Routes } from "react-router-dom";

import Admin from "./Admin";
import Bet from "./Bet";
import Events from "./Events";
import Home from "./Home";
import Login from "./Login";
import Profile from "./Profile";
import Register from "./Profile";

const AppRoutes = () => {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/inicio" element={<Home />} />
        <Route path="/admin" element={<Admin />} />
        <Route path="/eventos" element={<Events />} />
        <Route path="/login" element={<Login />} />
        <Route path="/perfil" element={<Profile />} />
        <Route path="/cadastro" element={<Register />} />
        <Route path="/apostar" element={<Bet />} />
      </Routes>
    </BrowserRouter>
  );
};

export default AppRoutes;
