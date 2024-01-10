from BallSorter_class import BallSorter
env = BallSorter()
episodes = 3

for episode in range(episodes):
	done = False
	obs = env.reset()
	for i in range(10):#not done:
		random_action = env.action_space.sample()
		print("action",random_action)
		obs, reward, done, _, info = env.step(random_action)
		print('reward',reward)
	