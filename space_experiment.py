from BallSorter_class import BallSorter
env = BallSorter()
episodes = 50

for episode in range(episodes):
	done = False
	obs = env.reset()
	while True:#not done:
		random_action = env.action_space.sample()
		print("action",random_action)
		obs, reward, done, _, info = env.step(random_action)
		print('reward',reward)
