import pymysql
conn = pymysql.connect(host='localhost', user='root', password='', db='new_test')
cursor = conn.cursor()
# Height (cm), Weight (kgs), Age, Waist (cm)

def insertData(data):
    try:
        insert_query = "INSERT IGNORE INTO  waisttable (height,weight,age,waist) VALUES (%s, %s, %s, %s)"
        height=data[0]
        weight=data[1]
        age=data[2]
        waist=data[3]
        print(height,weight,age,waist)
        cursor.execute(insert_query, (height,weight,age,waist))
        conn.commit()
        return True
    except:
        return False
def rangeWaist(data):
    height=data[0]
    weight=data[1]
    age=data[2]
    print(type(height))
   
    range_query="SELECT MAX(waist),MIN(waist) FROM waisttable Where ABS(height-%s)<=1 AND ABS(weight-%s)<=1 AND ABS(age-%s)<=1"
    cursor.execute(range_query, (height,weight,age))
    result= cursor.fetchone()
    # print(result[0])
    max_waist = result[0]
    min_waist = result[1]
    # print(max_waist,type(max_waist),float(max_waist))
    conn.commit()
    return [float(min_waist),float(max_waist)]


