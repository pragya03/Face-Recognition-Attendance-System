from tkinter import*
from pil import Image,ImageTk
import webbrowser


class Helpsupport:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1366x768+0+0")
        self.root.title("Face_Recogonition_System")

# This part is image labels setting start 
        # first header image  
        img=Image.open(r"D:\Project\Attendence face recognition\Images_GUI\banner.jpg")
        img=img.resize((1366,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        # set image as lable
        f_lb1 = Label(self.root,image=self.photoimg)
        f_lb1.place(x=0,y=0,width=1366,height=130)

        # backgorund image 
        bg1=Image.open(r"D:\Project\Attendence face recognition\Images_GUI\bg4.png")
        bg1=bg1.resize((1366,768),Image.ANTIALIAS)
        self.photobg1=ImageTk.PhotoImage(bg1)

        # set image as lable
        bg_img = Label(self.root,image=self.photobg1)
        bg_img.place(x=0,y=130,width=1366,height=768)


        #title section
        title_lb1 = Label(bg_img,text="Help Support",font=("verdana",30,"bold"),bg="white",fg="navyblue")
        title_lb1.place(x=0,y=0,width=1366,height=45)

        # Create buttons below the section 
        # ------------------------------------------------------------------------------------------------------------------- 
        # student button 1
        std_img_btn=Image.open(r"D:\Project\Attendence face recognition\Images_GUI\l.png")
        std_img_btn=std_img_btn.resize((180,180),Image.ANTIALIAS)
        self.std_img1=ImageTk.PhotoImage(std_img_btn)

        std_b1 = Button(bg_img,command=self.linkedin,image=self.std_img1,cursor="hand2")
        std_b1.place(x=300,y=200,width=180,height=180)

        std_b1_1 = Button(bg_img,command=self.linkedin,text="LinkedIn",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        std_b1_1.place(x=300,y=380,width=180,height=45)

        # Detect Face  button 2
        det_img_btn=Image.open(r"D:\Project\Attendence face recognition\Images_GUI\inst.jpg")
        det_img_btn=det_img_btn.resize((180,180),Image.ANTIALIAS)
        self.det_img1=ImageTk.PhotoImage(det_img_btn)

        det_b1 = Button(bg_img,command=self.instagram,image=self.det_img1,cursor="hand2",)
        det_b1.place(x=540,y=200,width=180,height=180)

        det_b1_1 = Button(bg_img,command=self.instagram,text="Instagram",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        det_b1_1.place(x=540,y=380,width=180,height=45)



         # Help  Support  button 3
        hlp_img_btn=Image.open(r"D:\Project\Attendence face recognition\Images_GUI\gmail.png")
        hlp_img_btn=hlp_img_btn.resize((180,180),Image.ANTIALIAS)
        self.hlp_img1=ImageTk.PhotoImage(hlp_img_btn)

        hlp_b1 = Button(bg_img,command=self.gmail,image=self.hlp_img1,cursor="hand2",)
        hlp_b1.place(x=800,y=200,width=180,height=180)

        hlp_b1_1 = Button(bg_img,command=self.gmail,text="Gmail",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        hlp_b1_1.place(x=800,y=380,width=180,height=45)


        # create function for button 
    
    
    def linkedin(self):
        self.new = 1
        self.url = "linkedin.com/in/saloni-32418b212"
        webbrowser.open(self.url,new=self.new)
    
    def instagram(self):
        self.new = 1
        self.url = "https://instagram.com/shubhamgupta_9_4?igshid=YmMyMTA2M2Y="
        webbrowser.open(self.url,new=self.new)
    
    
    def gmail(self):
        self.new = 1
        self.url = "www.gmail.com"
        webbrowser.open(self.url,new=self.new)

    






if __name__ == "__main__":
    root=Tk()
    obj=Helpsupport(root)
    root.mainloop()