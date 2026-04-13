from environment.railway_env import RailwayEnv
from agent.decision_agent import DecisionAgent


def train():
    env = RailwayEnv()
    agent = DecisionAgent()

    episodes = 10

    for ep in range(episodes):
        state = env.reset()
        total_reward = 0

        done = False

        while not done:
            action = agent.choose_action(state)

            next_state, reward, done = env.step(action)

            total_reward += reward
            state = next_state

        print(f"Episode {ep+1} → Total Reward: {total_reward}")


if __name__ == "__main__":
    train()