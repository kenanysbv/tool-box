
print("Salam !")
print("Tool Box programına xosh  gelmisiniz ! ","\n===================================================","\n ")
while True:

    
    systemEnter=int(input("Girish ~ 1 \nQeydiyyat ~ 2 \n\nCavab :  "))
    passwordS=123
    nameS="a"
    
    if systemEnter==2:
    
        nameU=input("\n============================================\nQeydiyyat : \n\nAdinizi daxil edin : ")
        loop=1
    
        while loop != 0:
      
            passwordU=int(input("Parolu daxil edin : "))
            passwordUchek=int(input("Parolu  yeniden daxil edin : "))
    
            if passwordU == passwordUchek:
                loop=0
                chek=True
                systemEnter=1
                passwordS=passwordU
                nameS=nameU
            else : 
                print("\n~~~~~~~~~~Parol eyni deyil ! ")
                loop=1
    
    if systemEnter ==1 :
        print("\n============================================\nGirish  : ")
        loop1=1
        while loop1 != 0:
            nameU=input("\n\nAdinizi daxil edin : ")
            passwordU=int(input("Parol : ")) 
            if (nameU == nameS ) and (passwordU == passwordS):
                loop1=0
                chek=True
            else:
                print("\n~~~~~~~~~~Ad veya Parol yanlishdir !! ")
                loop1=1
    
    
        
    if chek == True:
        print("\n\n========================================================= \n\nToollar : \n")
        # Kalkulyator , Mezenne konvertoru , Mesafe uzre xerc hesablama , VAhidler arasi konvertor , Sahe hesablama 
        while True:
            
            tool=6
            print("=====================================\nKalkulyator --> 1\nXerc hesablama  --> 2\nFiqur uzre hesablamalar --> 3\nMezenne konvertoru --> 4\nVahidler arasi konvertor --> 5 \nChixish --> 6")
            loop2=1
            toolID=int(input("\nEdilecek Emelliyati Sechin : "))
            
            while loop2!=0:
                
                if toolID <= tool and toolID>0:
                    loop2=0
                else:
                    print("\n~~~~~~~~~~Yanlish sechim  ! ")
                    loop2=1
                    toolID=int(input("\nEdilecek Emelliyati Sechin : "))
            if toolID==1:
                    
                 print("\n===============================================\n\nKalkulyator : ")
                 n1=float(input("Ededleri daxil edin : \nEded 1 ~ "))
                 n2=float(input("Eded 2 : "))
                 print("\n1~ Toplama\n2~ Chixma\n3~ Vurma\n4~ Bolme\n5~ Faktorial\n6~ Ustlu vurma")
                 s=int(input("\nSechim : "))
                 if s>0 and s<7:
                     if s==1:
                         cem=n1+n2
                         print(f"{n1} + {n2} = {cem} ")
                     elif s==2:
                         chixma=n1-n2
                         print(f"{n1} - {n2} = {chixma} ")
                     elif s==3:
                         vurma=n1*n2
                         print(f"{n1} * {n2} = {vurma} ")
                     elif s==4:
                         bolme=n1/n2
                         print(f"{n1} / {n2} = {bolme} ")
                     elif s==5:
                         i=2 
                         f1=1 
                         j=n1  
                         k=1                   
                            
                         while i!=0:
                             i-=1
                             while j!= 0:
                                     
                                 f1*=j
                                 j-=1
                             if k!=0: 
                                 print(f"{n1} != {f1}")
                             elif k==0:
                                 print(f"{n2} != {f1}") 
                                 
                             f1=1                        
                             k=0
                             j=n2                        
                     elif s==6:
                         print(f" {n1} ve {n2} uchun ustu daxil edin : ")
                         ust=int(input("Ust : "))
                         u1=n1**ust
                         u2=n2**ust
                         print(f"{n1} ustu {ust} = {u1} \n{n2} ustu {ust} = {u2} ")
            elif  toolID==2:  
                print("\n===============================================\n\nXerc hesablam : ")
                m=float(input("Mesafeni daxil edin : ")) 
                s=float(input("100 km serfiyati daxil edin : "))   
                a92=1.00
                a95=1.25
                p=1.40 
                q_92=((m/100)*s)*a92
                q_95=((m/100)*s)*a95
                q_p=((m/100)*s)*p
                print(f"\n\nA-92 ile mebleg : {q_92}\n\nA-95 ile qiymet: {q_95}\n\nPremium ile qiymet : {q_p}")
            
            elif toolID==3:
            
                print("\n===============================================\n\nFiqur uzre  hesablamalar :")
                print("\n~~~~Hesablamalar : \nPerimetr --> 1\nSahe --> 2")
                secimFm=int(input("Sechim : "))
                if secimFm>0 and secimFm<=2:
                    if secimFm==1:
                                print("\n~~~~~~~~~~~~~~~Perimetr")
                                print("\n~~~~~Fiqurlar : \n\nKvadarat --> 1\nDuzbucaqli --> 2 \nUchbucaq -->3 \nParaleloqram --> 4\nTrapesiya --> 5 \nRomb --> 6")
                                secimFmP=int(input("Sechim : "))
                                if secimFmP >0 : 
                                    if secimFmP ==1:
                                        side=int(input("Teref : "))
                                        perimetr=side*4
                                        if perimetr > 0:
                                            print(f"Kvadratin Perimetri : {perimetr}")
                                        else:
                                            print('~~~~~~Teref yanlishdir !')
                                    elif secimFmP ==2:
                                        uzun=int(input("Uzunluq : "))
                                        en = int(input("En : "))
                                        if uzun > en and (en*uzun)!=0  :
                                            perimetr=2*(uzun+en)
                                            print("Duzbucaqlinin Perimetri : ",perimetr)
                                        else:
                                            print("~~~~~~~~~~~~Uzunluq veya en sehvdir !")
                                    elif secimFmP==3:
                                        side1=int(input("Teref 1 : "))
                                        side2=int(input("Teref 2 : "))
                                        side3=int(input("Teref 3 : "))
                                        chek=0
                                        if (side1*side2*side3) != 0 :
                                                                                   
                                            sidE1=side1
                                            sidE2=side2
                                            sidE3=side3
                                            if sidE1 > sidE3:
                                                sidE1 = sidE1 + sidE3
                                                sidE3 = sidE1 - sidE3
                                                sidE1 = sidE1 - sidE3  
                                            if sidE1 > sidE2:
                                                sidE1 = sidE1 + sidE2
                                                sidE2 = sidE1 - sidE2
                                                sidE1 = sidE1 - sidE2
                                            if sidE2 > sidE3:
                                                sidE2 = sidE2 + sidE3
                                                sidE3 = sidE2 - sidE3
                                                sidE2 = sidE2 - sidE3
                                            b=sidE3
                                            o=sidE2
                                            k=sidE1
                                            if  b>o-k and b<o+k:
                                                chek+=1
                                            if  o>b-k and o<b+k:
                                                chek+=1
                                            if k>b-o  and k<o+b:
                                                chek+=1
                                            if chek==3:
                                                perimetr=b+o+k
                                                print("Uchbucaqin perimetri : ",perimetr)
                                            else:
                                                print("~~~~~~~~~~~~~Bele bir uchbucaq qurmaq olamaz !")
    
    
                                        else:
                                            print("~~~~~~~~~~~~~~~Tereflerde sehv var !  ")
                                    elif secimFmP==4:
                                        side1=int(input("Teref 1 : "))
                                        side2=int(input("Teref 2 :  "))
                                        if (side1*side2) != 0 and side1 != side2:
                                            perimetr=2*(side1*side2)
                                            print("Parelelogramin perimetri : {perimetr}")
                                        else:
                                            print("~~~~~~~~~~~~~~~Tereflerde sehv var !  ")
                                    elif secimFmP==5:
                                        side1=int(input("Oturacaq 1 : "))
                                        side2=int(input("Oturacaq 3 : "))
                                        side3=int(input("Yan  1 : "))
                                        side4=int(input("Yan  2 : "))
                                        if ((side1*side2*side3*side4) !=0 ) and ((side1 != side2 ) and (side3 != side4)):
                                            perimetr=side1+side2+side3+side4
                                            print("Trapesiya Perimetri : {perimetr}")
                                        else:
                                            print("~~~~~~~~~Tereflerde sehv var ! ")
                                    elif secimFmP==6:
                                        if secimFmP ==1:
                                            side=int(input("Teref : "))
                                            perimetr=side*4
                                        if perimetr > 0:
                                            print(f"Rombun Perimetri : {perimetr}")
                                        else:
                                            print('~~~~~~Teref yanlishdir !')
    
    
            
            
                                else: 
                                    print("~~~~~~~~~~~~~~~~Yanlish secim ! ")
                    else:
                        print("\n~~~~~~~~~~~~~~~Sahe")
                        print("\n~~~~~Fiqurlar : \n\nKvadarat --> 1\nDuzbucaqli --> 2 \nUchbucaq -->3 \nParaleloqram --> 4\nTrapesiya --> 5 \nRomb --> 6")
                        secimFmS=int(input("Sechim : "))
                        if secimFmS >0 and secimFmS<7:
                            if secimFmS==1:
                                        side=int(input("Teref : "))
                                        if side >0 :
                                            sahe=side**2
                                            print(f"Kvadratin sahei : {sahe}")
                                        else:
                                            print("~~~~~~~~~~~~~~~~Teref  yanlishdir !  ! ")
                            elif secimFmS==2:
                                        uzun=int(input("Uzunluq : "))
                                        en=int(input("En : "))
                                        if (uzun * en ) >0 and uzun > en :
                                            sahe=en*uzun 
                                            print(f"Duzbucaqlinin sahesi : {sahe}")
    
                                        else:
                                            print("~~~~~~~~~~~~~~~~Teref  yanlishdir !  ! ")
                            elif secimFmS==3:
                                        side1=int(input("Teref 1 : "))
                                        side2=int(input("Teref 2 : "))
                                        side3=int(input("Teref 3 : "))
                                        chek=0
                                        if (side1*side2*side3) != 0 :
                                                                                   
                                            sidE1=side1
                                            sidE2=side2
                                            sidE3=side3
                                            if sidE1 > sidE3:
                                                sidE1 = sidE1 + sidE3
                                                sidE3 = sidE1 - sidE3
                                                sidE1 = sidE1 - sidE3  
                                            if sidE1 > sidE2:
                                                sidE1 = sidE1 + sidE2
                                                sidE2 = sidE1 - sidE2
                                                sidE1 = sidE1 - sidE2
                                            if sidE2 > sidE3:
                                                sidE2 = sidE2 + sidE3
                                                sidE3 = sidE2 - sidE3
                                                sidE2 = sidE2 - sidE3
                                            b=sidE3
                                            o=sidE2
                                            k=sidE1
                                            if  b>o-k and b<o+k:
                                                chek+=1
                                            if  o>b-k and o<b+k:
                                                chek+=1
                                            if k>b-o  and k<o+b:
                                                chek+=1
                                            if chek==3:
                                                sahe=((b+o+k)*(b+o-k)*(b+k-o)*(k+o-b))*4
                                                print(f"Uchbucaqin sahesi : {sahe}")
                                            else:
                                                print("~~~~~~~~~~~~~Bele bir uchbucaq qurmaq olamaz !")
                            elif secimFmS==4:
                                        base=int(input("Oturacaq : "))
                                        height=int(input("Hundurluk : "))
                                        if (base*height)>0 and bas > heiht:
                                            sahe=base*height
                                            print(f"Paralelogramin sahesi : {sahe}")
                                        else:
                                            print("~~~~~~~~~~~~~~~~Teref  yanlishdir !  ! ")
                            elif secimFmS==5:
                                        s1=int(input("Oturacaq : "))
                                        s1=int(input("Yan Teref :  : "))
                                        s2=int(input("Hundurluk : "))
                                        if (s1*s2*s3)>0 and s1!=s2 and s1!= s3 :
                                            sahe=((s1+s2)/2)*s3
                                            print(f"Trapesiyanin sahesi : ")
                                        else: 
                                            print("~~~~~~~~~~~~~~~~Teref  yanlishdir !  ! ")
                            elif secimFmS==6:
                                        teref=int(input("Teref : "))
                                        hun=int(input("Hundurluk  : "))
                                        if (teref*hun )>0 :
                                            sahe=teref*hun
                                            print(f"Rombun sahesi : ")
                                        else:
                                            print("~~~~~~~~~~~~~~~~Teref  yanlishdir !  ! ")
                        else:
                            print("~~~~~~~~~~~~~~~~Yanlish secim ! ")
                                           
                else:
                    print("~~~~~~~~~~~~~~~~Yanlish secim ! ")
            
            elif toolID==4:
                print("\n===============================================\n\nValyuta konvertoru : ")
                m=float(input("AZN : ")) 
                a=2.00
                d=1.7
                r=0.023
                print("~~~~~~~~~~~~~~~~~\n\nMezenneni sechin : ")
                print("1~Avro \n2~Dollar\n3~Rubl")
                s=int(input("Sechim : "))
                if s==1:
                    p=m/a
                    print(f"{m} AZN  {p} Avro edir .")
                elif s==2:
                    p=m/d
                    print(f"{m} AZN  {p} Dollar edir .")
                else:
                    p=m/r
                    print(f"{m} AZN  {p} Rubl edir .")
            
            elif toolID==5: 
                print("\n===============================================\n\nVahidler arasi konvertor : ")
                # Vahidler : Temperator , uzunluq , agirliq 
                print("\n~~~~~~~~~~~~~~~~Kategoriyalar : \nTemperator --> 1\nUzunluq -->2\nAgirliq -->3")
                secimK=int(input("Sechim : "))
                if secimK==1:
                    print("\n~~~~~~~Temperator Vahidi : \nC --> 1\nK --> 2")
                    secimKt=int(input("\nSechim : "))
                    if secimKt==1:
                        c=int(input("C : "))
                        k=c+273.15
                        print(f"K --> {k}")
                    elif secimKt==2:
                        k=int(input("C : "))
                        c=k-273.15
                        print(f"C --> {c}")
                        
                    else:
                        print("~~~~~~~~~~~~~~Yanlish sechim ! ")
                elif secimK==2:
                    print("\n~~~~~~~Uzunluq  Vahidi : \nMM --> 1 \nSm --> 2 \nInch -->3 \nDm --> 4 \nM --> 5 \nKm --> 6")
                    secimKu=int(input("\nSechim : "))
                    if secimKu==1:
                        mm=int(input("MM : \n"))
                        sm=mm/10
                        inch=mm/25.4
                        dm=mm/100
                        m=mm/1000
                        km=mm/1000000
                        print(f"Mm : {mm} \nSm : {sm} \nInch : {inch} \nDm : {dm} \nM : {m} \nKm : {km}")
                    elif secimKu ==2:
                        sm=int(input("Sm : \n"))
                        mm=sm*10
                        inch=mm/25.4
                        dm=mm/100
                        m=mm/1000
                        km=mm/1000000
                        print(f"Mm : {mm} \nSm : {sm} \nInch : {inch} \nDm : {dm} \nM : {m} \nKm : {km}")
                    elif secimKu ==4:
                        dm=int(input("Dm : \n"))
                        mm=dm*100
                        sm=dm/10
                        inch=mm/25.4                
                        m=mm/1000
                        km=mm/1000000
                        print(f"Mm : {mm} \nSm : {sm} \nInch : {inch} \nDm : {dm} \nM : {m} \nKm : {km}")
                        
                    elif secimKu ==3:
                        inch=int(input("Inch : \n"))
                        mm=inch*25.4
                        sm=inch*2.5
                        dm=mm/100
                        m=mm/1000
                        km=mm/1000000
                        print(f"Mm : {mm} \nSm : {sm} \nInch : {inch} \nDm : {dm} \nM : {m} \nKm : {km}")
                    elif secimKu ==5:
                        m=int(input("M : \n"))
                        mm=m*1000
                        sm=m/100
                        inch=mm/25.4
                        dm=mm/100                   
                        km=mm/1000000
                        print(f"Mm : {mm} \nSm : {sm} \nInch : {inch} \nDm : {dm} \nM : {m} \nKm : {km}")
                    elif secimKu ==6:
                        km=int(input("Km : \n"))
                        mm=km*1000000
                        sm=mm/10
                        inch=mm/25.4
                        dm=mm/100
                        m=mm/1000
                        
                        print(f"Mm : {mm} \nSm : {sm} \nInch : {inch} \nDm : {dm} \nM : {m} \nKm : {km}")
                    
                elif secimK==3:
                    print("\n~~~~~~~~~~~~~~~~~~~Agirliq Vahidleri : \nMq -->1 \nQr --> 2 \nKq --> 3 \nS --> 4 \nT --> 5")
                    sA=int(input("Sechim : "))
                    if sA==1:
                        mq=int(input("Mq : "))
                        qr=mq/1000
                        kq=mq/1000000
                        s=mq/100000000
                        t=mq/10000000000
                        print(f"Mq : {mq} \nQr : {qr} \nKq : {kq} \nS : {s} \nT : {t}")
                    elif sA ==2:
                        qr=int(input("Mq : "))
                        mq=qr*1000
                        kq=mq/1000000
                        s=mq/100000000
                        t=mq/10000000000
                        print(f"Mq : {mq} \nQr : {qr} \nKq : {kq} \nS : {s} \nT : {t}")
                        
                    elif sA ==3:
                        kq=int(input("Kq : "))
                        mq=kq*1000000
                        s=mq/100000000
                        t=mq/10000000000
                        print(f"Mq : {mq} \nQr : {qr} \nKq : {kq} \nS : {s} \nT : {t}")
                    elif sA ==4:
                        s=int(input("S : "))
                        mq=s*100000000
                        qr=mq/1000
                        kq=mq/1000000
                        t=mq/10000000000
                        print(f"Mq : {mq} \nQr : {qr} \nKq : {kq} \nS : {s} \nT : {t}")
                        
                    elif sA ==5:
                        t=int(input("T : "))
                        mq=mq*10000000000
                        qr=mq/1000
                        kq=mq/1000000
                        s=mq/100000000
                        print(f"Mq : {mq} \nQr : {qr} \nKq : {kq} \nS : {s} \nT : {t}")
    
    
    
    
    
    
                else: 
                    print("~~~~~~~~~~~~~~Yanlish sechim ! ")
    
            elif toolID== 6:
                print("Sistemden chixilmani tesdiq edirsiz ? \nHe --> 1\nXeyr --> 2")
                tesdiq=int(input("Cavab : "))
                if tesdiq ==1:
                    print("\nSistemden chixilir ...... \n")
                    break
                    
                else:
                    print("Preses legv edilir  .....  ")
            
            else:
                print("~~~~~~~~~~~~~~Yanlish sechim ! ")
    
    else:
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~Xeta ! ")


