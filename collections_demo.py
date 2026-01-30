# collections_demo.py
# TASK 6: Lists, Tuples & Sets

print("===== PYTHON COLLECTIONS DEMO =====\n")

# 1. Store student names in a list
students = ["Ashok", "Ravi", "Sita", "Ashok", "Meena"]
print("Original Student List:", students)

# 2. Add an element
students.append("Kiran")
print("\nAfter Adding a Student:", students)

# 3. Remove an element
students.remove("Ravi")
print("\nAfter Removing a Student:", students)

# 4. Sort elements
students.sort()
print("\nAfter Sorting:", students)

# 5. Tuple for fixed data (immutable)
college_info = ("ANITS", "CSE", 2026)
print("\nCollege Info (Tuple):", college_info)

# 6. Convert list to set to remove duplicates
student_set = set(students)
print("\nStudents After Removing Duplicates (Set):", student_set)

# 7. Perform set operations
other_students = {"Meena", "Ramesh", "Kiran"}

print("\nUnion:", student_set.union(other_students))
print("Intersection:", student_set.intersection(other_students))
print("Difference:", student_set.difference(other_students))

# 8. Iterate over collections
print("\nIterating over Student List:")
for student in students:
    print(student)

print("\nIterating over Student Set:")
for student in student_set:
    print(student)

# 9. Mutable vs Immutable comparison
print("\nMutable vs Immutable:")
students[0] = "Anil"  # allowed
print("Modified List:", students)

print("\nTuple cannot be modified once created.")

print("\n===== END OF DEMO =====")
