# Reinforcement Learning Complete Guide

## What is Reinforcement Learning?

Reinforcement Learning (RL) is a machine learning paradigm where an agent learns to make decisions by interacting with an environment. The agent receives rewards or penalties for its actions and learns to maximize cumulative reward over time.

## Key Concepts

### Agent and Environment

- **Agent**: The learner/decision maker
- **Environment**: Everything the agent interacts with
- **State (s)**: Current situation of the agent
- **Action (a)**: What the agent can do
- **Reward (r)**: Feedback from the environment

### The RL Loop

1. Agent observes state s
2. Agent takes action a
3. Environment transitions to new state s'
4. Agent receives reward r
5. Repeat

### Markov Decision Process (MDP)

Formal framework for RL:
- Set of states S
- Set of actions A
- Transition function P(s'|s,a)
- Reward function R(s,a)
- Discount factor γ (0 < γ ≤ 1)

### Key Terms

- **Policy (π)**: Strategy that maps states to actions
- **Value Function V(s)**: Expected return from state s
- **Q-Function Q(s,a)**: Expected return from taking action a in state s
- **Return**: Cumulative discounted reward

## Classic RL Algorithms

### Dynamic Programming

Requires complete knowledge of environment:

1. **Policy Iteration**
   - Evaluate current policy
   - Improve policy greedily
   - Repeat until convergence

2. **Value Iteration**
   - Update value function directly
   - Extract policy at the end

### Monte Carlo Methods

Learn from complete episodes:
- No need for environment model
- Update values based on actual returns
- High variance, unbiased

### Temporal Difference (TD) Learning

Combines ideas from DP and Monte Carlo:

1. **TD(0)**: Update using one-step return
2. **TD(λ)**: Blend of n-step returns

### Q-Learning

Off-policy TD algorithm:
- Learns optimal Q-function directly
- Update: Q(s,a) ← Q(s,a) + α[r + γ max Q(s',a') - Q(s,a)]
- Doesn't require policy to follow

### SARSA

On-policy TD algorithm:
- Update: Q(s,a) ← Q(s,a) + α[r + γ Q(s',a') - Q(s,a)]
- Follows the behavior policy

## Deep Reinforcement Learning

Combines deep learning with RL for complex state spaces.

### Deep Q-Network (DQN)

Breakthrough by DeepMind (2013):
- Neural network approximates Q-function
- **Experience Replay**: Store and sample past experiences
- **Target Network**: Separate network for stable targets

**Improvements:**
- Double DQN: Reduce overestimation
- Dueling DQN: Separate value and advantage streams
- Prioritized Experience Replay: Sample important experiences more
- Rainbow: Combines multiple improvements

### Policy Gradient Methods

Directly optimize the policy:

1. **REINFORCE**
   - Monte Carlo policy gradient
   - High variance

2. **Actor-Critic**
   - Actor: Policy network
   - Critic: Value network
   - Lower variance than pure policy gradient

### Advanced Algorithms

1. **A2C/A3C (Advantage Actor-Critic)**
   - Uses advantage function
   - A3C: Asynchronous training

2. **PPO (Proximal Policy Optimization)**
   - Constrains policy updates
   - Stable and effective
   - Most popular algorithm currently

3. **TRPO (Trust Region Policy Optimization)**
   - Theoretical guarantees
   - More complex than PPO

4. **SAC (Soft Actor-Critic)**
   - Maximum entropy RL
   - Encourages exploration
   - State-of-the-art for continuous control

5. **TD3 (Twin Delayed DDPG)**
   - Improvement over DDPG
   - Uses twin critics, delayed updates

## Model-Based RL

Learn a model of the environment:

- **World Models**: Learn latent dynamics
- **MuZero**: Learns model without explicit state representation
- **Dreamer**: Model-based with imagination rollouts

## Multi-Agent RL

Multiple agents learning simultaneously:

- **Cooperative**: Agents work together
- **Competitive**: Agents compete (self-play)
- **Mixed**: Both cooperation and competition

Examples:
- OpenAI Five (Dota 2)
- AlphaStar (StarCraft II)
- Hide and Seek (OpenAI)

## Exploration Strategies

Balance exploration vs exploitation:

1. **ε-greedy**: Random action with probability ε
2. **UCB (Upper Confidence Bound)**: Optimism in face of uncertainty
3. **Thompson Sampling**: Bayesian approach
4. **Intrinsic Motivation**: Curiosity-driven exploration
5. **Count-based Exploration**: Visit less-seen states

## Applications

### Games
- Atari Games (DQN)
- Go (AlphaGo, AlphaZero)
- Chess (AlphaZero)
- Dota 2 (OpenAI Five)
- StarCraft (AlphaStar)

### Robotics
- Manipulation
- Locomotion
- Navigation

### Real-World Applications
- Recommendation Systems
- Trading Strategies
- Resource Management
- Autonomous Driving
- Industrial Control

## Challenges

1. **Sample Efficiency**: RL often needs millions of interactions
2. **Reward Design**: Difficult to specify correct rewards
3. **Exploration**: Hard in sparse reward environments
4. **Stability**: Training can be unstable
5. **Sim-to-Real Gap**: Policies learned in simulation may not transfer

## Libraries and Tools

- **Gymnasium (Gym)**: Standard environments
- **Stable Baselines3**: Reliable implementations
- **RLlib**: Scalable RL library
- **CleanRL**: Single-file implementations
- **MuJoCo**: Physics simulation
- **Isaac Gym**: GPU-accelerated simulation
