import re

class Stemming_Nazief:
    value = []
    def __init__(self):
        try:
            dokumen_teks = open('katadasar.txt','r')
        except IOError:
            print ("file katadasar.txt tidak ditemukan")
        for line in dokumen_teks:
            self.value.append(line.rstrip()) 

    def Cek_Kamus(self,kata):
        if kata in self.value:
            return True
        return False

    #Cek Prefix Disallowed Sufixes  (Kombinasi Awalan dan Akhiran yang tidak diijinkan)
    def Cek_Prefix_Disallowed_Suffixes(self,kata):
        if re.search("^(be)[a-z]+(i)$",kata):
            return True
        if re.search("^(di)[a-z]+(an)$",kata):
            return True
        if re.search("^(ke)[a-z]+(i|kan)$",kata):
            return True
        if re.search("^(me)[a-z]+(an)$",kata):
            return True
        if re.search("^(se)[a-z]+(i|kan)$",kata):
            return True
    
        return False

    #buang Inflection Suffixes
    def Del_Inflection_Suffixes(self,kata):
        kataAsal = kata
        if re.search("([km]u|nya|[kl]ah|pun)$",kata):
            _kata = re.sub("([km]u|nya|[kl]ah|pun)$",'',kata)
            if re.search("([klt]ah|pun)$",kata):
                if ("([km]u|nya)$",_kata):
                    __kata = re.sub("([km]u|nya)$",'',_kata)
                    return __kata
            return _kata
        return kataAsal

    #Hapus Derivation Suffixes
    def Del_Derivation_Suffixes(self,kata):
        kataAsal = kata
        if re.search("(i|an)$",kata):
            _kata = re.sub("(i|an)$",'',kata)
            if self.Cek_Kamus(_kata):
                return _kata

            if re.search("(kan)$",kata):
                __kata = re.sub("(kan)$",'',kata)
                if self.Cek_Kamus(__kata):
                    return __kata

            if self.Cek_Prefix_Disallowed_Suffixes(kata):
                return kataAsal
            
        return kataAsal

    #Hapus Derivation Prefix
    def Del_Derivation_Prefix(self,kata):
        kataAsal = kata
        if re.search("^(di|[ks]e)",kata):
            _kata = re.sub("^(di|[ks]e)",'',kata)
            if self.Cek_Kamus(_kata):
                return _kata
            __kata = self.Del_Derivation_Suffixes(_kata)
            if self.Cek_Kamus(__kata):
                return __kata

            if re.search("^(diper)",kata):
                _kata = re.sub("^(diper)",'',kata)
                if self.Cek_Kamus(_kata):
                    return _kata

                __kata = self.Del_Derivation_Suffixes(_kata)
                if self.Cek_Kamus(__kata):
                    return __kata
                _kata = re.sub("^(diper)",'r',kata)
                if self.Cek_Kamus(_kata):
                    return _kata
                __kata = self.Del_Derivation_Suffixes(_kata)
                if self.Cek_Kamus(__kata):
                    return __kata
        #awalan te- me- be- atau pe-
        if re.search("^([tmbp]e)",kata):

            #awalan te-
            if re.search("^(te)",kata):
                #1 terV ...
                if re.search("^(ter)[aiueo]",kata):
                    _kata = re.sub("^(ter)",'',kata)
                    if self.Cek_Kamus(_kata):
                        return _kata
                    
                    _kata = re.sub("^(ter)","r",kata)
                    if self.Cek_Kamus(_kata):
                        return _kata
                    
                    __kata = self.Del_Derivation_Suffixes(_kata)
                    if self.Cek_Kamus(__kata):
                        return __kata
                
                #2 terCerV... C != r
                if re.search("^(ter[^aiueor]er[aiueo])",kata):
                    _kata = re.sub("^(ter)","",kata)
                    if self.Cek_Kamus(_kata):
                        return _kata
                    __kata = self.Del_Derivation_Suffixes(_kata)
                    if self.Cek_Kamus(__kata):
                        return __kata
                #3 terCP... C != r, P != er
                if re.search("^(ter)[^aiueor][^(er)]",kata):
                    _kata = re.sub("^(ter)","",kata)
                    if self.Cek_Kamus(_kata):
                        return _kata
                    __kata = self.Del_Derivation_Suffixes(_kata)
                    if self.Cek_Kamus(__kata):
                        return __kata

                #4 terC1erC2... C1 != r
                if re.search("^(ter)[^aiueor]er[^aiueo]",kata):
                    _kata = re.sub("^(te)","",kata)
                    if self.Cek_Kamus(_kata):
                        return _kata
                    __kata = self.Del_Derivation_Suffixes(_kata)
                    if self.Cek_Kamus(__kata):
                        return __kata
        
            #awalan me-
            if re.search("^(me)",kata):
                #1 me{l|r|w|y}V... => me-{l|r|w|y}V...
                if re.search("^(me)[lrwy][aiueo]",kata):
                    _kata = re.sub("^(me)[lrwy][aiueo]",'',kata)
                    if self.Cek_Kamus(_kata):
                        return _kata
                    __kata = self.Del_Derivation_Suffixes(_kata)
                    if self.Cek_Kamus(__kata):
                        return __kata
                #2 mengV ... => meng-V... | meng-kV...
                if re.search("^(meng)[aiueokghq]",kata):
                    _kata = re.sub("^(meng)[aiueokghq]",'',kata)
                    if self.Cek_Kamus(_kata):
                        return _kata
                    __kata = self.Del_Derivation_Suffixes(_kata)
                    if self.Cek_Kamus(__kata):
                        return __kata

                    _kata = re.sub("^(meng)",'k',kata)
                    if self.Cek_Kamus(_kata):
                        return _kata
                    __kata = self.Del_Derivation_Suffixes(_kata)
                    if self.Cek_Kamus(__kata):
                        return __kata
                #2 meng{g|h|q}... => meng-{g|h|q}
                if re.search("^(meng)[ghq]",kata):
                    _kata = re.sub("^(meng)[ghq]",'',kata)
                    if self.Cek_Kamus(_kata):
                        return _kata
                    __kata = self.Del_Derivation_Suffixes(_kata)
                    if self.Cek_Kamus(__kata):
                        return __kata

                #3 mem{b|f|v}... => mem-{b|f|v}
                if re.search("^(mem)[bfv]",kata):
                    _kata = re.sub("^(mem)",'',kata)
                    if self.Cek_Kamus(_kata):
                        return _kata
                    __kata = self.Del_Derivation_Suffixes(_kata)
                    if self.Cek_Kamus(__kata):
                        return __kata

                #4 mempe{r|l}... => mem-pe ...
                if re.search("^(mempe)[rl]",kata):
                    _kata = re.sub("^(mem)",'pe',kata)
                    if self.Cek_Kamus(_kata):
                        return _kata
                    __kata = self.Del_Derivation_Suffixes(_kata)
                    if self.Cek_Kamus(__kata):
                        return __kata
                #5 mem{rV|V}... => me-m{rV|V}... | me-p{rV|V}...
                if re.search("^(mem)([r][aiueo]|[aiueo])",kata):
                    _kata = re.sub("^(mem)",'m',kata)
                    if self.Cek_Kamus(_kata):
                        return _kata

                    _kata = re.sub("^(mem)","p",kata)
                    if self.Cek_Kamus(_kata):
                        return _kata
                    
                    __kata = self.Del_Derivation_Suffixes(_kata)
                    if self.Cek_Kamus(__kata):
                        return __kata

                #6 men{c|d|j|z}... => men-{c|d|j|z}...
                if re.search("^(men)[cdjsz]",kata):
                    _kata = re.sub("^(men)",'',kata)
                    if self.Cek_Kamus(_kata):
                        return _kata
                    __kata = self.Del_Derivation_Suffixes(_kata)
                    if self.Cek_Kamus(__kata):
                        return __kata
                    
                #7 menV...  => me-nV... | me-tV                
                if re.search("^(men)[aiueo]",kata):
                    _kata = re.sub("^(men)",'n',kata)
                    if self.Cek_Kamus(_kata):
                        return _kata

                    _kata = re.sub("^(men)",'t',kata)
                    if self.Cek_Kamus(_kata):
                        return _kata
                        
                    __kata = self.Del_Derivation_Suffixes(_kata)
                    if self.Cek_Kamus(__kata):
                        return __kata
                #8 menyV... =>  meny-sV…
                if re.search("^(meny)[aiueo]",kata):
                    _kata = re.sub("^(meny)",'s',kata)
                    if self.Cek_Kamus(_kata):
                        return _kata
                        
                    __kata = self.Del_Derivation_Suffixes(_kata)
                    if self.Cek_Kamus(__kata):
                        return __kata

                #5
                if re.search("^(memp)[aiuo]",kata):
                    _kata = re.sub("^(mem)",'p',kata)
                    if self.Cek_Kamus(_kata):
                        return _kata
                    
                    __kata = self.Del_Derivation_Suffixes(_kata)
                    if self.Cek_Kamus(__kata):
                        return __kata
            #awalan be-
            if re.search("^(be)",kata):
                #1 berV... => ber-V... | be-rV...  
                if re.search("^(ber)[aiueo]",kata):
                    _kata = re.sub("^(ber)",'',kata)
                    if self.Cek_Kamus(_kata):
                        return _kata
                    _kata = re.sub("^(ber)","r",kata)
                    if self.Cek_Kamus(_kata):
                        return _kata
                    
                    __kata = self.Del_Derivation_Suffixes(_kata)
                    if self.Cek_Kamus(__kata):
                        return __kata
                #2 berCAP... => ber-CAP..., C!=‟r‟ & P!=‟er‟
                if re.search("^(ber)[^aiueor][a-z][^(er)]",kata):
                    _kata = re.sub("^(ber)",'',kata)
                    if self.Cek_Kamus(_kata):
                        return _kata
                    
                    __kata = self.Del_Derivation_Suffixes(_kata)
                    if self.Cek_Kamus(__kata):
                        return __kata
                
                #3 berCAerV...  => ber-CaerV... dimana C!=‟r‟  
                if re.search("^(ber)[^aiueor][a-z]er[aiueo]",kata):
                    _kata = re.sub("^(be)",'',kata)
                    if self.Cek_Kamus(_kata):
                        return _kata
                    
                    __kata = self.Del_Derivation_Suffixes(_kata)
                    if self.Cek_Kamus(__kata):
                        return __kata
                #4 belajar => bel-ajar
                if re.search("belajar",kata):
                    _kata = re.sub("^(bel)",'',kata)
                    if self.Cek_Kamus(_kata):
                        return _kata
                    
                    __kata = self.Del_Derivation_Suffixes(_kata)
                    if self.Cek_Kamus(__kata):
                        return __kata
                    
                #5 beC1erC2...  => be-C1erC2... dimana C1!={‟r‟|‟l‟}
                if re.search("^(be)[^aiueorl]er[^aiueo]",kata):
                    _kata = re.sub("^(be)",'',kata)
                    if self.Cek_Kamus(_kata):
                        return _kata
                    __kata = self.Del_Derivation_Suffixes(_kata)
                    if self.Cek_Kamus(__kata):
                        return __kata
            #awalan pe-
            if re.search("^(pe)",kata):
                #1 peng{g|h|q}... => peng-{g|h|q}...
                #2 pengV... => peng-V... | peng-kV... 
                if re.search("^(peng)[aiueokghq]",kata):
                    _kata = re.sub("^(peng)",'',kata)
                    if self.Cek_Kamus(_kata):
                        return _kata

                    _kata = re.sub("^(peng)",'k',kata)
                    if self.Cek_Kamus(_kata):
                        return _kata
                    
                    __kata = self.Del_Derivation_Suffixes(_kata)
                    if self.Cek_Kamus(__kata):
                        return __kata
                #3 penyV... => peny-sV… 
                if re.search("^(peny)",kata):
                    _kata = re.sub("^(peny)",'s',kata)
                    if self.Cek_Kamus(_kata):
                        return _kata
                    
                    __kata = self.Del_Derivation_Suffixes(_kata)
                    if self.Cek_Kamus(__kata):
                        return __kata
                #4 pe{w|y}V...  => pe-{w|y}V..
                if re.search("^(pe)[wy][aiueo]",kata):
                    _kata = re.sub("^(pe)",'',kata)
                    if self.Cek_Kamus(_kata):
                        return _kata
                    
                    __kata = self.Del_Derivation_Suffixes(_kata)
                    if self.Cek_Kamus(__kata):
                        return __kata
                #5 perV...  => per-V... | pe-rV...
                if re.search("^(per)[aiueo]",kata):
                    _kata = re.sub("^(per)",'',kata)
                    if self.Cek_Kamus(_kata):
                        return _kata
                    
                    _kata = re.sub("^(per)",'r',kata)
                    if self.Cek_Kamus(_kata):
                        return _kata
                    
                    __kata = self.Del_Derivation_Suffixes(_kata)
                    if self.Cek_Kamus(__kata):
                        return __kata
                #6 perCAP  => per-CAP... dimana C!=‟r‟ dan P!=‟er‟
                if re.search("^(per)[^aiueor][a-z][^(er)]",kata):
                    _kata = re.sub("^(per)",'',kata)
                    if self.Cek_Kamus(_kata):
                        return _kata
                    
                    __kata = self.Del_Derivation_Suffixes(_kata)
                    if self.Cek_Kamus(__kata):
                        return __kata

                #7 perCAerV... => per-CAerV... dimana C!=‟r‟
                if re.search("^(per)[^aiueor][a-z]er[aiueo]",kata):
                    _kata = re.sub("^(per)",'',kata)
                    if self.Cek_Kamus(_kata):
                        return _kata
                    
                    __kata = self.Del_Derivation_Suffixes(_kata)
                    if self.Cek_Kamus(__kata):
                        return __kata
                #8 pem{b|f|V}...  => pem-{b|f|V}...
                if re.search("^(pem)[bfp][aiueo]",kata):
                    _kata = re.sub("^(pem)",'',kata)
                    if self.Cek_Kamus(_kata):
                        return _kata
                    
                    __kata = self.Del_Derivation_Suffixes(_kata)
                    if self.Cek_Kamus(__kata):
                        return __kata

                #9 pem{rV|V}... => pe-m{rV|V}... | pe-p{rV|V}...
                if re.search("^(pem)([r][aiueo]|[aiueo])",kata):
                    _kata = re.sub("^(pe)",'m',kata)
                    if self.Cek_Kamus(_kata):
                        return _kata
                    
                    _kata = re.sub("^(pe)",'p',kata)
                    if self.Cek_Kamus(_kata):
                        return _kata
                    
                    __kata = self.Del_Derivation_Suffixes(_kata)
                    if self.Cek_Kamus(__kata):
                        return __kata
                    
                #10 pen{c|d|j|z}... =>  pen-{c|d|j|z}... 
                if re.search("^(pen)[cdjsz]",kata):
                    _kata = re.sub("^(pen)",'',kata)
                    if self.Cek_Kamus(_kata):
                        return _kata
                    
                    __kata = self.Del_Derivation_Suffixes(_kata)
                    if self.Cek_Kamus(__kata):
                        return __kata
                    
                #11 penV... => pe-nV... | pe-tV..
                if re.search("^(pen)[aiueo]",kata):
                    _kata = re.sub("^(pe)",'n',kata)
                    if self.Cek_Kamus(_kata):
                        return _kata

                    _kata = re.sub("^(pe)",'t',kata)
                    if self.Cek_Kamus(_kata):
                        return _kata
                    
                    __kata = self.Del_Derivation_Suffixes(_kata)
                    if self.Cek_Kamus(__kata):
                        return __kata

                #12 pelV... => pe-lV... kecuali “pelajar” yang menghasilkan “ajar”
                if re.search("^(pel)[aiueo]",kata):
                    _kata = re.sub("^(pel)",'l',kata)
                    if self.Cek_Kamus(_kata):
                        return _kata

                    _kata = re.sub("^(pel)",'',kata)
                    if self.Cek_Kamus(_kata):
                        return _kata
                    
                    __kata = self.Del_Derivation_Suffixes(_kata)
                    if self.Cek_Kamus(__kata):
                        return __kata
                    
                #13 peCerV...  per-erV... dimana C!={r|w|y|l|m|n}
                if re.search("^(pe)[^aiueorwylmn]er[aiueo]",kata):
                    _kata = re.sub("^(per)",'er',kata)
                    if self.Cek_Kamus(_kata):
                        return _kata
                    __kata = self.Del_Derivation_Suffixes(_kata)
                    if self.Cek_Kamus(__kata):
                        return __kata

                #14 peCP... => pe-CP... dimana C!={r|w|y|l|m|n} dan P!=‟er‟
                if re.search("^(pe)[^aiueorwylmn][^(er)]",kata):
                    _kata = re.sub("^(pe)",'',kata)
                    if self.Cek_Kamus(_kata):
                        return _kata
                    __kata = self.Del_Derivation_Suffixes(_kata)
                    if self.Cek_Kamus(__kata):
                        return __kata
                
        if re.search("^(di|[kstbmp])",kata) == False:
            return kataAsal
        
        return kataAsal

    def Nazief(self,kata):


        kata = self.Del_Inflection_Suffixes(kata)

        kata = self.Del_Derivation_Suffixes(kata)

        kata = self.Del_Derivation_Prefix(kata)

        return kata

Stemming = Stemming_Nazief();
