#import



#headline

print('Steam level keys vs gems profitability calculator  \n Made by Jeer \n ')

#questions
currency = input('What is your currency? ')
tf2key = input('How much is a TF2 key in cents? ')
tf2rate = input('What is the key to sets rate? ')
gemsprice = input('How much is a bag of gems in cents? ')
gemrate = input('What is the gem for set rate? ')
gemdiv = 1000.0

#tfcalc
tffinal = float(tf2key) / float(tf2rate)

#gemcalc
gemset = float(gemsprice) * float(gemrate)
gemfinal = float(gemset) / float(gemdiv)
#convert

gemfinal = str(gemfinal)
tffinal = str(tffinal)
#results

print('The price for one set with TF2 keys will be ' + tffinal + ' ' + currency + ' cents')

print('The price for one set with gems will be ' + gemfinal + ' ' + currency + ' cents')

input()
