# pip install pymysql

import pymysql


def listProducts_EX05_01():
    db = pymysql.connect(host='localhost',user='root',password='Rainier01',database='northwind')
    crsr = db.cursor()
   
    sql = "Select P.`List Price` , P.`List Price`*1.10 as `Adjusted list Price` "
    sql = sql + " From products P"
    sql = sql + " Where P.`List Price` > 0"
    sql = sql + " Limit 5"
   

    res = crsr.execute(sql)
    name = crsr.description
    print(f'{name[0][0]:<8} | {name[1][0]:>15}')
    for row in crsr :
        print(f'{row[0]:<8}   |{str(round(row[1],2)):>8}')


def targetlevel_EX05_02():
    db = pymysql.connect(host='localhost',user='root',password='Rainier01',database='northwind')
    crsr = db.cursor()

    sql = "Select max(P.`Target Level`) as `Max Targ Lvl` , min(P.`Target Level`) as `Min Targ LvL` , avg(P.`Target Level`) as `Avg Targ Lvl`"
    sql = sql + " From products P"

    res = crsr.execute(sql)
    name = crsr.description
    print(f'{name[0][0]:<8} | {name[1][0]:>15}  | {name[2][0]:>15}')

    for row in crsr :
        print(f'{str(row[0]):<8}  {str(row[1]):>15}  {str(round(row[2], 2)):>15}')


def discontinued_EX05_03():
    db = pymysql.connect(host='localhost',user='root',password='Rainier01',database='northwind')
    crsr = db.cursor()

    sql = "Select count(*) as `Discontinued Product Count` "
    sql = sql + " From products P"
    sql = sql + " Where P.`Discontinued` =1"

    res = crsr.execute(sql)
    name = crsr.description

    print(f'{name[0][0]:<8}')
    for row in crsr : 
        print(f'{str(row[0])}')


def contains_dried_EX05_04():
    db = pymysql.connect(host='localhost',user='root',password='Rainier01',database='northwind')
    crsr = db.cursor()

    sql = "Select *"
    sql = sql + " From products P"
    sql = sql + " Where P.`Product_Name` Like Concat('%' , 'dried' , '%') "
    sql = sql + " Limit 5"

    res = crsr.execute(sql)
    name = crsr.description

    print(f'{name[0][0]:<15} | {name[1][0]:<10} | {name[2][0]:<15} | {name[3][0]:<15}')
    for row in crsr : 
        print(f'{str(row[0]):<15} {str(row[1]):<15} {str(row[2]):<15} {str(row[3]):<15}')


def bevnotdiscontinued_EX05_05():
    db = pymysql.connect(host='localhost',user='root',password='Rainier01',database='northwind')
    crsr = db.cursor()

    sql = "Select *"
    sql = sql + " From products P "
    sql = sql + " Where P.`Discontinued` = 0 and P.`Category` = 'Beverages' "
    sql = sql = " Limit 5"

    res = crsr.execute(sql)
    name = crsr.description

    print(f'{name[0][0]:<15} | {name[1][0]:<15} | {name[2][0]:<10} | {name[3][0]:<10} | {name[4][0]:<10}')
    for row in crsr : 
        print(f'{str(row[0]):<15} {str(row[1]):<15} {str(row[2]):<15} {str(row[3]):<15}')


def shippingfeebig_EX05_06():
    db = pymysql.connect(host='localhost',user='root',password='Rainier01',database='northwind')
    crsr = db.cursor()

    sql = "Select S.`Company` "
    sql = sql + " From shippers S "
    sql = sql + " Where S.ID in (Select O.`Shipper ID` From orders O where O.`Shipping Fee` > 100) "
    sql = sql + " Limit 5"

    res = crsr.execute(sql)
    name = crsr.description

    print(f'{name[0][0]:<15}')
    for row in crsr : 
        print (f'{str(row[0]):<15}')


def employeenameandjob_EX05_07():
    db = pymysql.connect(host='localhost',user='root',password='Rainier01',database='northwind')
    crsr = db.cursor()

    sql = "Select E.`First Name` , E.`Last Name` , E.`Job Title` "
    sql = sql + " From employees E "
    sql = sql + " Limit 5"
    
    res = crsr.execute(sql)
    name = crsr.description

    print(f'{name[0][0]:<15} {name[1][0]:<15} {name[2][0]:15}')
    for row in crsr :
        print(f'{str(row[0]):<15} {str(row[1]):<15} {str(row[2]):<15}')


def shipdateandworker_EX05_08():
    db = pymysql.connect(host='localhost',user='root',password='Rainier01',database='northwind')
    crsr = db.cursor()

    sql = "Select O.`Shipped Date` , E.`First Name` , E.`Last Name` "
    sql = sql + " From orders O , employees E "
    sql = sql + " Where O.`Employee ID` = E.`ID` "
    sql = sql + " Limit 5"

    res = crsr.execute(sql)
    name = crsr.description

    print(f'{name[0][0]:<15} {name[1][0]:<15} {name[2][0]:<15}')
    for row in crsr : 
        print (f'{str(row[0]):<15} {str(row[1]):<15} {str(row[2]):<15}')


def priceinfo_EX05_09():
    db = pymysql.connect(host='localhost',user='root',password='Rainier01',database='northwind')
    crsr = db.cursor()

    sql = "Select max(P.`List Price`) as `Max price`, min(P.`List Price`) as `Min Price` , avg(P.`List Price`) as `Avg Price`  "
    sql = sql + " From products P"

    res = crsr.execute(sql)
    name = crsr.description

    print(f'{name[0][0]:<15} {name[1][0]:<15} {name[2][0]:<15}')
    for row in crsr : 
        print (f'{str(row[0]):<15} {str(row[1]):<15} {str(round(row[2], 2)):<15}')


def categoryinfor__EX05_10():
    db = pymysql.connect(host='localhost',user='root',password='Rainier01',database='northwind')
    crsr = db.cursor()

    sql = " Select P.`Category` , max(P.`List Price`) as `Max Price` , min(P.`List Price`) as `Min Price` , avg(P.`List Price`) as `Avg Price` "
    sql = sql + " From products P "
    sql = sql + " Group by P.`Category` "
    sql = sql + " Limit 5"

    res = crsr.execute(sql)
    name = crsr.description

    print(f'{name[0][0]:<15} {name[1][0]:<15} {name[2][0]:<15} {name[3][0]:<15} ')
    for row in crsr : 
        print (f'{str(row[0]):<15} {str(row[1]):<15} {str(row[2]):<15} {str(round(row[3],2)):<15}')


def pick_querey():
    x = input("Choose what query you would like displayed: ")


    if x == "1":
        listProducts_EX05_01()
    
    if x == "2":
        targetlevel_EX05_02()
    
    if x == "3":
        discontinued_EX05_03()
    
    if x == "4":
        contains_dried_EX05_04()
    
    if x == "5":
        bevnotdiscontinued_EX05_05()
    
    if x == "6":
        shippingfeebig_EX05_06()
    
    if x == "7":
        employeenameandjob_EX05_07()
    
    if x == "8":
        shipdateandworker_EX05_08()
    
    if x == "9":
        priceinfo_EX05_09()
    
    if x == "10":
        categoryinfor__EX05_10()


print("Below are our function options. ")
print ("1. List 100% product price.")
print("2. List Max, Min, Avg, target prices for the products.")
print("3. How Many products are discontinued.")
print("4. List all products with 'dried' in the name.")
print("5. List all discontinued beverages.")
print("6. List shippers who shipped with a shipping fee greater than $100.")
print("7. List employees and their job titles.")
print("8. List ship dates for orders and employee assigned to the order.")
print("9. List max, min, avg prices for the products.")
print("10. Max, min, and avg product price for each category of product")

pick_querey()