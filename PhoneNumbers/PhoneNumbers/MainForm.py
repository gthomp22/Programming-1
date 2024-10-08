﻿import System.Drawing
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
        self._label1.BackColor = System.Drawing.SystemColors.WindowFrame
        self._label1.Font = System.Drawing.Font("Microsoft Uighur", 36, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(136, 17)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(723, 414)
        self._label1.TabIndex = 0
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.SystemColors.ActiveCaption
        self._button1.Font = System.Drawing.Font("Microsoft Uighur", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(28, 17)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(81, 85)
        self._button1.TabIndex = 1
        self._button1.Text = "Show"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.SystemColors.ActiveCaption
        self._button2.Font = System.Drawing.Font("Microsoft Uighur", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(28, 182)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(81, 85)
        self._button2.TabIndex = 2
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.SystemColors.ActiveCaption
        self._button3.Font = System.Drawing.Font("Microsoft Uighur", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(28, 346)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(81, 85)
        self._button3.TabIndex = 3
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.SystemColors.WindowFrame
        self.ClientSize = System.Drawing.Size(871, 441)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "PhoneNumbers"
        self.ResumeLayout(False)


    def Button1Click(self, sender, e):
        self._label1.Text = "Best Buy - (608) 758-2156\nDick's Sporting Goods - (608) 302-4093\nTexas Roadhouse - (608) 757-9700\n QDBOA Mexican Eats - (608) 531-9138\nThe Janesville Athletic Club - (608) 756-3737"

    def Button2Click(self, sender, e):
        self._label1.Text = ""

    def Button3Click(self, sender, e):
        Application.Exit()