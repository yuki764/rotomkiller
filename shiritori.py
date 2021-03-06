#!/usr/bin/python3

import sys, random

# parameter check
if(len(sys.argv) > 2):
    print('Usage: {} [--auto|-a]'.format(sys.argv[0]))
    sys.exit(1)
elif(len(sys.argv) == 2):
    if(sys.argv[1] != '--auto' and sys.argv[1] != '-a'):
        print('Usage: {} [--auto|-a]'.format(sys.argv[0]))
        sys.exit(1)

pokemon_list = []
used_pokemon = {}

# translate lower case into upper case
# this map is generated by generate_filter.py
shiri_filter = {
        'ア':'ア','イ':'イ','ウ':'ウ','エ':'エ','オ':'オ',
        'カ':'カ','キ':'キ','ク':'ク','ケ':'ケ','コ':'コ',
        'サ':'サ','シ':'シ','ス':'ス','セ':'セ','ソ':'ソ',
        'タ':'タ','チ':'チ','ツ':'ツ','テ':'テ','ト':'ト',
        'ナ':'ナ','ニ':'ニ','ヌ':'ヌ','ネ':'ネ','ノ':'ノ',
        'ハ':'ハ','ヒ':'ヒ','フ':'フ','ヘ':'ヘ','ホ':'ホ',
        'マ':'マ','ミ':'ミ','ム':'ム','メ':'メ','モ':'モ',
        'ラ':'ラ','リ':'リ','ル':'ル','レ':'レ','ロ':'ロ',
        'ガ':'ガ','ギ':'ギ','グ':'グ','ゲ':'ゲ','ゴ':'ゴ',
        'ザ':'ザ','ジ':'ジ','ズ':'ズ','ゼ':'ゼ','ゾ':'ゾ',
        'ダ':'ダ','ヂ':'ヂ','ヅ':'ヅ','デ':'デ','ド':'ド',
        'バ':'バ','ビ':'ビ','ブ':'ブ','ベ':'ベ','ボ':'ボ',
        'パ':'パ','ピ':'ピ','プ':'プ','ペ':'ペ','ポ':'ポ',
        'ヤ':'ヤ','ユ':'ユ','ヨ':'ヨ','ワ':'ワ','ヲ':'ヲ',
        'ン':'ン','ァ':'ア','ィ':'イ','ゥ':'ウ','ェ':'エ',
        'ォ':'オ','ッ':'ツ','ャ':'ヤ','ュ':'ユ','ョ':'ヨ',
        '2':'ツ','Z':'ト','♂':'ス','♀':'ス'
}

def get_candidates_list(query):
    candidates_list = []
    shiri_pos = len(query) - 1
    if(query[shiri_pos] == 'ー'):
        shiri_pos = shiri_pos - 1
    for pokemon in pokemon_list:
        if(shiri_filter[query[shiri_pos]] == shiri_filter[pokemon[0]] and pokemon[len(pokemon) - 1] != 'ン' and used_pokemon[pokemon] == False):
            candidates_list.append(pokemon)
    return candidates_list

# create list and map
with open('pokemon_list.csv') as plf:
    for item in plf:
        pokemon_list.append(item.rstrip())
        used_pokemon[item.rstrip()] = False

# input Rotom's choice
while(True):
    query = input('Rotom: ')
    if(query in used_pokemon):
        # register in map
        used_pokemon[query] = True

        # get candidates
        candidates_list = get_candidates_list(query)

        # auto mode enabled
        if(len(sys.argv) == 2):
            # if there are no candidates, you lose...
            if(len(candidates_list) == 0):
                print('You lose...')
                sys.exit(0)

            # get indices of min of the # of next candidates
            next_candidates_num = []
            for candidate in candidates_list:
                next_candidates_list = get_candidates_list(candidate)
                next_candidates_num.append(len(next_candidates_list))
                # print a list of candidates
                #print('* {}: {}'.format(candidate, len(next_candidates_list)))

            min_next_candidates_num = min(next_candidates_num)
            min_next_candidates_indices = []
            for i in range(0, len(next_candidates_num)):
                if(next_candidates_num[i] == min_next_candidates_num):
                    min_next_candidates_indices.append(i)

            # choice randomly in indices of min
            choice = candidates_list[random.choice(min_next_candidates_indices)]
            used_pokemon[choice] = True
            print('You: {}'.format(choice))
        # auto mode disabled
        else:
            for candidate in candidates_list:
                # print a list of candidates
                print('* {}'.format(candidate))
            # input player's choice
            while(True):
                choice = input('You: ')
                if(choice == 'exit' or choice == 'surrender' or choice == 'コウサン'):
                    print('You lose...')
                    sys.exit(0)
                elif(choice in candidates_list):
                    # register in map
                    used_pokemon[choice] = True
                    break
                else:
                    print('error: This isn\'t a name of Pokemon and in a candidates list.')

    elif(query == 'exit' or query == 'surrender' or query == 'コウサン'):
        print('You win!')
        break
    else:
        print('error: This isn\'t a name of Pokemon.')
