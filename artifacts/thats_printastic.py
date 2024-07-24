
''' Purpose: demonstrate the end optional parameter for print()
'''

import pause

print( 'Wa-Hoo-Wa' )
print( 'Rah-Rah-Rah' )

print(); input( "Enter when ready: " ) ; print()

print( 'Wa-Hoo-Wa', end='!' )
print( 'Rah-Rah-Rah' )

print(); input( "Enter when ready: " ) ; print()

print( 'Wa-Hoo-Wa', end='! ' )
print( 'Rah-Rah-Rah' )

print(); pause.until_ready(); print()

for ch in 'tattarrattat' :
    print( ch, end='-' )

print()

print(); pause.until_ready(); print()

finish_seller_of_lye = 'saippuakivikauppias' 

for ch in finish_seller_of_lye :
    print( ch, end=' ' )

print()

print(); pause.until_ready(); print()

for ch in finish_seller_of_lye :
    print( ch, end='' )

print()
