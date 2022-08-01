import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt


order_dataset=pd.read_csv('orders_2016-2020_Dataset.csv')
review_dataset=pd.read_csv('review_dataset.csv')


str="""Input Value for genrate Graph chart:
       Enter 1 to see the analysis of Reviews given by Customers
       Enter 2 to see the analysis of different payment methods used by the Customers
       Enter 3 to see the analysis of Top Consumer States of India
       Enter 4 to see the analysis of Top Consumer Cities of India
       Enter 5 to see the analysis of Top Selling Product Categories
       Enter 6 to see the analysis of Reviews for All Product Categories
       Enter 7 to see the analysis of Number of Orders Per Month Per Year
       Enter 8 to see the analysis of Reviews for Number of Orders Per Month Per Year
       Enter 9 to see the analysis of Number of Orders Across Parts of a Day
       Enter 10 to see the Full Report"""


def Reviews():
    fig=plt.figure()
    plt.title('Reviews from the comsumer',fontsize=18)
    review_dataset['stars'].value_counts().plot(kind='bar')
    plt.show()
    
def Payment_Method():
    fig=plt.figure()
    order_dataset['Payment Method']=order_dataset['Payment Method'].fillna('Offline Payment ₹1,499.00')
    order_dataset['Payment Method']=order_dataset['Payment Method'].str.split('₹')
    New_dataframe=pd.DataFrame(order_dataset['Payment Method'].tolist())
    order_dataset['Payment Method']=New_dataframe[0]
    fig = plt.figure(figsize=(18,9))
    plt.title('Payment Method',fontsize=18)
    order_dataset['Payment Method'].value_counts().plot(kind='pie')
    plt.show()
    
def Top_Consumer_state():
    fig=plt.figure()
    plt.title('Top Consumers State of india',fontsize=18)
    order_dataset['Billing State']=order_dataset['Billing State'].fillna('IN_TN')
    order_dataset['Billing State'].value_counts()[:5].plot(kind='bar')
    plt.show()
    
    
def Top_Consumer_cities():
    fig=plt.figure()
    plt.title('Top Consumer Citys of india',fontsize=18)
    order_dataset['Billing City']=order_dataset['Billing City'].fillna('Chennai')
    order_dataset['Billin City']=order_dataset['Billing City'].replace('chennai','Chennai')
    order_dataset['Billing City']=order_dataset['Billing City'].replace('CHENNAI','Chennai')
    order_dataset['Billing City'].value_counts()[:5].plot(kind='bar')
    plt.show()
    
def Top_Selling_Product_Categories():
    fig=plt.figure()
    plt.title('Top Selling Product Categories',fontsize=18)
    order_dataset['LineItem Name'].value_counts()[:40].plot(kind='bar',figsize=(30,15))
    plt.show()
    
def Review_All_Pro_cate():
    fig=plt.figure()
    plt.title('Review for all product categories',fontsize=18)
    review_dataset.groupby('category')['stars'].count().plot(kind='bar',figsize=(18,9))
    plt.show()
    
    
def Orders_Per_Month_Per_Year():
    fig=plt.figure()
    plt.title('Order Per Month per Year',fontsize=18)
    pd.to_datetime(order_dataset['Order Date and Time Stamp']).dt.month.value_counts().plot(kind='pie',autopct='%0.2f%%',shadow=True)
    plt.show()
    
    
def reviews_Order_Per_Month():
    fig=plt.figure()
    plt.tight_layout()
    plt.title('Reviews for Number of Orders Per Month Per Year',fontsize=18)
    review_dataset['Month']=pd.to_datetime(order_dataset['Order Date and Time Stamp']).dt.month
    review_dataset.groupby('Month')['stars'].value_counts().plot(kind='bar',figsize=(20,10))
    plt.show()


def  Number_Of_Orders_Perday():
    fig=plt.figure()
    plt.title('Number of Orders Perday',fontsize=18)
    pd.to_datetime(order_dataset['Order Date and Time Stamp']).dt.day.value_counts().plot(kind='bar',figsize=(20,10))
    plt.show()

def Full_report():
    fig=plt.figure(figsize=(20,10))
    plt.title('Full Report')
    review_dataset['stars'].value_counts().plot(kind='bar',label='<2.0 is negative rating')
    plt.xlabel('Number of Reviews')
    plt.ylabel('Reviews')
    plt.show()
    plt.title('Diffrent Payment Method')
    order_dataset['Payment Method'].dropna().str.split().apply(lambda x:x[0]).value_counts().plot(kind='pie',autopct='%0.2f%%',figsize=(20,10))
    plt.show()
    plt.title('Top Consumer State')
    order_dataset['Billing State'].dropna().value_counts().head().plot(kind='pie',autopct='%0.2f%%',figsize=(20,10))
    plt.show()
    plt.title('Top Consumer Cities')
    order_dataset['Billing City'].dropna().value_counts().head().plot(kind='pie',autopct='%0.2f%%',figsize=(20,10))
    plt.show()
    plt.title('Top Selling Product Categories')
    order_dataset['LineItem Name'].value_counts()[:10].plot(kind='pie',autopct='%0.2f%%',figsize=(50,25))
    plt.show()
    plt.title('Review for all product categories')
    review_dataset.groupby('category')['stars'].count().plot(kind='bar',figsize=(18,9))
    plt.show()
    plt.title('Order per Month per Year')
    pd.to_datetime(order_dataset['Order Date and Time Stamp']).dt.month.value_counts().plot(kind='pie',autopct='%0.2f%%',shadow=True)
    plt.show()
    plt.title('Reviews for Number of Orders Per Month Per Year')
    review_dataset['Month']=pd.to_datetime(order_dataset['Order Date and Time Stamp']).dt.month
    review_dataset.groupby('Month')['stars'].value_counts().plot(kind='bar',figsize=(20,10))
    plt.show()
    plt.title('Number of Orders Across Parts of a day')
    pd.to_datetime(order_dataset['Order Date and Time Stamp']).dt.day.value_counts().plot(kind='bar',figsize=(20,10))
    plt.show()
    """wb = xw.Book()
    sht=wb.sheets[0]
    sht.name="Excel Chart"
    sht.pictures.add(fig,name="Excel Chart",update=True,left=sht.range("A4").left,top=sht.range("A4").top,
                      height=2000,width=1500)"""

print(str)
while(True):
    Number=int(input("Enter the number to see the analysis of your choice:"))
    if Number == 1:
        Reviews()
    elif Number == 2:
        Payment_Method()
    elif Number == 3:
        Top_Consumer_state()
    elif Number == 4:
        Top_Consumer_cities()
    elif Number == 5:
        Top_Selling_Product_Categories()
    elif Number == 6:
        Review_All_Pro_cate()
    elif Number == 7:
        Orders_Per_Month_Per_Year()
    elif Number == 8:
        reviews_Order_Per_Month()
    elif Number == 9:
        Number_Of_Orders_Perday()
    elif Number == 10:
        Full_report()
    elif Number==11:
        print("Please Enter Valid Number")
        break