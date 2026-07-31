import { Link, NavLink } from "react-router-dom";

export default function Navbar() {
  const linkClass = ({ isActive }: { isActive: boolean }) =>
    "px-3 py-2 rounded " + (isActive ? "bg-black text-white" : "text-black");

  return (
    <div style={{ display: "flex", gap: 12, alignItems: "center", padding: 12, borderBottom: "1px solid #ddd" }}>
      <Link to="/" style={{ fontWeight: 700 }}>KZ Esports</Link>
      <NavLink to="/" className={linkClass}>Главная</NavLink>
      <NavLink to="/gamers" className={linkClass}>Игроки</NavLink>
    </div>
  );
}
