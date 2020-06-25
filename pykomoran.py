from PyKomoran import *
import re
komoran = Komoran("EXP")

class Pykomoran_func():
    def parse(self,s):
        s = komoran.get_plain_text(s)
        return s
    
#[('롯데정보통신', 'NNP'), ('은', 'JX'), ('롯데', 'NNP'), ('그룹', 'NNG'), ('의', 'JKG'), ('계열사', 'NNG'), ('이', 'VCP'),('ㅂ니다', 'EF'), ('.', 'SF'), ('롯데정보통신', 'NNP'), ('은', 'JX'), ('글로벌', 'NNP'), ('기업', 'NNG'), ('으로', 'JKB'),('성장', 'NNG'), ('하', 'XSV'), ('고', 'EC'), ('있', 'VX'), ('습니다', 'EF'), ('.', 'SF')]
    def pos(self, s):
        s = self.parse(s)
        word_tag = []
        for r in s.split('\n'):
            for p in r.split(' '):
                d = p.split('/')
                #print(d)
                if len(d) > 1:
                    w, o = d
                    t = o.split(',')[0]
                    word_tag.append((w, t))
        return word_tag
    
#['롯데정보통신', '은', '롯데', '그룹', '의', '계열사', '이', 'ㅂ니다', '.', '롯데정보통신', '은', '글로벌', '기업', '으로', '성장', '하', '고', '있', '습니다', '.']
    def morphs(self, s):
        s = self.parse(s)
        morph_tag = []
        for r in s.split('\n'):
            for p in r.split(' '):
                d = p.split('/')
                #print(d)
                if len(d) > 1:
                    w, o = d
                    morph_tag.append(w)
        return morph_tag

       
#['롯데정보통신', '롯데', '그룹', '계열사', '롯데정보통신', '글로벌', '기업', '성장']
    def nouns(self,s):
        s = self.parse(s)
        noun_tag = []
        k = re.compile('^N')
        for r in s.split('\n'):
            for p in r.split(' '):
                d = p.split('/')
                #print(d)
                if len(d) > 1:
                    w, o = d
                    t = o.split(',')[0]
                    if k.match(t) is not None:
                        noun_tag.append(w)

        return noun_tag

    
    
P = Pykomoran_func()

print (P.nouns('롯데정보통신은 롯데 그룹의 계열사 입니다. 롯데정보통신은 글로벌 기업으로 성장하고 있습니다.'))