import pickle as p
f=open("sanvi.dat","wb")
a=input("enter:")
p.dump(a,f)
f.close()

f=open("sanvi.dat","rb")
print(p.load(f))
f.close()

#with image

f1="WhatsApp Image 2026-03-28 at 15.47.46.jpeg"
f2=open("sanvi.dat","wb")
p.dump(f1,f2)
f1.close()
