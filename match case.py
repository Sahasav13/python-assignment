calculate_grade = int(input("enter the numerical grade :"))

match calculate_grade :
    
    case calculate_grade if 90<= calculate_grade <=100 :
                      print("A grade")
    case calculate_grade if 80<= calculate_grade <90 :
                      print("B grade")
    case calculate_grade if 70<= calculate_grade <80 :
                      print("C grade")
    case calculate_grade if 60<= calculate_grade <70 :
                      print("D grade")
    case calculate_grade if 0< calculate_grade <60 :
                      print("F grade")
                      
        
