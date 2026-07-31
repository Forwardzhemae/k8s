import { http } from "./http";

export type Gamer = {
  id: number;
  nickname: string;
  game?: string;
  country?: string;
  team?: string;
};

export async function getGamers(): Promise<Gamer[]> {
  const { data } = await http.get<Gamer[]>("/gamers");
  return data;
}
