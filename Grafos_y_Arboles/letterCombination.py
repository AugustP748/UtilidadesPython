def getListofNum(num:int) -> list:
    res = []
    while num > 0:
        num, remainder = divmod(num, 10)
        res.insert(0,remainder)
    return list(res)

def getResult(number:int):
    list_result:list=[]
    list_elements:list=[]
    phone:dict = {1:None,2:["A","B","C"],3:["D","E","F"],4:["G","H","I"],5:["J","K","L"],
                  6:["M","N","O"],7:["P","Q","R","S"],8:["T","U","V"],9:["W","X","Y","Z"],0:None}
    list_Num:list = getListofNum(number)
    
    for element in list_Num:
        list_elements.append(phone.get(element))
        
    

   

if __name__ == '__main__':
    number:int = 2
    result = getResult(number)
    
    #print(result)
