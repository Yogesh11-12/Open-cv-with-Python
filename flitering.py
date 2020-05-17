import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("FuelConsumptionCo2.csv", usecols=["ENGINESIZE","CYLINDERS","CO2EMISSIONS"], squeeze=True)
mask1=df["ENGINESIZE"]>4.0
mask2=df["CYLINDERS"]>4
mask3=df["CO2EMISSIONS"]
print(df.head(15))
print(df[mask1 & mask2].head(16))
plt.plot(mask1,mask3,'--','r',label="ENGINE Size")
plt.xlabel("ENGINESIZE")
plt.ylabel("CO2EMISSION")
plt.plot(mask2,mask3,'*','v',label="Cyclinders")
plt.xlabel("CYCLINDERS")
plt.show()

