from stable_baselines3 import PPO, A2C
import os
from BallSorter_class import BallSorter
import time

from sb3_contrib import QRDQN, TRPO


# policy_kwargs = dict(n_quantiles=50)

models_dir = f"models/TRPO_10_obs/"
logdir = f"logs/TRPO_10_obs/"

if not os.path.exists(models_dir):
	os.makedirs(models_dir)

if not os.path.exists(logdir):
	os.makedirs(logdir)

env =  BallSorter(10)
env.reset()

# model = TRPO("MlpPolicy", env, verbose=1)

model = TRPO('MlpPolicy', env, verbose=1, tensorboard_log=logdir)

TIMESTEPS = 25000
iters = 0
while True:
	iters += 1
	model.learn(total_timesteps=TIMESTEPS, reset_num_timesteps=False, tb_log_name=f"TRPO_4_obs")
	model.save(f"{models_dir}/{iters}")
