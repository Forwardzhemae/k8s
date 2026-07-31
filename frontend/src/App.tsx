import { Routes, Route } from "react-router-dom";
import Navbar from "./components/Navbar";
import Home from "./pages/Home";
import Gamers from "./pages/Gamers";
import NotFound from "./pages/NotFound";

export default function App() {
  return (
    <div>
      <Navbar />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/gamers" element={<Gamers />} />
        <Route path="*" element={<NotFound />} />
      </Routes>
    </div>
  );
}
