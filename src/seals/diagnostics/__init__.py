"""Simple diagnostic environments."""

import gym

gym.register(
    id="seals/RiskyPath-v0",
    entry_point="seals.diagnostics.risky_path:RiskyPathEnv",
    max_episode_steps=5,
)

gym.register(
    id="seals/InitShiftTrain-v0",
    entry_point="seals.diagnostics.init_shift:InitShiftTrainEnv",
    max_episode_steps=3,
)

gym.register(
    id="seals/InitShiftTest-v0",
    entry_point="seals.diagnostics.init_shift:InitShiftTestEnv",
    max_episode_steps=3,
)

gym.register(
    id="seals/NoisyObs-v0",
    entry_point="seals.diagnostics.noisy_obs:NoisyObsEnv",
    max_episode_steps=15,
)

gym.register(
    id="seals/Sort-v0",
    entry_point="seals.diagnostics.sort:SortEnv",
    max_episode_steps=6,
)

gym.register(
    id="seals/Branching-v0",
    entry_point="seals.diagnostics.branching:BranchingEnv",
    max_episode_steps=11,
)