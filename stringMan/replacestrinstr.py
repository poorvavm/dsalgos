#How to replace string a with string b
# substring of a string
m_str= input("enter string:")
replace str = input ("enter replacement : ")
def replace_str(x,y):
    for i in range(x, y):
        m_str = m_str[:x] + replace_str + m_str[y:]
    print m_str