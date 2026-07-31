import { Link } from "react-router-dom";

export default function NotFound() {
  return (
    <div style={{ padding: 16 }}>
      <h2>404</h2>
      <Link to="/">На главную</Link>
    </div>
  );
}
