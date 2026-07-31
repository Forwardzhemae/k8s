import { Link } from "react-router-dom";

export default function Home() {
  return (
    <div style={{ padding: 16 }}>
      <h1 style={{ margin: 0 }}>Киберспорт Казахстана</h1>
      <p style={{ opacity: 0.8 }}>
        База игроков, команд и турниров. Начнем с раздела игроков.
      </p>
      <Link to="/gamers">Перейти к игрокам →</Link>
    </div>
  );
}
