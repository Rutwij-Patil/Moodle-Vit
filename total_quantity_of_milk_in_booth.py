n = int(input())
suml=0
summl=0
while(n>0) :
  a = str(input())
  l = a[0]
  ml a[1]+a[2]+a[3]
  suml +=int(l)
  summl += int(ml) *10
  if summl>999:
    suml += summl//1000
    summl -= (summl//1000)*1000
  n = n-1
print(suml,"(in liters)")
print(summl,"(in ml)")
