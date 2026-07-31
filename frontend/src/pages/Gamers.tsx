import { useEffect, useState } from "react";
import { getGamers, type Gamer } from "../api/gamers";
import GamerCard from "../components/GamerCard";

export default function Gamers() {
  const [items, setItems] = useState<Gamer[] | null>(null);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    getGamers()
      .then(setItems)
      .catch((e) => setError(e?.message || "Ошибка загрузки"));
  }, []);

  return (
    <div style={{ padding: 16 }}>
      <h2 style={{ marginTop: 0 }}>Игроки</h2>

      {error && <div style={{ padding: 12, border: "1px solid #f00", borderRadius: 12 }}>{error}</div>}
      {!items && !error && <div>Загрузка...</div>}

      {items && (
        <div style={{ display: "grid", gridTemplateColumns: "repeat(auto-fit, minmax(240px, 1fr))", gap: 12 }}>
          {items.map((g) => <GamerCard key={g.id} gamer={g} />)}
        </div>
      )}
    </div>
  );
}
