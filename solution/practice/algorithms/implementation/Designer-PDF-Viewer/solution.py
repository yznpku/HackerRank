def designerPdfViewer(h, word):
    word_height = [h[ord(c)-ord("a")] for c in word ]
    return max(word_height)*len(word)


if __name__ == '__main__':
    h = list(map(int, input().rstrip().split()))
    word = input()
    result = designerPdfViewer(h, word)
    print(result)
