from stable_baselines3 import PPO, A2C
import os
from BallSorter_class import BallSorter
import time

from sb3_contrib import TRPO


env =  BallSorter(n_balls =  10, debug_state= True)
env.reset()

model = TRPO.load("models/TRPO_10_obs_v3/281")

obs, _ = env.reset()
iter = 0

while True:

    action, _states = model.predict(obs, deterministic=True)
    obs, reward, terminated, truncated, info = env.step(action)
    iter += 1
    if terminated or truncated:
        print(iter)
        break

    if iter > 10000:
        break
    #   obs, _ = env.reset()