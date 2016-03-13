# substring of a string
m_str= input("enter string")
def get_substr(x,y):
r_str=""
for i in range(x,y):
    r_str+=m_str[i]
print r_str
#a= get_substr(5,11)
#print a