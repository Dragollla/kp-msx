from models.Episode import Episode



class Season:

    def __init__(self, data, content_id):
        self.content_id = content_id

        self.n = data.get('number')
        self.id = data.get('id')
        self.episodes = [Episode(i, content_id, self.n) for i in data.get('episodes')]

        self.watched = self._watched()

    def to_episode_pages(self, proxy: bool = False, alternative_player: bool = False):
        items = []
        for i, episode in enumerate(self.episodes):
            entry = {
                "label": episode.menu_title(),
                "playerLabel": episode.player_title(),
                'action': episode.msx_action(proxy=proxy, alternative_player=alternative_player),
                'stamp': '{ico:check}' if episode.watched else None,
                'focus': not episode.watched,
                'properties': episode.msx_properties(proxy=proxy, alternative_player=alternative_player)
            }
            items.append(entry)
        return items

    def _watched(self):
        watched = True
        for episode in self.episodes:
            watched = watched and episode.watched
        return watched