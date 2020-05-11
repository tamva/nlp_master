# bed7bd6457084decbfdb723645194f65
import requests

def flatten_json(nested_json):

    out = {}

    def flatten(x, name=''):
        if type(x) is dict:
            for a in x:
                flatten(x[a], name + a + '_')
        elif type(x) is list:
            i = 0
            for a in x:
                flatten(a, name + str(i) + '_')
                i += 1
        else:
            out[name[:-1]] = x

    flatten(nested_json)
    return out

def takeFreq(elem):
    return elem[1]

freq_tab = []
words = []
USERNAME = 'tamva'
API_KEY = 'bed7bd6457084decbfdb723645194f65'
base_url = 'https://api.sketchengine.eu/bonito/run.cgi/'


# ======> Start of First Question <========
can = ('can','q[lemma="can"]')
may = ('may','q[lemma="may"]')
must = ('must','q[lemma="must"]')
shall = ('shall','q[lemma="shall"]')
will = ('will','q[lemma="will"]')
could = ('could','q[lemma="could"]')
might = ('might','q[lemma="might"]')
should = ('should','q[lemma="should"]')
would = ('would','q[lemma="would"]')

words.append(can)
words.append(may)
words.append(must)
words.append(shall)
words.append(will)
words.append(could)
words.append(might)
words.append(should)
words.append(would)

for cword,word in words:
    data = {
        'corpname': 'preloaded/brexit_1',
        'format': 'json',
        'q': word,
        'fcrit': 'word/i 0~0>0',
    }

    d = requests.get(base_url + '/freqs?q=%s' % data['q'] + '&' + 'corpname=%s' % data['corpname'] + '&' + 'fcrit=%s' % data['fcrit'],  auth=(USERNAME, API_KEY)).json()
    out = flatten_json(d)
    # print(out['Blocks_0_Items_0_freq'])

    freq_tab.append((cword, out['Blocks_0_Items_0_freq']))

for word in freq_tab:
   print(word)

# ======> End of First Question <=========

# ========> Start of Second Question <========
data = {
'corpname': 'preloaded/brexit_1', # the corpus to be loaded
'format': 'json', # return results in JSON format
# 'lpos': '-v', # Part Of Speech (POS)
'wlattr': 'lemma',
# get your API key here: https://app.sketchengine.eu/ in My account
'username': 'tamva', # your registered username here
'api_key': 'bed7bd6457084decbfdb723645194f65' # the API key created
}

n_v = []
v_o = []
most_vn = []
for item in ['brexit']:
    data['lemma'] = item
    d = requests.get(base_url + '/wsketch', params=data).json()
    print('Word sketch data for', item)
    for g in d['Gramrels'][:3]:
        type = g['name']
        print(' ' + g['name'])
        for i in g['Words']:
            print(' ' + i['word'])
            part_of = str(i['lempos'])
            part_of = part_of[-1]
            most_vn.append((i['word'],i['count'],part_of,i['score'],type))
            if type == 'verbs with "%w" as object':
                v_o.append((i['word'],i['count'],part_of,i['score'],type))
            elif type == 'nouns and verbs modified by "%w"':
                n_v.append((i['word'],i['count'],part_of,i['score'],type))

n_v.sort(reverse=True,key=takeFreq)
v_o.sort(reverse=True,key=takeFreq)

print('\n')
for elem in n_v:
    print(elem)
print('\n')
for elem in v_o:
    print(elem)

# ========> End of Second Question <========