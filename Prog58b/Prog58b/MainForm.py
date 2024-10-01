import math
import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self._textBox1 = System.Windows.Forms.TextBox()
        self._textBox2 = System.Windows.Forms.TextBox()
        self._textBox3 = System.Windows.Forms.TextBox()
        self._label1 = System.Windows.Forms.Label()
        self._label2 = System.Windows.Forms.Label()
        self._label3 = System.Windows.Forms.Label()
        self._label4 = System.Windows.Forms.Label()
        self._label5 = System.Windows.Forms.Label()
        self._label6 = System.Windows.Forms.Label()
        self._label7 = System.Windows.Forms.Label()
        self._label8 = System.Windows.Forms.Label()
        self.SuspendLayout()
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.SystemColors.ButtonShadow
        self._button1.Location = System.Drawing.Point(34, 42)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(92, 72)
        self._button1.TabIndex = 0
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.SystemColors.ButtonShadow
        self._button2.Location = System.Drawing.Point(34, 164)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(92, 72)
        self._button2.TabIndex = 1
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.SystemColors.ButtonShadow
        self._button3.Location = System.Drawing.Point(34, 290)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(92, 72)
        self._button3.TabIndex = 2
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # textBox1
        # 
        self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox1.Location = System.Drawing.Point(256, 108)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(363, 29)
        self._textBox1.TabIndex = 3
        # 
        # textBox2
        # 
        self._textBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox2.Location = System.Drawing.Point(256, 153)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(363, 29)
        self._textBox2.TabIndex = 4
        # 
        # textBox3
        # 
        self._textBox3.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox3.Location = System.Drawing.Point(256, 207)
        self._textBox3.Name = "textBox3"
        self._textBox3.Size = System.Drawing.Size(363, 29)
        self._textBox3.TabIndex = 5
        # 
        # label1
        # 
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(135, 116)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(87, 21)
        self._label1.TabIndex = 6
        self._label1.Text = "a"
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label2
        # 
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(135, 161)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(87, 21)
        self._label2.TabIndex = 7
        self._label2.Text = "b"
        self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label3
        # 
        self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(136, 207)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(87, 26)
        self._label3.TabIndex = 8
        self._label3.Text = "c"
        self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        self._label3.Click += self.Label3Click
        # 
        # label4
        # 
        self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.Location = System.Drawing.Point(327, 290)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(190, 42)
        self._label4.TabIndex = 9
        # 
        # label5
        # 
        self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label5.Location = System.Drawing.Point(327, 17)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(236, 88)
        self._label5.TabIndex = 10
        self._label5.Text = " ax2 + bx + c"
        self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        self._label5.Click += self.Label5Click
        # 
        # label6
        # 
        self._label6.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label6.Location = System.Drawing.Point(327, 332)
        self._label6.Name = "label6"
        self._label6.Size = System.Drawing.Size(190, 42)
        self._label6.TabIndex = 11
        # 
        # label7
        # 
        self._label7.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label7.Location = System.Drawing.Point(151, 290)
        self._label7.Name = "label7"
        self._label7.Size = System.Drawing.Size(92, 41)
        self._label7.TabIndex = 12
        self._label7.Text = "Root 1"
        # 
        # label8
        # 
        self._label8.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label8.Location = System.Drawing.Point(151, 333)
        self._label8.Name = "label8"
        self._label8.Size = System.Drawing.Size(80, 41)
        self._label8.TabIndex = 13
        self._label8.Text = "Root 2"
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.SystemColors.ActiveCaption
        self.ClientSize = System.Drawing.Size(827, 440)
        self.Controls.Add(self._label8)
        self.Controls.Add(self._label7)
        self.Controls.Add(self._label6)
        self.Controls.Add(self._label5)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Controls.Add(self._textBox3)
        self.Controls.Add(self._textBox2)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Name = "MainForm"
        self.Text = "Prog58b"
        self.ResumeLayout(False)
        self.PerformLayout()

    def Button1Click(self, sender, e):
        a = int(self._textBox1.Text)
        b = int(self._textBox2.Text)
        c = int(self._textBox3.Text)
        root1 = (-b + (b ** 2 - 4 * a * c) ** 0.5) / 2 * a
        root2 = (-b - (b ** 2 - 4 * a * c) ** 0.5) / 2 * a
        self._label4.Text = str(root1)
        self._label6.Text = str(root2)
        

    def Button2Click(self, sender, e):
        self._label4.Text = ""
        self._label6.Text = ""
        self._textBox1.Text = ""
        self._textBox2.Text = ""
        self._textBox3.Text = ""

    def Button3Click(self, sender, e):
        Application.Exit()

    def Label5Click(self, sender, e):
        pass

    def Label3Click(self, sender, e):
        pass