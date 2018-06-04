if __name__ == '__main__':

    n = int(input().strip())
    all_scores = list(map(int, input().strip().split(" ")))
    scores = []
    previous_score = all_scores[0]
    scores.append(previous_score)

    # a)
    for i in range(1, len(all_scores)):
        if all_scores[i] != previous_score:
            scores.append(all_scores[i])
        previous_score = all_scores[i]

    m = int(input().strip())
    alice_scores = list(map(int, input().strip().split(" ")))
    current_index = len(scores) - 1

    # b)
    for alice_score in alice_scores:
        searching_position = True
        while searching_position:
            if current_index < 0:
                print(1)
                searching_position = False
            else:
                current_score = scores[current_index]
                if current_score == alice_score:
                    print(current_index + 1)
                    searching_position = False
                elif current_score > alice_score:
                    print(current_index + 2)
                    searching_position = False
                else:
                    current_index -= 1
