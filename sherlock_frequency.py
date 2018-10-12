    def sherlock(s):
        n = len(s)
        char_map = {}
        total_types = 1

        for i, c in enumerate(s):
            c_count = char_map.get(c, 0)
            if c_count == 0:
                total_types += 1
            char_map[c] = c_count + 1

        removed = False
        prev_count = 1
        out = 'YES' 
        for c, count in char_map.items():
            if not removed:
                if count < prev_count - 1:
                    out = 'NO'
                    break
                if count == prev_count - 1:
                    # print('removed one')
                    removed = True
                    continue
            else:
                if count != prev_count:
                    out = 'NO'
                    break
            prev_count = count
        return out


w1 = 'aabbccddeefghi' # not possiburu
0, 7 13, 18
# a 1
# a 2
# b 1
# b 
w2 = 'aabbccddi' # one removal and its good
w3 = 'aabbccdd' # is good
w4 = 'aabbcd'
w5 = 'aaaaabc'
w7 = 'ibfdgaeadiaefgbhbdghhhbgdfgeiccbiehhfcggchgghadhdhagfbahhddgghbdehidbibaeaagaeeigffcebfbaieggabcfbiiedcabfihchdfabifahcbhagccbdfifhghcadfiadeeaheeddddiecaicbgigccageicehfdhdgafaddhffadigfhhcaedcedecafeacbdacgfgfeeibgaiffdehigebhhehiaahfidibccdcdagifgaihacihadecgifihbebffebdfbchbgigeccahgihbcbcaggebaaafgfedbfgagfediddghdgbgehhhifhgcedechahidcbchebheihaadbbbiaiccededchdagfhccfdefigfibifabeiaccghcegfbcghaefifbachebaacbhbfgfddeceababbacgffbagidebeadfihaefefegbghgddbbgddeehgfbhafbccidebgehifafgbghafacgfdccgifdcbbbidfifhdaibgigebigaedeaaiadegfefbhacgddhchgcbgcaeaieiegiffchbgbebgbehbbfcebciiagacaiechdigbgbghefcahgbhfibhedaeeiffebdiabcifgccdefabccdghehfibfiifdaicfedagahhdcbhbicdgibgcedieihcichadgchgbdcdagaihebbabhibcihicadgadfcihdheefbhffiageddhgahaidfdhhdbgciiaciegchiiebfbcbhaeagccfhbfhaddagnfieihghfbaggiffbbfbecgaiiidccdceadbbdfgigibgcgchafccdchgifdeieicbaididhfcfdedbhaadedfageigfdehgcdaecaebebebfcieaecfagfdieaefdiedbcadchabhebgehiidfcgahcdhcdhgchhiiheffiifeegcfdgbdeffhgeghdfhbfbifgidcafbfcd'

w18 = 'abcdefghhgfedecba'

with open('sherlock_input13.txt') as f:
    read_data = f.read()
import pdb; pdb.set_trace()
print(sherlock(w1))
print(sherlock(w2))
print(sherlock(w3))
print(sherlock(w4))
print('-'*30)
print(sherlock(w5))



