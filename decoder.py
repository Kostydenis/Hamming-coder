import random
import copy

# ------------- Import data ------------
f = open('data.txt') # open coded file

str_hex = f.read(18)   # read 18 bytes
str_hex = str_hex[2:]  # and cut off first two bytes (they're zero)

f.close()

# ------------- Converting hex to bin ------------
lst_bin = [] # creating array for each word

for ch in str_hex: # for each symbol (8 chars) in source string 
	lst_bin.append(str(bin(ord(ch)))[3:]) # getting code of symbol
                                          # convertin to binary
                                          # converting to string
                                          # and put it to binary array


print('Source string: '+str(lst_bin))


# ------------- Break one symbol in one word ------------
rnd_wrd = random.randrange(len(lst_bin))
tmp_lst = list(''.join(lst_bin[rnd_wrd]))
rnd_pos = random.randrange(len(tmp_lst))
if (tmp_lst[rnd_pos] == '0'):
	tmp_lst[rnd_pos] = '>1<'
else:
	tmp_lst[rnd_pos] = '>0<'

brkn_lst_bin = copy.copy(lst_bin)
brkn_lst_bin[rnd_wrd] = str(''.join(tmp_lst))

print('Broken string: '+str(brkn_lst_bin))


# ------------- Find error ------------
corrected_lst_bin = copy.copy(brkn_lst_bin)

for it, wrd in enumerate(corrected_lst_bin):
	corrected_lst_bin[it] = wrd.replace('>', '').replace('<', '')


for it, wrd in enumerate(corrected_lst_bin):

	pos_of_err = ''
	pos_of_err = str(int(wrd[-1])^int(wrd[-3])^int(wrd[-5])^int(wrd[-7])) + pos_of_err
	pos_of_err = str(int(wrd[-2])^int(wrd[-3])^int(wrd[-6])^int(wrd[-7])) + pos_of_err
	pos_of_err = str(int(wrd[-4])^int(wrd[-5])^int(wrd[-6])^int(wrd[-7])) + pos_of_err

	pos_of_err = int(pos_of_err, base=2)

	if (pos_of_err != 0):
		print('Error is found in '+wrd+' in position: '+str(pos_of_err))

		wrd = list(wrd)
		if (wrd[-pos_of_err] == '0'):
			wrd[-pos_of_err] = '1'
		else:
			wrd[-pos_of_err] = '0'

		wrd = ''.join(wrd)
		corrected_lst_bin[it] = wrd
		print('Correct word is: '+str(wrd))

# ------------- Decoding ------------

out_wrd = ''
for it in xrange(0, len(corrected_lst_bin)-1, 2):
	out_wrd = out_wrd + chr(int(str(int(corrected_lst_bin[it][3:], base=2))+str(int(corrected_lst_bin[it+1][3:], base=2)), base=16))

print(out_wrd)

f = open('output.txt', 'w')
f.write(out_wrd)
f.close()

try:
	input('Done. Hit Enter for exit.')
except SyntaxError:
	print('Exiting')
