from typing import List
import random

def get_new_alpha(old_i : float) -> float:
    return old_i * 0.5

def hitung_jarak(weight : List[float], user_input : List[int]) -> float:
    jarak : float = 0.0
    for i in range(len(weight)):
        jarak += (user_input[i] - weight[i])**2
    jarak = jarak ** 0.5
    return round(jarak, 2)

def print_hitung_jarak(weight : List[float], user_input : List[int]) -> str:
    hasil : str = ""
    delimiter : str = "("
    kurung : str = ""
    for i in range(len(weight)):
        kurung += f"{delimiter}{weight[i]} - {user_input[i]})^2"
        delimiter = " + ("
    hasil = f"sqrt({kurung}) = {hitung_jarak(weight, user_input)}"
    return hasil

def update_weight(weight : List[float], alpha : float, input : List[int]) -> None:
    b : List[float] = []
    for i in range(len(weight)):
        b.append(alpha * (input[i] - weight[i]))
    for i in range(len(weight)):
        weight[i] = round(weight[i] + b[i], 2)

def print_updating_process(weight : List[float], alpha : float, input : List[int]) -> str:
    hasil : str = ""
    for i in range(len(weight)):
        hasil += f"{i+1} = {weight[i]} + {alpha} * ({input[i]} - {weight[i]}) = {round(weight[i] + alpha * (input[i] - weight[i]), 2)}\n"
    return hasil

def main():
    alpha : float = 0.6
    w1 : List[float] = [0.4,0.2,0.1,0.1]
    w2 : List[float] = [0.3,0.1,0.6,0.5]
    inputs : List[int] = [
        (1,1,0,0),
        (0,0,0,1),
        (1,0,0,0),
        (0,0,0,1)
    ]
    for _ in range(1):
        for i, inp in enumerate(inputs):
            print()
            print(f"\t\tIterasi-{i+1}".upper())
            print()
            print("Bobot Before")
            print(f"W1 = {w1}")
            print(f"W2 = {w2}")
            print()
            print("Jarak 1: ")
            print(print_hitung_jarak(w1, inp))
            jarak_w1 : float = hitung_jarak(w1, inp)
            print()
            print("Jarak 2: ")
            print(print_hitung_jarak(w2, inp))
            jarak_w2 : float = hitung_jarak(w2, inp)
            new_alpha : float = get_new_alpha(alpha)
            print(f"alpha yang baru = 0.5 * alpha lama = 0.5 * {alpha} = {new_alpha}")
            alpha = new_alpha
            if (jarak_w1 > jarak_w2):
                print()
                print("Karena jarak W2 lebih kecil dari W1, maka")
                print("Update Bobot-2")
                update_process_str : str = print_updating_process(w2, alpha, inp) 
                print(update_process_str)
                update_weight(w2, alpha, inp) 
                
            elif (jarak_w1 < jarak_w2):
                print()
                print("Karena jarak W1 lebih kecil dari W2, maka")
                print("Update Bobot-1")
                update_process_str = print_updating_process(w1, alpha, inp)
                print(update_process_str)
                update_weight(w1, alpha, inp)
            
            print()
            print("Bobot After")
            print(f"W1 = {w1}")
            print(f"W2 = {w2}")
            
    
if __name__ == "__main__":
    main()