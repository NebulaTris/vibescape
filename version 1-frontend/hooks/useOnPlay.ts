import { Song } from "@/types";

import usePlayer from "./usePlayer";
import useSubscribeModal from "./useSubscribeModal";
import useAuthModal from "./useAuthModal";
import { useUser } from "./useUser";

const useOnPlay = (songs: Song[]) => {
  const player = usePlayer();
  const subscribeModal = useSubscribeModal();
  const authModal = useAuthModal();
  const { subscription, user } = useUser();

  const onPlay = (id: string) => {
    if (!user) {
      return authModal.onOpen();
    }

    if (!subscription) {
      return subscribeModal.onOpen();
    }

    player.setId(id);
    player.setIds(songs.map((song) => song.id));
  }

  return onPlay;
};

export default useOnPlay;
