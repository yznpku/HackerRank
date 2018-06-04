def gridSearch(G, P):
    found = False
    # We iterate through the rows of G
    for i in range(len(G)):
        if found is True:
            break
        else:
            row_to_be_found = P[0]
            # We check if the first row of P is contained in G[i]
            if row_to_be_found in G[i]:
                # We find all the start_indexes, i.e. all the indexes of G[i] where P[0] starts
                start_indexes = find_all(G[i], row_to_be_found)
                # We iterate through the start_indexes
                for start_index in start_indexes:
                    if found is True:
                        break
                    else:
                        # if P is made of only row, found = True
                        if len(P) == 1:
                            found = True
                        else:
                            # We check if the remaining rows of P are equal to the corresponding parts of the rows of P,
                            # according to the current start_index
                            for j in range(1, len(P)):
                                row_to_be_found = P[j]
                                if i + j < len(G):
                                    if G[i + j][start_index:start_index + len(row_to_be_found)] != row_to_be_found:
                                        found = False
                                        break
                                    else:
                                        # If we have reached the last row of P, found = True
                                        if j == len(P) - 1:
                                            found = True
                                            break
    return "YES" if found else "NO"

def find_all(a_str, sub):
    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1: return
        yield start
        start += 1

if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        R, C = input().strip().split(' ')
        R, C = [int(R), int(C)]
        G = []
        G_i = 0
        for G_i in range(R):
           G_t = str(input().strip())
           G.append(G_t)
        r, c = input().strip().split(' ')
        r, c = [int(r), int(c)]
        P = []
        P_i = 0
        for P_i in range(r):
           P_t = str(input().strip())
           P.append(P_t)
        result = gridSearch(G, P)
print(result)
