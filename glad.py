import random


spelare_hälsa = 30
gladiator_hälsa = 30
print("Du vaknar upp i ett rum fullt med människor, en kille med en rödd tygg dräkt tittar glor ner på dig")
print("Välkommen till Rom främling, du är på ett väldigt tight situation just nu.")
print(" Du ser, du är en fångad med dem andra här och ska slåss till dödens om tjejsaren inte säger det själv")
print("Människorna här kallar oss för gladiator. Vi slåss för våran frihet eller ja, försöker iallafal.")
print("Jag tror att din första match är snart framme. *Han pekar på ett kort svärd som ligger på golvet* Öva med den så kommer du säkert klara dig.")
print("Nästa dag så va du ute i arenan, ljudet av folk ekar genom din öra och du håller i din kort svärd")
print("Du ser en rädd kille gå utt från andra sidan av arenan med samma vapen som du har och tittar på dig nervös och rädd")

while spelare_hälsa > 0 and gladiator_hälsa > 0:
    spelare_val = input("Ange din attack 1 för vanlig swing  2 för heavy swing: ")
    
    
    if spelare_val == "1":
        spelare_skada = random.randint(3, 5)
        print(f"Du gjorde {spelare_skada} skada på den rädda gladiatorn")
        gladiator_hälsa -= spelare_skada
    elif spelare_val == "2":
        spelare_skada = random.randint(1, 10)
        print(f"Du gjorde {spelare_skada} skada på den rädda gladiatorn")
        gladiator_hälsa -= spelare_skada
    else:
        print("Du ramlade, Du missade.")

    
    if gladiator_hälsa <= 0:
        print("Du dödade gladiatorn.")
        break

    
    print("den rädda gladiatorns tur")
    gladiator_val = random.choice(["vanlig", "tung"])

    
    if gladiator_val == "vanlig":
        gladiator_skada = random.randint(3, 5)
        print(f"den rädda gladiatorn använde en Vanlig Attack och gjorde {gladiator_skada} skada")
        spelare_hälsa -= gladiator_skada
    else:
        gladiator_skada = random.randint(1, 10)
        print(f"den rädda gladiatorn använde en Tung Attack och gjorde {gladiator_skada} skada")
        spelare_hälsa -= gladiator_skada

    
    if spelare_hälsa <= 0:
        print("Du har blivit dödad av gladiatorn.")
        break


print("Matchen är över.")
    

   
    
    