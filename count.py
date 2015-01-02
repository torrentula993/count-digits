
import sys, pprint


def digitsum(number,sum=0):
    while number:
        number,r = divmod(number,10)
        sum+=r
    return sum

def find_numbers(max,eqs):
    numbers,matches = range(max),list()
    for num in numbers:
        if digitsum(num) == eqs:
            matches.append(num)
    return matches 

def main():
    max,eqs = int(sys.argv[1]),int(sys.argv[2])
    matches = find_numbers(max,eqs)
    print(matches)
    print("count",len(matches))

if __name__ == "__main__":
     main()
