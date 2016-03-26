# -*- coding: utf-8 -*-


class StringMath():
   
       
   def reverse(self,s):#take string, reverse it  turns the string to reversed char array
       chars = []       #ve reverse it becouse least  valuable number at the and of string and most 
       for line in s:
           chars.append(line)
       chars.reverse()
       print(chars)
       return chars
   def rereverse(self,chararray):
       b=""
       for i in range(len(chararray)-1,-1,-1):
           a=str(chararray[i])
           b=b+a       
       return b

   def ssum(self,s1,s2):#sums the given strings
       elde=0
       liste=[]
       s1len=len(s1)-1
       s2len=len(s2)-1
       strsum1=self.reverse(s1)
       strsum2=self.reverse(s2)
       if(s1len>s2len):
           for i in range(0,s1len+1):            
              if(i<=s2len): 
                   a=int(strsum1[i])                   
                   b=int(strsum2[i])
                   liste.append((a+b+elde)%10)
                   elde=(a+b+elde)/10
                   elde=int(elde)
              else:
                  a=int(strsum1[i])
                  liste.append(a+elde)
                  elde=0
           return self.rereverse(liste)
       elif(s1len<s2len):
           for i in range(0,s2len+1):
              if(i<=s1len): 
                   a=int(strsum2[i])                   
                   b=int(strsum1[i])
                   liste.append((a+b+elde)%10)
                   elde=(a+b+elde)/10
                   elde=int(elde)
              else:
                  a=int(strsum2[i])
                  liste.append(a+elde)
                  elde=0
           return self.rereverse(liste) 
       else:
            for i in range(0,s1len+1):            
              if(i<s2len): 
                   a=int(strsum1[i])                   
                   b=int(strsum2[i])
                   liste.append((a+b+elde)%10)
                   elde=(a+b+elde)/10
                   elde=int(elde)
              elif(i==s2len):
                  a=int(strsum1[i])                   
                  b=int(strsum2[i])                 
                  liste.append((a+b+elde))    
                  elde=(a+b+elde)/10
                  elde=int(elde)                     
            return self.rereverse(liste)
            
   def mmultiply(self,s1,s2):#multiply the given strings
       chars=self.reverse(s1)
       chars2=self.reverse(s2)
       s1len=len(chars)
       s2len=len(chars2)
       carpimlar=[]
       for i in range(0,s1len):
           for j in range(0,s2len):
               carpim=int(chars[i])*int(chars2[j])
               strr=str(carpim)
               count=i+j
               for z in range(0,count):
                   strr=strr+"0"        
               carpimlar.append(strr)
       print(carpimlar)   
       i=0
       toplamlar=[]
       toplamlar.append(carpimlar)
       while(1):
           top=[]
           for index in range(0,len(toplamlar[i]),2):
               try:                                      
                   top.append(self.ssum(toplamlar[i][index],toplamlar[i][index+1]))
               except:
                   top.append(self.ssum(toplamlar[i][index],"0"))
         
           toplamlar.append(top)        
           i += 1         
           if(len(top)==1):
                break               
       return top[0] 
                           
              
    
   