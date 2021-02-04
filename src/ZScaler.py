import codecs
import re 

def feature_vector(text):
    # Write your code here
    d = {}
    for i in range(len(text)-1):
      #print(text[i:i+2])
      bigram = text[i:i+2]
      if bigram in d:
          d[bigram] += 1
      else:
          d[bigram] = 1
    feat_vec_dict = {}

    for key in d.keys():
        #print("key: " + key)
        encoded = ''
        for letter in key: 
            
            encoded += codecs.encode(letter.encode("utf-8"), 'hex').decode('utf-8')
        #print(encoded)
        decimal = int(encoded,16)
        #print(str(decimal) + ":" + str(d[key]))
        feat_vec_dict[decimal] = d[key]

        #print('\n')
    result = ''
    for key, val in sorted(feat_vec_dict.items()):
        result += str(key) + ":" + str(val) + ' '
    return result[:-1]

    
#print(feature_vector('banana'))

s = '''Wed Oct  7 17:33:08 2020;;9753885;;8892418;;""MTHgpVwEBb.org"";;797;;297;;995;;825;;596;;"None";;587;;903;;"AMqlzSdWxW.png"
Wed Oct  7 17:33:08 2020;;4039554;;4638074;;"skD"GzRkOrp".com";;621;;199;;105;;261;;334;;"None";;30;;803;;"FaMFjMTaBC.pdf"
Wed Oct  7 17:33:08 2020;;2062033;;8434637;;"JBKacjuYLQ.org";;814;;837;;331;;791;;672;;"None";;569;;312;;"GkZ"YpXP"SXp.xlsx"
Wed Oct  7 17:33:08 2020;;4146615;;6306482;;"GbaxZERUKz.org";;827;;62
7;;18;;77;;403;;"None";;291;;884;;"pqjJTabEdQ.pptx"
Wed Oct  7 17:33:08 2020;;6411304;;72545
36;;"dMulBggktz.com";;117;;889;;57;;5;;188;;"None";;858;;240;;"QkHyeDaFpz.docx"
Wed Oct  7 17:33:08 2020;;5714347;;816828;;""Twpudydnxr.net"";;845;;82;;909;;861;;962;;"None";
;948;;406;;"JIywrKuvIn.pptx"
'''

def loop(s):
    occurs = [m.start() for m in re.finditer('\n', s)]
    start = 0
    for end in occurs:
        substr = s[start:end]
        commas = substr.count(',')
        #print(substr) 
        #print("# commas: ", commas)
        if commas != 12:
            # end is bad 
            #print("Bad newline from %d to %d" % (start, end))
            s = s[0:end] + s[end+1:]
            s = s.replace(';;', ',')
            s = s.replace('""', '"')
            #print(s)
            return (s, True)

        else:
            start = end
    return (s, False)


def csv_cleanup(input_csv):
    output = input_csv.replace(';;', ',')
    output = output.replace('""', '"')
    status = True
    while status:
        #print("Iteration ", i)
        output, status = loop(output)
    

    return output


print(csv_cleanup(s))
#print("FINAL")
