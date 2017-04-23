import Adafruit_BBIO.GPIO as g
import time as t
                                                                                
r1=['P9_11','P8_18']                                                            
r2=['P8_11','P9_23']                                                            
y1=['P9_13','P8_16']                                                            
y2=['P8_13','P9_16']                                                            
g1=['P9_15','P9_24','P8_12','P8_14']                                            
g2=['P8_15','P8_17','P9_12','P9_14']                                            
                                                                                
#initialisation                                                                 
                                                                                
for i in range(len(r1)):                                                        
        g.setup(r1[i],g.OUT)                                                    
        g.setup(r2[i],g.OUT)                                                    
        g.setup(y1[i],g.OUT)                                                    
        g.setup(y2[i],g.OUT)                                                    
        g.output(r1[i],g.LOW)                                                   
        g.output(r2[i],g.LOW)                                                   
        g.output(y1[i],g.LOW)                                                   
        g.output(y2[i],g.LOW)                                                   
                                                                                
for i in range(len(g1)):                                                        
        g.setup(g1[i],g.OUT)                                                    
        g.setup(g2[i],g.OUT)                                                    
                                                                                
        g.output(g1[i],g.LOW)                                                   
        g.output(g2[i],g.LOW)                                                   
                                                                                
                                                                                
while(True):                                                                    
        for i in range(len(r1)):                                                
                g.output(r1[i],g.LOW)                                           
                g.output(r2[i],g.HIGH)                                          
                                                                                
        for i in range(len(g1)):                                                
                g.output(g1[i],g.HIGH)                                          
                g.output(g2[i],g.LOW)                                           
        t.sleep(10)                                                             
                                                                                
        for i in range(len(g1)):                                                
                g.output(g1[i],g.LOW)                                           
                                                                                
        for i in range(len(y1)):                                                
                g.output(y1[i],g.HIGH)                                          
                                                                                
        t.sleep(5)                                                              
        for i in range(len(y1)):                                                
                g.output(y1[i],g.LOW)                                           
                                                                                
        for i in range(len(r1)):                                                
                g.output(r2[i],g.LOW)                                           
                g.output(r1[i],g.HIGH)                                          
                                                                                
        for i in range(len(g1)):                                                
                g.output(g2[i],g.HIGH)                                          
                g.output(g1[i],g.LOW)                                           
        t.sleep(10)                                                             
                                                                                
        for i in range(len(g1)):                                                
                g.output(g2[i],g.LOW)                                           
                                                                                
        for i in range(len(y1)):                                                
                g.output(y2[i],g.HIGH)                                          
                                                                                
        t.sleep(5)                                                              
        for i in range(len(y1)):                                                
                g.output(y2[i],g.LOW)
