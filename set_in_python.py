# intersection_update()
set1 = {"Tokyo","Burlin","Delhi"}
set2 = {"Tokyo","Seoul","Kabul","Madrid"}

set1.intersection_update(set2)
print(set1)

# symitric_difference
set1 = {"Tokyo","Burlin","Delhi"}
set2 = {"Tokyo","Seoul","Kabul","Madrid"}

set3 = set1.symmetric_difference(set2)
print(set3)

# isdisjoint()
set1 = {"Tokyo","Burlin","Delhi"}
set2 = {"Tokyo","Seoul","Kabul","Madrid"}

print(set1.isdisjoint(set2))


# difference()
set1 = {"Tokyo","Burlin","Delhi"}
set2 = {"Tokyo","Seoul","Kabul","Madrid"}

print(set1.difference(set2))

# issupperset()
set1 = {"Tokyo","Burlin","Delhi"}
set2 = {"Tokyo","Seoul","Kabul","Madrid"}

print(set1.issuperset(set2))
print(set1.issubset(set2))
