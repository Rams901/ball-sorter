 # Ball Sorter Problem
 - <b>Description</b> you specify N = number of buckets, and an equal number of balls. Imagine all buckets a placed in a line, numbered from bucket 1 to lets say 4 (N=4). You start with all the 4 balls placed inside a single bucket (could be any one of the 4). And your destination is to distribute all the balls evenly across the buckets- so the end state is one ball per bucket. You can only move one ball from one bucket to the next in each move 
 - <b> Goal</b> the goal is to solve this in the optimal (least) number of total moves.

# Ball Sorter in Reinforcement Learning

BallSorter is a custom gymnasium environment that simulates sorting a given number of balls into equally filled buckets. This operator takes a single action and returns a reward and a new observation based on that action. The environment resets when all balls are sorted, and the goal is to minimize the number of moves required to sort all balls.

Inputs:

The input to this operator is an integer action from the action space. The action is an integer between 0 and 2 that represents moving the ball to the left, right, or no movement.

Parameters:

The operator has no parameters.

Outputs:

The operator returns a tuple containing the new observation, local reward, done flag, info dictionary, and whether the episode is truncated. The new observation is a one-dimensional numpy array that represents the state of the environment. The local reward is a float value between -100 and 100, and the done flag is a boolean indicating whether the episode is complete. The info dictionary is currently empty.

Functionality:

The BallSorter environment has several helper functions supporting its functionality. The `print_debug_info` function prints debug information to the console. The `swap_ball` function swaps the ball at a given position with the ball at the given moved position. The `no_balls_foul` function checks whether there are no balls in a given position and returns a boolean value. The `out_of_bound` function checks whether a given move is within the bounds of the environment and returns a boolean value. The `ball_to_greater_bucket` function checks whether a ball is being moved to a bucket that already has more balls than the current bucket and returns a boolean value. The `filled_balls` function creates an array of filled buckets.
## Reward System Purpose

The reward system has been designed to provide feedback to the agent for the different actions taken during training. The agent receives a reward based on:

- Number of moves made: A negative reward is given if the number of moves made is more than the optimal number of moves.
- Ball to greater bucket: A negative reward is given if the ball being moved is going to a bucket that already has more balls than the current bucket.
- Out of bounds: A negative reward is given if the agent moves a ball out of bounds.
- No balls in current position: A negative reward is given if there are no balls in the current position.
- Filled balls: A positive reward is given if the agent fills all the balls equally into each bucket.

The rewards are calculated using a function called `reward_system` and are applied during the `step` function.
# Agents Used
Using Stable Baseline 3, the approach involved several algorithms used such as PPO, A2C, TRPO.
<img width="893" alt="Screenshot 2024-01-11 at 10 50 32 AM" src="https://github.com/Rams901/ball-sorter/assets/47258547/76bb6491-6505-4648-b652-9ae0537f1202">
Tensorboard Tracking Models Training in Real Time. TRPO was the best model to reach rewarding results in shorter steps.

@misc{stable-baselines, 
  author = {Hill, Ashley and Raffin, Antonin and Ernestus, Maximilian and Gleave, Adam and Kanervisto, Anssi and Traore, Rene and Dhariwal, Prafulla and Hesse, Christopher and Klimov, Oleg and Nichol, Alex and Plappert, Matthias and Radford, Alec and Schulman, John and Sidor, Szymon and Wu, Yuhuai}, 
  title = {Stable Baselines}, 
  year = {2018}, 
  publisher = {GitHub}, 
  journal = {GitHub repository}, 
  howpublished = {\url{https://github.com/hill-a/stable-baselines}}
}

