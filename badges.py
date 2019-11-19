# Calculates the amount of exp to subtract from medium
# and easy cards for a single hard card (NOT the entire lab)

def assignPoints(basePts, numCards):
    # subtract the bonus
    bonusRate = 0.1
    bonus = bonusRate * basePts
    basePtsNoBonus = basePts - bonus

    # get amount to subtract for medium and easy cards
    totalWeights = numCards["medium"] + numCards["easy"] * 2
    subAmountM = basePtsNoBonus / totalWeights
    subAmountE = subAmountM * 2

    # floor amts
    subAmountM //= 1
    subAmountE //= 1
    print("Hard card: " + str(basePts))
    print("Medium card: " + str(subAmountM))
    print("Easy card: " + str(subAmountE))

def main():
    numMed = int(input("Enter number of medium cards under this hard card: "))
    numEasy = int(input("Enter number of easy cards under this hard card: "))
    basePts = int(input("Enter the exp split amount for this hard card: "))

    numCards = {"medium" : numMed, "easy" : numEasy}
    assignPoints(basePts, numCards)

while (True):
    main()
