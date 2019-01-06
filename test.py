from src import Functions

# FUNCTIONAL DEMO


if __name__ == '__main__':

    data, types = Functions.dataPreProcessing('data/sample.csv', 'all', ['Combination Id', 'Converted'])

    a = data[0]
    b = data[1]

    for i in range(0, len(a)):
        print(str(i) + " " + str(a[i]) + " " +str(b[i]))