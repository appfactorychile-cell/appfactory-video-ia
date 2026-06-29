def transition_plan(transitions: list[str], scene_count: int) -> list[str]:
    return [transitions[index % len(transitions)] for index in range(max(scene_count - 1, 1))]
