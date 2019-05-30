#Kgomotso Welcome
#WLCKGO001
#04 April 2019
#Page replacement algorithm


"""import statements"""
import sys 
import random

"""method definitions"""

#random page number generator
#takes length of pages from user
def Pages(pagesLength):
    #stores pages in a list called pages
    pages = [] 
    for j in range(pagesLength): 
        #pages randomly created using numbers from 0 to 9
        pages.append(random.randint(0, 9)) 
        #method returns pages
    return pages

#FIFO - first in, first out
def FIFO(size,pages):
    #frame = memory
    #pages are stored in memory
    pageFaults = 0
    frame = []
    
    for i in range(len(pages)):
        #appends first item in array
        if len(frame) == 0:
            frame.append(pages[0])
            pageFaults = pageFaults + 1
        #appends rest of items    
        else:
            for j in range(len(frame)):
                #check if item is in memory
                if(pages[i] not in frame):
                    #fill up memory
                    if (len(frame)<size): 
                        frame.append(pages[i])
                        pageFaults = pageFaults + 1
                    elif (len(frame)==size):
                        #replace page in memory
                        del frame[0]
                        frame.append(pages[i])
                        pageFaults = pageFaults + 1
    return pageFaults

#LRU - Least recently used
def LRU(size,pages):
    #frame = memory
    #pages are stored in memory    
    pageFaults = 0
    frame = []
    
    for i in range(len(pages)):
        #appends first item in array
        if len(frame) == 0:
            frame.append(pages[0])
            pageFaults = pageFaults + 1  
        else:
            #appends rest of items
            for j in range(len(frame)):
                #check if item is in memory
                if(pages[i] not in frame):
                    if (len(frame)<size): 
                        frame.append(pages[i])
                        pageFaults = pageFaults + 1
                    #replace page in memory
                    elif (len(frame)==size):
                        del frame[0]
                        frame.append(pages[i])
                        pageFaults = pageFaults + 1
                elif(pages[i]==frame[j]):
                    del frame[j]
                    frame.append(pages[i])                 
    return pageFaults

#return idex of farthest item in pages
def farthest(pages,frame,index):
    far = 0
    indexVal = 0
    for i in range(len(frame)):
        for j in range(index, len(pages)):
            if(frame[i] == pages[j]):
                if(j>far):
                    far = j
                    indexVal = i
                else:
                    pass
                break
            else:
                tempArray = pages[index:]
                if(frame[i] in tempArray):
                    pass
                else:
                    indexVal = i
                    return indexVal
    return indexVal

#Optimal Page Replacement     
def OPT(size,pages):
    #frame = memory
    #pages are stored in memory    
    pageFaults = 0
    frame = []
    for i in range(len(pages)):
        #appends first item in array
        if len(frame) == 0:
            frame.append(pages[0])
            pageFaults = pageFaults + 1 
        #appends rest of items
        else:
            for j in range(len(frame)):
                if(pages[i] not in frame):
                    #check if item is in memory
                    if (len(frame)<size): 
                        pageFaults = pageFaults + 1
                        frame.append(pages[i])
                    elif (len(frame)==size):
                        #replace page in memory
                        pageFaults = pageFaults + 1
                        del frame[farthest(pages,frame,i)]
                        frame.append(pages[i])
                    else:
                        pass
                else:
                    pass
    return pageFaults

"""implementation: Main method """
def main():
    #...TODO...
    size = int(sys.argv[1])
    pagesLength = input("Enter the total number of pages: ")
    pages = Pages(pagesLength)
    print (pages)
    print ("FIFO ",FIFO(size,pages), " page faults.")
    print ("LRU ",LRU(size,pages), " page faults.")
    print ("OPT ",OPT(size,pages), " page faults.")
    
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print ("Usage: python paging.py [number of pages]")
    else:
        main()