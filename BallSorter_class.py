import random
import gymnasium as gym

from gymnasium import spaces
import numpy as np

from ball_sorter_op import optimal_n_moves

N_BALLS = 4



# Switch + Check if it's Reaching Bounding Box.
# What if it only chooses a ball position
# And will get penalized if there are no balls near the position?
# Will That work?
# if it chooses 4, where do we take the ball from? 3 or 5? Does that make sense? I think this negates that method
# When choosing a different position, the surrounding for it (left/Right) should have balls or will get negative rewards
# Does it always take two consecutive actions? A curr position choice and then a move to make?
# NEW APPROACH:
# -2: Add ball left
# -1: Add ball right
# 0: Switch to position index 0
# ...
# n: Switch to position index n
# Experiment with the new approach and see what happens.
# How can the agent look at all different balls at once?
# 0, 0, 4, 0  -> Does it start always in position 0 or in the current position?
# If starting at the curr position: 
# Switch to Right
# Switch to Left
# No Move
# No move, No move, Right, No move -> No Move, No move, Left, No Move -> No move, left, left, No move -> 1, 1, 1, 1.
# on each round, it will iterate through the different positions! Awesome.

# Sealing
def swap_ball(observation, curr_position, move):
    

    observation[curr_position+move] += 1

    observation[curr_position] -= 1
    
    return observation

class BallSorter(gym.Env):

    def __init__(self):
        super(BallSorter, self).__init__()
        self.seed = 0
        self.debug_state = False

        # It can either add a ball to the right, left
        # or switch position to another one
        self.n = N_BALLS
        self.moves = 0
        self.action_space = spaces.Discrete(3)

        self.observation_space = spaces.Box(low = 0, high = self.n, shape = (self.n, ), dtype = np.int32)
    def print_debug_info(self, *x):
        
        if self.debug_state:
            print(", ".join(x))

    def no_balls_foul(self, observation, curr_position):
    
        if observation[curr_position] == 0:
    
            self.print_debug_info("No Balls in current position")
    
            return 1
    
        return 0

    def out_of_bound(self, observation, curr_position, move):
    
        if ((curr_position+move) >= len(observation) or (curr_position+move) < 0):
        
                self.print_debug_info("Out Of Bound Error")
        
                return 1
        
        return 0

# Penalize if a move is giving a ball to one that has more balls than it does
    def ball_to_greater_bucket(self, observation, curr_position, move):
        
        if observation[curr_position] < observation[curr_position+move]:
            return 1
        
        return 0

    def filled_balls(self, observation, curr_position):
            
            int("The balls are filled equally")
            observation = [0] * (len(observation))
            observation.insert(curr_position, len(observation))
            observation = np.array([observation])
            
            return observation

    def compare_to_optimal_n_moves(self, moves, optimal_moves):
        return optimal_moves - moves

    # Rewards
    def reward_system(self, observation, curr_position, move):
        
        reward = 0
        valid = 1

        if move:
            
            if self.out_of_bound(observation, curr_position, move):
                reward -= 10
                valid = 0
            
            elif self.no_balls_foul(observation, curr_position):
                reward -= 10
                valid = 0
            
            elif self.ball_to_greater_bucket(observation, curr_position, move):
                reward -= 2
    # 2, 3, 0, 0, 0 
            else:
                reward -= 1
        
        else:

            if observation[curr_position] > 1:
                reward -= 10
        # it seems to converge to not choosing any move for more rewards
        # Correlating to the variance to number of optimal moves (might need to adjust after tracking results)
    # reward += compare_to_optimal_n_moves(observation[0], optimal_moves)

        return reward, valid
    
    def step(self, action):
        
        # Execute actions:
        # If we choose to change the curr position, is giving two values or what's the idea here?
        # This is a two layer type of action
        # left, right, or change index -> range(N_BALLS); - Reward when chosen to chng index to current one
        # Is this possible? Is there another way to work on this?

        match action:

            # No Move
            # Penalize when it has more than 1 ball
            # Else do nothing
            case 0:
                move = 0

            # Reward if on the left has zero balls
            # Penalize if out of bound
            # Penalize if curr position has no balls
            # Put one Ball to the left
            case 1:
                move = 1
            # Reward if on the left has zero balls
            # Penalize if out of bound
            # Penalize if curr position has no balls
            # Put one Ball to the right
            case 2:
                move = -1

        loc_reward, valid = self.reward_system(self.obs, self.curr_position, move)
        
        self.print_debug_info(f"action: {action}, local reward: {loc_reward}, valid: {valid}, current position: {self.curr_position}")

        if valid:
            self.obs = swap_ball(self.obs, self.curr_position, move)
        
        self.print_debug_info(self.obs, np.ones(shape = (len(self.obs,),), dtype = np.int8))
        
        if  (self.obs == 1).all():
            loc_reward += 100
            self.done = True
            self.print_debug_info("sorting is done")


    
        if self.curr_position == (self.n - 1):
            self.curr_position = 0
        else:
            self.curr_position += 1
        

        return self.obs, loc_reward, self.done, False, {}
    
    def reset(self, seed = 0):

        self.curr_position = random.randint(0, self.n-1)
        self.optimal_moves = optimal_n_moves(self.n, self.curr_position)
        self.done = False

        observation  = [0] * (self.n)
        observation[self.curr_position] = self.n
        observation = np.array(observation, dtype = np.int8)
        
        self.obs = observation
        self.print_debug_info(f"OBSERVATION AT RESET: {observation}\nCurr Position: {self.curr_position}\nOptimal Moves: {self.optimal_moves}")
        return observation, {"info": ""}

        # We either switch or take a ball from the curr_position to the next

        # In rewards we lose if the current position doesn't have any balls yet we take right or left position
