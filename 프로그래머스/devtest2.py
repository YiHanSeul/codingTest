def solution(registered_list, new_id):
    answer = ''
    temp=[]
    #while new_id in registered_list:
    for i in new_id:
        if i > '0':
            if i<'9':
                temp.append(i)
        else:
            num_id+='1'
            print(num_id)


    return new_id
