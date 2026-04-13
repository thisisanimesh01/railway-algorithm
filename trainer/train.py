from environment.railway_env import RailwayEnv
from agent.decision_agent import DecisionAgent


def train():
    env = RailwayEnv()
    agent = DecisionAgent()

    episodes = 200
    rewards = []

    for ep in range(episodes):
        state = env.reset()
        total_reward = 0

        done = False

        while not done:
            action = agent.choose_action(state)

            next_state, reward, done = env.step(action)

            agent.update_q(state, action, reward, next_state)

            total_reward += reward
            state = next_state

        agent.decay_epsilon()

        rewards.append(total_reward)

        print(f"Episode {ep+1} → Total Reward: {total_reward:.2f}")     # episode = one complete of train movement from start to finish, reward = cumulative reward for that episode

    print(f"Average Reward: {sum(rewards)/len(rewards):.2f}")


if __name__ == "__main__":
    train()