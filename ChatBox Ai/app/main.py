from tkinter import *
import datetime
import google.generativeai as genai
'''genai.configure(api_key=os.getenv('GEMINI_API_KEY'))'''

genai.configure(api_key="/////")


root=Tk()
root.title("CHATBOX AI")
root.geometry('720x400')
root.configure(bg='light blue')
currenttime=datetime.datetime.now()

greet=""
if 6<currenttime.hour<12:
    greet="Good Morning"
elif 12<=currenttime.hour<4:
    greet="Good Afternoon"
else:
    greet="Good Evening"        
        
def clear_screen():
    history.config(state=NORMAL)
    history.delete('1.0',END)
    history.config(state=DISABLED)


def ask_ai(user_input):
    try:
        model = genai.GenerativeModel('gemini-1.5-flash')  
        response = model.generate_content(user_input)       
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"
    

def message_box(b1):
    history.config(state=NORMAL)
    history.insert(END, f"You: {b1}\n")
    ai_reply = ask_ai(b1)
    history.insert(END, f"{ai_reply}\n\n")
    history.config(state=DISABLED)
    question.delete(0, END)
    
def exit_chat():
    root.quit()



Label(root,text=f"{greet} 😄. I'm DevOps Chatbot. I have DevOps answers for you from the drop-down menu.", fg='#000', bg='white', font=('Microsoft YaHei UI Light', 10, 'bold')).place(x=10,y=5)

'''Question Box'''
text_var = StringVar()
text_var.set("Enter any Text")
question=Entry(root,textvariable=text_var,width=67)
question.place(x=20,y=50)
question.bind('<Return>', lambda event: message_box(question.get()))

'''History Box'''
history=Text(root,width=50,height=20, font=("cambria", 11))
history.place(x=20,y=90)
history.config(state=DISABLED)
'''Search'''
Button1=Button(root,text='Click for Answer',command=lambda:message_box(question.get()),width=20,padx=15,pady=15).place(x=500,y=100)
'''Clear'''
Button2=Button(root,text='Clear Screen',command=clear_screen,width=20,padx=15,pady=15).place(x=500,y=200)
'''Close'''
Button3=Button(root,text='Close Window',command=exit_chat,width=20,padx=15,pady=15).place(x=500,y=300)


root.mainloop()
