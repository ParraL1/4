#Name: Lilliana Parra
#Github Username: ParraL1
#Date: 01/26/2022
#Description: Calculates falling distance using time and given equation


time = float(input("Enter the amount of time the object is falling"))
def fall_distance(falling_time):
    return 0.5 * 9.8 *falling_time *falling_time
print("Distance object has fallen is", fall_distance(time))
