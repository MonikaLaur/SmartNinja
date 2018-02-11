if __name__ == '__main__':

    messages = []
    messages.append({"text":"hallo", "number":0})
    messages.append({"text": "joo", "number": 10})
    messages.append({"text": "abaa", "number": 5})
    print
    print messages
    print
    print sorted(messages, key=lambda x: x["number"]) # sorts by nr value
    print
    print sorted(messages, key=lambda x: x["text"])
