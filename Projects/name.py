STUDENT_LIST = ["Alice", "Bob", "Alice", "Charlie", "Bob", "Alice"]

def cunter(student_list):
    counts = {}
    
    for name in student_list:
        if name in counts:
            counts[name] += 1
        else:
            counts[name] = 1
    print(counts)
    return counts

def main():
    result = cunter(STUDENT_LIST)
    for name, count in result.items():
        print(f"{name}: {count}")
if __name__ == "__main__":
    main()