import type { Gamer } from "../api/gamers";

export default function GamerCard({ gamer }: { gamer: Gamer }) {
  return (
    <div style={{ border: "1px solid #e5e5e5", borderRadius: 12, padding: 12 }}>
      <div style={{ fontSize: 18, fontWeight: 700 }}>{gamer.nickname}</div>
      <div style={{ opacity: 0.8, marginTop: 6 }}>
        {gamer.game ? `Игра: ${gamer.game}` : "Игра: —"}<br />
        {gamer.team ? `Команда: ${gamer.team}` : "Команда: —"}<br />
        {gamer.country ? `Страна: ${gamer.country}` : "Страна: —"}
      </div>
    </div>
  );
}
