
# Line Chart
import matplotlib.pyplot as plt
hours=[1,2,3,4,5,6,7,8]
visitors=[50,60,55,70,90,120,110,130]

plt.plot(hours,visitors,
         color='green',
         marker='d',
         linestyle="--",
         linewidth=2,
         label="visitors")

plt.title("website Visitors Per Hour")
plt.xlabel("Hour of Day")
plt.ylabel("Number of Visitors")
plt.legend()

plt.grid(True)
plt.show()


# Bar Chart
import matplotlib.pyplot as plt
products=["Laptop","Mobile","Tablet","Headphones","Smartwatch"]
sales=[250,400,150,300,180]
plt.bar(products,sales, color="blue", edgecolor="red", alpha=0.3)

plt.title("Products Sales Comparison")
plt.xlabel("Products")
plt.ylabel("units Sold")
plt.show()


# Histogram char

import matplotlib.pyplot as plt
marks=[45,55,60,72,68,80,90,55,67,70,85,40,60,75,78,82,95,50,62,65,58,73,77,69,71,88,92,55,63,59]

plt.hist(marks, bins=13, color="orange", edgecolor="black", alpha=0.5)

plt.title("Distribution of Student Marks")
plt.xlabel("Marks Range")
plt.ylabel("Numbjher 0f Students")
plt.show()


# Scatter Plot

import matplotlib.pyplot as plt
ad_spend=[2,4,5,7,8,10,11,12]
sales=[20,25,28,35,40,48,50,52]
sizes=[200,250,280,350,400,480,500,520]
colors=sales
plt.scatter(ad_spend,sales,s=sizes,c=colors,cmap="viridis",alpha=0.8,edgecolors="black",linewidths=1.2)
plt.title("Advertising Spend vs sales (with color & size)",fontsize=14,fontweight="bold")
plt.xlabel("Ad Spend ($1000s)",fontsize=12)
plt.ylabel("sales($1000s)",fontsize=12)
plt.colorbar(label="sales Value")
plt.grid(True,linestyle='--',alpha=0.2)
plt.show()


# Pie chart
import matplotlib.pyplot as plt
brands=["Apple","Samsung","Xiaomi","Oppo","Others"]
market_share=[30,25,20,10,15]
plt.pie(market_share,labels=brands,autopct="%1.1f%%",startangle=0,colors=["gold","skyblue","lightcoral","lightgreen","violet"],explode=[0,0,0,0,0.2],shadow=True)
plt.title("Mobile Market Share 2025")
plt.show()

#Boxplot

import matplotlib.pyplot as plt
scores=[
    [78,85,90,92,88,76,95,9],
    [65,70,68,72,75,80,85,78],
    [90,92,94,96,88,91,89,93],
    [62,60,61,90,65,63,67,61],
    [70,85,8,50,92,91,100,89]]


plt.boxplot(scores,
             patch_artist=True,
             notch=False,
             vert=True,
             labels=["A","B","C","D","E"])
plt.title("Exam Scores Distribution Across Classes")
plt.xlabel("Classes")
plt.ylabel("Scores")
plt.grid(True, linestyle="--", alpha=0.7)
plt.show()
