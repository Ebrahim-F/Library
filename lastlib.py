#management of liberary 
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from Add_func import add_func

window=tk.Tk()
window.geometry("500x300")
window.title("Library")
allbooks=[]

#open file to save allbook in PC        
with open("allbooks.text","r" ) as book:
            lines=book.readlines()
            allbook=[]
            new_lines=[]
            for line in lines:
                new_lines.append(line.strip())
            long=len(new_lines)//5
            for i in range(1,long+1):
                   allbook.append(new_lines[5*(i-1):4+5*(i-1)]) 
            for b in allbook:
                        c=["","","",""]
                        c[0]=str(b[0])[7:]
                        c[1]=str(b[1])[8:]
                        c[2]=str(b[2])[6:]
                        c[3]=str(b[3])[10:]
                        allbooks.append(c)
              
#labeles
title_label=ttk.Label(window,text="Title:")
title_label.place(x=20,y=10)
author_label=ttk.Label(window,text="Author:").place(x=250,y=10)
year_label=ttk.Label(window,text="Year:").place(x=20,y=45)
isbn_label=ttk.Label(window,text="Language:").place(x=250,y=45)

#variable of entry
title_text=tk.StringVar()
author_text=tk.StringVar()
year_text=tk.StringVar()
language_text=tk.StringVar()


#Entry
title_entry=ttk.Entry(window,textvariable=title_text)
title_entry.place(x=50,y=10)
author_entry=ttk.Entry(window,textvariable=author_text)
author_entry.place(x=310,y=10)
year_entry=ttk.Entry(window,textvariable=year_text)
year_entry.place(x=50,y=45)
language_entry=ttk.Entry(window,textvariable=language_text)
language_entry.place(x=310,y=45)

#listbox and scroll
scroll=tk.Scrollbar()
listbox=tk.Listbox(yscrollcommand=scroll.set)
scroll.config(command=listbox.yview)
scroll.place(x=30,y=150)
listbox.place(x=50,y=100)

#functions
def add_func():
    book=[title_text.get(),author_text.get(),year_text.get(),language_text.get()]
    if book  not in allbooks:
                    j=0 
                    for item in book:
                        sum_len=j+len(item)
                        j=sum_len
                    if sum_len>0:
                                messagebox.showinfo("add","your book added!")
                                allbooks.append(book)
                                with open("allbooks.text","a" ) as b:
                                    b.write("Title: "+title_text.get()+"\n")
                                    b.write("Author: "+author_text.get()+"\n")
                                    b.write("Year: "+year_text.get()+"\n")
                                    b.write("Language: "+language_text.get()+"\n")
                                    b.write("-"*15+"\n")
                    else: 
                         messagebox.showinfo("warning","Enter information of your book!") 
                            
    title_entry.delete(0,"end")
    author_entry.delete(0,"end")
    year_entry.delete(0,"end")
    language_entry.delete(0,"end")


#2-function viewall
def viewall_func():
                
                with open("allbooks.text","r") as file_book:
                         lines=file_book.readlines()
                         new_lines=[]
                         for l in lines:
                                new_lines.append(l.strip())
                      
                
                for j in range(len(lines)):
                      if listbox.get(j)!=new_lines[j]:
                              listbox.insert(j,new_lines[j])
        
    
#3-function search
def search_func():
    listbox.delete(0,"end")
    bool=True
    i=0
    for book in allbooks:
            if title_text.get() in book:
                listbox.insert(i,"Title: "+book[0]+"\n")
                listbox.insert(i+1,"Author: "+book[1]+"\n")
                listbox.insert(i+2,"Year: "+book[2]+"\n")
                listbox.insert(i+3,"Language: "+book[3]+"\n")
                listbox.insert(i+4,"-"*15+"\n")
                i=i+5
                bool=False
            elif author_text.get() in book:
                listbox.insert(i,"Title: "+book[0]+"\n")
                listbox.insert(i+1,"Author: "+book[1]+"\n")
                listbox.insert(i+2,"Year: "+book[2]+"\n")
                listbox.insert(i+3,"Language: "+book[3]+"\n")
                listbox.insert(i+4,"-"*15+"\n")
                i=i+5
                bool=False
            elif year_text.get() in book:
                listbox.insert(i,"Title: "+book[0]+"\n")
                listbox.insert(i+1,"Author: "+book[1]+"\n")
                listbox.insert(i+2,"Year: "+book[2]+"\n")
                listbox.insert(i+3,"Language: "+book[3]+"\n")
                listbox.insert(i+4,"-"*15+"\n")
                i=i+5
                bool=False
            elif language_text.get() in book:
                listbox.insert(i,"Title: "+book[0]+"\n")
                listbox.insert(i+1,"Author: "+book[1]+"\n")
                listbox.insert(i+2,"Year: "+book[2]+"\n")
                listbox.insert(i+3,"Language: "+book[3]+"\n")
                listbox.insert(i+4,"-"*15+"\n")
                i=i+5
                bool=False
    if bool:
            messagebox.showinfo("RESULT","sorry your book isn't exist!")
    
            
#4-Edit function
def edit_func():
    for num_line in listbox.curselection():
        if num_line%5==0:
            if title_text.get()=="":
                messagebox.showinfo("Edit","please enter your new title")
            else:
                new_author=listbox.get(num_line+1)
                new_year=listbox.get(num_line+2)
                new_language=listbox.get(num_line+3)
                listbox.delete(num_line, last=num_line+3)
                new_title="Title: "+title_text.get()
                listbox.insert(num_line,new_title)
                listbox.insert(num_line+1,new_author)
                listbox.insert(num_line+2,new_year)
                listbox.insert(num_line+3,new_language)
                book_new=[new_title[7:],new_author[8:],new_year[6:],new_language[10:]]

                
                for book in allbooks:
                    if book[1]==book_new[1] and book[2]==book_new[2] and book[3]==book_new[3]:
                        allbooks.remove(book)
                        allbooks.append(book_new)
                      
                with open("allbooks.text","w" ) as b:
                                    b.write(new_title+"\n")
                                    b.write(new_author+"\n")
                                    b.write(new_year+"\n")
                                    b.write(new_language+"\n")
                                    b.write("-"*15+"\n")        
                for book in allbooks:
                    if book!=book_new:
                        with open("allbooks.text","a" ) as b:
                            b.write("Title: "+book[0]+"\n")
                            b.write("Author: "+book[1]+"\n")
                            b.write("Year: "+book[2]+"\n")
                            b.write("Language: "+book[3]+"\n")
                            b.write("-"*15+"\n")





                
        if num_line%5==1:
            if author_text.get()=="":
                messagebox.showinfo("Edit","please enter your new author")
            else:    
                new_title=listbox.get(num_line-1)
                new_year=listbox.get(num_line+1)
                new_language=listbox.get(num_line+2)
                listbox.delete(num_line-1,last=num_line+2)
                new_author="Author: "+author_text.get()
                listbox.insert(num_line-1,new_title)
                listbox.insert(num_line,new_author)
                listbox.insert(num_line+1,new_year)
                listbox.insert(num_line+2,new_language)
                book_new=[new_title[7:],new_author[8:],new_year[6:],new_language[10:]]

                for book in allbooks:
                    if book[0]==book_new[0] and book[2]==book_new[2] and book[3]==book_new[3]:
                        allbooks.remove(book)
                        allbooks.append(book_new)
                      
                with open("allbooks.text","w" ) as b:
                                    b.write(new_title+"\n")
                                    b.write(new_author+"\n")
                                    b.write(new_year+"\n")
                                    b.write(new_language+"\n")
                                    b.write("-"*15+"\n")        
                for book in allbooks:
                    if book!=book_new:
                        with open("allbooks.text","a" ) as b:
                            b.write("Title: "+book[0]+"\n")
                            b.write("Author: "+book[1]+"\n")
                            b.write("Year: "+book[2]+"\n")
                            b.write("Language: "+book[3]+"\n")
                            b.write("-"*15+"\n")





                
        if num_line%5==2:
            if year_text.get()=="":
                messagebox.showinfo("Edit","please enter your new year")
            else:    
                new_title=listbox.get(num_line-2)
                new_author=listbox.get(num_line-1)
                new_language=listbox.get(num_line+1)
                listbox.delete(num_line-2,last=num_line+1)
                new_year="Year: "+year_text.get()
                listbox.insert(num_line-2,new_title)
                listbox.insert(num_line-1,new_author)
                listbox.insert(num_line,new_year)
                listbox.insert(num_line+1,new_language)
                book_new=[new_title[7:],new_author[8:],new_year[6:],new_language[10:]]
    
                for book in allbooks:
                    if book[0]==book_new[0] and book[1]==book_new[1] and book[3]==book_new[3]:
                           allbooks.remove(book)
                           allbooks.append(book_new)
                      
                with open("allbooks.text","w" ) as b:
                                    b.write(new_title+"\n")
                                    b.write(new_author+"\n")
                                    b.write(new_year+"\n")
                                    b.write(new_language+"\n")
                                    b.write("-"*15+"\n")        
                for book in allbooks:
                    if book!=book_new:
                        with open("allbooks.text","a" ) as b:
                            b.write("Title: "+book[0]+"\n")
                            b.write("Author: "+book[1]+"\n")
                            b.write("Year: "+book[2]+"\n")
                            b.write("Language: "+book[3]+"\n")
                            b.write("-"*15+"\n")
                       

                
               
        if num_line%5==3:
            if language_text.get()=="":
                messagebox.showinfo("Edit","please enter your new Language")
            else:
                new_title=listbox.get(num_line-3)
                new_author=listbox.get(num_line-2)
                new_year=listbox.get(num_line-1)
                listbox.delete(num_line-3,last=num_line)
                new_language="Language: "+language_text.get()
                listbox.insert(num_line-3,new_title)
                listbox.insert(num_line-2,new_author)
                listbox.insert(num_line-1,new_year)
                listbox.insert(num_line,new_language)
                book_new=[new_title[7:],new_author[8:],new_year[6:],new_language[10:]]

                
                
                for book in allbooks:
                    if book[0]==book_new[0] and book[1]==book_new[1] and book[2]==book_new[2]:
                        allbooks.remove(book)
                        allbooks.append(book_new)
                      
                with open("allbooks.text","w" ) as b:
                                    b.write(new_title+"\n")
                                    b.write(new_author+"\n")
                                    b.write(new_year+"\n")
                                    b.write(new_language+"\n")
                                    b.write("-"*15+"\n")        
                for book in allbooks:
                    if book!=book_new:
                        with open("allbooks.text","a" ) as b:
                            b.write("Title: "+book[0]+"\n")
                            b.write("Author: "+book[1]+"\n")
                            b.write("Year: "+book[2]+"\n")
                            b.write("Language: "+book[3]+"\n")
                            b.write("-"*15+"\n")
                       


#5-delete function
def delete_func():
    for num_line in listbox.curselection():
        if num_line%5==0:
            new_title=listbox.get(num_line)
            new_author=listbox.get(num_line+1)
            new_year=listbox.get(num_line+2)
            new_language=listbox.get(num_line+3)
            listbox.delete(num_line, last=num_line+4)
            book_new=[new_title[7:],new_author[8:],new_year[6:],new_language[10:]]
            
            for book in allbooks:
                    if book[0]==book_new[0] and book[1]==book_new[1] and book[2]==book_new[2] and book[3]==book_new[3]:
                        allbooks.remove(book)

            
            for book in allbooks:
                        with open("allbooks.text","w" ) as b:
                            b.write("Title: "+book[0]+"\n")
                            b.write("Author: "+book[1]+"\n")
                            b.write("Year: "+book[2]+"\n")
                            b.write("Language: "+book[3]+"\n")
                            b.write("-"*15+"\n")           
    
        if num_line%5==1:
            new_title=listbox.get(num_line-1)
            new_author=listbox.get(num_line)
            new_year=listbox.get(num_line+1)
            new_language=listbox.get(num_line+2)
            listbox.delete(num_line-1, last=num_line+3)
            book_new=[new_title[7:],new_author[8:],new_year[6:],new_language[10:]]
            
            for book in allbooks:
                    if book[0]==book_new[0] and book[1]==book_new[1] and book[2]==book_new[2] and book[3]==book_new[3]:
                        allbooks.remove(book)

            
            for book in allbooks:
                        with open("allbooks.text","w" ) as b:
                            b.write("Title: "+book[0]+"\n")
                            b.write("Author: "+book[1]+"\n")
                            b.write("Year: "+book[2]+"\n")
                            b.write("Language: "+book[3]+"\n")
                            b.write("-"*15+"\n")   
            

        if num_line%5==2:
                new_title=listbox.get(num_line-2)
                new_author=listbox.get(num_line-1)
                new_year=listbox.get(num_line)
                new_language=listbox.get(num_line+1)
                listbox.delete(num_line-2, last=num_line+2)
                book_new=[new_title[7:],new_author[8:],new_year[6:],new_language[10:]]
            
                for book in allbooks:
                      if book[0]==book_new[0] and book[1]==book_new[1] and book[2]==book_new[2] and book[3]==book_new[3]:
                             allbooks.remove(book)

            
                for book in allbooks:
                        with open("allbooks.text","w" ) as b:
                            b.write("Title: "+book[0]+"\n")
                            b.write("Author: "+book[1]+"\n")
                            b.write("Year: "+book[2]+"\n")
                            b.write("Language: "+book[3]+"\n")
                            b.write("-"*15+"\n")   
            
        if num_line%5==3:
                new_title=listbox.get(num_line-3)
                new_author=listbox.get(num_line-2)
                new_year=listbox.get(num_line-1)
                new_language=listbox.get(num_line)
                listbox.delete(num_line-3, last=num_line+1)
                book_new=[new_title[7:],new_author[8:],new_year[6:],new_language[10:]]
            
                for book in allbooks:
                      if book[0]==book_new[0] and book[1]==book_new[1] and book[2]==book_new[2] and book[3]==book_new[3]:
                             allbooks.remove(book)

            
                for book in allbooks:
                        with open("allbooks.text","w" ) as b:
                            b.write("Title: "+book[0]+"\n")
                            b.write("Author: "+book[1]+"\n")
                            b.write("Year: "+book[2]+"\n")
                            b.write("Language: "+book[3]+"\n")
                            b.write("-"*15+"\n")   
#this condition added because the last book didn't delete
        if allbooks==[]:
               with open("allbooks.text","w") as b:
                   b.write("")
               
            
#buttons
viewall_button=ttk.Button(window, text="View all",command=viewall_func).place(x=320,y=100)
search_button=ttk.Button(window, text="Search Book",command=search_func).place(x=320,y=125)
add_button=ttk.Button(window, text="Add Book",command=add_func).place(x=320,y=150)
edit_button=ttk.Button(window, text="Edit Book",command=edit_func).place(x=320,y=175)
delete_button=ttk.Button(window, text="Delete Book",command=delete_func).place(x=320,y=200)
close_button=ttk.Button(window, text="Close",command=window.destroy).place(x=320,y=225)

window.mainloop()

