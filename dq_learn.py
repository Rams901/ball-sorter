import os
from BallSorter_class import BallSorter
from sb3_contrib import QRDQN


policy_kwargs = dict(n_quantiles=50)

models_dir = f"models/QR_DQN_10/"
logdir = f"logs/QR_DQN_10/"

if not os.path.exists(models_dir):
	os.makedirs(models_dir)

if not os.path.exists(logdir):
	os.makedirs(logdir)

env =  BallSorter(10)
env.reset()
model = QRDQN("MlpPolicy", env, verbose=1, tensorboard_log = logdir)

TIMESTEPS = 25000
iters = 0
while True:
	iters += 1
	model.learn(total_timesteps=TIMESTEPS, reset_num_timesteps=False, tb_log_name=f"QR_DQN_10")
	model.save(f"{models_dir}/{iters}")