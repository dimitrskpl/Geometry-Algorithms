def read_points(file_name):
    f = open(file_name, "r")
    f.readline() 
    f.readline()

    points_list = []
    for line in f:
        fields = line.split()
        points_list.append( (int(fields[1]), int(fields[2])) )

    return points_list
    f.close()

def main():
    points_list = read_points('../data/images/euro-night-0000010.instance')
    print(points_list)

if __name__ == "__main__":
    main()

