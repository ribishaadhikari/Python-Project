1.
items = [3,5,7,9,11,13]
r_items = items.pop(4)
items.insert(1,r_items)
items.append(11)
print(items)

2.
first_set = {23, 42, 65, 57, 78, 83, 29}
second_set = {57, 83, 29, 67, 73, 43, 48}
intersection = first_set & second_set
if intersection:
    print(f'Common elements: {intersection}')
    a = first_set.difference(second_set)
    print(a)
else:
    print('No common elements')

3.
first_set = {27, 43, 34}
second_set = {32, 93, 22, 27, 43, 53, 48}
if first_set.issubset(second_set):
    print("first_set is a subset of second_set")
    first_set.clear()
    print(first_set)
elif first_set.issuperset(second_set):
    print("first_set is a superset of second_set")
    second_set.clear()
    print(second_set)
else:
    print("No relationship found!")

4.
month = {
    'jan': 47,
    'feb': 52,
    'march': 47,
    'April': 44,
    'May': 52,
    'June': 53,
    'july': 54,
    'Aug': 44,
    'Sept': 54
}
month_values = list(set(month.values()))
print(month_values)

5.
sample_list = [87, 45, 41, 65, 94, 41, 99, 94]
new = tuple(set(sample_list))
print('Tuple without duplicates:' ,new)
print('Maximum value: ',max(new))
print('Minimum value: ',min(new))

6.
club_A = {"ram", "hari", "shyam"}
club_B = {"ram", "gita", "hari"}
common_members = club_A.intersection(club_B)
if common_members:
    print("The common members are :", common_members)
else:
    print("No overlapping members found between groups")

7.
required_tasks = {"Email", "Report", "Meeting"}
completed_tasks = {"Email", "Report"}
if required_tasks.issubset(completed_tasks):
    print("All tasks completed.")
else:
    print("Some tasks pending.")

