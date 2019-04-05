def weight_on_planets():
    y = int(input("What do you weigh on earth? "))
    print("\nOn Mars you would weigh {} pounds.\nOn Jupiter you would weigh {} pounds.".format(y*0.38,y*2.34))
if __name__ == '__main__':
    weight_on_planets()