import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._label1 = System.Windows.Forms.Label()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.SystemColors.ActiveBorder
        self._label1.Font = System.Drawing.Font("Monotype Corsiva", 26.25, System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(78, 60)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(270, 200)
        self._label1.TabIndex = 0
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        self._label1.Click += self.Label1Click
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.SystemColors.InactiveCaption
        self._button1.Font = System.Drawing.Font("Modern No. 20", 15.749999, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(78, 289)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(71, 64)
        self._button1.TabIndex = 1
        self._button1.Text = "Show"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.SystemColors.InactiveCaption
        self._button2.Font = System.Drawing.Font("Modern No. 20", 15.749999, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(181, 290)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(71, 63)
        self._button2.TabIndex = 2
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.SystemColors.InactiveCaption
        self._button3.Font = System.Drawing.Font("Modern No. 20", 15.749999, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(277, 289)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(71, 64)
        self._button3.TabIndex = 3
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.SystemColors.Desktop
        self.ClientSize = System.Drawing.Size(415, 392)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "AboutMe"
        self.ResumeLayout(False)


    def Label1Click(self, sender, e):
        pass

    def Button1Click(self, sender, e):
        self._label1.Text = "I am a junior at Craig High School."

    def Button2Click(self, sender, e):
        self._label1.Text = ""

    def Button3Click(self, sender, e):
        Application.Exit()