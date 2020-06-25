import MeCab
import re

class Mecab_func():
    def parse(self,s):
        me = MeCab.Tagger()
        s = me.parse(s)
        return s
    
#[('롯데', 'NNP'), ('정보', 'NNG'), ('통신', 'NNG'), ('은', 'JX'), ('롯데', 'NNP'), ('그룹', 'NNG'), ('의', 'JKG'), ('계열사', 'NNG'), ('입니다', 'VCP+EF'), ('.', 'SF'), ('롯데', 'NNP'), ('정보', 'NNG'), ('통신', 'NNG'), ('은', 'JX'), ('글로벌', 'NNG'), ('기업', 'NNG'), ('으로', 'JKB'), ('성장', 'NNG'), ('하', 'XSV'), ('고', 'EC'), ('있', 'VX'), ('습니다', 'EF'), ('.', 'SF')]
    def pos(self, s):
        s = self.parse(s)
        word_tag = []
        for r in s.split('\n'):
            p = r.split('\t')
            if len(p) > 1:
                w, o = p
                t = o.split(',')[0]
                word_tag.append((w, t))
        return word_tag

#['롯데', '정보', '통신', '은', '롯데', '그룹', '의', '계열사', '입니다', '.', '롯데', '정보', '통신', '은', '글로벌', '기업', '으로', '성장', '하', '고', '있', '습니다', '.']
    def morphs(self,s):
        s = self.parse(s)
        morph_tag = list()
        for r in s.split('\n'):
            p = r.split('\t')
            if len(p)>1:
                w,o = p
                morph_tag.append(w)
        return morph_tag

#['롯데', '정보', '통신', '롯데', '그룹', '계열사', '롯데', '정보', '통신', '글로벌', '기업', '성장']
    def nouns(self,s):
        s = self.parse(s)
        #print(s)
        noun_tag = list()
        k = re.compile('^N')
        for r in s.split('\n'):
            p = r.split('\t')
            if len(p)>1:
                w,o = p
                t = o.split(',')[0]
                if k.match(t) is not None:
                    noun_tag.append(w)
        return noun_tag

M = Mecab_func()

print (M.nouns('롯데정보통신은 롯데 그룹의 계열사 입니다. 롯데정보통신은 글로벌 기업으로 성장하고 있습니다.'))