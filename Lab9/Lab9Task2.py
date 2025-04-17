# Goal-Based Agent Example
class GoalBasedAgent:
    def __init__(self, goal):#Constructor function hai jo goal save karta hai.
          self.goal = goal#yahan goal save hoga ta k agent ko yad rhy goal kya ha
    def act(self, environment):#decide the action based on environment
        if self.goal in environment:
            return f"Action: Move towards {self.goal}"
        else:
            return "Action: Search for goal" #if not found in environment then search
# Model-Based Agent Example
class ModelBasedAgent:
    def __init__(self):
        self.internal_model = []#memory, empty list where agents save the observations
    def update_model(self, perception):#agent ny jo v dekha vo save kryga q k goal based agent memory save krta ha past vali
        self.internal_model.append(perception)
    def act(self):#Agar usay yaad hai ke obstacle mila tha, to woh turn karega.
        if "obstacle" in self.internal_model:
            return "Action: Turn to avoid obstacle"
        else:
            return "Action: Move forward"#Agar koi obstacle nahi mila to seedha move karega.
# Utility-Based Agent Example
class UtilityBasedAgent:
    def __init__(self):# No special variables needed initially.
        pass
    def evaluate(self, option):# evealuate krna action ko, Har action (e.g. study, play) ka ek score diya gaya — jitna zyada score, utna behtar.
        utilities = {#dictionary
            "eat": 8,
            "sleep": 7,
            "study": 10,
            "play": 5
        }
        return utilities.get(option, 0)  #Agar option dictionary m mila to uska score dega, warna 0.
    def act(self, options):#Yeh method options ke list ko le kar sabse best option (highest score) choose karta hai.
        best_option = max(options, key=self.evaluate)#Jo option sabse zyada score wala hai, usay select karega.
        #max() har option ka utility score self.evaluate() se lega aur phir sabse zyada score wale option ko choose karega.
        return f"Action: Choose to {best_option} (Highest utility)"
# Main Program to Test Agents
# Goal-based agent scenario
print("Goal-Based Agent:")
goal_agent = GoalBasedAgent("Treasure")#Goal-based agent banaya with goal = "Treasure",you're creating an instance of the GoalBasedAgent class
print(goal_agent.act(["Tree", "Stone", "Treasure"]))#calls the act() method, which was defined in the GoalBasedAgent class.
# Model-based agent scenario
print("Model-Based Agent:")
#Model-based agent ko pehle "road" aur "obstacle" mila.
#Woh yaad karega aur phir "turn" karega to avoid the obstacle.
model_agent = ModelBasedAgent()
model_agent.update_model("road")
model_agent.update_model("obstacle")
print(model_agent.act())
# Utility-based agent scenario
#Utility-based agent options ko check karega aur "study" choose karega because it has the highest score = 10.
print("Utility-Based Agent:")
utility_agent = UtilityBasedAgent()
print(utility_agent.act(["sleep", "study", "play"]))