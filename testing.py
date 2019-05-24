import pyodbc as py
import pandas as pd
conn = py.connect('Driver={SQL Server};'
                          'Server=LAPTOP-4D3T9VBG;'
                          'Database=django_test;'
                          'Trusted_Connection=yes;')
query = 'select * from category'
category=pd.read_sql(query,conn)
query = 'select * from product'
product = pd.read_sql(query,conn)
dic={}
k=0
for i in range(0,len(product['product_id'])):
    dic['row _'+str(i)] = [product['product_name'][i],
       product['prodcut_price'][i],
        product['product_weight'][i],
        product['product_color'][i],
        product['product_description'][i]]
temp_dic = {'product':dic}
print(dic)
context = {
    'c_name': category['category_name']}
context.update(temp_dic)
print(context)
# context = {
#     'c_name': category['category_name'],
#     'product':{
#         'p_name': product['product_name'],
#         'p_price': product['prodcut_price'],
#         'p_weight': product['product_weight'],
#         'p_color': product['product_color'],
#         'p_description': product['product_description']
#     }