def solution(distance, scope, times):
    # times : [work, rest]
    # save all scope and times and sort
    enemy_dictionary = dict()
    for one_scope, one_time in zip(scope, times):
        one_scope.sort() # missing point
        enemy_dictionary[one_scope[0]] = (one_scope, one_time)
    dictioanry_order = sorted(enemy_dictionary)

    for index in dictioanry_order:
        one_scope, one_time = enemy_dictionary[index]
        
        total_time = sum(one_time)
        start_scope, end_scope = one_scope
        # if hwarang is in scope during working times, return current distance
        for i in range(start_scope, end_scope + 1):
            if 0 < (i % total_time) <= one_time[0]:
                return i
    return distance
