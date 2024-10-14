import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._textBox1 = System.Windows.Forms.TextBox()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self._label1 = System.Windows.Forms.Label()
        self._label2 = System.Windows.Forms.Label()
        self._label3 = System.Windows.Forms.Label()
        self._label4 = System.Windows.Forms.Label()
        self._label5 = System.Windows.Forms.Label()
        self._label6 = System.Windows.Forms.Label()
        self._label7 = System.Windows.Forms.Label()
        self._label8 = System.Windows.Forms.Label()
        self._label9 = System.Windows.Forms.Label()
        self._label10 = System.Windows.Forms.Label()
        self._label11 = System.Windows.Forms.Label()
        self._label12 = System.Windows.Forms.Label()
        self._label13 = System.Windows.Forms.Label()
        self._label14 = System.Windows.Forms.Label()
        self._label15 = System.Windows.Forms.Label()
        self.SuspendLayout()
        # 
        # textBox1
        # 
        self._textBox1.Location = System.Drawing.Point(199, 38)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(106, 20)
        self._textBox1.TabIndex = 0
        # 
        # button1
        # 
        self._button1.Location = System.Drawing.Point(43, 253)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(66, 46)
        self._button1.TabIndex = 1
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = True
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.Location = System.Drawing.Point(139, 253)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(66, 46)
        self._button2.TabIndex = 2
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = True
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.Location = System.Drawing.Point(232, 253)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(66, 46)
        self._button3.TabIndex = 3
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = True
        self._button3.Click += self.Button3Click
        # 
        # label1
        # 
        self._label1.Location = System.Drawing.Point(199, 73)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(99, 24)
        self._label1.TabIndex = 4
        # 
        # label2
        # 
        self._label2.Location = System.Drawing.Point(199, 97)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(99, 24)
        self._label2.TabIndex = 5
        # 
        # label3
        # 
        self._label3.Location = System.Drawing.Point(199, 121)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(99, 24)
        self._label3.TabIndex = 6
        # 
        # label4
        # 
        self._label4.Location = System.Drawing.Point(199, 145)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(99, 12)
        self._label4.TabIndex = 7
        self._label4.Text = "----------------"
        self._label4.Click += self.Label4Click
        # 
        # label5
        # 
        self._label5.Location = System.Drawing.Point(199, 171)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(99, 24)
        self._label5.TabIndex = 8
        # 
        # label6
        # 
        self._label6.Location = System.Drawing.Point(199, 195)
        self._label6.Name = "label6"
        self._label6.Size = System.Drawing.Size(99, 24)
        self._label6.TabIndex = 9
        # 
        # label7
        # 
        self._label7.Location = System.Drawing.Point(43, 41)
        self._label7.Name = "label7"
        self._label7.Size = System.Drawing.Size(128, 19)
        self._label7.TabIndex = 10
        self._label7.Text = "Kilowatts Used"
        self._label7.Click += self.Label7Click
        # 
        # label8
        # 
        self._label8.Location = System.Drawing.Point(43, 73)
        self._label8.Name = "label8"
        self._label8.Size = System.Drawing.Size(99, 24)
        self._label8.TabIndex = 11
        self._label8.Text = "Base Rate"
        # 
        # label9
        # 
        self._label9.Location = System.Drawing.Point(43, 97)
        self._label9.Name = "label9"
        self._label9.Size = System.Drawing.Size(99, 24)
        self._label9.TabIndex = 12
        self._label9.Text = "Surcharge"
        # 
        # label10
        # 
        self._label10.Location = System.Drawing.Point(43, 121)
        self._label10.Name = "label10"
        self._label10.Size = System.Drawing.Size(99, 24)
        self._label10.TabIndex = 13
        self._label10.Text = "Citytax"
        # 
        # label11
        # 
        self._label11.Location = System.Drawing.Point(43, 171)
        self._label11.Name = "label11"
        self._label11.Size = System.Drawing.Size(99, 24)
        self._label11.TabIndex = 14
        self._label11.Text = "Pay this amount"
        # 
        # label12
        # 
        self._label12.Location = System.Drawing.Point(43, 195)
        self._label12.Name = "label12"
        self._label12.Size = System.Drawing.Size(108, 24)
        self._label12.TabIndex = 15
        self._label12.Text = "After May 20th Pay"
        # 
        # label13
        # 
        self._label13.Location = System.Drawing.Point(43, 55)
        self._label13.Name = "label13"
        self._label13.Size = System.Drawing.Size(262, 18)
        self._label13.TabIndex = 16
        self._label13.Text = "--------------------------------------------------------------------------------------------------------------------------------"
        # 
        # label14
        # 
        self._label14.Location = System.Drawing.Point(43, 23)
        self._label14.Name = "label14"
        self._label14.Size = System.Drawing.Size(262, 18)
        self._label14.TabIndex = 17
        self._label14.Text = "--------------------------------------------------------------------------------------------------------------------------------"
        # 
        # label15
        # 
        self._label15.Location = System.Drawing.Point(43, 7)
        self._label15.Name = "label15"
        self._label15.Size = System.Drawing.Size(262, 16)
        self._label15.TabIndex = 18
        self._label15.Text = "C O M P S C I Electric"
        self._label15.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.SystemColors.Highlight
        self.ClientSize = System.Drawing.Size(351, 322)
        self.Controls.Add(self._label15)
        self.Controls.Add(self._label14)
        self.Controls.Add(self._label13)
        self.Controls.Add(self._label12)
        self.Controls.Add(self._label11)
        self.Controls.Add(self._label10)
        self.Controls.Add(self._label9)
        self.Controls.Add(self._label8)
        self.Controls.Add(self._label7)
        self.Controls.Add(self._label6)
        self.Controls.Add(self._label5)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._textBox1)
        self.Name = "MainForm"
        self.Text = "Prog93a"
        self.ResumeLayout(False)
        self.PerformLayout()


    def Button1Click(self, sender, e):
        KWH = int(self._textBox1.Text)
        BR = 0.0475 * KWH
        sur = BR * .10
        CT = BR * .03
        Tot = round(BR, 2) + round(sur, 2) + round(CT, 2)
        LC = Tot * .04
        Ltot = LC + Tot
        self._label1.Text = "$" + str(round(BR, 2))
        self._label2.Text = "$" + str(round(sur, 2))
        self._label3.Text = "$" + str(round(CT, 2))
        self._label5.Text = "$" + str(round(Tot, 2))
        self._label6.Text = "$" + str(round(Ltot, 2))

    def Label4Click(self, sender, e):
        pass

    def Label7Click(self, sender, e):
        pass

    def Button2Click(self, sender, e):
        self._label1.Text = ""
        self._label2.Text = ""
        self._label3.Text = ""
        self._label5.Text = ""
        self._label6.Text = ""
        self._textBox1.Text = ""

    def Button3Click(self, sender, e):
        Application.Exit()