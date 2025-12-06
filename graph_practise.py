import numpy as np
import matplotlib.pyplot as pt

x=np.array(["mon","tue","wed","thu","fri","sat","sun"])
y=np.array([20,10,15,30,40,70,90])

pt.plot(x,y,'o:r',ms=15, mec="#4CAF50")
pt.show()
ecommerceData=[
    {
        "product":"iphone"
        "sold qty":[20,33,44,55,34]
    },
    {
         "product":"ipad"
        "sold qty":[12,45,67,23,44]

    }
]
iphoneData=ecommerceData[0]['sold qty']
tabData=ecommerceData[1]['sold qty']
iphoneData=np.array(iphoneData)
ipadData=np.array(ipadData)
dayList=[]
for day in range(1,phoneData.size+1):
    dayList.append("day"+str(day))
pt.plot(dayData,iphoneData,dayData,tabData)
pt.xlabel("Last 5 Days")
pt.ylabel("sold qty ")
pt.show()

