import codecs

filesToCsv = ['sms-hamspam-val', 'sms-hamspam-train']

for el in filesToCsv:

    with codecs.open(el + ".csv", "w", encoding="utf8") as csv:

        csv.write("class_label,message\n")
        with codecs.open(el + ".txt", "r", encoding="utf8") as f:
            lines = f.readlines()

            for line in lines:

                line = line.split('	')
                line[1] = line[1].split('\n')[0]

                if "," in line[1]:
                    line[1] = '"' + line[1] + '"\n'
                else:
                    line[1] = line[1] + '\n'

                lineJoin = ','.join(line)

                csv.write(lineJoin)

        f.close()
    csv.close()
