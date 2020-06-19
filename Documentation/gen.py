import codecs

def gen_toc(order):
    toc = "" # table of content
    for i, name in enumerate(order):
        file = codecs.open(name+".md", "r", "utf_8_sig")
        title = file.readline()
        if (len(title) < 3):
            title = file.readline()
        title = title.replace('### ','')
        title = title.strip()
        file.close()
        toc += "[" + str(i+1) + ". " + title + "]" + "(#" + name[2:] + ")\n\n"
    return toc

def main():
    order = []
    with open("order.txt", "r") as order_file:
        for line in order_file:
            order.append(line.strip())
    toc = gen_toc(order)

    res = codecs.open("Documentation.md", "w", "utf_8_sig")
    res.write(toc)
    res.write("\n")
    for name in order:
        file = codecs.open(name+".md", "r", "utf_8_sig")
        content = "\n<a name=\""+name[2:]+"\"/>\n\n"
        content += file.read()
        file.close()
        res.write(content)
    res.close()

if __name__ == "__main__":
    main()