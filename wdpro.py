import random
import msvcrt
mode = ''
wrongs = []
wrongord = []
rights = []
words = []

def subj(words,defi):
    """ while True:
        replace = input("是否开启同义词替换(同义词填写其中任意一个都可以，不得重复填写)?(\"y\"or\"n\')")
        if replace == 'y':
            rep = 1
            break
        elif replace == 'n':
            rep = 0
            break
        else:
            print("重新输入，", end = "") """
    print("总共",len(words),'个单词，按任意键开始')
    domain = []
    done = []
    nows = None
    for a in range (len(words)):
        domain.append(a)
    while True:
        msvcrt.getch()
        diff = list(set(domain).difference(set(done)))
        lenthss = len(diff)
        if lenthss == 0:
            break
        else:
            nows = random.choice(diff)
            done.append(nows)
            print("\n第",len(done),"个")
            print(defi[nows])
            tpin = input('输入答案：')
            if tpin == words[nows]:
                rights.append(tpin)
                print("Correct!")
            else:
                wrongs.append(words[nows])
                wrongord.append(len(done))
                print("Wrong!")
    riper = len(rights)/len(words)*100
    riper = round(riper,2)
    print("\n总共",len(words),"个单词，对了",len(rights),"个，错了",len(wrongs),"个，正确率约为",riper,"%\n错误单词为：")
    for b in range(len(wrongs)):
        num1 = wrongs[b]
        num2 = words.index(num1)
        wrdefi = defi[num2]
        print("第",wrongord[b],"个-> ",wrongs[b],":",wrdefi,",  ",end = '')
    print("\n")

def start():
    while True:
        while True:
            mode = input("输入学科(任意一个上方学科)，或输入“all”：")
            match mode:
                case 'bio':
                    words = biow
                    defi = biotr
                    break
                case 'art':
                    words = artw
                    defi = arttr
                    break
                case 'all':
                    words = allwords
                    defi = alldefi
                    break
                case _:
                    print("重新输入，", end = "")
        subj(words,defi)

biow = ['parasite','parasitic','mimicry','symbiosis','symbiotic','creature','strain','vital','ripe','breed','proliferate','propagate','subsist','exist','posterity','fermentation','stodgy','secret','assimilate','immune','morphology','vaccine','viability','fungus']
#tbiow = [2,'subsist']
biotr = ['寄生虫，寄生植物','寄生的','模仿，拟态','共生，合作','共生的','生物','种，血统','活的，活体','成熟的','养育，繁殖，品种','繁衍v.','繁殖vt.','生存(刚好够)','生存(艰苦地)','后代','发酵','难消化的','分泌','吸收','免除的，免疫的','形态学','疫苗','生存能力，发育能力，可行性','真菌，霉菌，菌类']
artw = ['picturesque','vivid','statue','portray','mold','embroider','tragedy','enact','prelude','profile','conjure','aesthetic','mythology','arcade','virtuoso','fresco','baroque']
arttr = ['如画般的','生动的','雕像','绘制','塑造','绣花','悲剧','扮演','序幕','外形，轮廓','用魔术变出','审美的，美学的','神话，神话学，神话集','拱廊','艺术品鉴赏家，古董收藏家，艺术大师','壁画','巴洛克式的，结构复杂的；巴洛特艺术']
allwords = biow + artw
alldefi = biotr + arttr

print("bio,art")
start()