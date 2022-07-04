def solution(bridge_length, weight, truck_weights):
    cnt =0
    time =0
    list =[]
    for i in truck_weights :
        if not list:
            list.append(truck_weights[i])
            if weight>cnt:
                cnt=truck_weights+cnt
    

    answer = 0
    return answer



solution(2,10,[7,4,5,6])
solution(100,100,[10])
solution(100,100,[10,10,10,10,10,10,10,10,10,10])