print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
percentage = float(input("What percentage of tip do you want to give?"))
tip = (bill / 100) * percentage
total = round((bill + tip), 2)
people = int(input("How many people are going to split the bill?"))
total_split = round((total / people), 2)
print("For a bill of " + str(bill) + "$, and by giving " + str(percentage) +
      "% of tip, the total value of the " + str(total) + "$ bill per person if we split it in " + str(people) + " will be " + str(total_split) + "$.")
