# Learning Python

firstvar = 'Apple'
secondvar = 'Pear'
var=firstvar+' and '+secondvar

firstvaramt=2.6756
secondvaramt=float(input('how much'+secondvar))

uppervar=var.upper()
varlen=len(var)
varlenstring='The length of var is: ' + str(varlen)
varlenstringlen=len(varlenstring)

print ('\n')
#print ('variable is', '\n' * 3)
#print ('var is' * 2, var *2)
print ('{0:>20} {1:>8}'.format('length var is:',varlen) )
print ( varlenstring+'|'+str(varlen))
print ( 'OR ', '{0:24} {1:>8}'.format (varlenstring, varlen))
#print ('But the length of varlenstring is', varlenstringlen)
#print ('uppercase is', uppervar, '\n')
print ('\n')

print ('{0:8} {1:>8.2f}'.format(firstvar,firstvaramt))
print ('{0:8} {1:>8.2f}'.format(secondvar,secondvaramt))
print ('\n')

