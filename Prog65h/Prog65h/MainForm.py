﻿import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._textBox1 = System.Windows.Forms.TextBox()
        self._textBox2 = System.Windows.Forms.TextBox()
        self._textBox3 = System.Windows.Forms.TextBox()
        self._label1 = System.Windows.Forms.Label()
        self._label2 = System.Windows.Forms.Label()
        self._label3 = System.Windows.Forms.Label()
        self._label4 = System.Windows.Forms.Label()
        self._label5 = System.Windows.Forms.Label()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self.SuspendLayout()
        # 
        # textBox1
        # 
        self._textBox1.BackColor = System.Drawing.Color.White
        self._textBox1.Location = System.Drawing.Point(138, 32)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(136, 20)
        self._textBox1.TabIndex = 0
        # 
        # textBox2
        # 
        self._textBox2.Location = System.Drawing.Point(138, 58)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(136, 20)
        self._textBox2.TabIndex = 1
        # 
        # textBox3
        # 
        self._textBox3.Location = System.Drawing.Point(138, 84)
        self._textBox3.Name = "textBox3"
        self._textBox3.Size = System.Drawing.Size(136, 20)
        self._textBox3.TabIndex = 2
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.Green
        self._label1.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._label1.Location = System.Drawing.Point(25, 32)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(77, 20)
        self._label1.TabIndex = 3
        self._label1.Text = "Pounds"
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.Color.Green
        self._label2.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._label2.Location = System.Drawing.Point(25, 58)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(77, 20)
        self._label2.TabIndex = 4
        self._label2.Text = "Shillings"
        self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.Color.Green
        self._label3.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._label3.Location = System.Drawing.Point(25, 84)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(77, 20)
        self._label3.TabIndex = 5
        self._label3.Text = "Pence"
        self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label4
        # 
        self._label4.BackColor = System.Drawing.Color.Green
        self._label4.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._label4.Location = System.Drawing.Point(25, 132)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(87, 29)
        self._label4.TabIndex = 6
        self._label4.Text = "Decimal Pounds"
        self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label5
        # 
        self._label5.BackColor = System.Drawing.Color.Green
        self._label5.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._label5.Location = System.Drawing.Point(138, 132)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(136, 29)
        self._label5.TabIndex = 7
        self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.PaleGreen
        self._button1.Location = System.Drawing.Point(25, 189)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(70, 47)
        self._button1.TabIndex = 8
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.PaleGreen
        self._button2.Location = System.Drawing.Point(113, 189)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(70, 47)
        self._button2.TabIndex = 9
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.PaleGreen
        self._button3.Location = System.Drawing.Point(204, 189)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(70, 47)
        self._button3.TabIndex = 10
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.OliveDrab
        self.ClientSize = System.Drawing.Size(304, 261)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label5)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Controls.Add(self._textBox3)
        self.Controls.Add(self._textBox2)
        self.Controls.Add(self._textBox1)
        self.Name = "MainForm"
        self.Text = "Prog65h"
        self.ResumeLayout(False)
        self.PerformLayout()


    def Button1Click(self, sender, e):
        pds = int(self._textBox1.Text)
        shl = int(self._textBox2.Text)
        pnc = int(self._textBox3.Text)
        shl1 = shl * 0.05
        pnc1 = pnc * 0.004
        pds1 = pnc1 + shl1 + pds
        self._label5.Text = str(round(pds1,2))
    def Button2Click(self, sender, e):
        self._textBox1.Text = ""
        self._textBox2.Text = ""
        self._textBox3.Text = ""
        self._label5.Text = ""

    def Button3Click(self, sender, e):
        Application.Exit()