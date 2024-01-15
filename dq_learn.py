from stable_baselines3 import PPO, A2C
import os
from BallSorter_class import BallSorter
import time

from sb3_contrib import QRDQN, TRPO


policy_kwargs = dict(n_quantiles=50)

models_dir = f"models/QR_DQN/"
logdir = f"logs/QR_DQN/"

if not os.path.exists(models_dir):
	os.makedirs(models_dir)

if not os.path.exists(logdir):
	os.makedirs(logdir)

env =  BallSorter(4)
env.reset()
model = QRDQN("MlpPolicy", env, policy_kwargs=policy_kwargs, verbose=1, tensorboard_log = logdir)

# model = PPO('MlpPolicy', env, verbose=1, ent_coef=0.1,tensorboard_log=logdir)

TIMESTEPS = 25000
iters = 0
while True:
	iters += 1
	model.learn(total_timesteps=TIMESTEPS, reset_num_timesteps=False, tb_log_name=f"QR_DQN")
	model.save(f"{models_dir}/{iters}")