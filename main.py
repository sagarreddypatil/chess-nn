import random

env = gym.make("ChessVsRandomBot-v0")
env.reset()

done = False

while not done:
    actions = env.get_possible_actions(state, player)
    action = random.choice(actions)
    observation, reward, done, info = env.step(action)
    print(env.render())
    print(f"Reward: {reward}\n")

env.close()
