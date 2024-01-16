import random
import gymnasium as gym

from gymnasium import spaces
import numpy as np

N_BALLS = 5

class BallSorter(gym.Env):

    def __init__(self, n_balls, debug_state = False):
        super(BallSorter, self).__init__()
        self.seed = 0
        self.debug_state = debug_state

        self.n = n_balls
        self.moves = 0
        self.action_space = spaces.Discrete(3)

        self.observation_space = spaces.Box(low = 0, high = self.n+1, shape = (self.n+1, ), dtype = np.int32)

    def print_debug_info(self, *x):
        
        if self.debug_state:
            print([str(elem) for elem in x])

    def swap_ball(self, observation, curr_position, move):
    
        observation[curr_position+move] += 1

        observation[curr_position] -= 1
        
        return observation
    
    def no_balls_foul(self, observation, curr_position):
    
        if observation[curr_position] == 0:
    
            self.print_debug_info("No Balls in current position")
    
            return 1
    
        return 0
    
    def optimal_n_moves(self,):
        n = self.n
        init_bucket = self.curr_position
        buckets = [0] * (n-1)
        buckets.insert(init_bucket, n)

        moves = 0
        center = init_bucket

        for i in range(center, n-1):
            buckets[i+1] =  (n - i -1)
            buckets[i] -= buckets[i + 1]
            moves += buckets[i+1]

        for i in range(center, 0, -1):
            buckets[i-1] = i 
            buckets[i] -= buckets[i - 1]
            moves += buckets[i-1]

        return moves
    
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
    
    def encourage_giving_to_least(self, observation, move):
        
        try:
            if observation[self.curr_position+move] < observation[self.curr_position-move]:
                return 1
            return 0
        except Exception as e:
            if observation[self.curr_position+move] < observation[self.curr_position]:
                return 1
        return 0
            # 2, 1 / 1, 2 / 2, 3

    # Rewards
    def reward_system(self, observation, curr_position, move):
        
        reward = 0
        valid = 1

        if move:
            
            if self.out_of_bound(observation, curr_position, move):
                reward -= 1
                valid = 0
            
            elif self.no_balls_foul(observation, curr_position):
                reward -= 1
                valid = 0

            elif self.encourage_giving_to_least(observation, move):
                reward += 0.5

        
        else:

            if observation[curr_position] > 1:
                reward -= 1

        return reward, valid
    
    def step(self, action):

        match action:

            case 0:
                move = 0

            case 1:
                move = 1

            case 2:
                move = -1

        loc_reward, valid = self.reward_system(self.obs[:-1], self.curr_position, move)
        
        self.print_debug_info(f"action: {action}, local reward: {loc_reward}, valid: {valid}, current position: {self.curr_position}")

        if valid:
            self.obs[:-1] = self.swap_ball(self.obs[:-1], self.curr_position, move)
        
        self.print_debug_info(self.obs[:], np.ones(shape = (len(self.obs[:-1],),), dtype = np.int8))
        
        if  (self.obs[:-1] == 1).all():
            loc_reward += 100
            self.done = True
            self.print_debug_info("sorting is done")


    
        if self.curr_position == (self.n - 1):
            self.curr_position = 0
        else:
            self.curr_position += 1

        self.obs[-1] = self.curr_position

        return self.obs, loc_reward, self.done, False, {}
    
    def reset(self, seed = 0):

        self.curr_position = random.randint(0, self.n-1)
        self.optimal_moves = self.optimal_n_moves()
        self.done = False

        observation  = [0] * (self.n)
        observation[self.curr_position] = self.n
        observation.append(self.curr_position)

        observation = np.array(observation, dtype = np.int32)
        
        self.obs = observation
        self.print_debug_info(f"OBSERVATION AT RESET: {observation}\nCurr Position: {self.curr_position}\nOptimal Moves: {self.optimal_moves}")
        
        return observation, {"info": ""}
