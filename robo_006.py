year = int(input())
print(f"{13 if year % 4 != 0 else 12}/09/{"0"* (4-len(str(year)))+str(year)}")