def calcNE(p,k):
    ans = p + k*p**2
    #print(ans)
    return ans

n = 48789828618640905340268650455641742611513932500406667
e = 65537
encMessage = 35527844866852571287965978399657369491580791928209728
factorsOfN = [176795785843333659350390219, 275967146987743635463977793]
p,q = factorsOfN
PHI = (p-1) * (q-1)
d = (e**-1) % PHI
print(d)
for i in range(1,e):
    if calcNE(p,i) == n*e:
        K = i
        break
try:
    print(K)
except NameError as namerror:
    print(n*e)