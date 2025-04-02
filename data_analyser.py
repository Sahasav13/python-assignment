def data_analyser(numbers):
    sum_num = sum(numbers)
    minimum = min(numbers)
    maximum = max(numbers)
    average = sum(numbers)/len(numbers)
    sort = sorted(numbers)

    aboveavg =0
    for i in numbers :
        if(i<average):
            aboveavg+=1
        return { "sum" : sum_num,
                 "minimum" :minimum,
                 "maximum" :maximum,
                 "average" :average,
                 "above_avg" :aboveavg,
                 "sort" : sort
                }
numbers = [70,80,90,20,40]
print(data_analyser(numbers))
