#_*_ coding=GBK _*_
def fac(n):
    if n==1 or n==0:
        return 1
    else:
        return n*fac(n-1)
def main():
    print("����һ����׳˵ĳ���\n")
    n=input("������һ����������")
    try:
        n=int(n)
    except ValueError:
        print("�������������һ����������")
    print('%d!=%d' %(n,fac(n)))
if __name__=="__main__":
    main()


