end_of_game = False
blind_aution = {}

while not end_of_game:

    name = input("What is your name? ")
    bid = int(input("What is your bid? $"))

    blind_aution[name] = bid

    another_bid = input("Are there any other bidders? type 'yes' or 'no'.\n")

    if another_bid == "no":
        end_of_game = True

        blind_aution_value = []
        key_name = []

        for key in blind_aution:
            blind_aution_value.append(blind_aution[key])
            key_name.append(key)


            max_value = blind_aution_value[0]

            for i in range(0, len(blind_aution_value)):
                if blind_aution_value[i] > max_value:
                    max_value = blind_aution_value[i]

        index_blind_aution_value = blind_aution_value.index(max_value)


        print(f"The Winner is {key_name[index_blind_aution_value]} with a bid of ${blind_aution_value[index_blind_aution_value]}")
