class Competition:
    def _change_score(self, participant_id, change):
        self._scores[participant_id] += change

    def __init__(self, participant_count):
        self._scores = [0] * participant_count

    def like(self, participant_id):
        self._change_score(participant_id, 1)

    def dislike(self, participant_id):
        self._change_score(participant_id, -1)

    def get_best_works(self, count):
        scores_ids = [(value, id) for id, value in enumerate(self._scores)]
        scores_ids.sort(reverse=True)
        return [id for _, id in scores_ids[:count]]
