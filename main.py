def create_abstract_noun(verb):
    if verb.endswith("ати") or verb.endswith("яти") or verb.endswith("іти"):
       abs_noun = verb[:-2] + "нн" + "я"
       print(f"Абстрактний іменник: {abs_noun}, суфікс абстрактності -нн")
    elif verb.endswith("ити"):
       abs_noun = verb[:-3] + "енн" + "я"
       print(f"Абстрактний іменник: {abs_noun}, суфікс абстрактності -енн")
    else:
        print("Не вдалося згенерувати абстрактний іменник для введеного дієслова.")
     
def create_noun():
    while True:
        user_inp = input("Введіть інфінітив: ").strip().lower()

        if user_inp.endswith("ся") or user_inp.endswith("сь"):
            non_reflexive_verb = user_inp[:-2] 
            create_abstract_noun(non_reflexive_verb)
        else:
            create_abstract_noun(user_inp)
        
        while True:
            repeat = input("Бажаєте утворити інший абстрактний іменник? (так/ні): ").strip().lower()
            if repeat == "ні":
                print("Дякуємо за користування!")
                return
            elif repeat == "так":
                break 
            else:
                print("Нерозпізнана відповідь. Введіть 'так' або 'ні'.")
create_noun()