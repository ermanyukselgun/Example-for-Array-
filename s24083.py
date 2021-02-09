def rank(numbers):
    ### Kodunuzu rank fonksiyonun blogu icerisinde girintilemeye dikkat ederek yaziniz.
    result = 0
    for i in numbers:
        if (i+1) not in numbers:
            continue
        else:
            result = result + abs(numbers.index(i)-numbers.index(i+1))         
        
    return result



