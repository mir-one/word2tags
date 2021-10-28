from word2tags import word2tags


if __name__ == '__main__':
    word2tags = word2tags()
    word2tags.load()

    for word in u'кошки рой для'.split():
        for i, tagset in enumerate(word2tags[word]):
            print(u'{}[{}] => {}'.format(word, i, tagset))
