girl_names = ["Evelyn", "Jessica", "Somto", "Edith", "Liza", "Madonna", "Waje", "Tola", "Aisha", "Latifa"]
girl_ages = [17, 16, 17, 18, 16, 18, 17, 20, 19, 17]
girl_heights = [5.5, 6.0, 5.4, 5.9, 5.6, 5.5, 6.1, 6.0, 5.7, 5.5]
girl_scores = [80, 85, 70, 60, 76, 66, 87, 95, 50, 49]

boy_names = ["Chinedu", "Liam", "Wale", "Gbenga", "Abiola", "Kola", "Kunle", "George", "Thomas", "Wesley"]
boy_ages = [19, 16, 18, 17, 20, 19, 16, 18, 17, 19]
boy_heights = [5.7, 5.9, 5.8, 6.1, 5.9, 5.5, 6.1, 5.4, 5.8, 5.7]
boy_scores = [74, 87, 75, 68, 66, 78, 87, 98, 54, 60]

all_names = girl_names + boy_names
all_ages = girl_ages + boy_ages
all_heights = girl_heights + boy_heights
all_scores = girl_scores + boy_scores

print("Name \t| Age \t| Height | Score")
print("-" * 30)  # Separator line
for i in range(len(all_names)):
    print(f"{all_names[i]} \t| {all_ages[i]} \t| {all_heights[i]} \t| {all_scores[i]}")