from itertools import combinations
import math
import csv


def generate_combinations(query, min_words=1):
    words = query.split()
    combinations_list = []
    for r in range(min_words, len(words) + 1):
        for subset in combinations(words, r):
            combinations_list.append(' '.join(subset))
    return combinations_list


if __name__ == "__main__":
    query = "AI-Driven Adaptive Emotional Intelligence Enhancement in Personalized Learning Environments"
    n = len(query.split())
    k = n
    
    words = generate_combinations(query)
    print(len(words))
    print(words)
    
    
# Save the words in a CSV file
    with open('combinations.csv', 'w', newline='') as file:
      writer = csv.writer(file)
      for word in words:
        writer.writerow([word])
    # n, k = 3,3
    s = 0
    for i in range(1, n+1):
        s += math.comb(n, i)
    print(s)
    # print(math.comb(n, k)) 