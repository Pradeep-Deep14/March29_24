def my_args(a,b=9,*args,**kwargs):
    print(a,b,args,kwargs)

my_args(1,2,3,4,5,x=6,y=7)