isAgents = True
Play = input("Do you play valorant? (yes/no): ").lower()
Agents = []
while isAgents == True:

    if Play == "yes":
        Agents_name = input("Who's your favorite agent?:")
        Agents.append(Agents_name)
        print(Agents)
        Agents1 = input("Do you main any other agents? would you like to share? (yes/no): ").lower()

        if Agents1 == "yes":
            continue

        else:
            print("Bruh!")
            isAgents = False
            break

    else:
        print("Bruh!")
        isAgents = False
        break